#!/usr/bin/python

import os
import json

from time import sleep
from datetime import datetime, timedelta

from pyrogram import Client
from pyrogram.raw.functions.messages import Search
from pyrogram.raw.types import InputPeerSelf, InputMessagesFilterEmpty
from pyrogram.raw.types.messages import ChannelMessages
from pyrogram.errors import FloodWait, UnknownError

runPath = os.path.abspath(__file__)
configPath = os.path.join(os.path.dirname(runPath), "config.json")

API_ID = 'API_ID'
API_HASH = 'API_HASH'
SELECTED_GROUPS = 'SELECTED_GROUPS'
OLDER_THAN_DAYS = 'OLDER_THAN_DAYS'
ASSUME_YES = 'ASSUME_YES'

config = {}
assume_yes = os.getenv(ASSUME_YES, False) == '1'  # not storing this in config


class Cleaner:
    def __init__(self, app, search_chunk_size=100, delete_chunk_size=100):
        self.app = app
        self.chats = []
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

    def get_all_chats(self):
        dialogs = self.app.get_dialogs(pinned_only=True)

        dialog_chunk = self.app.get_dialogs()
        while len(dialog_chunk) > 0:
            dialogs.extend(dialog_chunk)
            dialog_chunk = self.app.get_dialogs(offset_date=dialogs[-1].top_message.date-1)

        return [d.chat for d in dialogs]

    def select_groups(self):
        chats = self.get_all_chats()
        groups = [c for c in chats if c.type in ('group', 'supergroup')]

        print('Delete all your messages in')
        for group in groups:
            print(f'  {group.id}) {group.title}')

        print('(!) DELETE ALL YOUR MESSAGES IN ALL OF THOSE GROUPS (!)\n')
        selected_groups = []
        if SELECTED_GROUPS in config and len(config[SELECTED_GROUPS]) != 0:
            previously_selected = ', '.join(map(lambda s: str(s), config[SELECTED_GROUPS]))
            print(f'You have previously selected: {previously_selected}')
            if assume_yes or (input('Do you want to use the same list (YES/NO)?').upper() == 'YES'):
                selected_groups = config[SELECTED_GROUPS]

        if len(selected_groups) == 0:
            nums_str = input('Insert option numbers (comma separated): ')
            selected_groups = list(map(lambda s: int(s.strip()), nums_str.split(',')))
            config[SELECTED_GROUPS] = selected_groups

        self.chats = []
        # sanity check - do all these groups exist?
        for chat_id in selected_groups:
            found = False
            for group in groups:
                if group.id == chat_id:
                    self.chats.append(group)
                    found = True
                    break
            if not found:
                print(f'Invalid option {chat_id} selected. Exiting...')
                exit(-1)

        if not assume_yes and len(self.chats) == len(groups):
            print('\nTHIS WILL DELETE ALL YOUR MESSSAGES IN ALL GROUPS!')
            answer = input('Please type "I understand" to proceed: ')
            if answer.upper() != 'I UNDERSTAND':
                print('Better safe than sorry. Aborting...')
                exit(-1)
        
        groups_str = ', '.join(c.title for c in self.chats)
        print(f'\nSelected {groups_str}.\n')

    def time_days_ago(self, days):
        return int((datetime.now() - timedelta(days=days)).timestamp())

    def select_duration(self):
        if OLDER_THAN_DAYS in config:
            print(f'Delete messages older than {config[OLDER_THAN_DAYS]} days')
            if assume_yes or input('Use this value (YES/NO)?').upper() == 'YES':
                self.max_date = self.time_days_ago(config[OLDER_THAN_DAYS])
                return
        config[OLDER_THAN_DAYS] = int(input('How many last days to keep? Entering 0 deletes all: ').strip())
        self.max_date = self.time_days_ago(config[OLDER_THAN_DAYS])

    def run(self):
        for chat in self.chats:
            peer = self.app.resolve_peer(chat.id)
            message_ids = []
            add_offset = 0

            while True:
                q = self.search_messages(peer, add_offset)
                message_ids.extend(msg.id for msg in q['messages'])
                messages_count = len(q['messages'])
                print(f'Found {messages_count} of your messages in "{chat.title}"')
                if messages_count < self.search_chunk_size:
                    break
                add_offset += self.search_chunk_size

            self.delete_messages(chat.id, message_ids)

    def delete_messages(self, chat_id, message_ids):
        print(f'Deleting {len(message_ids)} messages with message IDs:')
        print(message_ids)
        for chunk in self.chunks(message_ids, self.delete_chunk_size):
            try:
                self.app.delete_messages(chat_id=chat_id, message_ids=chunk)
            except FloodWait as flood_exception:
                sleep(flood_exception.x)

    def search_messages(self, peer, add_offset):
        print(f'Searching messages. OFFSET: {add_offset}')
        return self.app.send(
            Search(
                peer=peer,
                q='',
                filter=InputMessagesFilterEmpty(),
                min_date=0,
                max_date=self.max_date,
                offset_id=0,
                add_offset=add_offset,
                limit=self.search_chunk_size,
                max_id=0,
                min_id=0,
                hash=0,
                from_id=InputPeerSelf()
            ),
            sleep_threshold=60
        )


if __name__ == '__main__':
    if os.path.exists(configPath):
        with open(configPath, "r") as configFile:
            config = json.loads(configFile.read())
    else:
        config[API_ID] = os.getenv(API_ID, None) or int(input('Enter your Telegram API id: '))
        config[API_HASH] = os.getenv(API_HASH, None) or input('Enter your Telegram API hash: ')

    app = Client("client", api_id=config[API_ID], api_hash=config[API_HASH])
    app.start()

    try:
        deleter = Cleaner(app)
        deleter.select_groups()
        deleter.select_duration()
        deleter.run()
    except UnknownError as e:
        print(f'UnknownError occured: {e}')
        print('Probably API has changed, ask developers to update this utility')
    finally:
        app.stop()

    print("Saving config...")
    with open(configPath, "w") as configFile:
        configFile.write(json.dumps(config))
