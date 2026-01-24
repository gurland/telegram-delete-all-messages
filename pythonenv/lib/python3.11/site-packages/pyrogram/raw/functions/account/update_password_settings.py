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


class UpdatePasswordSettings(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``A59B102F``

    Parameters:
        password (:obj:`InputCheckPasswordSRP <pyrogram.raw.base.InputCheckPasswordSRP>`):
            N/A

        new_settings (:obj:`account.PasswordInputSettings <pyrogram.raw.base.account.PasswordInputSettings>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["password", "new_settings"]

    ID = 0xa59b102f
    QUALNAME = "functions.account.UpdatePasswordSettings"

    def __init__(self, *, password: "raw.base.InputCheckPasswordSRP", new_settings: "raw.base.account.PasswordInputSettings") -> None:
        self.password = password  # InputCheckPasswordSRP
        self.new_settings = new_settings  # account.PasswordInputSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePasswordSettings":
        # No flags
        
        password = TLObject.read(b)
        
        new_settings = TLObject.read(b)
        
        return UpdatePasswordSettings(password=password, new_settings=new_settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.password.write())
        
        b.write(self.new_settings.write())
        
        return b.getvalue()
