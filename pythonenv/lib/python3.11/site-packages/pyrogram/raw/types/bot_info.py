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


class BotInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.BotInfo`.

    Details:
        - Layer: ``158``
        - ID: ``8F300B57``

    Parameters:
        user_id (``int`` ``64-bit``, *optional*):
            N/A

        description (``str``, *optional*):
            N/A

        description_photo (:obj:`Photo <pyrogram.raw.base.Photo>`, *optional*):
            N/A

        description_document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        commands (List of :obj:`BotCommand <pyrogram.raw.base.BotCommand>`, *optional*):
            N/A

        menu_button (:obj:`BotMenuButton <pyrogram.raw.base.BotMenuButton>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "description", "description_photo", "description_document", "commands", "menu_button"]

    ID = 0x8f300b57
    QUALNAME = "types.BotInfo"

    def __init__(self, *, user_id: Optional[int] = None, description: Optional[str] = None, description_photo: "raw.base.Photo" = None, description_document: "raw.base.Document" = None, commands: Optional[List["raw.base.BotCommand"]] = None, menu_button: "raw.base.BotMenuButton" = None) -> None:
        self.user_id = user_id  # flags.0?long
        self.description = description  # flags.1?string
        self.description_photo = description_photo  # flags.4?Photo
        self.description_document = description_document  # flags.5?Document
        self.commands = commands  # flags.2?Vector<BotCommand>
        self.menu_button = menu_button  # flags.3?BotMenuButton

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInfo":
        
        flags = Int.read(b)
        
        user_id = Long.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        description_photo = TLObject.read(b) if flags & (1 << 4) else None
        
        description_document = TLObject.read(b) if flags & (1 << 5) else None
        
        commands = TLObject.read(b) if flags & (1 << 2) else []
        
        menu_button = TLObject.read(b) if flags & (1 << 3) else None
        
        return BotInfo(user_id=user_id, description=description, description_photo=description_photo, description_document=description_document, commands=commands, menu_button=menu_button)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.user_id is not None else 0
        flags |= (1 << 1) if self.description is not None else 0
        flags |= (1 << 4) if self.description_photo is not None else 0
        flags |= (1 << 5) if self.description_document is not None else 0
        flags |= (1 << 2) if self.commands else 0
        flags |= (1 << 3) if self.menu_button is not None else 0
        b.write(Int(flags))
        
        if self.user_id is not None:
            b.write(Long(self.user_id))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.description_photo is not None:
            b.write(self.description_photo.write())
        
        if self.description_document is not None:
            b.write(self.description_document.write())
        
        if self.commands is not None:
            b.write(Vector(self.commands))
        
        if self.menu_button is not None:
            b.write(self.menu_button.write())
        
        return b.getvalue()
