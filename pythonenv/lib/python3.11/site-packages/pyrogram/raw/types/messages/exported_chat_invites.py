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


class ExportedChatInvites(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.messages.ExportedChatInvites`.

    Details:
        - Layer: ``158``
        - ID: ``BDC62DCC``

    Parameters:
        count (``int`` ``32-bit``):
            N/A

        invites (List of :obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetExportedChatInvites
    """

    __slots__: List[str] = ["count", "invites", "users"]

    ID = 0xbdc62dcc
    QUALNAME = "types.messages.ExportedChatInvites"

    def __init__(self, *, count: int, invites: List["raw.base.ExportedChatInvite"], users: List["raw.base.User"]) -> None:
        self.count = count  # int
        self.invites = invites  # Vector<ExportedChatInvite>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportedChatInvites":
        # No flags
        
        count = Int.read(b)
        
        invites = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ExportedChatInvites(count=count, invites=invites, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.count))
        
        b.write(Vector(self.invites))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
