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


class ChannelAdminLogEvent(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEvent`.

    Details:
        - Layer: ``158``
        - ID: ``1FAD68CD``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        user_id (``int`` ``64-bit``):
            N/A

        action (:obj:`ChannelAdminLogEventAction <pyrogram.raw.base.ChannelAdminLogEventAction>`):
            N/A

    """

    __slots__: List[str] = ["id", "date", "user_id", "action"]

    ID = 0x1fad68cd
    QUALNAME = "types.ChannelAdminLogEvent"

    def __init__(self, *, id: int, date: int, user_id: int, action: "raw.base.ChannelAdminLogEventAction") -> None:
        self.id = id  # long
        self.date = date  # int
        self.user_id = user_id  # long
        self.action = action  # ChannelAdminLogEventAction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEvent":
        # No flags
        
        id = Long.read(b)
        
        date = Int.read(b)
        
        user_id = Long.read(b)
        
        action = TLObject.read(b)
        
        return ChannelAdminLogEvent(id=id, date=date, user_id=user_id, action=action)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Int(self.date))
        
        b.write(Long(self.user_id))
        
        b.write(self.action.write())
        
        return b.getvalue()
