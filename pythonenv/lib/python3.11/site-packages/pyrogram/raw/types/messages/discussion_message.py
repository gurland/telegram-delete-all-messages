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


class DiscussionMessage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.DiscussionMessage`.

    Details:
        - Layer: ``158``
        - ID: ``A6341782``

    Parameters:
        messages (List of :obj:`Message <pyrogram.raw.base.Message>`):
            N/A

        unread_count (``int`` ``32-bit``):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        max_id (``int`` ``32-bit``, *optional*):
            N/A

        read_inbox_max_id (``int`` ``32-bit``, *optional*):
            N/A

        read_outbox_max_id (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDiscussionMessage
    """

    __slots__: List[str] = ["messages", "unread_count", "chats", "users", "max_id", "read_inbox_max_id", "read_outbox_max_id"]

    ID = 0xa6341782
    QUALNAME = "types.messages.DiscussionMessage"

    def __init__(self, *, messages: List["raw.base.Message"], unread_count: int, chats: List["raw.base.Chat"], users: List["raw.base.User"], max_id: Optional[int] = None, read_inbox_max_id: Optional[int] = None, read_outbox_max_id: Optional[int] = None) -> None:
        self.messages = messages  # Vector<Message>
        self.unread_count = unread_count  # int
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.max_id = max_id  # flags.0?int
        self.read_inbox_max_id = read_inbox_max_id  # flags.1?int
        self.read_outbox_max_id = read_outbox_max_id  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DiscussionMessage":
        
        flags = Int.read(b)
        
        messages = TLObject.read(b)
        
        max_id = Int.read(b) if flags & (1 << 0) else None
        read_inbox_max_id = Int.read(b) if flags & (1 << 1) else None
        read_outbox_max_id = Int.read(b) if flags & (1 << 2) else None
        unread_count = Int.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return DiscussionMessage(messages=messages, unread_count=unread_count, chats=chats, users=users, max_id=max_id, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.max_id is not None else 0
        flags |= (1 << 1) if self.read_inbox_max_id is not None else 0
        flags |= (1 << 2) if self.read_outbox_max_id is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.messages))
        
        if self.max_id is not None:
            b.write(Int(self.max_id))
        
        if self.read_inbox_max_id is not None:
            b.write(Int(self.read_inbox_max_id))
        
        if self.read_outbox_max_id is not None:
            b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
