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


class MessageActionBotAllowed(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``158``
        - ID: ``C516D679``

    Parameters:
        attach_menu (``bool``, *optional*):
            N/A

        domain (``str``, *optional*):
            N/A

        app (:obj:`BotApp <pyrogram.raw.base.BotApp>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["attach_menu", "domain", "app"]

    ID = 0xc516d679
    QUALNAME = "types.MessageActionBotAllowed"

    def __init__(self, *, attach_menu: Optional[bool] = None, domain: Optional[str] = None, app: "raw.base.BotApp" = None) -> None:
        self.attach_menu = attach_menu  # flags.1?true
        self.domain = domain  # flags.0?string
        self.app = app  # flags.2?BotApp

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionBotAllowed":
        
        flags = Int.read(b)
        
        attach_menu = True if flags & (1 << 1) else False
        domain = String.read(b) if flags & (1 << 0) else None
        app = TLObject.read(b) if flags & (1 << 2) else None
        
        return MessageActionBotAllowed(attach_menu=attach_menu, domain=domain, app=app)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.attach_menu else 0
        flags |= (1 << 0) if self.domain is not None else 0
        flags |= (1 << 2) if self.app is not None else 0
        b.write(Int(flags))
        
        if self.domain is not None:
            b.write(String(self.domain))
        
        if self.app is not None:
            b.write(self.app.write())
        
        return b.getvalue()
