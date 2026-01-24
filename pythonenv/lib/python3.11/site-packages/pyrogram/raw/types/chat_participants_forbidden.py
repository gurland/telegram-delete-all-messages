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


class ChatParticipantsForbidden(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatParticipants`.

    Details:
        - Layer: ``158``
        - ID: ``8763D3E1``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        self_participant (:obj:`ChatParticipant <pyrogram.raw.base.ChatParticipant>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["chat_id", "self_participant"]

    ID = 0x8763d3e1
    QUALNAME = "types.ChatParticipantsForbidden"

    def __init__(self, *, chat_id: int, self_participant: "raw.base.ChatParticipant" = None) -> None:
        self.chat_id = chat_id  # long
        self.self_participant = self_participant  # flags.0?ChatParticipant

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatParticipantsForbidden":
        
        flags = Int.read(b)
        
        chat_id = Long.read(b)
        
        self_participant = TLObject.read(b) if flags & (1 << 0) else None
        
        return ChatParticipantsForbidden(chat_id=chat_id, self_participant=self_participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.self_participant is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.chat_id))
        
        if self.self_participant is not None:
            b.write(self.self_participant.write())
        
        return b.getvalue()
