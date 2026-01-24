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


class EditGroupCallParticipant(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``A5273ABF``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        participant (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        muted (``bool``, *optional*):
            N/A

        volume (``int`` ``32-bit``, *optional*):
            N/A

        raise_hand (``bool``, *optional*):
            N/A

        video_stopped (``bool``, *optional*):
            N/A

        video_paused (``bool``, *optional*):
            N/A

        presentation_paused (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "participant", "muted", "volume", "raise_hand", "video_stopped", "video_paused", "presentation_paused"]

    ID = 0xa5273abf
    QUALNAME = "functions.phone.EditGroupCallParticipant"

    def __init__(self, *, call: "raw.base.InputGroupCall", participant: "raw.base.InputPeer", muted: Optional[bool] = None, volume: Optional[int] = None, raise_hand: Optional[bool] = None, video_stopped: Optional[bool] = None, video_paused: Optional[bool] = None, presentation_paused: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.participant = participant  # InputPeer
        self.muted = muted  # flags.0?Bool
        self.volume = volume  # flags.1?int
        self.raise_hand = raise_hand  # flags.2?Bool
        self.video_stopped = video_stopped  # flags.3?Bool
        self.video_paused = video_paused  # flags.4?Bool
        self.presentation_paused = presentation_paused  # flags.5?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditGroupCallParticipant":
        
        flags = Int.read(b)
        
        call = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        muted = Bool.read(b) if flags & (1 << 0) else None
        volume = Int.read(b) if flags & (1 << 1) else None
        raise_hand = Bool.read(b) if flags & (1 << 2) else None
        video_stopped = Bool.read(b) if flags & (1 << 3) else None
        video_paused = Bool.read(b) if flags & (1 << 4) else None
        presentation_paused = Bool.read(b) if flags & (1 << 5) else None
        return EditGroupCallParticipant(call=call, participant=participant, muted=muted, volume=volume, raise_hand=raise_hand, video_stopped=video_stopped, video_paused=video_paused, presentation_paused=presentation_paused)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted is not None else 0
        flags |= (1 << 1) if self.volume is not None else 0
        flags |= (1 << 2) if self.raise_hand is not None else 0
        flags |= (1 << 3) if self.video_stopped is not None else 0
        flags |= (1 << 4) if self.video_paused is not None else 0
        flags |= (1 << 5) if self.presentation_paused is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        b.write(self.participant.write())
        
        if self.muted is not None:
            b.write(Bool(self.muted))
        
        if self.volume is not None:
            b.write(Int(self.volume))
        
        if self.raise_hand is not None:
            b.write(Bool(self.raise_hand))
        
        if self.video_stopped is not None:
            b.write(Bool(self.video_stopped))
        
        if self.video_paused is not None:
            b.write(Bool(self.video_paused))
        
        if self.presentation_paused is not None:
            b.write(Bool(self.presentation_paused))
        
        return b.getvalue()
