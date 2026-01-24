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


class KeyboardButtonUrlAuth(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``158``
        - ID: ``10B78D29``

    Parameters:
        text (``str``):
            N/A

        url (``str``):
            N/A

        button_id (``int`` ``32-bit``):
            N/A

        fwd_text (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["text", "url", "button_id", "fwd_text"]

    ID = 0x10b78d29
    QUALNAME = "types.KeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, button_id: int, fwd_text: Optional[str] = None) -> None:
        self.text = text  # string
        self.url = url  # string
        self.button_id = button_id  # int
        self.fwd_text = fwd_text  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonUrlAuth":
        
        flags = Int.read(b)
        
        text = String.read(b)
        
        fwd_text = String.read(b) if flags & (1 << 0) else None
        url = String.read(b)
        
        button_id = Int.read(b)
        
        return KeyboardButtonUrlAuth(text=text, url=url, button_id=button_id, fwd_text=fwd_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.fwd_text is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        b.write(Int(self.button_id))
        
        return b.getvalue()
