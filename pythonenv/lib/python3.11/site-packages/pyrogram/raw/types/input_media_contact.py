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


class InputMediaContact(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``158``
        - ID: ``F8AB7DFB``

    Parameters:
        phone_number (``str``):
            N/A

        first_name (``str``):
            N/A

        last_name (``str``):
            N/A

        vcard (``str``):
            N/A

    """

    __slots__: List[str] = ["phone_number", "first_name", "last_name", "vcard"]

    ID = 0xf8ab7dfb
    QUALNAME = "types.InputMediaContact"

    def __init__(self, *, phone_number: str, first_name: str, last_name: str, vcard: str) -> None:
        self.phone_number = phone_number  # string
        self.first_name = first_name  # string
        self.last_name = last_name  # string
        self.vcard = vcard  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaContact":
        # No flags
        
        phone_number = String.read(b)
        
        first_name = String.read(b)
        
        last_name = String.read(b)
        
        vcard = String.read(b)
        
        return InputMediaContact(phone_number=phone_number, first_name=first_name, last_name=last_name, vcard=vcard)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone_number))
        
        b.write(String(self.first_name))
        
        b.write(String(self.last_name))
        
        b.write(String(self.vcard))
        
        return b.getvalue()
