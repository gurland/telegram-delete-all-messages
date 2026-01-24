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


class ClearSavedInfo(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``D83D70C1``

    Parameters:
        credentials (``bool``, *optional*):
            N/A

        info (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["credentials", "info"]

    ID = 0xd83d70c1
    QUALNAME = "functions.payments.ClearSavedInfo"

    def __init__(self, *, credentials: Optional[bool] = None, info: Optional[bool] = None) -> None:
        self.credentials = credentials  # flags.0?true
        self.info = info  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ClearSavedInfo":
        
        flags = Int.read(b)
        
        credentials = True if flags & (1 << 0) else False
        info = True if flags & (1 << 1) else False
        return ClearSavedInfo(credentials=credentials, info=info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.credentials else 0
        flags |= (1 << 1) if self.info else 0
        b.write(Int(flags))
        
        return b.getvalue()
