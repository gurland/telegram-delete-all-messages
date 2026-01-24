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


class GetFile(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``BE5335BE``

    Parameters:
        location (:obj:`InputFileLocation <pyrogram.raw.base.InputFileLocation>`):
            N/A

        offset (``int`` ``64-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

        precise (``bool``, *optional*):
            N/A

        cdn_supported (``bool``, *optional*):
            N/A

    Returns:
        :obj:`upload.File <pyrogram.raw.base.upload.File>`
    """

    __slots__: List[str] = ["location", "offset", "limit", "precise", "cdn_supported"]

    ID = 0xbe5335be
    QUALNAME = "functions.upload.GetFile"

    def __init__(self, *, location: "raw.base.InputFileLocation", offset: int, limit: int, precise: Optional[bool] = None, cdn_supported: Optional[bool] = None) -> None:
        self.location = location  # InputFileLocation
        self.offset = offset  # long
        self.limit = limit  # int
        self.precise = precise  # flags.0?true
        self.cdn_supported = cdn_supported  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetFile":
        
        flags = Int.read(b)
        
        precise = True if flags & (1 << 0) else False
        cdn_supported = True if flags & (1 << 1) else False
        location = TLObject.read(b)
        
        offset = Long.read(b)
        
        limit = Int.read(b)
        
        return GetFile(location=location, offset=offset, limit=limit, precise=precise, cdn_supported=cdn_supported)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.precise else 0
        flags |= (1 << 1) if self.cdn_supported else 0
        b.write(Int(flags))
        
        b.write(self.location.write())
        
        b.write(Long(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
