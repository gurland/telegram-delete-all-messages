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


class ChannelParticipantBanned(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``158``
        - ID: ``6DF8014E``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        kicked_by (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`):
            N/A

        left (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "kicked_by", "date", "banned_rights", "left"]

    ID = 0x6df8014e
    QUALNAME = "types.ChannelParticipantBanned"

    def __init__(self, *, peer: "raw.base.Peer", kicked_by: int, date: int, banned_rights: "raw.base.ChatBannedRights", left: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.kicked_by = kicked_by  # long
        self.date = date  # int
        self.banned_rights = banned_rights  # ChatBannedRights
        self.left = left  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantBanned":
        
        flags = Int.read(b)
        
        left = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        kicked_by = Long.read(b)
        
        date = Int.read(b)
        
        banned_rights = TLObject.read(b)
        
        return ChannelParticipantBanned(peer=peer, kicked_by=kicked_by, date=date, banned_rights=banned_rights, left=left)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.left else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.kicked_by))
        
        b.write(Int(self.date))
        
        b.write(self.banned_rights.write())
        
        return b.getvalue()
