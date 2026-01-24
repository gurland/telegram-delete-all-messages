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


class CreateForumTopic(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``F40C0224``

    Parameters:
        channel (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`):
            N/A

        title (``str``):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        icon_color (``int`` ``32-bit``, *optional*):
            N/A

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "title", "random_id", "icon_color", "icon_emoji_id", "send_as"]

    ID = 0xf40c0224
    QUALNAME = "functions.channels.CreateForumTopic"

    def __init__(self, *, channel: "raw.base.InputChannel", title: str, random_id: int, icon_color: Optional[int] = None, icon_emoji_id: Optional[int] = None, send_as: "raw.base.InputPeer" = None) -> None:
        self.channel = channel  # InputChannel
        self.title = title  # string
        self.random_id = random_id  # long
        self.icon_color = icon_color  # flags.0?int
        self.icon_emoji_id = icon_emoji_id  # flags.3?long
        self.send_as = send_as  # flags.2?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateForumTopic":
        
        flags = Int.read(b)
        
        channel = TLObject.read(b)
        
        title = String.read(b)
        
        icon_color = Int.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 3) else None
        random_id = Long.read(b)
        
        send_as = TLObject.read(b) if flags & (1 << 2) else None
        
        return CreateForumTopic(channel=channel, title=title, random_id=random_id, icon_color=icon_color, icon_emoji_id=icon_emoji_id, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.icon_color is not None else 0
        flags |= (1 << 3) if self.icon_emoji_id is not None else 0
        flags |= (1 << 2) if self.send_as is not None else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(String(self.title))
        
        if self.icon_color is not None:
            b.write(Int(self.icon_color))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        b.write(Long(self.random_id))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()
