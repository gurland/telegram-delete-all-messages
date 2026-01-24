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


class MsgDetailedInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MsgDetailedInfo`.

    Details:
        - Layer: ``158``
        - ID: ``276D3EC6``

    Parameters:
        msg_id (``int`` ``64-bit``):
            N/A

        answer_msg_id (``int`` ``64-bit``):
            N/A

        bytes (``int`` ``32-bit``):
            N/A

        status (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["msg_id", "answer_msg_id", "bytes", "status"]

    ID = 0x276d3ec6
    QUALNAME = "types.MsgDetailedInfo"

    def __init__(self, *, msg_id: int, answer_msg_id: int, bytes: int, status: int) -> None:
        self.msg_id = msg_id  # long
        self.answer_msg_id = answer_msg_id  # long
        self.bytes = bytes  # int
        self.status = status  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MsgDetailedInfo":
        # No flags
        
        msg_id = Long.read(b)
        
        answer_msg_id = Long.read(b)
        
        bytes = Int.read(b)
        
        status = Int.read(b)
        
        return MsgDetailedInfo(msg_id=msg_id, answer_msg_id=answer_msg_id, bytes=bytes, status=status)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.msg_id))
        
        b.write(Long(self.answer_msg_id))
        
        b.write(Int(self.bytes))
        
        b.write(Int(self.status))
        
        return b.getvalue()
