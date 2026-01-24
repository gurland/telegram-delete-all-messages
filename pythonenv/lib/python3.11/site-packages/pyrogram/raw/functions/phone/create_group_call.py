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


class CreateGroupCall(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``48CDC6D8``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        random_id (``int`` ``32-bit``):
            N/A

        rtmp_stream (``bool``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "random_id", "rtmp_stream", "title", "schedule_date"]

    ID = 0x48cdc6d8
    QUALNAME = "functions.phone.CreateGroupCall"

    def __init__(self, *, peer: "raw.base.InputPeer", random_id: int, rtmp_stream: Optional[bool] = None, title: Optional[str] = None, schedule_date: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.random_id = random_id  # int
        self.rtmp_stream = rtmp_stream  # flags.2?true
        self.title = title  # flags.0?string
        self.schedule_date = schedule_date  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateGroupCall":
        
        flags = Int.read(b)
        
        rtmp_stream = True if flags & (1 << 2) else False
        peer = TLObject.read(b)
        
        random_id = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        schedule_date = Int.read(b) if flags & (1 << 1) else None
        return CreateGroupCall(peer=peer, random_id=random_id, rtmp_stream=rtmp_stream, title=title, schedule_date=schedule_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.rtmp_stream else 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.schedule_date is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.random_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        return b.getvalue()
