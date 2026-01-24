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


class DialogFilter(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DialogFilter`.

    Details:
        - Layer: ``158``
        - ID: ``7438F7E8``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        title (``str``):
            N/A

        pinned_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        include_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        exclude_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        contacts (``bool``, *optional*):
            N/A

        non_contacts (``bool``, *optional*):
            N/A

        groups (``bool``, *optional*):
            N/A

        broadcasts (``bool``, *optional*):
            N/A

        bots (``bool``, *optional*):
            N/A

        exclude_muted (``bool``, *optional*):
            N/A

        exclude_read (``bool``, *optional*):
            N/A

        exclude_archived (``bool``, *optional*):
            N/A

        emoticon (``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetDialogFilters
    """

    __slots__: List[str] = ["id", "title", "pinned_peers", "include_peers", "exclude_peers", "contacts", "non_contacts", "groups", "broadcasts", "bots", "exclude_muted", "exclude_read", "exclude_archived", "emoticon"]

    ID = 0x7438f7e8
    QUALNAME = "types.DialogFilter"

    def __init__(self, *, id: int, title: str, pinned_peers: List["raw.base.InputPeer"], include_peers: List["raw.base.InputPeer"], exclude_peers: List["raw.base.InputPeer"], contacts: Optional[bool] = None, non_contacts: Optional[bool] = None, groups: Optional[bool] = None, broadcasts: Optional[bool] = None, bots: Optional[bool] = None, exclude_muted: Optional[bool] = None, exclude_read: Optional[bool] = None, exclude_archived: Optional[bool] = None, emoticon: Optional[str] = None) -> None:
        self.id = id  # int
        self.title = title  # string
        self.pinned_peers = pinned_peers  # Vector<InputPeer>
        self.include_peers = include_peers  # Vector<InputPeer>
        self.exclude_peers = exclude_peers  # Vector<InputPeer>
        self.contacts = contacts  # flags.0?true
        self.non_contacts = non_contacts  # flags.1?true
        self.groups = groups  # flags.2?true
        self.broadcasts = broadcasts  # flags.3?true
        self.bots = bots  # flags.4?true
        self.exclude_muted = exclude_muted  # flags.11?true
        self.exclude_read = exclude_read  # flags.12?true
        self.exclude_archived = exclude_archived  # flags.13?true
        self.emoticon = emoticon  # flags.25?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFilter":
        
        flags = Int.read(b)
        
        contacts = True if flags & (1 << 0) else False
        non_contacts = True if flags & (1 << 1) else False
        groups = True if flags & (1 << 2) else False
        broadcasts = True if flags & (1 << 3) else False
        bots = True if flags & (1 << 4) else False
        exclude_muted = True if flags & (1 << 11) else False
        exclude_read = True if flags & (1 << 12) else False
        exclude_archived = True if flags & (1 << 13) else False
        id = Int.read(b)
        
        title = String.read(b)
        
        emoticon = String.read(b) if flags & (1 << 25) else None
        pinned_peers = TLObject.read(b)
        
        include_peers = TLObject.read(b)
        
        exclude_peers = TLObject.read(b)
        
        return DialogFilter(id=id, title=title, pinned_peers=pinned_peers, include_peers=include_peers, exclude_peers=exclude_peers, contacts=contacts, non_contacts=non_contacts, groups=groups, broadcasts=broadcasts, bots=bots, exclude_muted=exclude_muted, exclude_read=exclude_read, exclude_archived=exclude_archived, emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.contacts else 0
        flags |= (1 << 1) if self.non_contacts else 0
        flags |= (1 << 2) if self.groups else 0
        flags |= (1 << 3) if self.broadcasts else 0
        flags |= (1 << 4) if self.bots else 0
        flags |= (1 << 11) if self.exclude_muted else 0
        flags |= (1 << 12) if self.exclude_read else 0
        flags |= (1 << 13) if self.exclude_archived else 0
        flags |= (1 << 25) if self.emoticon is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.title))
        
        if self.emoticon is not None:
            b.write(String(self.emoticon))
        
        b.write(Vector(self.pinned_peers))
        
        b.write(Vector(self.include_peers))
        
        b.write(Vector(self.exclude_peers))
        
        return b.getvalue()
