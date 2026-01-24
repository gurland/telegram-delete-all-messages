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


class SetBotInfo(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``10CF3123``

    Parameters:
        lang_code (``str``):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`, *optional*):
            N/A

        name (``str``, *optional*):
            N/A

        about (``str``, *optional*):
            N/A

        description (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["lang_code", "bot", "name", "about", "description"]

    ID = 0x10cf3123
    QUALNAME = "functions.bots.SetBotInfo"

    def __init__(self, *, lang_code: str, bot: "raw.base.InputUser" = None, name: Optional[str] = None, about: Optional[str] = None, description: Optional[str] = None) -> None:
        self.lang_code = lang_code  # string
        self.bot = bot  # flags.2?InputUser
        self.name = name  # flags.3?string
        self.about = about  # flags.0?string
        self.description = description  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotInfo":
        
        flags = Int.read(b)
        
        bot = TLObject.read(b) if flags & (1 << 2) else None
        
        lang_code = String.read(b)
        
        name = String.read(b) if flags & (1 << 3) else None
        about = String.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        return SetBotInfo(lang_code=lang_code, bot=bot, name=name, about=about, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.bot is not None else 0
        flags |= (1 << 3) if self.name is not None else 0
        flags |= (1 << 0) if self.about is not None else 0
        flags |= (1 << 1) if self.description is not None else 0
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        b.write(String(self.lang_code))
        
        if self.name is not None:
            b.write(String(self.name))
        
        if self.about is not None:
            b.write(String(self.about))
        
        if self.description is not None:
            b.write(String(self.description))
        
        return b.getvalue()
