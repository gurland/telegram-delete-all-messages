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


class Chat(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Chat`.

    Details:
        - Layer: ``158``
        - ID: ``41CBF256``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        title (``str``):
            N/A

        photo (:obj:`ChatPhoto <pyrogram.raw.base.ChatPhoto>`):
            N/A

        participants_count (``int`` ``32-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        version (``int`` ``32-bit``):
            N/A

        creator (``bool``, *optional*):
            N/A

        left (``bool``, *optional*):
            N/A

        deactivated (``bool``, *optional*):
            N/A

        call_active (``bool``, *optional*):
            N/A

        call_not_empty (``bool``, *optional*):
            N/A

        noforwards (``bool``, *optional*):
            N/A

        migrated_to (:obj:`InputChannel <pyrogram.raw.base.InputChannel>`, *optional*):
            N/A

        admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            N/A

        default_banned_rights (:obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "title", "photo", "participants_count", "date", "version", "creator", "left", "deactivated", "call_active", "call_not_empty", "noforwards", "migrated_to", "admin_rights", "default_banned_rights"]

    ID = 0x41cbf256
    QUALNAME = "types.Chat"

    def __init__(self, *, id: int, title: str, photo: "raw.base.ChatPhoto", participants_count: int, date: int, version: int, creator: Optional[bool] = None, left: Optional[bool] = None, deactivated: Optional[bool] = None, call_active: Optional[bool] = None, call_not_empty: Optional[bool] = None, noforwards: Optional[bool] = None, migrated_to: "raw.base.InputChannel" = None, admin_rights: "raw.base.ChatAdminRights" = None, default_banned_rights: "raw.base.ChatBannedRights" = None) -> None:
        self.id = id  # long
        self.title = title  # string
        self.photo = photo  # ChatPhoto
        self.participants_count = participants_count  # int
        self.date = date  # int
        self.version = version  # int
        self.creator = creator  # flags.0?true
        self.left = left  # flags.2?true
        self.deactivated = deactivated  # flags.5?true
        self.call_active = call_active  # flags.23?true
        self.call_not_empty = call_not_empty  # flags.24?true
        self.noforwards = noforwards  # flags.25?true
        self.migrated_to = migrated_to  # flags.6?InputChannel
        self.admin_rights = admin_rights  # flags.14?ChatAdminRights
        self.default_banned_rights = default_banned_rights  # flags.18?ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Chat":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        left = True if flags & (1 << 2) else False
        deactivated = True if flags & (1 << 5) else False
        call_active = True if flags & (1 << 23) else False
        call_not_empty = True if flags & (1 << 24) else False
        noforwards = True if flags & (1 << 25) else False
        id = Long.read(b)
        
        title = String.read(b)
        
        photo = TLObject.read(b)
        
        participants_count = Int.read(b)
        
        date = Int.read(b)
        
        version = Int.read(b)
        
        migrated_to = TLObject.read(b) if flags & (1 << 6) else None
        
        admin_rights = TLObject.read(b) if flags & (1 << 14) else None
        
        default_banned_rights = TLObject.read(b) if flags & (1 << 18) else None
        
        return Chat(id=id, title=title, photo=photo, participants_count=participants_count, date=date, version=version, creator=creator, left=left, deactivated=deactivated, call_active=call_active, call_not_empty=call_not_empty, noforwards=noforwards, migrated_to=migrated_to, admin_rights=admin_rights, default_banned_rights=default_banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 2) if self.left else 0
        flags |= (1 << 5) if self.deactivated else 0
        flags |= (1 << 23) if self.call_active else 0
        flags |= (1 << 24) if self.call_not_empty else 0
        flags |= (1 << 25) if self.noforwards else 0
        flags |= (1 << 6) if self.migrated_to is not None else 0
        flags |= (1 << 14) if self.admin_rights is not None else 0
        flags |= (1 << 18) if self.default_banned_rights is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.title))
        
        b.write(self.photo.write())
        
        b.write(Int(self.participants_count))
        
        b.write(Int(self.date))
        
        b.write(Int(self.version))
        
        if self.migrated_to is not None:
            b.write(self.migrated_to.write())
        
        if self.admin_rights is not None:
            b.write(self.admin_rights.write())
        
        if self.default_banned_rights is not None:
            b.write(self.default_banned_rights.write())
        
        return b.getvalue()
