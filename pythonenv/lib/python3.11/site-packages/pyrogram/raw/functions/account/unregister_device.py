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


class UnregisterDevice(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``6A0D3206``

    Parameters:
        token_type (``int`` ``32-bit``):
            N/A

        token (``str``):
            N/A

        other_uids (List of ``int`` ``64-bit``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["token_type", "token", "other_uids"]

    ID = 0x6a0d3206
    QUALNAME = "functions.account.UnregisterDevice"

    def __init__(self, *, token_type: int, token: str, other_uids: List[int]) -> None:
        self.token_type = token_type  # int
        self.token = token  # string
        self.other_uids = other_uids  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UnregisterDevice":
        # No flags
        
        token_type = Int.read(b)
        
        token = String.read(b)
        
        other_uids = TLObject.read(b, Long)
        
        return UnregisterDevice(token_type=token_type, token=token, other_uids=other_uids)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.token_type))
        
        b.write(String(self.token))
        
        b.write(Vector(self.other_uids, Long))
        
        return b.getvalue()
