import os
import unittest
from contextlib import redirect_stdout
from io import StringIO
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

os.environ.setdefault('API_ID', '12345')
os.environ.setdefault('API_HASH', 'test-api-hash')

from cleaner import Cleaner


class SafeDeletionTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.chat = SimpleNamespace(id=-100123, title='Test group')
        self.cleaner = Cleaner(chats=[self.chat])
        self.cleaner.search_messages = AsyncMock(
            return_value=[SimpleNamespace(id=10), SimpleNamespace(id=20)]
        )
        self.cleaner.delete_messages = AsyncMock()

    async def test_default_mode_is_a_non_destructive_preview(self):
        output = StringIO()
        with patch('builtins.input', side_effect=AssertionError('input should not be called')):
            with redirect_stdout(output):
                await self.cleaner.run()

        self.cleaner.delete_messages.assert_not_awaited()
        self.assertIn('chat ID: -100123', output.getvalue())
        self.assertIn('Dry run complete. 2 messages would be deleted.', output.getvalue())

    async def test_execute_requires_exact_final_confirmation(self):
        with patch('builtins.input', return_value='no'):
            await self.cleaner.run(execute=True)

        self.cleaner.delete_messages.assert_not_awaited()

    async def test_execute_deletes_only_after_confirmation(self):
        with patch('builtins.input', return_value='DELETE'):
            await self.cleaner.run(execute=True)

        self.cleaner.delete_messages.assert_awaited_once_with(
            chat_id=-100123,
            message_ids=[10, 20],
        )


if __name__ == '__main__':
    unittest.main()
