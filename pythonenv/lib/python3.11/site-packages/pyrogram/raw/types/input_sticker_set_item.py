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


class InputStickerSetItem(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStickerSetItem`.

    Details:
        - Layer: ``158``
        - ID: ``32DA9E9C``

    Parameters:
        document (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

        emoji (``str``):
            N/A

        mask_coords (:obj:`MaskCoords <pyrogram.raw.base.MaskCoords>`, *optional*):
            N/A

        keywords (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["document", "emoji", "mask_coords", "keywords"]

    ID = 0x32da9e9c
    QUALNAME = "types.InputStickerSetItem"

    def __init__(self, *, document: "raw.base.InputDocument", emoji: str, mask_coords: "raw.base.MaskCoords" = None, keywords: Optional[str] = None) -> None:
        self.document = document  # InputDocument
        self.emoji = emoji  # string
        self.mask_coords = mask_coords  # flags.0?MaskCoords
        self.keywords = keywords  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetItem":
        
        flags = Int.read(b)
        
        document = TLObject.read(b)
        
        emoji = String.read(b)
        
        mask_coords = TLObject.read(b) if flags & (1 << 0) else None
        
        keywords = String.read(b) if flags & (1 << 1) else None
        return InputStickerSetItem(document=document, emoji=emoji, mask_coords=mask_coords, keywords=keywords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.mask_coords is not None else 0
        flags |= (1 << 1) if self.keywords is not None else 0
        b.write(Int(flags))
        
        b.write(self.document.write())
        
        b.write(String(self.emoji))
        
        if self.mask_coords is not None:
            b.write(self.mask_coords.write())
        
        if self.keywords is not None:
            b.write(String(self.keywords))
        
        return b.getvalue()
