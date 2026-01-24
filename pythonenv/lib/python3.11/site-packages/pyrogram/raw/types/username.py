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


class Username(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Username`.

    Details:
        - Layer: ``158``
        - ID: ``B4073647``

    Parameters:
        username (``str``):
            N/A

        editable (``bool``, *optional*):
            N/A

        active (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["username", "editable", "active"]

    ID = 0xb4073647
    QUALNAME = "types.Username"

    def __init__(self, *, username: str, editable: Optional[bool] = None, active: Optional[bool] = None) -> None:
        self.username = username  # string
        self.editable = editable  # flags.0?true
        self.active = active  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Username":
        
        flags = Int.read(b)
        
        editable = True if flags & (1 << 0) else False
        active = True if flags & (1 << 1) else False
        username = String.read(b)
        
        return Username(username=username, editable=editable, active=active)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.editable else 0
        flags |= (1 << 1) if self.active else 0
        b.write(Int(flags))
        
        b.write(String(self.username))
        
        return b.getvalue()
