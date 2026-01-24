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


class PostAddress(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PostAddress`.

    Details:
        - Layer: ``158``
        - ID: ``1E8CAAEB``

    Parameters:
        street_line1 (``str``):
            N/A

        street_line2 (``str``):
            N/A

        city (``str``):
            N/A

        state (``str``):
            N/A

        country_iso2 (``str``):
            N/A

        post_code (``str``):
            N/A

    """

    __slots__: List[str] = ["street_line1", "street_line2", "city", "state", "country_iso2", "post_code"]

    ID = 0x1e8caaeb
    QUALNAME = "types.PostAddress"

    def __init__(self, *, street_line1: str, street_line2: str, city: str, state: str, country_iso2: str, post_code: str) -> None:
        self.street_line1 = street_line1  # string
        self.street_line2 = street_line2  # string
        self.city = city  # string
        self.state = state  # string
        self.country_iso2 = country_iso2  # string
        self.post_code = post_code  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PostAddress":
        # No flags
        
        street_line1 = String.read(b)
        
        street_line2 = String.read(b)
        
        city = String.read(b)
        
        state = String.read(b)
        
        country_iso2 = String.read(b)
        
        post_code = String.read(b)
        
        return PostAddress(street_line1=street_line1, street_line2=street_line2, city=city, state=state, country_iso2=country_iso2, post_code=post_code)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.street_line1))
        
        b.write(String(self.street_line2))
        
        b.write(String(self.city))
        
        b.write(String(self.state))
        
        b.write(String(self.country_iso2))
        
        b.write(String(self.post_code))
        
        return b.getvalue()
