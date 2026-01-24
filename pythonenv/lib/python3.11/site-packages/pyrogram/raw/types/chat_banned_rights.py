#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class ChatBannedRights(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatBannedRights`.

    Details:
        - Layer: ``158``
        - ID: ``9F120418``

    Parameters:
        until_date (``int`` ``32-bit``):
            N/A

        view_messages (``bool``, *optional*):
            N/A

        send_messages (``bool``, *optional*):
            N/A

        send_media (``bool``, *optional*):
            N/A

        send_stickers (``bool``, *optional*):
            N/A

        send_gifs (``bool``, *optional*):
            N/A

        send_games (``bool``, *optional*):
            N/A

        send_inline (``bool``, *optional*):
            N/A

        embed_links (``bool``, *optional*):
            N/A

        send_polls (``bool``, *optional*):
            N/A

        change_info (``bool``, *optional*):
            N/A

        invite_users (``bool``, *optional*):
            N/A

        pin_messages (``bool``, *optional*):
            N/A

        manage_topics (``bool``, *optional*):
            N/A

        send_photos (``bool``, *optional*):
            N/A

        send_videos (``bool``, *optional*):
            N/A

        send_roundvideos (``bool``, *optional*):
            N/A

        send_audios (``bool``, *optional*):
            N/A

        send_voices (``bool``, *optional*):
            N/A

        send_docs (``bool``, *optional*):
            N/A

        send_plain (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["until_date", "view_messages", "send_messages", "send_media", "send_stickers", "send_gifs", "send_games", "send_inline", "embed_links", "send_polls", "change_info", "invite_users", "pin_messages", "manage_topics", "send_photos", "send_videos", "send_roundvideos", "send_audios", "send_voices", "send_docs", "send_plain"]

    ID = 0x9f120418
    QUALNAME = "types.ChatBannedRights"

    def __init__(self, *, until_date: int, view_messages: Optional[bool] = None, send_messages: Optional[bool] = None, send_media: Optional[bool] = None, send_stickers: Optional[bool] = None, send_gifs: Optional[bool] = None, send_games: Optional[bool] = None, send_inline: Optional[bool] = None, embed_links: Optional[bool] = None, send_polls: Optional[bool] = None, change_info: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, manage_topics: Optional[bool] = None, send_photos: Optional[bool] = None, send_videos: Optional[bool] = None, send_roundvideos: Optional[bool] = None, send_audios: Optional[bool] = None, send_voices: Optional[bool] = None, send_docs: Optional[bool] = None, send_plain: Optional[bool] = None) -> None:
        self.until_date = until_date  # int
        self.view_messages = view_messages  # flags.0?true
        self.send_messages = send_messages  # flags.1?true
        self.send_media = send_media  # flags.2?true
        self.send_stickers = send_stickers  # flags.3?true
        self.send_gifs = send_gifs  # flags.4?true
        self.send_games = send_games  # flags.5?true
        self.send_inline = send_inline  # flags.6?true
        self.embed_links = embed_links  # flags.7?true
        self.send_polls = send_polls  # flags.8?true
        self.change_info = change_info  # flags.10?true
        self.invite_users = invite_users  # flags.15?true
        self.pin_messages = pin_messages  # flags.17?true
        self.manage_topics = manage_topics  # flags.18?true
        self.send_photos = send_photos  # flags.19?true
        self.send_videos = send_videos  # flags.20?true
        self.send_roundvideos = send_roundvideos  # flags.21?true
        self.send_audios = send_audios  # flags.22?true
        self.send_voices = send_voices  # flags.23?true
        self.send_docs = send_docs  # flags.24?true
        self.send_plain = send_plain  # flags.25?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatBannedRights":
        
        flags = Int.read(b)
        
        view_messages = True if flags & (1 << 0) else False
        send_messages = True if flags & (1 << 1) else False
        send_media = True if flags & (1 << 2) else False
        send_stickers = True if flags & (1 << 3) else False
        send_gifs = True if flags & (1 << 4) else False
        send_games = True if flags & (1 << 5) else False
        send_inline = True if flags & (1 << 6) else False
        embed_links = True if flags & (1 << 7) else False
        send_polls = True if flags & (1 << 8) else False
        change_info = True if flags & (1 << 10) else False
        invite_users = True if flags & (1 << 15) else False
        pin_messages = True if flags & (1 << 17) else False
        manage_topics = True if flags & (1 << 18) else False
        send_photos = True if flags & (1 << 19) else False
        send_videos = True if flags & (1 << 20) else False
        send_roundvideos = True if flags & (1 << 21) else False
        send_audios = True if flags & (1 << 22) else False
        send_voices = True if flags & (1 << 23) else False
        send_docs = True if flags & (1 << 24) else False
        send_plain = True if flags & (1 << 25) else False
        until_date = Int.read(b)
        
        return ChatBannedRights(until_date=until_date, view_messages=view_messages, send_messages=send_messages, send_media=send_media, send_stickers=send_stickers, send_gifs=send_gifs, send_games=send_games, send_inline=send_inline, embed_links=embed_links, send_polls=send_polls, change_info=change_info, invite_users=invite_users, pin_messages=pin_messages, manage_topics=manage_topics, send_photos=send_photos, send_videos=send_videos, send_roundvideos=send_roundvideos, send_audios=send_audios, send_voices=send_voices, send_docs=send_docs, send_plain=send_plain)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.view_messages else 0
        flags |= (1 << 1) if self.send_messages else 0
        flags |= (1 << 2) if self.send_media else 0
        flags |= (1 << 3) if self.send_stickers else 0
        flags |= (1 << 4) if self.send_gifs else 0
        flags |= (1 << 5) if self.send_games else 0
        flags |= (1 << 6) if self.send_inline else 0
        flags |= (1 << 7) if self.embed_links else 0
        flags |= (1 << 8) if self.send_polls else 0
        flags |= (1 << 10) if self.change_info else 0
        flags |= (1 << 15) if self.invite_users else 0
        flags |= (1 << 17) if self.pin_messages else 0
        flags |= (1 << 18) if self.manage_topics else 0
        flags |= (1 << 19) if self.send_photos else 0
        flags |= (1 << 20) if self.send_videos else 0
        flags |= (1 << 21) if self.send_roundvideos else 0
        flags |= (1 << 22) if self.send_audios else 0
        flags |= (1 << 23) if self.send_voices else 0
        flags |= (1 << 24) if self.send_docs else 0
        flags |= (1 << 25) if self.send_plain else 0
        b.write(Int(flags))
        
        b.write(Int(self.until_date))
        
        return b.getvalue()
