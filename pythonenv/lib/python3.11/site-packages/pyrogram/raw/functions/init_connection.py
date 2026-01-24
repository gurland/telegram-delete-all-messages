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


class InitConnection(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``C1CD5EA9``

    Parameters:
        api_id (``int`` ``32-bit``):
            N/A

        device_model (``str``):
            N/A

        system_version (``str``):
            N/A

        app_version (``str``):
            N/A

        system_lang_code (``str``):
            N/A

        lang_pack (``str``):
            N/A

        lang_code (``str``):
            N/A

        query (Any function from :obj:`~pyrogram.raw.functions`):
            N/A

        proxy (:obj:`InputClientProxy <pyrogram.raw.base.InputClientProxy>`, *optional*):
            N/A

        params (:obj:`JSONValue <pyrogram.raw.base.JSONValue>`, *optional*):
            N/A

    Returns:
        Any object from :obj:`~pyrogram.raw.types`
    """

    __slots__: List[str] = ["api_id", "device_model", "system_version", "app_version", "system_lang_code", "lang_pack", "lang_code", "query", "proxy", "params"]

    ID = 0xc1cd5ea9
    QUALNAME = "functions.InitConnection"

    def __init__(self, *, api_id: int, device_model: str, system_version: str, app_version: str, system_lang_code: str, lang_pack: str, lang_code: str, query: TLObject, proxy: "raw.base.InputClientProxy" = None, params: "raw.base.JSONValue" = None) -> None:
        self.api_id = api_id  # int
        self.device_model = device_model  # string
        self.system_version = system_version  # string
        self.app_version = app_version  # string
        self.system_lang_code = system_lang_code  # string
        self.lang_pack = lang_pack  # string
        self.lang_code = lang_code  # string
        self.query = query  # !X
        self.proxy = proxy  # flags.0?InputClientProxy
        self.params = params  # flags.1?JSONValue

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InitConnection":
        
        flags = Int.read(b)
        
        api_id = Int.read(b)
        
        device_model = String.read(b)
        
        system_version = String.read(b)
        
        app_version = String.read(b)
        
        system_lang_code = String.read(b)
        
        lang_pack = String.read(b)
        
        lang_code = String.read(b)
        
        proxy = TLObject.read(b) if flags & (1 << 0) else None
        
        params = TLObject.read(b) if flags & (1 << 1) else None
        
        query = TLObject.read(b)
        
        return InitConnection(api_id=api_id, device_model=device_model, system_version=system_version, app_version=app_version, system_lang_code=system_lang_code, lang_pack=lang_pack, lang_code=lang_code, query=query, proxy=proxy, params=params)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.proxy is not None else 0
        flags |= (1 << 1) if self.params is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.api_id))
        
        b.write(String(self.device_model))
        
        b.write(String(self.system_version))
        
        b.write(String(self.app_version))
        
        b.write(String(self.system_lang_code))
        
        b.write(String(self.lang_pack))
        
        b.write(String(self.lang_code))
        
        if self.proxy is not None:
            b.write(self.proxy.write())
        
        if self.params is not None:
            b.write(self.params.write())
        
        b.write(self.query.write())
        
        return b.getvalue()
