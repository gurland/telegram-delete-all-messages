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


class AttachMenuBotIcon(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AttachMenuBotIcon`.

    Details:
        - Layer: ``158``
        - ID: ``B2A7386B``

    Parameters:
        name (``str``):
            N/A

        icon (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        colors (List of :obj:`AttachMenuBotIconColor <pyrogram.raw.base.AttachMenuBotIconColor>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["name", "icon", "colors"]

    ID = 0xb2a7386b
    QUALNAME = "types.AttachMenuBotIcon"

    def __init__(self, *, name: str, icon: "raw.base.Document", colors: Optional[List["raw.base.AttachMenuBotIconColor"]] = None) -> None:
        self.name = name  # string
        self.icon = icon  # Document
        self.colors = colors  # flags.0?Vector<AttachMenuBotIconColor>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotIcon":
        
        flags = Int.read(b)
        
        name = String.read(b)
        
        icon = TLObject.read(b)
        
        colors = TLObject.read(b) if flags & (1 << 0) else []
        
        return AttachMenuBotIcon(name=name, icon=icon, colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.colors else 0
        b.write(Int(flags))
        
        b.write(String(self.name))
        
        b.write(self.icon.write())
        
        if self.colors is not None:
            b.write(Vector(self.colors))
        
        return b.getvalue()
