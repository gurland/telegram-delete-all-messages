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


class FileHash(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.FileHash`.

    Details:
        - Layer: ``158``
        - ID: ``F39B035C``

    Parameters:
        offset (``int`` ``64-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        hash (``bytes``):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            upload.ReuploadCdnFile
            upload.GetCdnFileHashes
            upload.GetFileHashes
    """

    __slots__: List[str] = ["offset", "limit", "hash"]

    ID = 0xf39b035c
    QUALNAME = "types.FileHash"

    def __init__(self, *, offset: int, limit: int, hash: bytes) -> None:
        self.offset = offset  # long
        self.limit = limit  # int
        self.hash = hash  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FileHash":
        # No flags
        
        offset = Long.read(b)
        
        limit = Int.read(b)
        
        hash = Bytes.read(b)
        
        return FileHash(offset=offset, limit=limit, hash=hash)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Bytes(self.hash))
        
        return b.getvalue()
