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


class MessageExtendedMediaPreview(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageExtendedMedia`.

    Details:
        - Layer: ``158``
        - ID: ``AD628CC8``

    Parameters:
        w (``int`` ``32-bit``, *optional*):
            N/A

        h (``int`` ``32-bit``, *optional*):
            N/A

        thumb (:obj:`PhotoSize <pyrogram.raw.base.PhotoSize>`, *optional*):
            N/A

        video_duration (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["w", "h", "thumb", "video_duration"]

    ID = 0xad628cc8
    QUALNAME = "types.MessageExtendedMediaPreview"

    def __init__(self, *, w: Optional[int] = None, h: Optional[int] = None, thumb: "raw.base.PhotoSize" = None, video_duration: Optional[int] = None) -> None:
        self.w = w  # flags.0?int
        self.h = h  # flags.0?int
        self.thumb = thumb  # flags.1?PhotoSize
        self.video_duration = video_duration  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageExtendedMediaPreview":
        
        flags = Int.read(b)
        
        w = Int.read(b) if flags & (1 << 0) else None
        h = Int.read(b) if flags & (1 << 0) else None
        thumb = TLObject.read(b) if flags & (1 << 1) else None
        
        video_duration = Int.read(b) if flags & (1 << 2) else None
        return MessageExtendedMediaPreview(w=w, h=h, thumb=thumb, video_duration=video_duration)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.w is not None else 0
        flags |= (1 << 0) if self.h is not None else 0
        flags |= (1 << 1) if self.thumb is not None else 0
        flags |= (1 << 2) if self.video_duration is not None else 0
        b.write(Int(flags))
        
        if self.w is not None:
            b.write(Int(self.w))
        
        if self.h is not None:
            b.write(Int(self.h))
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        if self.video_duration is not None:
            b.write(Int(self.video_duration))
        
        return b.getvalue()
