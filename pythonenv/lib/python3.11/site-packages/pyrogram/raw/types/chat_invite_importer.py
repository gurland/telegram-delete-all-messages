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


class ChatInviteImporter(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatInviteImporter`.

    Details:
        - Layer: ``158``
        - ID: ``8C5ADFD9``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        requested (``bool``, *optional*):
            N/A

        via_chatlist (``bool``, *optional*):
            N/A

        about (``str``, *optional*):
            N/A

        approved_by (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "date", "requested", "via_chatlist", "about", "approved_by"]

    ID = 0x8c5adfd9
    QUALNAME = "types.ChatInviteImporter"

    def __init__(self, *, user_id: int, date: int, requested: Optional[bool] = None, via_chatlist: Optional[bool] = None, about: Optional[str] = None, approved_by: Optional[int] = None) -> None:
        self.user_id = user_id  # long
        self.date = date  # int
        self.requested = requested  # flags.0?true
        self.via_chatlist = via_chatlist  # flags.3?true
        self.about = about  # flags.2?string
        self.approved_by = approved_by  # flags.1?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteImporter":
        
        flags = Int.read(b)
        
        requested = True if flags & (1 << 0) else False
        via_chatlist = True if flags & (1 << 3) else False
        user_id = Long.read(b)
        
        date = Int.read(b)
        
        about = String.read(b) if flags & (1 << 2) else None
        approved_by = Long.read(b) if flags & (1 << 1) else None
        return ChatInviteImporter(user_id=user_id, date=date, requested=requested, via_chatlist=via_chatlist, about=about, approved_by=approved_by)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.requested else 0
        flags |= (1 << 3) if self.via_chatlist else 0
        flags |= (1 << 2) if self.about is not None else 0
        flags |= (1 << 1) if self.approved_by is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(Int(self.date))
        
        if self.about is not None:
            b.write(String(self.about))
        
        if self.approved_by is not None:
            b.write(Long(self.approved_by))
        
        return b.getvalue()
