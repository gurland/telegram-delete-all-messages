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


class LangPackStringPluralized(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.LangPackString`.

    Details:
        - Layer: ``158``
        - ID: ``6C47AC9F``

    Parameters:
        key (``str``):
            N/A

        other_value (``str``):
            N/A

        zero_value (``str``, *optional*):
            N/A

        one_value (``str``, *optional*):
            N/A

        two_value (``str``, *optional*):
            N/A

        few_value (``str``, *optional*):
            N/A

        many_value (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            langpack.GetStrings
    """

    __slots__: List[str] = ["key", "other_value", "zero_value", "one_value", "two_value", "few_value", "many_value"]

    ID = 0x6c47ac9f
    QUALNAME = "types.LangPackStringPluralized"

    def __init__(self, *, key: str, other_value: str, zero_value: Optional[str] = None, one_value: Optional[str] = None, two_value: Optional[str] = None, few_value: Optional[str] = None, many_value: Optional[str] = None) -> None:
        self.key = key  # string
        self.other_value = other_value  # string
        self.zero_value = zero_value  # flags.0?string
        self.one_value = one_value  # flags.1?string
        self.two_value = two_value  # flags.2?string
        self.few_value = few_value  # flags.3?string
        self.many_value = many_value  # flags.4?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LangPackStringPluralized":
        
        flags = Int.read(b)
        
        key = String.read(b)
        
        zero_value = String.read(b) if flags & (1 << 0) else None
        one_value = String.read(b) if flags & (1 << 1) else None
        two_value = String.read(b) if flags & (1 << 2) else None
        few_value = String.read(b) if flags & (1 << 3) else None
        many_value = String.read(b) if flags & (1 << 4) else None
        other_value = String.read(b)
        
        return LangPackStringPluralized(key=key, other_value=other_value, zero_value=zero_value, one_value=one_value, two_value=two_value, few_value=few_value, many_value=many_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.zero_value is not None else 0
        flags |= (1 << 1) if self.one_value is not None else 0
        flags |= (1 << 2) if self.two_value is not None else 0
        flags |= (1 << 3) if self.few_value is not None else 0
        flags |= (1 << 4) if self.many_value is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.key))
        
        if self.zero_value is not None:
            b.write(String(self.zero_value))
        
        if self.one_value is not None:
            b.write(String(self.one_value))
        
        if self.two_value is not None:
            b.write(String(self.two_value))
        
        if self.few_value is not None:
            b.write(String(self.few_value))
        
        if self.many_value is not None:
            b.write(String(self.many_value))
        
        b.write(String(self.other_value))
        
        return b.getvalue()
