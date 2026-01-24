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


class ChannelForbidden(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Chat`.

    Details:
        - Layer: ``158``
        - ID: ``17D493D5``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        title (``str``):
            N/A

        broadcast (``bool``, *optional*):
            N/A

        megagroup (``bool``, *optional*):
            N/A

        until_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "access_hash", "title", "broadcast", "megagroup", "until_date"]

    ID = 0x17d493d5
    QUALNAME = "types.ChannelForbidden"

    def __init__(self, *, id: int, access_hash: int, title: str, broadcast: Optional[bool] = None, megagroup: Optional[bool] = None, until_date: Optional[int] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.title = title  # string
        self.broadcast = broadcast  # flags.5?true
        self.megagroup = megagroup  # flags.8?true
        self.until_date = until_date  # flags.16?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelForbidden":
        
        flags = Int.read(b)
        
        broadcast = True if flags & (1 << 5) else False
        megagroup = True if flags & (1 << 8) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        title = String.read(b)
        
        until_date = Int.read(b) if flags & (1 << 16) else None
        return ChannelForbidden(id=id, access_hash=access_hash, title=title, broadcast=broadcast, megagroup=megagroup, until_date=until_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.broadcast else 0
        flags |= (1 << 8) if self.megagroup else 0
        flags |= (1 << 16) if self.until_date is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.title))
        
        if self.until_date is not None:
            b.write(Int(self.until_date))
        
        return b.getvalue()
