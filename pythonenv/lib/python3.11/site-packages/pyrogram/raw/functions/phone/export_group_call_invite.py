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


class ExportGroupCallInvite(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``E6AA647F``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        can_self_unmute (``bool``, *optional*):
            N/A

    Returns:
        :obj:`phone.ExportedGroupCallInvite <pyrogram.raw.base.phone.ExportedGroupCallInvite>`
    """

    __slots__: List[str] = ["call", "can_self_unmute"]

    ID = 0xe6aa647f
    QUALNAME = "functions.phone.ExportGroupCallInvite"

    def __init__(self, *, call: "raw.base.InputGroupCall", can_self_unmute: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.can_self_unmute = can_self_unmute  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportGroupCallInvite":
        
        flags = Int.read(b)
        
        can_self_unmute = True if flags & (1 << 0) else False
        call = TLObject.read(b)
        
        return ExportGroupCallInvite(call=call, can_self_unmute=can_self_unmute)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_self_unmute else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        return b.getvalue()
