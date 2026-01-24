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


class Theme(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Theme`.

    Details:
        - Layer: ``158``
        - ID: ``A00E67D6``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        slug (``str``):
            N/A

        title (``str``):
            N/A

        creator (``bool``, *optional*):
            N/A

        default (``bool``, *optional*):
            N/A

        for_chat (``bool``, *optional*):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        settings (List of :obj:`ThemeSettings <pyrogram.raw.base.ThemeSettings>`, *optional*):
            N/A

        emoticon (``str``, *optional*):
            N/A

        installs_count (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.CreateTheme
            account.UpdateTheme
            account.GetTheme
    """

    __slots__: List[str] = ["id", "access_hash", "slug", "title", "creator", "default", "for_chat", "document", "settings", "emoticon", "installs_count"]

    ID = 0xa00e67d6
    QUALNAME = "types.Theme"

    def __init__(self, *, id: int, access_hash: int, slug: str, title: str, creator: Optional[bool] = None, default: Optional[bool] = None, for_chat: Optional[bool] = None, document: "raw.base.Document" = None, settings: Optional[List["raw.base.ThemeSettings"]] = None, emoticon: Optional[str] = None, installs_count: Optional[int] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.slug = slug  # string
        self.title = title  # string
        self.creator = creator  # flags.0?true
        self.default = default  # flags.1?true
        self.for_chat = for_chat  # flags.5?true
        self.document = document  # flags.2?Document
        self.settings = settings  # flags.3?Vector<ThemeSettings>
        self.emoticon = emoticon  # flags.6?string
        self.installs_count = installs_count  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Theme":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        default = True if flags & (1 << 1) else False
        for_chat = True if flags & (1 << 5) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        slug = String.read(b)
        
        title = String.read(b)
        
        document = TLObject.read(b) if flags & (1 << 2) else None
        
        settings = TLObject.read(b) if flags & (1 << 3) else []
        
        emoticon = String.read(b) if flags & (1 << 6) else None
        installs_count = Int.read(b) if flags & (1 << 4) else None
        return Theme(id=id, access_hash=access_hash, slug=slug, title=title, creator=creator, default=default, for_chat=for_chat, document=document, settings=settings, emoticon=emoticon, installs_count=installs_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 1) if self.default else 0
        flags |= (1 << 5) if self.for_chat else 0
        flags |= (1 << 2) if self.document is not None else 0
        flags |= (1 << 3) if self.settings else 0
        flags |= (1 << 6) if self.emoticon is not None else 0
        flags |= (1 << 4) if self.installs_count is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.slug))
        
        b.write(String(self.title))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.settings is not None:
            b.write(Vector(self.settings))
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        if self.installs_count is not None:
            b.write(Int(self.installs_count))
        
        return b.getvalue()
