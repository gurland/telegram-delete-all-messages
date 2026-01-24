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


class WebPage(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPage`.

    Details:
        - Layer: ``158``
        - ID: ``E89C45B2``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        url (``str``):
            N/A

        display_url (``str``):
            N/A

        hash (``int`` ``32-bit``):
            N/A

        type (``str``, *optional*):
            N/A

        site_name (``str``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        description (``str``, *optional*):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        embed_url (``str``, *optional*):
            N/A

        embed_type (``str``, *optional*):
            N/A

        embed_width (``int`` ``32-bit``, *optional*):
            N/A

        embed_height (``int`` ``32-bit``, *optional*):
            N/A

        duration (``int`` ``32-bit``, *optional*):
            N/A

        author (``str``, *optional*):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        cached_page (:obj:`Page <pyrogram.raw.base.Page>`, *optional*):
            N/A

        attributes (List of :obj:`WebPageAttribute <pyrogram.raw.base.WebPageAttribute>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPage
    """

    __slots__: List[str] = ["id", "url", "display_url", "hash", "type", "site_name", "title", "description", "photo", "embed_url", "embed_type", "embed_width", "embed_height", "duration", "author", "document", "cached_page", "attributes"]

    ID = 0xe89c45b2
    QUALNAME = "types.WebPage"

    def __init__(self, *, id: int, url: str, display_url: str, hash: int, type: Optional[str] = None, site_name: Optional[str] = None, title: Optional[str] = None, description: Optional[str] = None, photo: "raw.base.Photo" = None, embed_url: Optional[str] = None, embed_type: Optional[str] = None, embed_width: Optional[int] = None, embed_height: Optional[int] = None, duration: Optional[int] = None, author: Optional[str] = None, document: "raw.base.Document" = None, cached_page: "raw.base.Page" = None, attributes: Optional[List["raw.base.WebPageAttribute"]] = None) -> None:
        self.id = id  # long
        self.url = url  # string
        self.display_url = display_url  # string
        self.hash = hash  # int
        self.type = type  # flags.0?string
        self.site_name = site_name  # flags.1?string
        self.title = title  # flags.2?string
        self.description = description  # flags.3?string
        self.photo = photo  # flags.4?Photo
        self.embed_url = embed_url  # flags.5?string
        self.embed_type = embed_type  # flags.5?string
        self.embed_width = embed_width  # flags.6?int
        self.embed_height = embed_height  # flags.6?int
        self.duration = duration  # flags.7?int
        self.author = author  # flags.8?string
        self.document = document  # flags.9?Document
        self.cached_page = cached_page  # flags.10?Page
        self.attributes = attributes  # flags.12?Vector<WebPageAttribute>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPage":
        
        flags = Int.read(b)
        
        id = Long.read(b)
        
        url = String.read(b)
        
        display_url = String.read(b)
        
        hash = Int.read(b)
        
        type = String.read(b) if flags & (1 << 0) else None
        site_name = String.read(b) if flags & (1 << 1) else None
        title = String.read(b) if flags & (1 << 2) else None
        description = String.read(b) if flags & (1 << 3) else None
        photo = TLObject.read(b) if flags & (1 << 4) else None
        
        embed_url = String.read(b) if flags & (1 << 5) else None
        embed_type = String.read(b) if flags & (1 << 5) else None
        embed_width = Int.read(b) if flags & (1 << 6) else None
        embed_height = Int.read(b) if flags & (1 << 6) else None
        duration = Int.read(b) if flags & (1 << 7) else None
        author = String.read(b) if flags & (1 << 8) else None
        document = TLObject.read(b) if flags & (1 << 9) else None
        
        cached_page = TLObject.read(b) if flags & (1 << 10) else None
        
        attributes = TLObject.read(b) if flags & (1 << 12) else []
        
        return WebPage(id=id, url=url, display_url=display_url, hash=hash, type=type, site_name=site_name, title=title, description=description, photo=photo, embed_url=embed_url, embed_type=embed_type, embed_width=embed_width, embed_height=embed_height, duration=duration, author=author, document=document, cached_page=cached_page, attributes=attributes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.type is not None else 0
        flags |= (1 << 1) if self.site_name is not None else 0
        flags |= (1 << 2) if self.title is not None else 0
        flags |= (1 << 3) if self.description is not None else 0
        flags |= (1 << 4) if self.photo is not None else 0
        flags |= (1 << 5) if self.embed_url is not None else 0
        flags |= (1 << 5) if self.embed_type is not None else 0
        flags |= (1 << 6) if self.embed_width is not None else 0
        flags |= (1 << 6) if self.embed_height is not None else 0
        flags |= (1 << 7) if self.duration is not None else 0
        flags |= (1 << 8) if self.author is not None else 0
        flags |= (1 << 9) if self.document is not None else 0
        flags |= (1 << 10) if self.cached_page is not None else 0
        flags |= (1 << 12) if self.attributes else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.url))
        
        b.write(String(self.display_url))
        
        b.write(Int(self.hash))
        
        if self.type is not None:
            b.write(String(self.type))
        
        if self.site_name is not None:
            b.write(String(self.site_name))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.embed_url is not None:
            b.write(String(self.embed_url))
        
        if self.embed_type is not None:
            b.write(String(self.embed_type))
        
        if self.embed_width is not None:
            b.write(Int(self.embed_width))
        
        if self.embed_height is not None:
            b.write(Int(self.embed_height))
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        if self.author is not None:
            b.write(String(self.author))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.cached_page is not None:
            b.write(self.cached_page.write())
        
        if self.attributes is not None:
            b.write(Vector(self.attributes))
        
        return b.getvalue()
