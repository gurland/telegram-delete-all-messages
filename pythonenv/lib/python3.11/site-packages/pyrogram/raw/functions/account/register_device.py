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


class RegisterDevice(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``EC86017A``

    Parameters:
        token_type (``int`` ``32-bit``):
            N/A

        token (``str``):
            N/A

        app_sandbox (``bool``):
            N/A

        secret (``bytes``):
            N/A

        other_uids (List of ``int`` ``64-bit``):
            N/A

        no_muted (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["token_type", "token", "app_sandbox", "secret", "other_uids", "no_muted"]

    ID = 0xec86017a
    QUALNAME = "functions.account.RegisterDevice"

    def __init__(self, *, token_type: int, token: str, app_sandbox: bool, secret: bytes, other_uids: List[int], no_muted: Optional[bool] = None) -> None:
        self.token_type = token_type  # int
        self.token = token  # string
        self.app_sandbox = app_sandbox  # Bool
        self.secret = secret  # bytes
        self.other_uids = other_uids  # Vector<long>
        self.no_muted = no_muted  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RegisterDevice":
        
        flags = Int.read(b)
        
        no_muted = True if flags & (1 << 0) else False
        token_type = Int.read(b)
        
        token = String.read(b)
        
        app_sandbox = Bool.read(b)
        
        secret = Bytes.read(b)
        
        other_uids = TLObject.read(b, Long)
        
        return RegisterDevice(token_type=token_type, token=token, app_sandbox=app_sandbox, secret=secret, other_uids=other_uids, no_muted=no_muted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.no_muted else 0
        b.write(Int(flags))
        
        b.write(Int(self.token_type))
        
        b.write(String(self.token))
        
        b.write(Bool(self.app_sandbox))
        
        b.write(Bytes(self.secret))
        
        b.write(Vector(self.other_uids, Long))
        
        return b.getvalue()
