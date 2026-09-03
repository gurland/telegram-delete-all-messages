import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

os.environ.setdefault('API_ID', '12345')
os.environ.setdefault('API_HASH', 'test-api-hash')

from cleaner import Cleaner, parse_args


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


class ExecuteArgumentTests(unittest.TestCase):
    def test_execute_option_cannot_be_abbreviated(self):
        with patch.object(sys, 'argv', ['cleaner.py', '--e']):
            with redirect_stderr(StringIO()):
                with self.assertRaises(SystemExit) as exit_context:
                    parse_args()

        self.assertEqual(2, exit_context.exception.code)

    @unittest.skipUnless(os.name == 'nt', 'Windows batch launcher test')
    def test_windows_launcher_forwards_execute_argument(self):
        project_root = os.path.dirname(os.path.dirname(__file__))

        with tempfile.TemporaryDirectory() as directory:
            launcher = os.path.join(directory, 'start.bat')
            shutil.copy2(os.path.join(project_root, 'start.bat'), launcher)

            scripts = os.path.join(directory, 'venv', 'Scripts')
            os.makedirs(scripts)
            with open(os.path.join(scripts, 'activate.bat'), 'w') as activate:
                activate.write('@set PATH=%~dp0;%PATH%\n')
            with open(os.path.join(scripts, 'python.bat'), 'w') as python:
                python.write('@echo %*>"%CAPTURE_FILE%"\n')
            with open(os.path.join(scripts, 'deactivate.bat'), 'w') as deactivate:
                deactivate.write('@echo off\n')

            capture_file = os.path.join(directory, 'arguments.txt')
            environment = os.environ.copy()
            environment['CAPTURE_FILE'] = capture_file
            subprocess.run(
                ['cmd', '/c', launcher, '--execute'],
                check=True,
                capture_output=True,
                env=environment,
                text=True,
            )

            with open(capture_file, 'r') as captured:
                arguments = captured.read().strip()
            self.assertTrue(arguments.endswith('cleaner.py --execute'), arguments)


if __name__ == '__main__':
    unittest.main()
