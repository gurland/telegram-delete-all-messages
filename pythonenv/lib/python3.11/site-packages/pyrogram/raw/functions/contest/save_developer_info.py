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


class SaveDeveloperInfo(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``9A5F6E95``

    Parameters:
        vk_id (``int`` ``32-bit``):
            N/A

        name (``str``):
            N/A

        phone_number (``str``):
            N/A

        age (``int`` ``32-bit``):
            N/A

        city (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["vk_id", "name", "phone_number", "age", "city"]

    ID = 0x9a5f6e95
    QUALNAME = "functions.contest.SaveDeveloperInfo"

    def __init__(self, *, vk_id: int, name: str, phone_number: str, age: int, city: str) -> None:
        self.vk_id = vk_id  # int
        self.name = name  # string
        self.phone_number = phone_number  # string
        self.age = age  # int
        self.city = city  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveDeveloperInfo":
        # No flags
        
        vk_id = Int.read(b)
        
        name = String.read(b)
        
        phone_number = String.read(b)
        
        age = Int.read(b)
        
        city = String.read(b)
        
        return SaveDeveloperInfo(vk_id=vk_id, name=name, phone_number=phone_number, age=age, city=city)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.vk_id))
        
        b.write(String(self.name))
        
        b.write(String(self.phone_number))
        
        b.write(Int(self.age))
        
        b.write(String(self.city))
        
        return b.getvalue()
