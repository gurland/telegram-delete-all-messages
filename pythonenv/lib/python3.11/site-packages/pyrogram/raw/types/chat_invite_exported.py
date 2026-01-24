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


class ChatInviteExported(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ExportedChatInvite`.

    Details:
        - Layer: ``158``
        - ID: ``AB4A819``

    Parameters:
        link (``str``):
            N/A

        admin_id (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        revoked (``bool``, *optional*):
            N/A

        permanent (``bool``, *optional*):
            N/A

        request_needed (``bool``, *optional*):
            N/A

        start_date (``int`` ``32-bit``, *optional*):
            N/A

        expire_date (``int`` ``32-bit``, *optional*):
            N/A

        usage_limit (``int`` ``32-bit``, *optional*):
            N/A

        usage (``int`` ``32-bit``, *optional*):
            N/A

        requested (``int`` ``32-bit``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.ExportChatInvite
    """

    __slots__: List[str] = ["link", "admin_id", "date", "revoked", "permanent", "request_needed", "start_date", "expire_date", "usage_limit", "usage", "requested", "title"]

    ID = 0xab4a819
    QUALNAME = "types.ChatInviteExported"

    def __init__(self, *, link: str, admin_id: int, date: int, revoked: Optional[bool] = None, permanent: Optional[bool] = None, request_needed: Optional[bool] = None, start_date: Optional[int] = None, expire_date: Optional[int] = None, usage_limit: Optional[int] = None, usage: Optional[int] = None, requested: Optional[int] = None, title: Optional[str] = None) -> None:
        self.link = link  # string
        self.admin_id = admin_id  # long
        self.date = date  # int
        self.revoked = revoked  # flags.0?true
        self.permanent = permanent  # flags.5?true
        self.request_needed = request_needed  # flags.6?true
        self.start_date = start_date  # flags.4?int
        self.expire_date = expire_date  # flags.1?int
        self.usage_limit = usage_limit  # flags.2?int
        self.usage = usage  # flags.3?int
        self.requested = requested  # flags.7?int
        self.title = title  # flags.8?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInviteExported":
        
        flags = Int.read(b)
        
        revoked = True if flags & (1 << 0) else False
        permanent = True if flags & (1 << 5) else False
        request_needed = True if flags & (1 << 6) else False
        link = String.read(b)
        
        admin_id = Long.read(b)
        
        date = Int.read(b)
        
        start_date = Int.read(b) if flags & (1 << 4) else None
        expire_date = Int.read(b) if flags & (1 << 1) else None
        usage_limit = Int.read(b) if flags & (1 << 2) else None
        usage = Int.read(b) if flags & (1 << 3) else None
        requested = Int.read(b) if flags & (1 << 7) else None
        title = String.read(b) if flags & (1 << 8) else None
        return ChatInviteExported(link=link, admin_id=admin_id, date=date, revoked=revoked, permanent=permanent, request_needed=request_needed, start_date=start_date, expire_date=expire_date, usage_limit=usage_limit, usage=usage, requested=requested, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoked else 0
        flags |= (1 << 5) if self.permanent else 0
        flags |= (1 << 6) if self.request_needed else 0
        flags |= (1 << 4) if self.start_date is not None else 0
        flags |= (1 << 1) if self.expire_date is not None else 0
        flags |= (1 << 2) if self.usage_limit is not None else 0
        flags |= (1 << 3) if self.usage is not None else 0
        flags |= (1 << 7) if self.requested is not None else 0
        flags |= (1 << 8) if self.title is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.link))
        
        b.write(Long(self.admin_id))
        
        b.write(Int(self.date))
        
        if self.start_date is not None:
            b.write(Int(self.start_date))
        
        if self.expire_date is not None:
            b.write(Int(self.expire_date))
        
        if self.usage_limit is not None:
            b.write(Int(self.usage_limit))
        
        if self.usage is not None:
            b.write(Int(self.usage))
        
        if self.requested is not None:
            b.write(Int(self.requested))
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()
