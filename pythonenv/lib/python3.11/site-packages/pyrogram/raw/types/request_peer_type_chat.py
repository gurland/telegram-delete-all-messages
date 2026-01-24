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


class RequestPeerTypeChat(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.RequestPeerType`.

    Details:
        - Layer: ``158``
        - ID: ``C9F06E1B``

    Parameters:
        creator (``bool``, *optional*):
            N/A

        bot_participant (``bool``, *optional*):
            N/A

        has_username (``bool``, *optional*):
            N/A

        forum (``bool``, *optional*):
            N/A

        user_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            N/A

        bot_admin_rights (:obj:`ChatAdminRights <pyrogram.raw.base.ChatAdminRights>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["creator", "bot_participant", "has_username", "forum", "user_admin_rights", "bot_admin_rights"]

    ID = 0xc9f06e1b
    QUALNAME = "types.RequestPeerTypeChat"

    def __init__(self, *, creator: Optional[bool] = None, bot_participant: Optional[bool] = None, has_username: Optional[bool] = None, forum: Optional[bool] = None, user_admin_rights: "raw.base.ChatAdminRights" = None, bot_admin_rights: "raw.base.ChatAdminRights" = None) -> None:
        self.creator = creator  # flags.0?true
        self.bot_participant = bot_participant  # flags.5?true
        self.has_username = has_username  # flags.3?Bool
        self.forum = forum  # flags.4?Bool
        self.user_admin_rights = user_admin_rights  # flags.1?ChatAdminRights
        self.bot_admin_rights = bot_admin_rights  # flags.2?ChatAdminRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestPeerTypeChat":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        bot_participant = True if flags & (1 << 5) else False
        has_username = Bool.read(b) if flags & (1 << 3) else None
        forum = Bool.read(b) if flags & (1 << 4) else None
        user_admin_rights = TLObject.read(b) if flags & (1 << 1) else None
        
        bot_admin_rights = TLObject.read(b) if flags & (1 << 2) else None
        
        return RequestPeerTypeChat(creator=creator, bot_participant=bot_participant, has_username=has_username, forum=forum, user_admin_rights=user_admin_rights, bot_admin_rights=bot_admin_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 5) if self.bot_participant else 0
        flags |= (1 << 3) if self.has_username is not None else 0
        flags |= (1 << 4) if self.forum is not None else 0
        flags |= (1 << 1) if self.user_admin_rights is not None else 0
        flags |= (1 << 2) if self.bot_admin_rights is not None else 0
        b.write(Int(flags))
        
        if self.has_username is not None:
            b.write(Bool(self.has_username))
        
        if self.forum is not None:
            b.write(Bool(self.forum))
        
        if self.user_admin_rights is not None:
            b.write(self.user_admin_rights.write())
        
        if self.bot_admin_rights is not None:
            b.write(self.bot_admin_rights.write())
        
        return b.getvalue()
