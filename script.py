from time import sleep
from os import getenv

from pyrogram import Client
from pyrogram.api.functions.messages import Search
from pyrogram.api.types import InputPeerSelf, InputMessagesFilterEmpty
from pyrogram.api.types.messages import ChannelMessages
from pyrogram.errors import FloodWait, UnknownError


API_ID = getenv('API_ID', None) or int(input('Enter your Telegram API id: '))
API_HASH = getenv('API_ID', None) or input('Enter your Telegram API hash: ')

app = Client("client", api_id=API_ID, api_hash=API_HASH)
app.start()


class Cleaner:
    def __init__(self, peer=None, chat_id=None):
        self.peer = peer
        self.chat_id = chat_id
        self.message_ids = []
        self.add_offset = 0

    def select_supergroup(self):
        dialogs = app.get_dialogs()
        groups = [x for x in dialogs.dialogs if x.chat.type == 'supergroup']

        for i, group in enumerate(groups):
            print(f'{i+1}. {group.chat.title}')

        group_n = int(input('Insert group number: '))
        selected_group = groups[group_n - 1]

        selected_group_peer = app.resolve_peer(selected_group.chat.id)
        self.peer = selected_group_peer
        self.chat_id = selected_group.chat.id

        print(f'Selected {selected_group.chat.title}')

        return selected_group, selected_group_peer

    def run(self):
        q = self.search_messages()
        self.update_ids(q)
        messages_count = q.count
        print(f'Found {messages_count} your messages in selected supergroup')

        if messages_count < 100:
            pass
        else:
            self.add_offset = 100

            for i in range(0, messages_count, 100):
                q = self.search_messages()
                self.update_ids(q)
                self.add_offset += 100

        self.delete_messages()

    @staticmethod
    def chunks(l, n):
        """Yield successive n-sized chunks from l.
        https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks#answer-312464"""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def update_ids(self, query: ChannelMessages):
        for msg in query.messages:
            self.message_ids.append(msg.id)

        return len(query.messages)

    def delete_messages(self):
        print(f'Deleting {len(self.message_ids)} messages with next message IDs:')
        print(self.message_ids)
        for message_ids_chunk in self.chunks(self.message_ids, 100):
            try:
                app.delete_messages(chat_id=self.chat_id, message_ids=message_ids_chunk)
            except FloodWait as flood_exception:
                sleep(flood_exception.x)

    def search_messages(self):
        print(f'Searching messages. OFFSET: {self.add_offset}')
        return app.send(
            Search(
                peer=self.peer,
                q='',
                filter=InputMessagesFilterEmpty(),
                min_date=0,
                max_date=0,
                offset_id=0,
                add_offset=self.add_offset,
                limit=100,
                max_id=0,
                min_id=0,
                hash=0,
                from_id=InputPeerSelf()
            )
        )


if __name__ == '__main__':
    try:
        deleter = Cleaner()
        deleter.select_supergroup()
        deleter.run()
    except UnknownError as e:
        print(f'UnknownError occured: {e}')
        print('Probably API has changed, ask developers to update this utility')
    finally:
        app.stop()
