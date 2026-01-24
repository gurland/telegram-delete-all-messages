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


class PhoneCall(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PhoneCall`.

    Details:
        - Layer: ``158``
        - ID: ``967F7C67``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        admin_id (``int`` ``64-bit``):
            N/A

        participant_id (``int`` ``64-bit``):
            N/A

        g_a_or_b (``bytes``):
            N/A

        key_fingerprint (``int`` ``64-bit``):
            N/A

        protocol (:obj:`PhoneCallProtocol <pyrogram.raw.base.PhoneCallProtocol>`):
            N/A

        connections (List of :obj:`PhoneConnection <pyrogram.raw.base.PhoneConnection>`):
            N/A

        start_date (``int`` ``32-bit``):
            N/A

        p2p_allowed (``bool``, *optional*):
            N/A

        video (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a_or_b", "key_fingerprint", "protocol", "connections", "start_date", "p2p_allowed", "video"]

    ID = 0x967f7c67
    QUALNAME = "types.PhoneCall"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a_or_b: bytes, key_fingerprint: int, protocol: "raw.base.PhoneCallProtocol", connections: List["raw.base.PhoneConnection"], start_date: int, p2p_allowed: Optional[bool] = None, video: Optional[bool] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # long
        self.participant_id = participant_id  # long
        self.g_a_or_b = g_a_or_b  # bytes
        self.key_fingerprint = key_fingerprint  # long
        self.protocol = protocol  # PhoneCallProtocol
        self.connections = connections  # Vector<PhoneConnection>
        self.start_date = start_date  # int
        self.p2p_allowed = p2p_allowed  # flags.5?true
        self.video = video  # flags.6?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCall":
        
        flags = Int.read(b)
        
        p2p_allowed = True if flags & (1 << 5) else False
        video = True if flags & (1 << 6) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Long.read(b)
        
        participant_id = Long.read(b)
        
        g_a_or_b = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        protocol = TLObject.read(b)
        
        connections = TLObject.read(b)
        
        start_date = Int.read(b)
        
        return PhoneCall(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_or_b=g_a_or_b, key_fingerprint=key_fingerprint, protocol=protocol, connections=connections, start_date=start_date, p2p_allowed=p2p_allowed, video=video)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.p2p_allowed else 0
        flags |= (1 << 6) if self.video else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Long(self.admin_id))
        
        b.write(Long(self.participant_id))
        
        b.write(Bytes(self.g_a_or_b))
        
        b.write(Long(self.key_fingerprint))
        
        b.write(self.protocol.write())
        
        b.write(Vector(self.connections))
        
        b.write(Int(self.start_date))
        
        return b.getvalue()
