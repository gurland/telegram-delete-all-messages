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


class UpdateTranscribedAudio(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``158``
        - ID: ``84CD5A``

    Parameters:
        peer (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        transcription_id (``int`` ``64-bit``):
            N/A

        text (``str``):
            N/A

        pending (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "msg_id", "transcription_id", "text", "pending"]

    ID = 0x84cd5a
    QUALNAME = "types.UpdateTranscribedAudio"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int, transcription_id: int, text: str, pending: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int
        self.transcription_id = transcription_id  # long
        self.text = text  # string
        self.pending = pending  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateTranscribedAudio":
        
        flags = Int.read(b)
        
        pending = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        transcription_id = Long.read(b)
        
        text = String.read(b)
        
        return UpdateTranscribedAudio(peer=peer, msg_id=msg_id, transcription_id=transcription_id, text=text, pending=pending)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pending else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Long(self.transcription_id))
        
        b.write(String(self.text))
        
        return b.getvalue()
