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


class GetForumTopics(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``DE560D1``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        offset_date (``int`` ``32-bit``):
            N/A

        offset_id (``int`` ``32-bit``):
            N/A

        offset_topic (``int`` ``32-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        q (``str``, *optional*):
            N/A

    Returns:
        :obj:`messages.ForumTopics <pyrogram.raw.base.messages.ForumTopics>`
    """

    __slots__: List[str] = ["channel", "offset_date", "offset_id", "offset_topic", "limit", "q"]

    ID = 0xde560d1
    QUALNAME = "functions.channels.GetForumTopics"

    def __init__(self, *, channel: "raw.base.InputChannel", offset_date: int, offset_id: int, offset_topic: int, limit: int, q: Optional[str] = None) -> None:
        self.channel = channel  # InputChannel
        self.offset_date = offset_date  # int
        self.offset_id = offset_id  # int
        self.offset_topic = offset_topic  # int
        self.limit = limit  # int
        self.q = q  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetForumTopics":
        
        flags = Int.read(b)
        
        channel = TLObject.read(b)
        
        q = String.read(b) if flags & (1 << 0) else None
        offset_date = Int.read(b)
        
        offset_id = Int.read(b)
        
        offset_topic = Int.read(b)
        
        limit = Int.read(b)
        
        return GetForumTopics(channel=channel, offset_date=offset_date, offset_id=offset_id, offset_topic=offset_topic, limit=limit, q=q)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.q is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        if self.q is not None:
            b.write(String(self.q))
        
        b.write(Int(self.offset_date))
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.offset_topic))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
