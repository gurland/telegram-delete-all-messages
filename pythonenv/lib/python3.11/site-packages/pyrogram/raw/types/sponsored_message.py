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


class SponsoredMessage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SponsoredMessage`.

    Details:
        - Layer: ``158``
        - ID: ``FC25B828``

    Parameters:
        random_id (``bytes``):
            N/A

        message (``str``):
            N/A

        recommended (``bool``, *optional*):
            N/A

        show_peer_photo (``bool``, *optional*):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        chat_invite (:obj:`ChatInvite <pyrogram.raw.base.ChatInvite>`, *optional*):
            N/A

        chat_invite_hash (``str``, *optional*):
            N/A

        channel_post (``int`` ``32-bit``, *optional*):
            N/A

        start_param (``str``, *optional*):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

        sponsor_info (``str``, *optional*):
            N/A

        additional_info (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["random_id", "message", "recommended", "show_peer_photo", "from_id", "chat_invite", "chat_invite_hash", "channel_post", "start_param", "entities", "sponsor_info", "additional_info"]

    ID = 0xfc25b828
    QUALNAME = "types.SponsoredMessage"

    def __init__(self, *, random_id: bytes, message: str, recommended: Optional[bool] = None, show_peer_photo: Optional[bool] = None, from_id: "raw.base.Peer" = None, chat_invite: "raw.base.ChatInvite" = None, chat_invite_hash: Optional[str] = None, channel_post: Optional[int] = None, start_param: Optional[str] = None, entities: Optional[List["raw.base.MessageEntity"]] = None, sponsor_info: Optional[str] = None, additional_info: Optional[str] = None) -> None:
        self.random_id = random_id  # bytes
        self.message = message  # string
        self.recommended = recommended  # flags.5?true
        self.show_peer_photo = show_peer_photo  # flags.6?true
        self.from_id = from_id  # flags.3?Peer
        self.chat_invite = chat_invite  # flags.4?ChatInvite
        self.chat_invite_hash = chat_invite_hash  # flags.4?string
        self.channel_post = channel_post  # flags.2?int
        self.start_param = start_param  # flags.0?string
        self.entities = entities  # flags.1?Vector<MessageEntity>
        self.sponsor_info = sponsor_info  # flags.7?string
        self.additional_info = additional_info  # flags.8?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SponsoredMessage":
        
        flags = Int.read(b)
        
        recommended = True if flags & (1 << 5) else False
        show_peer_photo = True if flags & (1 << 6) else False
        random_id = Bytes.read(b)
        
        from_id = TLObject.read(b) if flags & (1 << 3) else None
        
        chat_invite = TLObject.read(b) if flags & (1 << 4) else None
        
        chat_invite_hash = String.read(b) if flags & (1 << 4) else None
        channel_post = Int.read(b) if flags & (1 << 2) else None
        start_param = String.read(b) if flags & (1 << 0) else None
        message = String.read(b)
        
        entities = TLObject.read(b) if flags & (1 << 1) else []
        
        sponsor_info = String.read(b) if flags & (1 << 7) else None
        additional_info = String.read(b) if flags & (1 << 8) else None
        return SponsoredMessage(random_id=random_id, message=message, recommended=recommended, show_peer_photo=show_peer_photo, from_id=from_id, chat_invite=chat_invite, chat_invite_hash=chat_invite_hash, channel_post=channel_post, start_param=start_param, entities=entities, sponsor_info=sponsor_info, additional_info=additional_info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.recommended else 0
        flags |= (1 << 6) if self.show_peer_photo else 0
        flags |= (1 << 3) if self.from_id is not None else 0
        flags |= (1 << 4) if self.chat_invite is not None else 0
        flags |= (1 << 4) if self.chat_invite_hash is not None else 0
        flags |= (1 << 2) if self.channel_post is not None else 0
        flags |= (1 << 0) if self.start_param is not None else 0
        flags |= (1 << 1) if self.entities else 0
        flags |= (1 << 7) if self.sponsor_info is not None else 0
        flags |= (1 << 8) if self.additional_info is not None else 0
        b.write(Int(flags))
        
        b.write(Bytes(self.random_id))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        if self.chat_invite is not None:
            b.write(self.chat_invite.write())
        
        if self.chat_invite_hash is not None:
            b.write(String(self.chat_invite_hash))
        
        if self.channel_post is not None:
            b.write(Int(self.channel_post))
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.sponsor_info is not None:
            b.write(String(self.sponsor_info))
        
        if self.additional_info is not None:
            b.write(String(self.additional_info))
        
        return b.getvalue()
