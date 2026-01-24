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


class CodeSettings(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.CodeSettings`.

    Details:
        - Layer: ``158``
        - ID: ``AD253D78``

    Parameters:
        allow_flashcall (``bool``, *optional*):
            N/A

        current_number (``bool``, *optional*):
            N/A

        allow_app_hash (``bool``, *optional*):
            N/A

        allow_missed_call (``bool``, *optional*):
            N/A

        allow_firebase (``bool``, *optional*):
            N/A

        logout_tokens (List of ``bytes``, *optional*):
            N/A

        token (``str``, *optional*):
            N/A

        app_sandbox (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["allow_flashcall", "current_number", "allow_app_hash", "allow_missed_call", "allow_firebase", "logout_tokens", "token", "app_sandbox"]

    ID = 0xad253d78
    QUALNAME = "types.CodeSettings"

    def __init__(self, *, allow_flashcall: Optional[bool] = None, current_number: Optional[bool] = None, allow_app_hash: Optional[bool] = None, allow_missed_call: Optional[bool] = None, allow_firebase: Optional[bool] = None, logout_tokens: Optional[List[bytes]] = None, token: Optional[str] = None, app_sandbox: Optional[bool] = None) -> None:
        self.allow_flashcall = allow_flashcall  # flags.0?true
        self.current_number = current_number  # flags.1?true
        self.allow_app_hash = allow_app_hash  # flags.4?true
        self.allow_missed_call = allow_missed_call  # flags.5?true
        self.allow_firebase = allow_firebase  # flags.7?true
        self.logout_tokens = logout_tokens  # flags.6?Vector<bytes>
        self.token = token  # flags.8?string
        self.app_sandbox = app_sandbox  # flags.8?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CodeSettings":
        
        flags = Int.read(b)
        
        allow_flashcall = True if flags & (1 << 0) else False
        current_number = True if flags & (1 << 1) else False
        allow_app_hash = True if flags & (1 << 4) else False
        allow_missed_call = True if flags & (1 << 5) else False
        allow_firebase = True if flags & (1 << 7) else False
        logout_tokens = TLObject.read(b, Bytes) if flags & (1 << 6) else []
        
        token = String.read(b) if flags & (1 << 8) else None
        app_sandbox = Bool.read(b) if flags & (1 << 8) else None
        return CodeSettings(allow_flashcall=allow_flashcall, current_number=current_number, allow_app_hash=allow_app_hash, allow_missed_call=allow_missed_call, allow_firebase=allow_firebase, logout_tokens=logout_tokens, token=token, app_sandbox=app_sandbox)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_flashcall else 0
        flags |= (1 << 1) if self.current_number else 0
        flags |= (1 << 4) if self.allow_app_hash else 0
        flags |= (1 << 5) if self.allow_missed_call else 0
        flags |= (1 << 7) if self.allow_firebase else 0
        flags |= (1 << 6) if self.logout_tokens else 0
        flags |= (1 << 8) if self.token is not None else 0
        flags |= (1 << 8) if self.app_sandbox is not None else 0
        b.write(Int(flags))
        
        if self.logout_tokens is not None:
            b.write(Vector(self.logout_tokens, Bytes))
        
        if self.token is not None:
            b.write(String(self.token))
        
        if self.app_sandbox is not None:
            b.write(Bool(self.app_sandbox))
        
        return b.getvalue()
