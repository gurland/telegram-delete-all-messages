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


class DocumentAttributeAudio(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``158``
        - ID: ``9852F9C6``

    Parameters:
        duration (``int`` ``32-bit``):
            N/A

        voice (``bool``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        performer (``str``, *optional*):
            N/A

        waveform (``bytes``, *optional*):
            N/A

    """

    __slots__: List[str] = ["duration", "voice", "title", "performer", "waveform"]

    ID = 0x9852f9c6
    QUALNAME = "types.DocumentAttributeAudio"

    def __init__(self, *, duration: int, voice: Optional[bool] = None, title: Optional[str] = None, performer: Optional[str] = None, waveform: Optional[bytes] = None) -> None:
        self.duration = duration  # int
        self.voice = voice  # flags.10?true
        self.title = title  # flags.0?string
        self.performer = performer  # flags.1?string
        self.waveform = waveform  # flags.2?bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeAudio":
        
        flags = Int.read(b)
        
        voice = True if flags & (1 << 10) else False
        duration = Int.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        performer = String.read(b) if flags & (1 << 1) else None
        waveform = Bytes.read(b) if flags & (1 << 2) else None
        return DocumentAttributeAudio(duration=duration, voice=voice, title=title, performer=performer, waveform=waveform)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 10) if self.voice else 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.performer is not None else 0
        flags |= (1 << 2) if self.waveform is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.duration))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.performer is not None:
            b.write(String(self.performer))
        
        if self.waveform is not None:
            b.write(Bytes(self.waveform))
        
        return b.getvalue()
