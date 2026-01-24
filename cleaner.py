import os
import json

from time import sleep

from pyrogram import Client
from pyrogram.raw.functions.messages import Search
from pyrogram.raw.types import InputPeerSelf, InputMessagesFilterEmpty
from pyrogram.raw.types.messages import ChannelMessages
from pyrogram.errors import FloodWait, UnknownError
from pyrogram.enums import ChatType

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
app.start()

if not os.path.exists(cachePath):
    with open(cachePath, "w") as cacheFile:
        cache = {"API_ID": API_ID, "API_HASH": API_HASH}
        cacheFile.write(json.dumps(cache))


class Cleaner:
    def __init__(self, search_chunk_size=100, delete_chunk_size=100):
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

    def run(self, chat_id):
            peer = app.resolve_peer(chat_id)
            message_ids = []
            add_offset = 0

            while True:
                q = self.search_messages(peer, add_offset)
                #message_ids.extend(msg.id for msg in q['messages'])
                #messages_count = len(q['messages'])
                message_ids.extend(msg.id for msg in q.messages)
                messages_count = len(q.messages)
                print(f'Found {messages_count} of your messages in "{app.get_chat(chat_id).title}"')
                if messages_count < self.search_chunk_size:
                    break
                add_offset += self.search_chunk_size

            self.delete_messages(chat_id, message_ids)

    def delete_messages(self, chat_id, message_ids):
        print(f'Deleting {len(message_ids)} messages with message IDs:')
        print(message_ids)
        for chunk in self.chunks(message_ids, self.delete_chunk_size):
            try:
                app.delete_messages(chat_id=chat_id, message_ids=chunk)
            except FloodWait as flood_exception:
                sleep(flood_exception.x)

    def search_messages(self, peer, add_offset):
        print(f'Searching messages. OFFSET: {add_offset}')
        return app.invoke(
        #return app.send(
            Search(
                peer=peer,
                q='',
                filter=InputMessagesFilterEmpty(),
                min_date=0,
                max_date=0,
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
    try:
        deleter = Cleaner()
        deleter.run(int(input('Enter chat_id: ')))
    except UnknownError as e:
        print(f'UnknownError occured: {e}')
        print('Probably API has changed, ask developers to update this utility')
    finally:
        app.stop()
