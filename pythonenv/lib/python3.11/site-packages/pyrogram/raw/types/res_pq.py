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


class ResPQ(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ResPQ`.

    Details:
        - Layer: ``158``
        - ID: ``05162463``

    Parameters:
        nonce (``int`` ``128-bit``):
            N/A

        server_nonce (``int`` ``128-bit``):
            N/A

        pq (``bytes``):
            N/A

        server_public_key_fingerprints (List of ``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            ReqPq
            ReqPqMulti
    """

    __slots__: List[str] = ["nonce", "server_nonce", "pq", "server_public_key_fingerprints"]

    ID = 0x05162463
    QUALNAME = "types.ResPQ"

    def __init__(self, *, nonce: int, server_nonce: int, pq: bytes, server_public_key_fingerprints: List[int]) -> None:
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.pq = pq  # bytes
        self.server_public_key_fingerprints = server_public_key_fingerprints  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ResPQ":
        # No flags
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        pq = Bytes.read(b)
        
        server_public_key_fingerprints = TLObject.read(b, Long)
        
        return ResPQ(nonce=nonce, server_nonce=server_nonce, pq=pq, server_public_key_fingerprints=server_public_key_fingerprints)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Bytes(self.pq))
        
        b.write(Vector(self.server_public_key_fingerprints, Long))
        
        return b.getvalue()
