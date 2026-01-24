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


class AvailableReaction(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.AvailableReaction`.

    Details:
        - Layer: ``158``
        - ID: ``C077EC01``

    Parameters:
        reaction (``str``):
            N/A

        title (``str``):
            N/A

        static_icon (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        appear_animation (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        select_animation (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        activate_animation (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        effect_animation (:obj:`Document <pyrogram.raw.base.Document>`):
            N/A

        inactive (``bool``, *optional*):
            N/A

        premium (``bool``, *optional*):
            N/A

        around_animation (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        center_icon (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["reaction", "title", "static_icon", "appear_animation", "select_animation", "activate_animation", "effect_animation", "inactive", "premium", "around_animation", "center_icon"]

    ID = 0xc077ec01
    QUALNAME = "types.AvailableReaction"

    def __init__(self, *, reaction: str, title: str, static_icon: "raw.base.Document", appear_animation: "raw.base.Document", select_animation: "raw.base.Document", activate_animation: "raw.base.Document", effect_animation: "raw.base.Document", inactive: Optional[bool] = None, premium: Optional[bool] = None, around_animation: "raw.base.Document" = None, center_icon: "raw.base.Document" = None) -> None:
        self.reaction = reaction  # string
        self.title = title  # string
        self.static_icon = static_icon  # Document
        self.appear_animation = appear_animation  # Document
        self.select_animation = select_animation  # Document
        self.activate_animation = activate_animation  # Document
        self.effect_animation = effect_animation  # Document
        self.inactive = inactive  # flags.0?true
        self.premium = premium  # flags.2?true
        self.around_animation = around_animation  # flags.1?Document
        self.center_icon = center_icon  # flags.1?Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AvailableReaction":
        
        flags = Int.read(b)
        
        inactive = True if flags & (1 << 0) else False
        premium = True if flags & (1 << 2) else False
        reaction = String.read(b)
        
        title = String.read(b)
        
        static_icon = TLObject.read(b)
        
        appear_animation = TLObject.read(b)
        
        select_animation = TLObject.read(b)
        
        activate_animation = TLObject.read(b)
        
        effect_animation = TLObject.read(b)
        
        around_animation = TLObject.read(b) if flags & (1 << 1) else None
        
        center_icon = TLObject.read(b) if flags & (1 << 1) else None
        
        return AvailableReaction(reaction=reaction, title=title, static_icon=static_icon, appear_animation=appear_animation, select_animation=select_animation, activate_animation=activate_animation, effect_animation=effect_animation, inactive=inactive, premium=premium, around_animation=around_animation, center_icon=center_icon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.inactive else 0
        flags |= (1 << 2) if self.premium else 0
        flags |= (1 << 1) if self.around_animation is not None else 0
        flags |= (1 << 1) if self.center_icon is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.reaction))
        
        b.write(String(self.title))
        
        b.write(self.static_icon.write())
        
        b.write(self.appear_animation.write())
        
        b.write(self.select_animation.write())
        
        b.write(self.activate_animation.write())
        
        b.write(self.effect_animation.write())
        
        if self.around_animation is not None:
            b.write(self.around_animation.write())
        
        if self.center_icon is not None:
            b.write(self.center_icon.write())
        
        return b.getvalue()
