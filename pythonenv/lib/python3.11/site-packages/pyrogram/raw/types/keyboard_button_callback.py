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


class KeyboardButtonCallback(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``158``
        - ID: ``35BBDB6B``

    Parameters:
        text (``str``):
            N/A

        data (``bytes``):
            N/A

        requires_password (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["text", "data", "requires_password"]

    ID = 0x35bbdb6b
    QUALNAME = "types.KeyboardButtonCallback"

    def __init__(self, *, text: str, data: bytes, requires_password: Optional[bool] = None) -> None:
        self.text = text  # string
        self.data = data  # bytes
        self.requires_password = requires_password  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonCallback":
        
        flags = Int.read(b)
        
        requires_password = True if flags & (1 << 0) else False
        text = String.read(b)
        
        data = Bytes.read(b)
        
        return KeyboardButtonCallback(text=text, data=data, requires_password=requires_password)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.requires_password else 0
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        b.write(Bytes(self.data))
        
        return b.getvalue()
