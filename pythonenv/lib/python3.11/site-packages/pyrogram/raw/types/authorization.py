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


class Authorization(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Authorization`.

    Details:
        - Layer: ``158``
        - ID: ``AD01D61D``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        device_model (``str``):
            N/A

        platform (``str``):
            N/A

        system_version (``str``):
            N/A

        api_id (``int`` ``32-bit``):
            N/A

        app_name (``str``):
            N/A

        app_version (``str``):
            N/A

        date_created (``int`` ``32-bit``):
            N/A

        date_active (``int`` ``32-bit``):
            N/A

        ip (``str``):
            N/A

        country (``str``):
            N/A

        region (``str``):
            N/A

        current (``bool``, *optional*):
            N/A

        official_app (``bool``, *optional*):
            N/A

        password_pending (``bool``, *optional*):
            N/A

        encrypted_requests_disabled (``bool``, *optional*):
            N/A

        call_requests_disabled (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.AcceptLoginToken
    """

    __slots__: List[str] = ["hash", "device_model", "platform", "system_version", "api_id", "app_name", "app_version", "date_created", "date_active", "ip", "country", "region", "current", "official_app", "password_pending", "encrypted_requests_disabled", "call_requests_disabled"]

    ID = 0xad01d61d
    QUALNAME = "types.Authorization"

    def __init__(self, *, hash: int, device_model: str, platform: str, system_version: str, api_id: int, app_name: str, app_version: str, date_created: int, date_active: int, ip: str, country: str, region: str, current: Optional[bool] = None, official_app: Optional[bool] = None, password_pending: Optional[bool] = None, encrypted_requests_disabled: Optional[bool] = None, call_requests_disabled: Optional[bool] = None) -> None:
        self.hash = hash  # long
        self.device_model = device_model  # string
        self.platform = platform  # string
        self.system_version = system_version  # string
        self.api_id = api_id  # int
        self.app_name = app_name  # string
        self.app_version = app_version  # string
        self.date_created = date_created  # int
        self.date_active = date_active  # int
        self.ip = ip  # string
        self.country = country  # string
        self.region = region  # string
        self.current = current  # flags.0?true
        self.official_app = official_app  # flags.1?true
        self.password_pending = password_pending  # flags.2?true
        self.encrypted_requests_disabled = encrypted_requests_disabled  # flags.3?true
        self.call_requests_disabled = call_requests_disabled  # flags.4?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Authorization":
        
        flags = Int.read(b)
        
        current = True if flags & (1 << 0) else False
        official_app = True if flags & (1 << 1) else False
        password_pending = True if flags & (1 << 2) else False
        encrypted_requests_disabled = True if flags & (1 << 3) else False
        call_requests_disabled = True if flags & (1 << 4) else False
        hash = Long.read(b)
        
        device_model = String.read(b)
        
        platform = String.read(b)
        
        system_version = String.read(b)
        
        api_id = Int.read(b)
        
        app_name = String.read(b)
        
        app_version = String.read(b)
        
        date_created = Int.read(b)
        
        date_active = Int.read(b)
        
        ip = String.read(b)
        
        country = String.read(b)
        
        region = String.read(b)
        
        return Authorization(hash=hash, device_model=device_model, platform=platform, system_version=system_version, api_id=api_id, app_name=app_name, app_version=app_version, date_created=date_created, date_active=date_active, ip=ip, country=country, region=region, current=current, official_app=official_app, password_pending=password_pending, encrypted_requests_disabled=encrypted_requests_disabled, call_requests_disabled=call_requests_disabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.current else 0
        flags |= (1 << 1) if self.official_app else 0
        flags |= (1 << 2) if self.password_pending else 0
        flags |= (1 << 3) if self.encrypted_requests_disabled else 0
        flags |= (1 << 4) if self.call_requests_disabled else 0
        b.write(Int(flags))
        
        b.write(Long(self.hash))
        
        b.write(String(self.device_model))
        
        b.write(String(self.platform))
        
        b.write(String(self.system_version))
        
        b.write(Int(self.api_id))
        
        b.write(String(self.app_name))
        
        b.write(String(self.app_version))
        
        b.write(Int(self.date_created))
        
        b.write(Int(self.date_active))
        
        b.write(String(self.ip))
        
        b.write(String(self.country))
        
        b.write(String(self.region))
        
        return b.getvalue()
