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


class ExportChatInvite(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``A02CE5D5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        legacy_revoke_permanent (``bool``, *optional*):
            N/A

        request_needed (``bool``, *optional*):
            N/A

        expire_date (``int`` ``32-bit``, *optional*):
            N/A

        usage_limit (``int`` ``32-bit``, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

    Returns:
        :obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`
    """

    __slots__: List[str] = ["peer", "legacy_revoke_permanent", "request_needed", "expire_date", "usage_limit", "title"]

    ID = 0xa02ce5d5
    QUALNAME = "functions.messages.ExportChatInvite"

    def __init__(self, *, peer: "raw.base.InputPeer", legacy_revoke_permanent: Optional[bool] = None, request_needed: Optional[bool] = None, expire_date: Optional[int] = None, usage_limit: Optional[int] = None, title: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.legacy_revoke_permanent = legacy_revoke_permanent  # flags.2?true
        self.request_needed = request_needed  # flags.3?true
        self.expire_date = expire_date  # flags.0?int
        self.usage_limit = usage_limit  # flags.1?int
        self.title = title  # flags.4?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ExportChatInvite":
        
        flags = Int.read(b)
        
        legacy_revoke_permanent = True if flags & (1 << 2) else False
        request_needed = True if flags & (1 << 3) else False
        peer = TLObject.read(b)
        
        expire_date = Int.read(b) if flags & (1 << 0) else None
        usage_limit = Int.read(b) if flags & (1 << 1) else None
        title = String.read(b) if flags & (1 << 4) else None
        return ExportChatInvite(peer=peer, legacy_revoke_permanent=legacy_revoke_permanent, request_needed=request_needed, expire_date=expire_date, usage_limit=usage_limit, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.legacy_revoke_permanent else 0
        flags |= (1 << 3) if self.request_needed else 0
        flags |= (1 << 0) if self.expire_date is not None else 0
        flags |= (1 << 1) if self.usage_limit is not None else 0
        flags |= (1 << 4) if self.title is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.expire_date is not None:
            b.write(Int(self.expire_date))
        
        if self.usage_limit is not None:
            b.write(Int(self.usage_limit))
        
        if self.title is not None:
            b.write(String(self.title))
        
        return b.getvalue()
