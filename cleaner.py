#!/usr/bin/env python3
import os
import json
import tempfile

from time import sleep
from datetime import datetime, timedelta, timezone

from pyrogram import Client
from pyrogram.raw.functions.messages import Search
from pyrogram.raw.types import InputPeerSelf, InputMessagesFilterEmpty
from pyrogram.raw.types.messages import ChannelMessages
from pyrogram.errors import FloodWait, UnknownError

script_path = os.path.abspath(__file__)
project_cache = os.path.join(os.path.dirname(script_path), "cache")

env_cache = os.getenv("TELEGRAM_DELETE_CACHE")
if env_cache:
    user_cache_candidate = env_cache
else:
    xdg_cache = os.getenv("XDG_CACHE_HOME")
    if xdg_cache:
        user_cache_candidate = os.path.join(xdg_cache, "telegram-delete-all-messages")
    else:
        user_cache_candidate = os.path.join(os.path.expanduser("~"), ".cache", "telegram-delete-all-messages")

running_in_nix = script_path.startswith("/nix/store")

def ensure_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception:
        return False

if running_in_nix:
    primary_cache = user_cache_candidate
    if not ensure_dir(primary_cache):
        primary_cache = os.path.join(tempfile.gettempdir(), "telegram-delete-all-messages")
        ensure_dir(primary_cache)
    secondary_cache = project_cache
else:
    primary_cache = project_cache
    if not ensure_dir(primary_cache):
        primary_cache = user_cache_candidate
        if not ensure_dir(primary_cache):
            primary_cache = os.path.join(tempfile.gettempdir(), "telegram-delete-all-messages")
            ensure_dir(primary_cache)
    secondary_cache = None

cache_file = os.path.join(primary_cache, "cache")

if os.path.exists(cache_file):
    with open(cache_file, "r") as cacheFile:
        cache = json.loads(cacheFile.read())
    API_ID = cache.get("API_ID")
    API_HASH = cache.get("API_HASH")
else:
    API_ID = os.getenv('API_ID', None) or int(input('Enter your Telegram API id: '))
    API_HASH = os.getenv('API_HASH', None) or input('Enter your Telegram API hash: ')
    try:
        with open(cache_file, "w") as cacheFile:
            json.dump({"API_ID": API_ID, "API_HASH": API_HASH}, cacheFile)
    except Exception:
        pass
    if running_in_nix and secondary_cache:
        try:
            os.makedirs(secondary_cache, exist_ok=True)
            with open(os.path.join(secondary_cache, "cache"), "w") as cf2:
                json.dump({"API_ID": API_ID, "API_HASH": API_HASH}, cf2)
        except Exception:
            pass

app_session_path = os.path.join(primary_cache, "client")
app = Client(app_session_path, api_id=API_ID, api_hash=API_HASH)

class Cleaner:
    def __init__(self, chats=None, search_chunk_size=100, delete_chunk_size=100, keep_hours=0):
        self.chats = chats or []
        self.keep_hours = keep_hours
        if search_chunk_size > 100:
            # https://github.com/gurland/telegram-delete-all-messages/issues/31
            #
            # The issue is that pyrogram.raw.functions.messages.Search uses
            # pagination with chunks of 100 messages. Might consider switching
            # to search_messages, which handles pagination transparently.
            raise ValueError('search_chunk_size > 100 not supported')
        self.search_chunk_size = search_chunk_size
        self.delete_chunk_size = delete_chunk_size

    @staticmethod
    def chunks(l, n):
        """Yield successive n-sized chunks from l.
        https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks#answer-312464"""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    @staticmethod
    async def get_all_chats():        
        async with app:
            dialogs = []
            async for dialog in app.get_dialogs():
                dialogs.append(dialog.chat)
            return dialogs

    async def select_groups(self, recursive=0):
        chats = await self.get_all_chats()
        groups = [c for c in chats if c.type.name in ('GROUP, SUPERGROUP')]

        print('Delete all your messages in')
        for i, group in enumerate(groups):
            print(f'  {i+1}. {group.title}')

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
                print('\nTHIS WILL DELETE ALL YOUR MESSSAGES IN ALL GROUPS!')
                answer = input('Please type "I understand" to proceed: ')
                if answer.upper() != 'I UNDERSTAND':
                    print('Better safe than sorry. Aborting...')
                    exit(-1)
                self.chats = groups
                break
            else:
                self.chats.append(groups[n - 1])
        
        groups_str = ', '.join(c.title for c in self.chats)
        print(f'\nSelected {groups_str}.\n')

        keep_str = input('Keep messages from last how many hours? Enter number (e.g. 72). Enter 0 to delete all: ').strip()
        try:
            kh = int(keep_str) if keep_str != '' else 0
        except ValueError:
            print('Invalid number, defaulting to 0 (delete all).')
            kh = 0
        self.keep_hours = max(0, kh)

        if recursive == 1:
            self.run()

    async def run(self):
        for chat in self.chats:
            chat_id = chat.id
            message_ids = []
            add_offset = 0

            if self.keep_hours and self.keep_hours > 0:
                cutoff = datetime.now(timezone.utc) - timedelta(hours=self.keep_hours)
            else:
                cutoff = None

            while True:
                q = await self.search_messages(chat_id, add_offset)
                if cutoff:
                    for msg in q:
                        msg_date = msg.date
                        if getattr(msg_date, "tzinfo", None) is None:
                            msg_date = msg_date.replace(tzinfo=timezone.utc)
                        else:
                            msg_date = msg_date.astimezone(timezone.utc)
                        if msg_date < cutoff:
                            message_ids.append(msg.id)
                else:
                    message_ids.extend(msg.id for msg in q)

                messages_count = len(q)
                print(f'Found {len(message_ids)} of your messages in "{chat.title}"')
                if messages_count < self.search_chunk_size:
                    break
                add_offset += self.search_chunk_size

            await self.delete_messages(chat_id=chat.id, message_ids=message_ids)

    async def delete_messages(self, chat_id, message_ids):
        print(f'Deleting {len(message_ids)} messages with message IDs:')
        print(message_ids)
        for chunk in self.chunks(message_ids, self.delete_chunk_size):
            try:
                async with app:
                    await app.delete_messages(chat_id=chat_id, message_ids=chunk)
            except FloodWait as flood_exception:
                sleep(flood_exception.x)

    async def search_messages(self, chat_id, add_offset):
        async with app:
            messages = []
            print(f'Searching messages. OFFSET: {add_offset}')
            async for message in app.search_messages(chat_id=chat_id, offset=add_offset, from_user="me", limit=100):
                messages.append(message)
            return messages

async def main():
    try:
        deleter = Cleaner()
        await deleter.select_groups()
        await deleter.run()
    except UnknownError as e:
        print(f'UnknownError occured: {e}')
        print('Probably API has changed, ask developers to update this utility')

app.run(main())
