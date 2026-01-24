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


class TranslateText(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``63183030``

    Parameters:
        to_lang (``str``):
            N/A

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        id (List of ``int`` ``32-bit``, *optional*):
            N/A

        text (List of :obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            N/A

    Returns:
        :obj:`messages.TranslatedText <pyrogram.raw.base.messages.TranslatedText>`
    """

    __slots__: List[str] = ["to_lang", "peer", "id", "text"]

    ID = 0x63183030
    QUALNAME = "functions.messages.TranslateText"

    def __init__(self, *, to_lang: str, peer: "raw.base.InputPeer" = None, id: Optional[List[int]] = None, text: Optional[List["raw.base.TextWithEntities"]] = None) -> None:
        self.to_lang = to_lang  # string
        self.peer = peer  # flags.0?InputPeer
        self.id = id  # flags.0?Vector<int>
        self.text = text  # flags.1?Vector<TextWithEntities>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "TranslateText":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b) if flags & (1 << 0) else None
        
        id = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        text = TLObject.read(b) if flags & (1 << 1) else []
        
        to_lang = String.read(b)
        
        return TranslateText(to_lang=to_lang, peer=peer, id=id, text=text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.peer is not None else 0
        flags |= (1 << 0) if self.id else 0
        flags |= (1 << 1) if self.text else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        if self.id is not None:
            b.write(Vector(self.id, Int))
        
        if self.text is not None:
            b.write(Vector(self.text))
        
        b.write(String(self.to_lang))
        
        return b.getvalue()
