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


class WebAuthorization(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebAuthorization`.

    Details:
        - Layer: ``158``
        - ID: ``A6F8F452``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        bot_id (``int`` ``64-bit``):
            N/A

        domain (``str``):
            N/A

        browser (``str``):
            N/A

        platform (``str``):
            N/A

        date_created (``int`` ``32-bit``):
            N/A

        date_active (``int`` ``32-bit``):
            N/A

        ip (``str``):
            N/A

        region (``str``):
            N/A

    """

    __slots__: List[str] = ["hash", "bot_id", "domain", "browser", "platform", "date_created", "date_active", "ip", "region"]

    ID = 0xa6f8f452
    QUALNAME = "types.WebAuthorization"

    def __init__(self, *, hash: int, bot_id: int, domain: str, browser: str, platform: str, date_created: int, date_active: int, ip: str, region: str) -> None:
        self.hash = hash  # long
        self.bot_id = bot_id  # long
        self.domain = domain  # string
        self.browser = browser  # string
        self.platform = platform  # string
        self.date_created = date_created  # int
        self.date_active = date_active  # int
        self.ip = ip  # string
        self.region = region  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebAuthorization":
        # No flags
        
        hash = Long.read(b)
        
        bot_id = Long.read(b)
        
        domain = String.read(b)
        
        browser = String.read(b)
        
        platform = String.read(b)
        
        date_created = Int.read(b)
        
        date_active = Int.read(b)
        
        ip = String.read(b)
        
        region = String.read(b)
        
        return WebAuthorization(hash=hash, bot_id=bot_id, domain=domain, browser=browser, platform=platform, date_created=date_created, date_active=date_active, ip=ip, region=region)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.domain))
        
        b.write(String(self.browser))
        
        b.write(String(self.platform))
        
        b.write(Int(self.date_created))
        
        b.write(Int(self.date_active))
        
        b.write(String(self.ip))
        
        b.write(String(self.region))
        
        return b.getvalue()
