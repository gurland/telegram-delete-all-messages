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


class Game(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Game`.

    Details:
        - Layer: ``158``
        - ID: ``BDF9653B``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        short_name (``str``):
            N/A

        title (``str``):
            N/A

        description (``str``):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "access_hash", "short_name", "title", "description", "photo", "document"]

    ID = 0xbdf9653b
    QUALNAME = "types.Game"

    def __init__(self, *, id: int, access_hash: int, short_name: str, title: str, description: str, photo: "raw.base.Photo", document: "raw.base.Document" = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.short_name = short_name  # string
        self.title = title  # string
        self.description = description  # string
        self.photo = photo  # Photo
        self.document = document  # flags.0?Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Game":
        
        flags = Int.read(b)
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        short_name = String.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b)
        
        document = TLObject.read(b) if flags & (1 << 0) else None
        
        return Game(id=id, access_hash=access_hash, short_name=short_name, title=title, description=description, photo=photo, document=document)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.document is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.short_name))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        b.write(self.photo.write())
        
        if self.document is not None:
            b.write(self.document.write())
        
        return b.getvalue()
