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


class AppUpdate(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.help.AppUpdate`.

    Details:
        - Layer: ``158``
        - ID: ``CCBBCE30``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        version (``str``):
            N/A

        text (``str``):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            N/A

        can_not_skip (``bool``, *optional*):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

        sticker (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            help.GetAppUpdate
    """

    __slots__: List[str] = ["id", "version", "text", "entities", "can_not_skip", "document", "url", "sticker"]

    ID = 0xccbbce30
    QUALNAME = "types.help.AppUpdate"

    def __init__(self, *, id: int, version: str, text: str, entities: List["raw.base.MessageEntity"], can_not_skip: Optional[bool] = None, document: "raw.base.Document" = None, url: Optional[str] = None, sticker: "raw.base.Document" = None) -> None:
        self.id = id  # int
        self.version = version  # string
        self.text = text  # string
        self.entities = entities  # Vector<MessageEntity>
        self.can_not_skip = can_not_skip  # flags.0?true
        self.document = document  # flags.1?Document
        self.url = url  # flags.2?string
        self.sticker = sticker  # flags.3?Document

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AppUpdate":
        
        flags = Int.read(b)
        
        can_not_skip = True if flags & (1 << 0) else False
        id = Int.read(b)
        
        version = String.read(b)
        
        text = String.read(b)
        
        entities = TLObject.read(b)
        
        document = TLObject.read(b) if flags & (1 << 1) else None
        
        url = String.read(b) if flags & (1 << 2) else None
        sticker = TLObject.read(b) if flags & (1 << 3) else None
        
        return AppUpdate(id=id, version=version, text=text, entities=entities, can_not_skip=can_not_skip, document=document, url=url, sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_not_skip else 0
        flags |= (1 << 1) if self.document is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        flags |= (1 << 3) if self.sticker is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.version))
        
        b.write(String(self.text))
        
        b.write(Vector(self.entities))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.sticker is not None:
            b.write(self.sticker.write())
        
        return b.getvalue()
