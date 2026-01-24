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


class RequestFirebaseSms(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``89464B50``

    Parameters:
        phone_number (``str``):
            N/A

        phone_code_hash (``str``):
            N/A

        safety_net_token (``str``, *optional*):
            N/A

        ios_push_secret (``str``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["phone_number", "phone_code_hash", "safety_net_token", "ios_push_secret"]

    ID = 0x89464b50
    QUALNAME = "functions.auth.RequestFirebaseSms"

    def __init__(self, *, phone_number: str, phone_code_hash: str, safety_net_token: Optional[str] = None, ios_push_secret: Optional[str] = None) -> None:
        self.phone_number = phone_number  # string
        self.phone_code_hash = phone_code_hash  # string
        self.safety_net_token = safety_net_token  # flags.0?string
        self.ios_push_secret = ios_push_secret  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestFirebaseSms":
        
        flags = Int.read(b)
        
        phone_number = String.read(b)
        
        phone_code_hash = String.read(b)
        
        safety_net_token = String.read(b) if flags & (1 << 0) else None
        ios_push_secret = String.read(b) if flags & (1 << 1) else None
        return RequestFirebaseSms(phone_number=phone_number, phone_code_hash=phone_code_hash, safety_net_token=safety_net_token, ios_push_secret=ios_push_secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.safety_net_token is not None else 0
        flags |= (1 << 1) if self.ios_push_secret is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.phone_number))
        
        b.write(String(self.phone_code_hash))
        
        if self.safety_net_token is not None:
            b.write(String(self.safety_net_token))
        
        if self.ios_push_secret is not None:
            b.write(String(self.ios_push_secret))
        
        return b.getvalue()
