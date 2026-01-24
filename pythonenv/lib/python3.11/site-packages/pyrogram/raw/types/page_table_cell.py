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


class PageTableCell(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageTableCell`.

    Details:
        - Layer: ``158``
        - ID: ``34566B6A``

    Parameters:
        header (``bool``, *optional*):
            N/A

        align_center (``bool``, *optional*):
            N/A

        align_right (``bool``, *optional*):
            N/A

        valign_middle (``bool``, *optional*):
            N/A

        valign_bottom (``bool``, *optional*):
            N/A

        text (:obj:`RichText <pyrogram.raw.base.RichText>`, *optional*):
            N/A

        colspan (``int`` ``32-bit``, *optional*):
            N/A

        rowspan (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["header", "align_center", "align_right", "valign_middle", "valign_bottom", "text", "colspan", "rowspan"]

    ID = 0x34566b6a
    QUALNAME = "types.PageTableCell"

    def __init__(self, *, header: Optional[bool] = None, align_center: Optional[bool] = None, align_right: Optional[bool] = None, valign_middle: Optional[bool] = None, valign_bottom: Optional[bool] = None, text: "raw.base.RichText" = None, colspan: Optional[int] = None, rowspan: Optional[int] = None) -> None:
        self.header = header  # flags.0?true
        self.align_center = align_center  # flags.3?true
        self.align_right = align_right  # flags.4?true
        self.valign_middle = valign_middle  # flags.5?true
        self.valign_bottom = valign_bottom  # flags.6?true
        self.text = text  # flags.7?RichText
        self.colspan = colspan  # flags.1?int
        self.rowspan = rowspan  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageTableCell":
        
        flags = Int.read(b)
        
        header = True if flags & (1 << 0) else False
        align_center = True if flags & (1 << 3) else False
        align_right = True if flags & (1 << 4) else False
        valign_middle = True if flags & (1 << 5) else False
        valign_bottom = True if flags & (1 << 6) else False
        text = TLObject.read(b) if flags & (1 << 7) else None
        
        colspan = Int.read(b) if flags & (1 << 1) else None
        rowspan = Int.read(b) if flags & (1 << 2) else None
        return PageTableCell(header=header, align_center=align_center, align_right=align_right, valign_middle=valign_middle, valign_bottom=valign_bottom, text=text, colspan=colspan, rowspan=rowspan)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.header else 0
        flags |= (1 << 3) if self.align_center else 0
        flags |= (1 << 4) if self.align_right else 0
        flags |= (1 << 5) if self.valign_middle else 0
        flags |= (1 << 6) if self.valign_bottom else 0
        flags |= (1 << 7) if self.text is not None else 0
        flags |= (1 << 1) if self.colspan is not None else 0
        flags |= (1 << 2) if self.rowspan is not None else 0
        b.write(Int(flags))
        
        if self.text is not None:
            b.write(self.text.write())
        
        if self.colspan is not None:
            b.write(Int(self.colspan))
        
        if self.rowspan is not None:
            b.write(Int(self.rowspan))
        
        return b.getvalue()
