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


class PageBlockDetails(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageBlock`.

    Details:
        - Layer: ``158``
        - ID: ``76768BED``

    Parameters:
        blocks (List of :obj:`PageBlock <pyrogram.raw.base.PageBlock>`):
            N/A

        title (:obj:`RichText <pyrogram.raw.base.RichText>`):
            N/A

        open (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["blocks", "title", "open"]

    ID = 0x76768bed
    QUALNAME = "types.PageBlockDetails"

    def __init__(self, *, blocks: List["raw.base.PageBlock"], title: "raw.base.RichText", open: Optional[bool] = None) -> None:
        self.blocks = blocks  # Vector<PageBlock>
        self.title = title  # RichText
        self.open = open  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockDetails":
        
        flags = Int.read(b)
        
        open = True if flags & (1 << 0) else False
        blocks = TLObject.read(b)
        
        title = TLObject.read(b)
        
        return PageBlockDetails(blocks=blocks, title=title, open=open)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.open else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        b.write(self.title.write())
        
        return b.getvalue()
