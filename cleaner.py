from time import sleep
from os import getenv

from pyrogram import Client
from pyrogram.raw.functions.messages import Search
from pyrogram.raw.types import InputPeerSelf, InputMessagesFilterEmpty
from pyrogram.raw.types.messages import ChannelMessages
from pyrogram.errors import FloodWait, UnknownError

API_ID = getenv('API_ID', None) or int(input('Enter your Telegram API id: '))
API_HASH = getenv('API_HASH', None) or input('Enter your Telegram API hash: ')

app = Client("client", api_id=API_ID, api_hash=API_HASH)
app.start()


class Cleaner:
    def __init__(self, chats=None, search_chunk_size=1000, delete_chunk_size=100, search_limit=5000, offset=10):
        self.chats = chats or []
        self.search_chunk_size = search_chunk_size
        self.delete_chunk_size = delete_chunk_size
        self.search_limit = search_limit
        self.offset = offset
        
    @staticmethod
    def chunks(l, n):
        """Yield successive n-sized chunks from l.
        https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks#answer-312464"""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    @staticmethod
    def get_all_chats():
        dialogs = app.get_dialogs(pinned_only=True)

        dialog_chunk = app.get_dialogs()
        while len(dialog_chunk) > 0:
            dialogs.extend(dialog_chunk)
            dialog_chunk = app.get_dialogs(offset_date=dialogs[-1].top_message.date)

        return [d.chat for d in dialogs]

    def select_groups(self):
        chats = self.get_all_chats()
        groups = [c for c in chats if c.type in ('bot', 'group', 'supergroup')]

        print('Delete all messages in which of the following groups:')
        for i, group in enumerate(groups):
            if group.type == 'bot':
                group_name = group.first_name
            elif group.type in ('group', 'supergroup'):
                group_name = group.title
            print(f'  {i+1}. {group_name} ({group.type})')

        print(
            f'  {len(groups) + 1}. '
            '(!) DELETE ALL YOUR MESSAGES IN ALL OF THOSE GROUPS (!)\n'
        )

        n = int(input('Insert option number: '))
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
        else:
            self.chats = [groups[n - 1]]

        groups_str = ""
        for c in self.chats:
            if c.type == 'bot':
                groups_str += f"{c.first_name}\n"
            elif c.type in ('group', 'supergroup'):
                groups_str += f"{c.title}\n"

        print(f'\nDeleting messages from:\n{groups_str}')

    def run(self):
        for chat in self.chats:
            peer = app.resolve_peer(chat.id)
            message_ids = []
            q = self.get_total_messages(peer)
            add_offset = self.offset
            chat_tot_messages = q.count
            if chat.type == 'bot':
                group_name = chat.first_name
            elif chat.type in ('group', 'supergroup'):
                group_name = chat.title
            print(f'Found {chat_tot_messages} of your messages in "{group_name}"')
            print(f'Offset by {add_offset} latest messages')
            print(f'Searching up to the defined limit of {self.search_limit}')
            while True:
                a = self.search_messages(chat.id, add_offset)
                message_ids.extend(msg.message_id for msg in a)
                tot_messages = len(message_ids)
                messages_count = len(a)
                if messages_count < self.search_chunk_size:
                    print(f'Deleting {messages_count} messages...\n')
                    break
                if tot_messages >= self.search_limit:
                    print(f'Deleting {tot_messages} messages (defined search limit)...\n')
                    break
                add_offset += self.search_chunk_size

            # 
            self.delete_messages(chat.id, message_ids, peer)

    def delete_messages(self, chat_id, message_ids, peer):
        for chunk in self.chunks(message_ids, self.delete_chunk_size):
            try:
                app.delete_messages(chat_id=chat_id, message_ids=chunk)
            except FloodWait as flood_exception:
                sleep(flood_exception.x)
        sleep(1)
        q = self.get_total_messages(peer)
        print(f'{q.count} messages remaining...')

    def search_messages(self, chat_id, add_offset):
        return app.search_messages(
            chat_id, 
            limit=self.search_chunk_size,
            offset=add_offset
        )
        tot_messages = len(a)

    def get_total_messages(self, peer):
        return app.send(
            Search(
                peer=peer,
                q='',
                filter=InputMessagesFilterEmpty(),
                min_date=0,
                max_date=0,
                offset_id=0,
                add_offset=0,
                limit=1,
                max_id=0,
                min_id=0,
                hash=0,
                # from_id=InputPeerSelf()
            )
        )


if __name__ == '__main__':
    try:
        deleter = Cleaner()
        deleter.select_groups()
        deleter.run()
    except UnknownError as e:
        print(f'UnknownError occured: {e}')
        print('Probably API has changed, ask developers to update this utility')
    finally:
        app.stop()
