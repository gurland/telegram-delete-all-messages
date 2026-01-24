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


class BotApp(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.BotApp`.

    Details:
        - Layer: ``158``
        - ID: ``EB50ADF5``

    Parameters:
        app (:obj:`BotApp <pyrogram.raw.base.BotApp>`):
            N/A

        inactive (``bool``, *optional*):
            N/A

        request_write_access (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetBotApp
    """

    __slots__: List[str] = ["app", "inactive", "request_write_access"]

    ID = 0xeb50adf5
    QUALNAME = "types.messages.BotApp"

    def __init__(self, *, app: "raw.base.BotApp", inactive: Optional[bool] = None, request_write_access: Optional[bool] = None) -> None:
        self.app = app  # BotApp
        self.inactive = inactive  # flags.0?true
        self.request_write_access = request_write_access  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotApp":
        
        flags = Int.read(b)
        
        inactive = True if flags & (1 << 0) else False
        request_write_access = True if flags & (1 << 1) else False
        app = TLObject.read(b)
        
        return BotApp(app=app, inactive=inactive, request_write_access=request_write_access)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.inactive else 0
        flags |= (1 << 1) if self.request_write_access else 0
        b.write(Int(flags))
        
        b.write(self.app.write())
        
        return b.getvalue()
