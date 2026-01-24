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


class UpdateBotInlineSend(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``158``
        - ID: ``12F12A07``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        query (``str``):
            N/A

        id (``str``):
            N/A

        geo (:obj:`GeoPoint <pyrogram.raw.base.GeoPoint>`, *optional*):
            N/A

        msg_id (:obj:`InputBotInlineMessageID <pyrogram.raw.base.InputBotInlineMessageID>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "query", "id", "geo", "msg_id"]

    ID = 0x12f12a07
    QUALNAME = "types.UpdateBotInlineSend"

    def __init__(self, *, user_id: int, query: str, id: str, geo: "raw.base.GeoPoint" = None, msg_id: "raw.base.InputBotInlineMessageID" = None) -> None:
        self.user_id = user_id  # long
        self.query = query  # string
        self.id = id  # string
        self.geo = geo  # flags.0?GeoPoint
        self.msg_id = msg_id  # flags.1?InputBotInlineMessageID

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBotInlineSend":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        query = String.read(b)
        
        geo = TLObject.read(b) if flags & (1 << 0) else None
        
        id = String.read(b)
        
        msg_id = TLObject.read(b) if flags & (1 << 1) else None
        
        return UpdateBotInlineSend(user_id=user_id, query=query, id=id, geo=geo, msg_id=msg_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.geo is not None else 0
        flags |= (1 << 1) if self.msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(String(self.query))
        
        if self.geo is not None:
            b.write(self.geo.write())
        
        b.write(String(self.id))
        
        if self.msg_id is not None:
            b.write(self.msg_id.write())
        
        return b.getvalue()
