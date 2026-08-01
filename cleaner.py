import os
import json

from asyncio import sleep

from pyrogram import Client, enums, raw
from pyrogram.errors import FloodWait, UnknownError

from qr_auth import login_with_qr

cachePath = os.path.abspath(__file__)
cachePath = os.path.dirname(cachePath)
cachePath = os.path.join(cachePath, "cache")

if os.path.exists(cachePath):
    with open(cachePath, "r") as cacheFile:
        cache = json.loads(cacheFile.read())
    
    API_ID = cache["API_ID"]
    API_HASH = cache["API_HASH"]
else:
    API_ID = os.getenv('API_ID', None) or int(input('Enter your Telegram API id: '))
    API_HASH = os.getenv('API_HASH', None) or input('Enter your Telegram API hash: ')

app = Client("client", api_id=API_ID, api_hash=API_HASH)

if not os.path.exists(cachePath):
    with open(cachePath, "w") as cacheFile:
        cache = {"API_ID": API_ID, "API_HASH": API_HASH}
        cacheFile.write(json.dumps(cache))


class Cleaner:
    def __init__(self, chats=None, search_chunk_size=100, delete_chunk_size=100):
        self.chats = chats or []
        self.search_chunk_size = search_chunk_size
        self.delete_chunk_size = delete_chunk_size

    @staticmethod
    def chunks(l, n):
        """Yield successive n-sized chunks from l.
        https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks#answer-312464"""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    @classmethod
    def _format_chat_title(cls, chat, parent_channel=None):
        title = chat.title or 'Unknown'
        if chat.username:
            title = f'{title} (@{chat.username})'
        if parent_channel:
            parent = f'@{parent_channel.username}' if parent_channel.username else parent_channel.title
            title = f'{title} [discussion of {parent}]'
        if cls._migrated_to_supergroup(chat):
            title = f'{title} [pre-migration history]'
        return title

    @staticmethod
    async def get_all_chats():
        chats_by_id = {}
        for chat_list in (0, 1):
            async for dialog in app.get_dialogs(chat_list=chat_list):
                if dialog.chat:
                    chats_by_id[dialog.chat.id] = dialog.chat
        return list(chats_by_id.values())

    @staticmethod
    def _is_group_chat(chat):
        return chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP)

    @staticmethod
    def _migrated_to_supergroup(chat):
        """Whether this legacy group has been converted into a supergroup.

        Both chats keep their own dialog entry and share a title, which is why
        such a group shows up twice in the list. They are not interchangeable:
        the legacy chat keeps the history from before the migration, and the
        supergroup does not return it.
        https://github.com/gurland/telegram-delete-all-messages/issues/56"""
        return getattr(getattr(chat, '_raw', None), 'migrated_to', None) is not None

    @staticmethod
    async def get_linked_chat(channel):
        """Return the discussion group attached to a channel, if there is one."""
        for attempt in range(2):
            try:
                return (await app.get_chat(channel.id)).linked_chat
            except FloodWait as flood_exception:
                if attempt:
                    return None
                await sleep(flood_exception.value)
            except Exception:
                return None

    async def get_groups(self):
        chats = await self.get_all_chats()
        groups_by_id = {}
        discussion_parents = {}

        for chat in chats:
            if self._is_group_chat(chat):
                groups_by_id[chat.id] = chat

        channels = [chat for chat in chats if chat.type == enums.ChatType.CHANNEL]
        if channels:
            print(f'Scanning {len(channels)} channels for linked discussion groups...')

        for channel in channels:
            linked = await self.get_linked_chat(channel)
            if linked and self._is_group_chat(linked):
                groups_by_id[linked.id] = linked
                discussion_parents[linked.id] = channel

        groups = sorted(
            groups_by_id.values(),
            key=lambda chat: (chat.title or '').lower(),
        )
        return groups, discussion_parents

    async def select_groups(self, recursive=0):
        groups, discussion_parents = await self.get_groups()

        print('Delete all your messages in')
        print(
            f'  ({len(groups)} groups found, including archived chats '
            f'and channel discussions)\n'
        )
        for i, group in enumerate(groups):
            print(f'  {i+1}. {self._format_chat_title(group, discussion_parents.get(group.id))}')

        print(
            f'  {len(groups) + 1}. '
            '(!) DELETE ALL YOUR MESSAGES IN ALL OF THOSE GROUPS (!)\n'
        )

        nums_str = input('Insert option numbers (comma separated): ')
        nums = map(lambda s: int(s.strip()), nums_str.split(','))

        for n in nums:
            if not 1 <= n <= len(groups) + 1:
                print('Invalid option selected. Exiting...')
                exit(-1)

            if n == len(groups) + 1:
                print('\nTHIS WILL DELETE ALL YOUR MESSAGES IN ALL GROUPS!')
                answer = input('Please type "I understand" to proceed: ')
                if answer.upper() != 'I UNDERSTAND':
                    print('Better safe than sorry. Aborting...')
                    exit(-1)
                self.chats = groups
                break
            else:
                self.chats.append(groups[n - 1])
        
        groups_str = ', '.join(
            self._format_chat_title(c, discussion_parents.get(c.id)) for c in self.chats
        )
        print(f'\nSelected {groups_str}.\n')

        if recursive == 1:
            self.run()

    async def run(self):
        for chat in self.chats:
            chat_id = chat.id
            message_ids = []
            add_offset = 0

            while True:
                q = await self.search_messages(chat_id, add_offset)
                message_ids.extend(msg.id for msg in q)
                messages_count = len(q)
                print(f'Found {len(message_ids)} of your messages in "{chat.title}"')
                if messages_count < self.search_chunk_size:
                    break
                add_offset += self.search_chunk_size

            await self.delete_messages(chat_id=chat.id, message_ids=message_ids)

    async def delete_messages(self, chat_id, message_ids):
        if not message_ids:
            return

        print(f'Deleting {len(message_ids)} messages with message IDs:')
        print(message_ids)
        for chunk in self.chunks(message_ids, self.delete_chunk_size):
            while True:
                try:
                    await app.delete_messages(chat_id=chat_id, message_ids=chunk, revoke=True)
                except FloodWait as flood_exception:
                    # Wait out the limit and retry, otherwise the chunk stays undeleted.
                    print(f'Flood limit reached, waiting {flood_exception.value} seconds...')
                    await sleep(flood_exception.value)
                else:
                    break

    async def search_messages(self, chat_id, add_offset):
        messages = []
        print(f'Searching messages. OFFSET: {add_offset}')
        async for message in app.search_messages(chat_id=chat_id, offset=add_offset, from_user="me",
                                                 limit=self.search_chunk_size):
            messages.append(message)
        return messages


def select_login_method():
    print('\nHow do you want to log in?')
    print('  1. Phone number and confirmation code')
    print('  2. QR code')

    while True:
        choice = input('Insert option number [1]: ').strip() or '1'
        if choice in ('1', '2'):
            return choice
        print('Invalid option selected. Try again.')


async def ensure_logged_in():
    """Connect the client, authorizing it first if there is no session yet."""
    is_authorized = await app.connect()

    if not is_authorized:
        if select_login_method() == '2':
            # QR login needs the dispatcher running to be notified about the scan,
            # so the client gets initialized before instead of after authorization.
            await app.initialize()
            await login_with_qr(app)
        else:
            await app.authorize()

    await app.invoke(raw.functions.updates.GetState())
    app.me = await app.get_me()

    if not app.is_initialized:
        await app.initialize()


async def main():
    try:
        await ensure_logged_in()
        deleter = Cleaner()
        await deleter.select_groups()
        await deleter.run()
    except UnknownError as e:
        print(f'UnknownError occured: {e}')
        print('Probably API has changed, ask developers to update this utility')
    finally:
        if app.is_initialized:
            await app.stop()
        elif app.is_connected:
            await app.disconnect()


app.run(main())
