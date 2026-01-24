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


class DocumentAttributeSticker(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``158``
        - ID: ``6319D612``

    Parameters:
        alt (``str``):
            N/A

        stickerset (:obj:`InputStickerSet <pyrogram.raw.base.InputStickerSet>`):
            N/A

        mask (``bool``, *optional*):
            N/A

        mask_coords (:obj:`MaskCoords <pyrogram.raw.base.MaskCoords>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["alt", "stickerset", "mask", "mask_coords"]

    ID = 0x6319d612
    QUALNAME = "types.DocumentAttributeSticker"

    def __init__(self, *, alt: str, stickerset: "raw.base.InputStickerSet", mask: Optional[bool] = None, mask_coords: "raw.base.MaskCoords" = None) -> None:
        self.alt = alt  # string
        self.stickerset = stickerset  # InputStickerSet
        self.mask = mask  # flags.1?true
        self.mask_coords = mask_coords  # flags.0?MaskCoords

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeSticker":
        
        flags = Int.read(b)
        
        mask = True if flags & (1 << 1) else False
        alt = String.read(b)
        
        stickerset = TLObject.read(b)
        
        mask_coords = TLObject.read(b) if flags & (1 << 0) else None
        
        return DocumentAttributeSticker(alt=alt, stickerset=stickerset, mask=mask, mask_coords=mask_coords)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.mask else 0
        flags |= (1 << 0) if self.mask_coords is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.alt))
        
        b.write(self.stickerset.write())
        
        if self.mask_coords is not None:
            b.write(self.mask_coords.write())
        
        return b.getvalue()
