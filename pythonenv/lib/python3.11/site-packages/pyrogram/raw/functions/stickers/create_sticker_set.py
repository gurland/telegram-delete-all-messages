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


class CreateStickerSet(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``9021AB67``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        title (``str``):
            N/A

        short_name (``str``):
            N/A

        stickers (List of :obj:`InputStickerSetItem <pyrogram.raw.base.InputStickerSetItem>`):
            N/A

        masks (``bool``, *optional*):
            N/A

        animated (``bool``, *optional*):
            N/A

        videos (``bool``, *optional*):
            N/A

        emojis (``bool``, *optional*):
            N/A

        text_color (``bool``, *optional*):
            N/A

        thumb (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

        software (``str``, *optional*):
            N/A

    Returns:
        :obj:`messages.StickerSet <pyrogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["user_id", "title", "short_name", "stickers", "masks", "animated", "videos", "emojis", "text_color", "thumb", "software"]

    ID = 0x9021ab67
    QUALNAME = "functions.stickers.CreateStickerSet"

    def __init__(self, *, user_id: "raw.base.InputUser", title: str, short_name: str, stickers: List["raw.base.InputStickerSetItem"], masks: Optional[bool] = None, animated: Optional[bool] = None, videos: Optional[bool] = None, emojis: Optional[bool] = None, text_color: Optional[bool] = None, thumb: "raw.base.InputDocument" = None, software: Optional[str] = None) -> None:
        self.user_id = user_id  # InputUser
        self.title = title  # string
        self.short_name = short_name  # string
        self.stickers = stickers  # Vector<InputStickerSetItem>
        self.masks = masks  # flags.0?true
        self.animated = animated  # flags.1?true
        self.videos = videos  # flags.4?true
        self.emojis = emojis  # flags.5?true
        self.text_color = text_color  # flags.6?true
        self.thumb = thumb  # flags.2?InputDocument
        self.software = software  # flags.3?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateStickerSet":
        
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        animated = True if flags & (1 << 1) else False
        videos = True if flags & (1 << 4) else False
        emojis = True if flags & (1 << 5) else False
        text_color = True if flags & (1 << 6) else False
        user_id = TLObject.read(b)
        
        title = String.read(b)
        
        short_name = String.read(b)
        
        thumb = TLObject.read(b) if flags & (1 << 2) else None
        
        stickers = TLObject.read(b)
        
        software = String.read(b) if flags & (1 << 3) else None
        return CreateStickerSet(user_id=user_id, title=title, short_name=short_name, stickers=stickers, masks=masks, animated=animated, videos=videos, emojis=emojis, text_color=text_color, thumb=thumb, software=software)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks else 0
        flags |= (1 << 1) if self.animated else 0
        flags |= (1 << 4) if self.videos else 0
        flags |= (1 << 5) if self.emojis else 0
        flags |= (1 << 6) if self.text_color else 0
        flags |= (1 << 2) if self.thumb is not None else 0
        flags |= (1 << 3) if self.software is not None else 0
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(String(self.title))
        
        b.write(String(self.short_name))
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        b.write(Vector(self.stickers))
        
        if self.software is not None:
            b.write(String(self.software))
        
        return b.getvalue()
