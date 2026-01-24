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


class WallPaperSettings(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WallPaperSettings`.

    Details:
        - Layer: ``158``
        - ID: ``1DC1BCA4``

    Parameters:
        blur (``bool``, *optional*):
            N/A

        motion (``bool``, *optional*):
            N/A

        background_color (``int`` ``32-bit``, *optional*):
            N/A

        second_background_color (``int`` ``32-bit``, *optional*):
            N/A

        third_background_color (``int`` ``32-bit``, *optional*):
            N/A

        fourth_background_color (``int`` ``32-bit``, *optional*):
            N/A

        intensity (``int`` ``32-bit``, *optional*):
            N/A

        rotation (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["blur", "motion", "background_color", "second_background_color", "third_background_color", "fourth_background_color", "intensity", "rotation"]

    ID = 0x1dc1bca4
    QUALNAME = "types.WallPaperSettings"

    def __init__(self, *, blur: Optional[bool] = None, motion: Optional[bool] = None, background_color: Optional[int] = None, second_background_color: Optional[int] = None, third_background_color: Optional[int] = None, fourth_background_color: Optional[int] = None, intensity: Optional[int] = None, rotation: Optional[int] = None) -> None:
        self.blur = blur  # flags.1?true
        self.motion = motion  # flags.2?true
        self.background_color = background_color  # flags.0?int
        self.second_background_color = second_background_color  # flags.4?int
        self.third_background_color = third_background_color  # flags.5?int
        self.fourth_background_color = fourth_background_color  # flags.6?int
        self.intensity = intensity  # flags.3?int
        self.rotation = rotation  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WallPaperSettings":
        
        flags = Int.read(b)
        
        blur = True if flags & (1 << 1) else False
        motion = True if flags & (1 << 2) else False
        background_color = Int.read(b) if flags & (1 << 0) else None
        second_background_color = Int.read(b) if flags & (1 << 4) else None
        third_background_color = Int.read(b) if flags & (1 << 5) else None
        fourth_background_color = Int.read(b) if flags & (1 << 6) else None
        intensity = Int.read(b) if flags & (1 << 3) else None
        rotation = Int.read(b) if flags & (1 << 4) else None
        return WallPaperSettings(blur=blur, motion=motion, background_color=background_color, second_background_color=second_background_color, third_background_color=third_background_color, fourth_background_color=fourth_background_color, intensity=intensity, rotation=rotation)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.blur else 0
        flags |= (1 << 2) if self.motion else 0
        flags |= (1 << 0) if self.background_color is not None else 0
        flags |= (1 << 4) if self.second_background_color is not None else 0
        flags |= (1 << 5) if self.third_background_color is not None else 0
        flags |= (1 << 6) if self.fourth_background_color is not None else 0
        flags |= (1 << 3) if self.intensity is not None else 0
        flags |= (1 << 4) if self.rotation is not None else 0
        b.write(Int(flags))
        
        if self.background_color is not None:
            b.write(Int(self.background_color))
        
        if self.second_background_color is not None:
            b.write(Int(self.second_background_color))
        
        if self.third_background_color is not None:
            b.write(Int(self.third_background_color))
        
        if self.fourth_background_color is not None:
            b.write(Int(self.fourth_background_color))
        
        if self.intensity is not None:
            b.write(Int(self.intensity))
        
        if self.rotation is not None:
            b.write(Int(self.rotation))
        
        return b.getvalue()
