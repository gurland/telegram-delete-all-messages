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


class DcOption(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DcOption`.

    Details:
        - Layer: ``158``
        - ID: ``18B7A10D``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        ip_address (``str``):
            N/A

        port (``int`` ``32-bit``):
            N/A

        ipv6 (``bool``, *optional*):
            N/A

        media_only (``bool``, *optional*):
            N/A

        tcpo_only (``bool``, *optional*):
            N/A

        cdn (``bool``, *optional*):
            N/A

        static (``bool``, *optional*):
            N/A

        this_port_only (``bool``, *optional*):
            N/A

        secret (``bytes``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "ip_address", "port", "ipv6", "media_only", "tcpo_only", "cdn", "static", "this_port_only", "secret"]

    ID = 0x18b7a10d
    QUALNAME = "types.DcOption"

    def __init__(self, *, id: int, ip_address: str, port: int, ipv6: Optional[bool] = None, media_only: Optional[bool] = None, tcpo_only: Optional[bool] = None, cdn: Optional[bool] = None, static: Optional[bool] = None, this_port_only: Optional[bool] = None, secret: Optional[bytes] = None) -> None:
        self.id = id  # int
        self.ip_address = ip_address  # string
        self.port = port  # int
        self.ipv6 = ipv6  # flags.0?true
        self.media_only = media_only  # flags.1?true
        self.tcpo_only = tcpo_only  # flags.2?true
        self.cdn = cdn  # flags.3?true
        self.static = static  # flags.4?true
        self.this_port_only = this_port_only  # flags.5?true
        self.secret = secret  # flags.10?bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DcOption":
        
        flags = Int.read(b)
        
        ipv6 = True if flags & (1 << 0) else False
        media_only = True if flags & (1 << 1) else False
        tcpo_only = True if flags & (1 << 2) else False
        cdn = True if flags & (1 << 3) else False
        static = True if flags & (1 << 4) else False
        this_port_only = True if flags & (1 << 5) else False
        id = Int.read(b)
        
        ip_address = String.read(b)
        
        port = Int.read(b)
        
        secret = Bytes.read(b) if flags & (1 << 10) else None
        return DcOption(id=id, ip_address=ip_address, port=port, ipv6=ipv6, media_only=media_only, tcpo_only=tcpo_only, cdn=cdn, static=static, this_port_only=this_port_only, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ipv6 else 0
        flags |= (1 << 1) if self.media_only else 0
        flags |= (1 << 2) if self.tcpo_only else 0
        flags |= (1 << 3) if self.cdn else 0
        flags |= (1 << 4) if self.static else 0
        flags |= (1 << 5) if self.this_port_only else 0
        flags |= (1 << 10) if self.secret is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.ip_address))
        
        b.write(Int(self.port))
        
        if self.secret is not None:
            b.write(Bytes(self.secret))
        
        return b.getvalue()
