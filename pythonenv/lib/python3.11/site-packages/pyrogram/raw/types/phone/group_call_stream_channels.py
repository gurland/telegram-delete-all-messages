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


class GroupCallStreamChannels(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.phone.GroupCallStreamChannels`.

    Details:
        - Layer: ``158``
        - ID: ``D0E482B2``

    Parameters:
        channels (List of :obj:`GroupCallStreamChannel <pyrogram.raw.base.GroupCallStreamChannel>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.GetGroupCallStreamChannels
    """

    __slots__: List[str] = ["channels"]

    ID = 0xd0e482b2
    QUALNAME = "types.phone.GroupCallStreamChannels"

    def __init__(self, *, channels: List["raw.base.GroupCallStreamChannel"]) -> None:
        self.channels = channels  # Vector<GroupCallStreamChannel>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GroupCallStreamChannels":
        # No flags
        
        channels = TLObject.read(b)
        
        return GroupCallStreamChannels(channels=channels)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.channels))
        
        return b.getvalue()
