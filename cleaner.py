import argparse
import os
import json

from asyncio import sleep

from pyrogram import Client, enums, raw
from pyrogram.errors import (
    AuthKeyInvalid, AuthKeyUnregistered, FloodWait, SessionExpired, SessionRevoked, UnknownError,
)

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
    reaction_batch_size = 100

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

    @staticmethod
    async def resolve_chat(reference):
        """Look up a chat by id or @username instead of picking it from the list."""
        try:
            reference = int(reference)
        except ValueError:
            pass
        return await app.get_chat(reference)

    async def enter_chats_manually(self):
        """Ask for groups that are missing from the dialog list, e.g. left ones.

        https://github.com/gurland/telegram-delete-all-messages/issues/48"""
        print(
            '\nEnter a chat id (like -1001234567890) or a @username, one per line.\n'
            'Press Enter on an empty line when you are done.'
        )

        chats = []
        while True:
            reference = input('  Chat id or @username: ').strip()
            if not reference:
                return chats

            try:
                chat = await self.resolve_chat(reference)
            except Exception as e:
                print(f'  Could not open "{reference}": {e}')
                continue

            if not self._is_group_chat(chat):
                print(f'  "{self._format_chat_title(chat)}" is not a group, skipping.')
                continue

            print(f'  Added {self._format_chat_title(chat)}.')
            chats.append(chat)

    async def select_groups(self, recursive=0, remove_reactions=False):
        groups, discussion_parents = await self.get_groups()
        delete_all_option = len(groups) + 1
        manual_option = len(groups) + 2

        if remove_reactions:
            print('Remove all your reactions from messages in')
        else:
            print('Delete all your messages in')
        print(
            f'  ({len(groups)} groups found, including archived chats '
            f'and channel discussions)\n'
        )
        for i, group in enumerate(groups):
            print(f'  {i+1}. {self._format_chat_title(group, discussion_parents.get(group.id))}')

        if remove_reactions:
            print(
                f'  {delete_all_option}. '
                '(!) REMOVE ALL YOUR REACTIONS IN ALL OF THOSE GROUPS (!)'
            )
        else:
            print(
                f'  {delete_all_option}. '
                '(!) DELETE ALL YOUR MESSAGES IN ALL OF THOSE GROUPS (!)'
            )
        print(
            f'  {manual_option}. Enter a chat id or @username by hand '
            '(for groups you have left)\n'
        )

        nums_str = input('Insert option numbers (comma separated): ')
        nums = map(lambda s: int(s.strip()), nums_str.split(','))

        for n in nums:
            if not 1 <= n <= manual_option:
                print('Invalid option selected. Exiting...')
                exit(-1)

            if n == delete_all_option:
                if remove_reactions:
                    print('\nTHIS WILL REMOVE ALL YOUR REACTIONS IN ALL GROUPS!')
                else:
                    print('\nTHIS WILL DELETE ALL YOUR MESSAGES IN ALL GROUPS!')
                answer = input('Please type "I understand" to proceed: ')
                if answer.upper() != 'I UNDERSTAND':
                    print('Better safe than sorry. Aborting...')
                    exit(-1)
                self.chats = groups
                break
            elif n == manual_option:
                self.chats.extend(await self.enter_chats_manually())
            else:
                self.chats.append(groups[n - 1])

        # A chat entered by hand may also be one that was picked from the list.
        self.chats = list({chat.id: chat for chat in self.chats}.values())

        if not self.chats:
            print('No chats selected. Exiting...')
            exit(-1)

        groups_str = ', '.join(
            self._format_chat_title(c, discussion_parents.get(c.id)) for c in self.chats
        )
        print(f'\nSelected {groups_str}.\n')

        if recursive == 1:
            await self.run(remove_reactions=remove_reactions)

    async def run(self, remove_reactions=False):
        if remove_reactions:
            await self.run_reaction_removal()
            return

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

    @staticmethod
    def _chosen_reaction_kind(reaction):
        if reaction.chosen_order is None:
            return None
        if isinstance(reaction.reaction, raw.types.ReactionPaid):
            return 'paid'
        return 'removable'

    async def _invoke_with_flood_wait(self, request, action):
        while True:
            try:
                return await app.invoke(request)
            except FloodWait as flood_exception:
                print(
                    f'Flood limit reached while {action}, waiting '
                    f'{flood_exception.value} seconds...'
                )
                await sleep(flood_exception.value)

    async def get_full_reactions(self, peer, message_ids):
        response = await self._invoke_with_flood_wait(
            raw.functions.messages.GetMessagesReactions(
                peer=peer,
                id=message_ids,
            ),
            'checking reactions',
        )
        return {
            update.msg_id: update.reactions
            for update in getattr(response, 'updates', [])
            if isinstance(update, raw.types.UpdateMessageReactions)
        }

    async def classify_reaction_batch(self, peer, message_ids):
        removable_message_ids = []
        paid_message_count = 0
        full_reactions = await self.get_full_reactions(peer, message_ids)

        for message_id in message_ids:
            summary = full_reactions.get(message_id)
            chosen_kinds = {
                kind
                for reaction in getattr(summary, 'results', [])
                if (kind := self._chosen_reaction_kind(reaction)) is not None
            }

            if 'removable' in chosen_kinds:
                removable_message_ids.append(message_id)
            if 'paid' in chosen_kinds:
                paid_message_count += 1

        return removable_message_ids, paid_message_count

    async def search_reactions(self, chat_id):
        message_ids = []
        paid_message_count = 0
        scanned_count = 0
        candidate_batch = []
        peer = None

        async for message in app.get_chat_history(chat_id):
            scanned_count += 1
            if message.reactions:
                candidate_batch.append(message.id)

            if len(candidate_batch) == self.reaction_batch_size:
                if peer is None:
                    peer = await app.resolve_peer(chat_id)
                removable, paid = await self.classify_reaction_batch(
                    peer,
                    candidate_batch,
                )
                message_ids.extend(removable)
                paid_message_count += paid
                candidate_batch = []

            if scanned_count % 1000 == 0:
                print(f'Scanned {scanned_count} messages...')

        if candidate_batch:
            if peer is None:
                peer = await app.resolve_peer(chat_id)
            removable, paid = await self.classify_reaction_batch(peer, candidate_batch)
            message_ids.extend(removable)
            paid_message_count += paid

        print(
            f'Scanned {scanned_count} messages and found '
            f'{len(message_ids)} messages with removable reactions.'
        )
        return message_ids, paid_message_count, peer

    async def run_reaction_removal(self):
        reaction_plan = []
        total_paid_messages = 0

        for chat in self.chats:
            print(f'Searching for your reactions in "{chat.title}"...')
            message_ids, paid_message_count, peer = await self.search_reactions(chat.id)
            reaction_plan.append((chat, peer, message_ids))
            total_paid_messages += paid_message_count

        print('\nReaction removal preview:')
        for chat, _, message_ids in reaction_plan:
            print(
                f'  "{chat.title}" (chat ID: {chat.id}): '
                f'{len(message_ids)} messages with removable reactions'
            )

        total_messages = sum(len(message_ids) for _, _, message_ids in reaction_plan)
        if total_paid_messages:
            print(
                f'  {total_paid_messages} messages also contain paid reactions, '
                'which Telegram does not allow users to retract.'
            )

        if not total_messages:
            print('No removable reactions found. Nothing will be changed.')
            return

        try:
            answer = input(
                f'\nType "REMOVE REACTIONS" to retract reactions from '
                f'{total_messages} messages: '
            )
        except EOFError:
            print('No confirmation received. Aborting without removing reactions.')
            return

        if answer != 'REMOVE REACTIONS':
            print('Confirmation did not match. Aborting without removing reactions.')
            return

        for _, peer, message_ids in reaction_plan:
            await self.remove_reactions(peer, message_ids)

    async def remove_reactions(self, peer, message_ids):
        if not message_ids:
            return

        for message_id in message_ids:
            await self._invoke_with_flood_wait(
                raw.functions.messages.SendReaction(
                    peer=peer,
                    msg_id=message_id,
                    reaction=None,
                ),
                'removing reactions',
            )

        print(f'Removed reactions from {len(message_ids)} messages.')

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


async def reset_session():
    """Disconnect and delete the stored session so the next connect starts from scratch."""
    await app.disconnect()
    await app.storage.delete()
    # The session is a SQLite database in WAL mode, drop its sidecar files as well.
    for suffix in ('-wal', '-shm'):
        sidecar = f'{app.storage.database}{suffix}'
        if os.path.exists(sidecar):
            os.remove(sidecar)


async def ensure_logged_in():
    """Connect the client, authorizing it first if there is no valid session yet."""
    is_authorized = await app.connect()

    if is_authorized:
        try:
            await app.invoke(raw.functions.updates.GetState())
        except (AuthKeyUnregistered, AuthKeyInvalid, SessionExpired, SessionRevoked):
            # The session was terminated from another device or expired on Telegram's side.
            print('Saved session is no longer valid, please log in again.')
            await reset_session()
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


def parse_args():
    parser = argparse.ArgumentParser(
        description='Delete your messages or remove your reactions in Telegram groups.',
        allow_abbrev=False,
    )
    parser.add_argument(
        '--remove-reactions',
        action='store_true',
        help='remove your non-paid reactions instead of deleting your messages',
    )
    return parser.parse_args()


async def main(remove_reactions=False):
    try:
        await ensure_logged_in()
        deleter = Cleaner()
        await deleter.select_groups(remove_reactions=remove_reactions)
        await deleter.run(remove_reactions=remove_reactions)
    except UnknownError as e:
        print(f'UnknownError occured: {e}')
        print('Probably API has changed, ask developers to update this utility')
    finally:
        if app.is_initialized:
            await app.stop()
        elif app.is_connected:
            await app.disconnect()


if __name__ == '__main__':
    args = parse_args()
    app.run(main(remove_reactions=args.remove_reactions))
