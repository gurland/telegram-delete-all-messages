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


class MessageActionSetMessagesTTL(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``158``
        - ID: ``3C134D7B``

    Parameters:
        period (``int`` ``32-bit``):
            N/A

        auto_setting_from (``int`` ``64-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["period", "auto_setting_from"]

    ID = 0x3c134d7b
    QUALNAME = "types.MessageActionSetMessagesTTL"

    def __init__(self, *, period: int, auto_setting_from: Optional[int] = None) -> None:
        self.period = period  # int
        self.auto_setting_from = auto_setting_from  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetMessagesTTL":
        
        flags = Int.read(b)
        
        period = Int.read(b)
        
        auto_setting_from = Long.read(b) if flags & (1 << 0) else None
        return MessageActionSetMessagesTTL(period=period, auto_setting_from=auto_setting_from)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.auto_setting_from is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.period))
        
        if self.auto_setting_from is not None:
            b.write(Long(self.auto_setting_from))
        
        return b.getvalue()
