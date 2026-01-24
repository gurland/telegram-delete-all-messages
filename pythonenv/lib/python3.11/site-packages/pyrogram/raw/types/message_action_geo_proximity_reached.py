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


class MessageActionGeoProximityReached(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``158``
        - ID: ``98E0D697``

    Parameters:
        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        to_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        distance (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["from_id", "to_id", "distance"]

    ID = 0x98e0d697
    QUALNAME = "types.MessageActionGeoProximityReached"

    def __init__(self, *, from_id: "raw.base.Peer", to_id: "raw.base.Peer", distance: int) -> None:
        self.from_id = from_id  # Peer
        self.to_id = to_id  # Peer
        self.distance = distance  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGeoProximityReached":
        # No flags
        
        from_id = TLObject.read(b)
        
        to_id = TLObject.read(b)
        
        distance = Int.read(b)
        
        return MessageActionGeoProximityReached(from_id=from_id, to_id=to_id, distance=distance)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.from_id.write())
        
        b.write(self.to_id.write())
        
        b.write(Int(self.distance))
        
        return b.getvalue()
