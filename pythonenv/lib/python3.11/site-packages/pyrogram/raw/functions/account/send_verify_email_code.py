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


class SendVerifyEmailCode(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``98E037BB``

    Parameters:
        purpose (:obj:`EmailVerifyPurpose <pyrogram.raw.base.EmailVerifyPurpose>`):
            N/A

        email (``str``):
            N/A

    Returns:
        :obj:`account.SentEmailCode <pyrogram.raw.base.account.SentEmailCode>`
    """

    __slots__: List[str] = ["purpose", "email"]

    ID = 0x98e037bb
    QUALNAME = "functions.account.SendVerifyEmailCode"

    def __init__(self, *, purpose: "raw.base.EmailVerifyPurpose", email: str) -> None:
        self.purpose = purpose  # EmailVerifyPurpose
        self.email = email  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendVerifyEmailCode":
        # No flags
        
        purpose = TLObject.read(b)
        
        email = String.read(b)
        
        return SendVerifyEmailCode(purpose=purpose, email=email)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.purpose.write())
        
        b.write(String(self.email))
        
        return b.getvalue()
