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


class MessageActionTopicCreate(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``158``
        - ID: ``D999256``

    Parameters:
        title (``str``):
            N/A

        icon_color (``int`` ``32-bit``):
            N/A

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["title", "icon_color", "icon_emoji_id"]

    ID = 0xd999256
    QUALNAME = "types.MessageActionTopicCreate"

    def __init__(self, *, title: str, icon_color: int, icon_emoji_id: Optional[int] = None) -> None:
        self.title = title  # string
        self.icon_color = icon_color  # int
        self.icon_emoji_id = icon_emoji_id  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionTopicCreate":
        
        flags = Int.read(b)
        
        title = String.read(b)
        
        icon_color = Int.read(b)
        
        icon_emoji_id = Long.read(b) if flags & (1 << 0) else None
        return MessageActionTopicCreate(title=title, icon_color=icon_color, icon_emoji_id=icon_emoji_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.icon_emoji_id is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(Int(self.icon_color))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        return b.getvalue()
