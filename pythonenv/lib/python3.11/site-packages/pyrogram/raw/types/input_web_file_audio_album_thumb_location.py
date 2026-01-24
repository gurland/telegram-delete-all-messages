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


class InputWebFileAudioAlbumThumbLocation(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputWebFileLocation`.

    Details:
        - Layer: ``158``
        - ID: ``F46FE924``

    Parameters:
        small (``bool``, *optional*):
            N/A

        document (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        performer (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["small", "document", "title", "performer"]

    ID = 0xf46fe924
    QUALNAME = "types.InputWebFileAudioAlbumThumbLocation"

    def __init__(self, *, small: Optional[bool] = None, document: "raw.base.InputDocument" = None, title: Optional[str] = None, performer: Optional[str] = None) -> None:
        self.small = small  # flags.2?true
        self.document = document  # flags.0?InputDocument
        self.title = title  # flags.1?string
        self.performer = performer  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputWebFileAudioAlbumThumbLocation":
        
        flags = Int.read(b)
        
        small = True if flags & (1 << 2) else False
        document = TLObject.read(b) if flags & (1 << 0) else None
        
        title = String.read(b) if flags & (1 << 1) else None
        performer = String.read(b) if flags & (1 << 1) else None
        return InputWebFileAudioAlbumThumbLocation(small=small, document=document, title=title, performer=performer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.small else 0
        flags |= (1 << 0) if self.document is not None else 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 1) if self.performer is not None else 0
        b.write(Int(flags))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.performer is not None:
            b.write(String(self.performer))
        
        return b.getvalue()
