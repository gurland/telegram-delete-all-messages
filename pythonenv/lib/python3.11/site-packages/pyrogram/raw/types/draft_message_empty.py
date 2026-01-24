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


class DraftMessageEmpty(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DraftMessage`.

    Details:
        - Layer: ``158``
        - ID: ``1B0C841A``

    Parameters:
        date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["date"]

    ID = 0x1b0c841a
    QUALNAME = "types.DraftMessageEmpty"

    def __init__(self, *, date: Optional[int] = None) -> None:
        self.date = date  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DraftMessageEmpty":
        
        flags = Int.read(b)
        
        date = Int.read(b) if flags & (1 << 0) else None
        return DraftMessageEmpty(date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.date is not None else 0
        b.write(Int(flags))
        
        if self.date is not None:
            b.write(Int(self.date))
        
        return b.getvalue()
