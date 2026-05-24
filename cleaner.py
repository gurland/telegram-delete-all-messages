import argparse
import os
import json
from datetime import datetime, timedelta, timezone

from time import sleep

from pyrogram import Client
from pyrogram.errors import FloodWait, UnknownError

def parse_cli_args():
    parser = argparse.ArgumentParser(
        description='Delete or preview your Telegram messages in selected groups.'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='List messages that would be deleted without actually deleting them.',
    )
    return parser.parse_args()

CLI_ARGS = parse_cli_args()

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
    def __init__(
        self,
        chats=None,
        search_chunk_size=100,
        delete_chunk_size=100,
        days_threshold=None,
        dry_run=False,
    ):
        self.chats = chats or []
        self.search_chunk_size = search_chunk_size
        self.delete_chunk_size = delete_chunk_size
        self.days_threshold = days_threshold
        self.cutoff_datetime = None
        self.local_timezone = datetime.now().astimezone().tzinfo or timezone.utc
        self.dry_run = dry_run
        self.delete_all = False
        if days_threshold:
            self.set_days_threshold(days_threshold)

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

        if recursive == 1:
            self.run()

    def prompt_cutoff(self):
        prompt_text = (
            '\nChoose how far back to delete your messages:\n'
            '  • Enter a positive number of days (e.g. 30)\n'
            '  • Enter a timestamp in MM-DD-YYYY[ hh:mm[:ss]] (e.g. 04-19-2025 11:30)\n'
            '  • Enter "all" or 0 to delete all\n'
            'Your choice: '
        )
        while True:
            user_input = input(prompt_text).strip()
            if not user_input:
                print('Input cannot be empty.')
                continue

            if self.try_set_delete_all(user_input):
                break

            if self.try_set_days_threshold(user_input):
                break

            if self.try_set_timestamp_cutoff(user_input):
                break

            print(
                'Invalid input. Provide a positive integer number of days or '
                'a timestamp such as 03-25-2024 15:30:00.'
            )

    def try_set_delete_all(self, raw_value):
        normalized = raw_value.strip().lower()
        if normalized not in ('all', '0'):
            return False

        self.delete_all = True
        self.days_threshold = None
        self.cutoff_datetime = None
        print('\nDelete-all mode enabled: every message in the selected chats will be deleted.\n')
        return True

    def try_set_days_threshold(self, raw_value):
        try:
            days = int(raw_value)
        except ValueError:
            return False

        if days <= 0:
            print('Please enter a positive integer value (e.g. 30).')
            return False

        self.set_days_threshold(days)
        print(f'\nMessages newer than {days} day(s) will be skipped.\n')
        return True

    def try_set_timestamp_cutoff(self, raw_value):
        cutoff = self.parse_cutoff_timestamp(raw_value)
        if not cutoff:
            return False

        self.set_cutoff_datetime(cutoff)
        local_str, utc_str = self.describe_cutoff_times()
        print(f'\nMessages sent after {local_str} (local) / {utc_str} will be skipped.\n')
        return True

    @staticmethod
    def parse_cutoff_timestamp(raw_value):
        formats = (
            '%m-%d-%Y %H:%M:%S',
            '%m-%d-%Y %H:%M',
            '%m-%d-%Y',
        )
        for date_format in formats:
            try:
                parsed = datetime.strptime(raw_value, date_format)
                return parsed
            except ValueError:
                continue
        return None

    def set_days_threshold(self, days):
        if days <= 0:
            raise ValueError('days_threshold must be a positive integer')
        self.days_threshold = days
        self.delete_all = False
        now = datetime.now(timezone.utc)
        self.cutoff_datetime = now - timedelta(days=days)

    def set_cutoff_datetime(self, cutoff_datetime):
        if cutoff_datetime.tzinfo is None:
            cutoff_datetime = cutoff_datetime.replace(tzinfo=self.local_timezone)
        else:
            cutoff_datetime = cutoff_datetime.astimezone(self.local_timezone)
        cutoff_datetime = cutoff_datetime.astimezone(timezone.utc)
        self.days_threshold = None
        self.delete_all = False
        self.cutoff_datetime = cutoff_datetime

    def describe_cutoff_times(self):
        if not self.cutoff_datetime:
            return ('', '')
        local_time = self.cutoff_datetime.astimezone(self.local_timezone)
        local_str = local_time.strftime('%Y-%m-%d %H:%M:%S %Z')
        utc_str = self.cutoff_datetime.strftime('%Y-%m-%d %H:%M:%S %Z')
        return local_str, utc_str

    @staticmethod
    def message_preview(message, max_length=30):
        content = message.text or message.caption or ''
        content = content.replace('\n', ' ').strip()
        if not content:
            content = '[non-text message]'
        if len(content) > max_length:
            content = content[:max_length - 3] + '...'
        return content

    def filter_messages_by_age(self, messages):
        if self.delete_all or not self.cutoff_datetime:
            return messages

        filtered_messages = []
        for message in messages:
            message_date = message.date
            if message_date.tzinfo is None:
                message_date = message_date.replace(tzinfo=self.local_timezone)
            message_date = message_date.astimezone(timezone.utc)
            if message_date <= self.cutoff_datetime:
                filtered_messages.append(message)

        return filtered_messages

    async def run(self):
        if not self.delete_all and not self.cutoff_datetime:
            raise ValueError('Cutoff not set. Call prompt_cutoff() before run().')

        for chat in self.chats:
            chat_id = chat.id
            message_ids = []
            add_offset = 0

            while True:
                q = await self.search_messages(chat_id, add_offset)
                filtered_messages = self.filter_messages_by_age(q)
                message_ids.extend(msg.id for msg in filtered_messages)
                for msg in filtered_messages:
                    preview = self.message_preview(msg)
                    print(f'    - #{msg.id}: {preview}')
                messages_count = len(q)
                print(f'Found {len(message_ids)} of your messages in "{chat.title}"')
                if messages_count < self.search_chunk_size:
                    break
                add_offset += self.search_chunk_size

            await self.delete_messages(chat_id=chat.id, message_ids=message_ids)

    async def delete_messages(self, chat_id, message_ids):
        action = 'Dry run - would delete' if self.dry_run else 'Deleting'
        print(f'{action} {len(message_ids)} messages with message IDs:')
        print(message_ids)
        for chunk in self.chunks(message_ids, self.delete_chunk_size):
            if self.dry_run:
                print(f'Dry run: skipping deletion of {len(chunk)} messages in this chunk.')
                continue
            try:
                async with app:
                    await app.delete_messages(chat_id=chat_id, message_ids=chunk)
            except FloodWait as flood_exception:
                sleep(flood_exception.x)

    async def search_messages(self, chat_id, add_offset):
        async with app:
            messages = []
            print(f'Searching messages. OFFSET: {add_offset}')
            async for message in app.search_messages(
                chat_id=chat_id,
                offset=add_offset,
                from_user="me",
                limit=self.search_chunk_size,
            ):
                messages.append(message)
            return messages

async def main():
    try:
        deleter = Cleaner(dry_run=CLI_ARGS.dry_run)
        if deleter.dry_run:
            print('Dry run enabled: no messages will be deleted.')
        await deleter.select_groups()
        deleter.prompt_cutoff()
        await deleter.run()
    except UnknownError as e:
        print(f'UnknownError occured: {e}')
        print('Probably API has changed, ask developers to update this utility')

app.run(main())
