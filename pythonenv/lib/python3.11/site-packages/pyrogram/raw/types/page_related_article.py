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


class PageRelatedArticle(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PageRelatedArticle`.

    Details:
        - Layer: ``158``
        - ID: ``B390DC08``

    Parameters:
        url (``str``):
            N/A

        webpage_id (``int`` ``64-bit``):
            N/A

        title (``str``, *optional*):
            N/A

        description (``str``, *optional*):
            N/A

        photo_id (``int`` ``64-bit``, *optional*):
            N/A

        author (``str``, *optional*):
            N/A

        published_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["url", "webpage_id", "title", "description", "photo_id", "author", "published_date"]

    ID = 0xb390dc08
    QUALNAME = "types.PageRelatedArticle"

    def __init__(self, *, url: str, webpage_id: int, title: Optional[str] = None, description: Optional[str] = None, photo_id: Optional[int] = None, author: Optional[str] = None, published_date: Optional[int] = None) -> None:
        self.url = url  # string
        self.webpage_id = webpage_id  # long
        self.title = title  # flags.0?string
        self.description = description  # flags.1?string
        self.photo_id = photo_id  # flags.2?long
        self.author = author  # flags.3?string
        self.published_date = published_date  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageRelatedArticle":
        
        flags = Int.read(b)
        
        url = String.read(b)
        
        webpage_id = Long.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        photo_id = Long.read(b) if flags & (1 << 2) else None
        author = String.read(b) if flags & (1 << 3) else None
        published_date = Int.read(b) if flags & (1 << 4) else None
        return PageRelatedArticle(url=url, webpage_id=webpage_id, title=title, description=description, photo_id=photo_id, author=author, published_date=published_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.description is not None else 0
        flags |= (1 << 2) if self.photo_id is not None else 0
        flags |= (1 << 3) if self.author is not None else 0
        flags |= (1 << 4) if self.published_date is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        b.write(Long(self.webpage_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.photo_id is not None:
            b.write(Long(self.photo_id))
        
        if self.author is not None:
            b.write(String(self.author))
        
        if self.published_date is not None:
            b.write(Int(self.published_date))
        
        return b.getvalue()
