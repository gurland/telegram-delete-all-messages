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


class BlockFromReplies(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``29A8962C``

    Parameters:
        msg_id (``int`` ``32-bit``):
            N/A

        delete_message (``bool``, *optional*):
            N/A

        delete_history (``bool``, *optional*):
            N/A

        report_spam (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["msg_id", "delete_message", "delete_history", "report_spam"]

    ID = 0x29a8962c
    QUALNAME = "functions.contacts.BlockFromReplies"

    def __init__(self, *, msg_id: int, delete_message: Optional[bool] = None, delete_history: Optional[bool] = None, report_spam: Optional[bool] = None) -> None:
        self.msg_id = msg_id  # int
        self.delete_message = delete_message  # flags.0?true
        self.delete_history = delete_history  # flags.1?true
        self.report_spam = report_spam  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BlockFromReplies":
        
        flags = Int.read(b)
        
        delete_message = True if flags & (1 << 0) else False
        delete_history = True if flags & (1 << 1) else False
        report_spam = True if flags & (1 << 2) else False
        msg_id = Int.read(b)
        
        return BlockFromReplies(msg_id=msg_id, delete_message=delete_message, delete_history=delete_history, report_spam=report_spam)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.delete_message else 0
        flags |= (1 << 1) if self.delete_history else 0
        flags |= (1 << 2) if self.report_spam else 0
        b.write(Int(flags))
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
