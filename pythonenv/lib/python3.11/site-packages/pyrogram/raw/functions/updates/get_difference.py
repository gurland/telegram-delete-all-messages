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


class GetDifference(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``25939651``

    Parameters:
        pts (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        qts (``int`` ``32-bit``):
            N/A

        pts_total_limit (``int`` ``32-bit``, *optional*):
            N/A

    Returns:
        :obj:`updates.Difference <pyrogram.raw.base.updates.Difference>`
    """

    __slots__: List[str] = ["pts", "date", "qts", "pts_total_limit"]

    ID = 0x25939651
    QUALNAME = "functions.updates.GetDifference"

    def __init__(self, *, pts: int, date: int, qts: int, pts_total_limit: Optional[int] = None) -> None:
        self.pts = pts  # int
        self.date = date  # int
        self.qts = qts  # int
        self.pts_total_limit = pts_total_limit  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDifference":
        
        flags = Int.read(b)
        
        pts = Int.read(b)
        
        pts_total_limit = Int.read(b) if flags & (1 << 0) else None
        date = Int.read(b)
        
        qts = Int.read(b)
        
        return GetDifference(pts=pts, date=date, qts=qts, pts_total_limit=pts_total_limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pts_total_limit is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.pts))
        
        if self.pts_total_limit is not None:
            b.write(Int(self.pts_total_limit))
        
        b.write(Int(self.date))
        
        b.write(Int(self.qts))
        
        return b.getvalue()
