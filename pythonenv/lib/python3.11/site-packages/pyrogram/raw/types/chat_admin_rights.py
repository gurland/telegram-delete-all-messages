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


class ChatAdminRights(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatAdminRights`.

    Details:
        - Layer: ``158``
        - ID: ``5FB224D5``

    Parameters:
        change_info (``bool``, *optional*):
            N/A

        post_messages (``bool``, *optional*):
            N/A

        edit_messages (``bool``, *optional*):
            N/A

        delete_messages (``bool``, *optional*):
            N/A

        ban_users (``bool``, *optional*):
            N/A

        invite_users (``bool``, *optional*):
            N/A

        pin_messages (``bool``, *optional*):
            N/A

        add_admins (``bool``, *optional*):
            N/A

        anonymous (``bool``, *optional*):
            N/A

        manage_call (``bool``, *optional*):
            N/A

        other (``bool``, *optional*):
            N/A

        manage_topics (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["change_info", "post_messages", "edit_messages", "delete_messages", "ban_users", "invite_users", "pin_messages", "add_admins", "anonymous", "manage_call", "other", "manage_topics"]

    ID = 0x5fb224d5
    QUALNAME = "types.ChatAdminRights"

    def __init__(self, *, change_info: Optional[bool] = None, post_messages: Optional[bool] = None, edit_messages: Optional[bool] = None, delete_messages: Optional[bool] = None, ban_users: Optional[bool] = None, invite_users: Optional[bool] = None, pin_messages: Optional[bool] = None, add_admins: Optional[bool] = None, anonymous: Optional[bool] = None, manage_call: Optional[bool] = None, other: Optional[bool] = None, manage_topics: Optional[bool] = None) -> None:
        self.change_info = change_info  # flags.0?true
        self.post_messages = post_messages  # flags.1?true
        self.edit_messages = edit_messages  # flags.2?true
        self.delete_messages = delete_messages  # flags.3?true
        self.ban_users = ban_users  # flags.4?true
        self.invite_users = invite_users  # flags.5?true
        self.pin_messages = pin_messages  # flags.7?true
        self.add_admins = add_admins  # flags.9?true
        self.anonymous = anonymous  # flags.10?true
        self.manage_call = manage_call  # flags.11?true
        self.other = other  # flags.12?true
        self.manage_topics = manage_topics  # flags.13?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatAdminRights":
        
        flags = Int.read(b)
        
        change_info = True if flags & (1 << 0) else False
        post_messages = True if flags & (1 << 1) else False
        edit_messages = True if flags & (1 << 2) else False
        delete_messages = True if flags & (1 << 3) else False
        ban_users = True if flags & (1 << 4) else False
        invite_users = True if flags & (1 << 5) else False
        pin_messages = True if flags & (1 << 7) else False
        add_admins = True if flags & (1 << 9) else False
        anonymous = True if flags & (1 << 10) else False
        manage_call = True if flags & (1 << 11) else False
        other = True if flags & (1 << 12) else False
        manage_topics = True if flags & (1 << 13) else False
        return ChatAdminRights(change_info=change_info, post_messages=post_messages, edit_messages=edit_messages, delete_messages=delete_messages, ban_users=ban_users, invite_users=invite_users, pin_messages=pin_messages, add_admins=add_admins, anonymous=anonymous, manage_call=manage_call, other=other, manage_topics=manage_topics)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.change_info else 0
        flags |= (1 << 1) if self.post_messages else 0
        flags |= (1 << 2) if self.edit_messages else 0
        flags |= (1 << 3) if self.delete_messages else 0
        flags |= (1 << 4) if self.ban_users else 0
        flags |= (1 << 5) if self.invite_users else 0
        flags |= (1 << 7) if self.pin_messages else 0
        flags |= (1 << 9) if self.add_admins else 0
        flags |= (1 << 10) if self.anonymous else 0
        flags |= (1 << 11) if self.manage_call else 0
        flags |= (1 << 12) if self.other else 0
        flags |= (1 << 13) if self.manage_topics else 0
        b.write(Int(flags))
        
        return b.getvalue()
