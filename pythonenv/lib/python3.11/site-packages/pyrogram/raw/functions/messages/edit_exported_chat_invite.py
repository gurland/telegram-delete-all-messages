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


class EditExportedChatInvite(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``BDCA2F75``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        link (``str``):
            N/A

        revoked (``bool``, *optional*):
            N/A

        expire_date (``int`` ``32-bit``, *optional*):
            N/A

        usage_limit (``int`` ``32-bit``, *optional*):
            N/A

        request_needed (``bool``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

    Returns:
        :obj:`messages.ExportedChatInvite <pyrogram.raw.base.messages.ExportedChatInvite>`
    """

    __slots__: List[str] = ["peer", "link", "revoked", "expire_date", "usage_limit", "request_needed", "title"]

    ID = 0xbdca2f75
    QUALNAME = "functions.messages.EditExportedChatInvite"

    def __init__(self, *, peer: "raw.base.InputPeer", link: str, revoked: Optional[bool] = None, expire_date: Optional[int] = None, usage_limit: Optional[int] = None, request_needed: Optional[bool] = None, title: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.link = link  # string
        self.revoked = revoked  # flags.2?true
        self.expire_date = expire_date  # flags.0?int
        self.usage_limit = usage_limit  # flags.1?int
        self.request_needed = request_needed  # flags.3?Bool
        self.title = title  # flags.4?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditExportedChatInvite":
        
        flags = Int.read(b)
        
        revoked = True if flags & (1 << 2) else False
        peer = TLObject.read(b)
        
        link = String.read(b)
        
        expire_date = Int.read(b) if flags & (1 << 0) else None
        usage_limit = Int.read(b) if flags & (1 << 1) else None
        request_needed = Bool.read(b) if flags & (1 << 3) else None
        title = String.read(b) if flags & (1 << 4) else None
        return EditExportedChatInvite(peer=peer, link=link, revoked=revoked, expire_date=expire_date, usage_limit=usage_limit, request_needed=request_needed, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.revoked else 0
        flags |= (1 << 0) if self.expire_date is not None else 0
        flags |= (1 << 1) if self.usage_limit is not None else 0
        flags |= (1 << 3) if self.request_needed is not None else 0
        flags |= (1 << 4) if self.title is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.link))
        
        if self.expire_date is not None:
            b.write(Int(self.expire_date))
        
        if self.usage_limit is not None:
            b.write(Int(self.usage_limit))
        
        if self.request_needed is not None:
            b.write(Bool(self.request_needed))
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()
