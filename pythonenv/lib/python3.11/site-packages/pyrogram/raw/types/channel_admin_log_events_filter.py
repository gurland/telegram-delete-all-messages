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


class ChannelAdminLogEventsFilter(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChannelAdminLogEventsFilter`.

    Details:
        - Layer: ``158``
        - ID: ``EA107AE4``

    Parameters:
        join (``bool``, *optional*):
            N/A

        leave (``bool``, *optional*):
            N/A

        invite (``bool``, *optional*):
            N/A

        ban (``bool``, *optional*):
            N/A

        unban (``bool``, *optional*):
            N/A

        kick (``bool``, *optional*):
            N/A

        unkick (``bool``, *optional*):
            N/A

        promote (``bool``, *optional*):
            N/A

        demote (``bool``, *optional*):
            N/A

        info (``bool``, *optional*):
            N/A

        settings (``bool``, *optional*):
            N/A

        pinned (``bool``, *optional*):
            N/A

        edit (``bool``, *optional*):
            N/A

        delete (``bool``, *optional*):
            N/A

        group_call (``bool``, *optional*):
            N/A

        invites (``bool``, *optional*):
            N/A

        send (``bool``, *optional*):
            N/A

        forums (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["join", "leave", "invite", "ban", "unban", "kick", "unkick", "promote", "demote", "info", "settings", "pinned", "edit", "delete", "group_call", "invites", "send", "forums"]

    ID = 0xea107ae4
    QUALNAME = "types.ChannelAdminLogEventsFilter"

    def __init__(self, *, join: Optional[bool] = None, leave: Optional[bool] = None, invite: Optional[bool] = None, ban: Optional[bool] = None, unban: Optional[bool] = None, kick: Optional[bool] = None, unkick: Optional[bool] = None, promote: Optional[bool] = None, demote: Optional[bool] = None, info: Optional[bool] = None, settings: Optional[bool] = None, pinned: Optional[bool] = None, edit: Optional[bool] = None, delete: Optional[bool] = None, group_call: Optional[bool] = None, invites: Optional[bool] = None, send: Optional[bool] = None, forums: Optional[bool] = None) -> None:
        self.join = join  # flags.0?true
        self.leave = leave  # flags.1?true
        self.invite = invite  # flags.2?true
        self.ban = ban  # flags.3?true
        self.unban = unban  # flags.4?true
        self.kick = kick  # flags.5?true
        self.unkick = unkick  # flags.6?true
        self.promote = promote  # flags.7?true
        self.demote = demote  # flags.8?true
        self.info = info  # flags.9?true
        self.settings = settings  # flags.10?true
        self.pinned = pinned  # flags.11?true
        self.edit = edit  # flags.12?true
        self.delete = delete  # flags.13?true
        self.group_call = group_call  # flags.14?true
        self.invites = invites  # flags.15?true
        self.send = send  # flags.16?true
        self.forums = forums  # flags.17?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventsFilter":
        
        flags = Int.read(b)
        
        join = True if flags & (1 << 0) else False
        leave = True if flags & (1 << 1) else False
        invite = True if flags & (1 << 2) else False
        ban = True if flags & (1 << 3) else False
        unban = True if flags & (1 << 4) else False
        kick = True if flags & (1 << 5) else False
        unkick = True if flags & (1 << 6) else False
        promote = True if flags & (1 << 7) else False
        demote = True if flags & (1 << 8) else False
        info = True if flags & (1 << 9) else False
        settings = True if flags & (1 << 10) else False
        pinned = True if flags & (1 << 11) else False
        edit = True if flags & (1 << 12) else False
        delete = True if flags & (1 << 13) else False
        group_call = True if flags & (1 << 14) else False
        invites = True if flags & (1 << 15) else False
        send = True if flags & (1 << 16) else False
        forums = True if flags & (1 << 17) else False
        return ChannelAdminLogEventsFilter(join=join, leave=leave, invite=invite, ban=ban, unban=unban, kick=kick, unkick=unkick, promote=promote, demote=demote, info=info, settings=settings, pinned=pinned, edit=edit, delete=delete, group_call=group_call, invites=invites, send=send, forums=forums)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.join else 0
        flags |= (1 << 1) if self.leave else 0
        flags |= (1 << 2) if self.invite else 0
        flags |= (1 << 3) if self.ban else 0
        flags |= (1 << 4) if self.unban else 0
        flags |= (1 << 5) if self.kick else 0
        flags |= (1 << 6) if self.unkick else 0
        flags |= (1 << 7) if self.promote else 0
        flags |= (1 << 8) if self.demote else 0
        flags |= (1 << 9) if self.info else 0
        flags |= (1 << 10) if self.settings else 0
        flags |= (1 << 11) if self.pinned else 0
        flags |= (1 << 12) if self.edit else 0
        flags |= (1 << 13) if self.delete else 0
        flags |= (1 << 14) if self.group_call else 0
        flags |= (1 << 15) if self.invites else 0
        flags |= (1 << 16) if self.send else 0
        flags |= (1 << 17) if self.forums else 0
        b.write(Int(flags))
        
        return b.getvalue()
