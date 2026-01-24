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


class UpdateEncryptedMessagesRead(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``158``
        - ID: ``38FE25B7``

    Parameters:
        chat_id (``int`` ``32-bit``):
            N/A

        max_date (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["chat_id", "max_date", "date"]

    ID = 0x38fe25b7
    QUALNAME = "types.UpdateEncryptedMessagesRead"

    def __init__(self, *, chat_id: int, max_date: int, date: int) -> None:
        self.chat_id = chat_id  # int
        self.max_date = max_date  # int
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEncryptedMessagesRead":
        # No flags
        
        chat_id = Int.read(b)
        
        max_date = Int.read(b)
        
        date = Int.read(b)
        
        return UpdateEncryptedMessagesRead(chat_id=chat_id, max_date=max_date, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.chat_id))
        
        b.write(Int(self.max_date))
        
        b.write(Int(self.date))
        
        return b.getvalue()
