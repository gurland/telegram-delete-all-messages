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


class SearchResultPosition(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SearchResultsPosition`.

    Details:
        - Layer: ``158``
        - ID: ``7F648B67``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        offset (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["msg_id", "date", "offset"]

    ID = 0x7f648b67
    QUALNAME = "types.SearchResultPosition"

    def __init__(self, *, msg_id: int, date: int, offset: int) -> None:
        self.msg_id = msg_id  # int
        self.date = date  # int
        self.offset = offset  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultPosition":
        # No flags
        
        msg_id = Int.read(b)
        
        date = Int.read(b)
        
        offset = Int.read(b)
        
        return SearchResultPosition(msg_id=msg_id, date=date, offset=offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.offset))
        
        return b.getvalue()
