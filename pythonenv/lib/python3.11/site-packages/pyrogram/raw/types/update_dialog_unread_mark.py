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


class UpdateDialogUnreadMark(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``158``
        - ID: ``E16459C3``

    Parameters:
        peer (:obj:`DialogPeer <pyrogram.raw.base.DialogPeer>`):
            N/A

        unread (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "unread"]

    ID = 0xe16459c3
    QUALNAME = "types.UpdateDialogUnreadMark"

    def __init__(self, *, peer: "raw.base.DialogPeer", unread: Optional[bool] = None) -> None:
        self.peer = peer  # DialogPeer
        self.unread = unread  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDialogUnreadMark":
        
        flags = Int.read(b)
        
        unread = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        return UpdateDialogUnreadMark(peer=peer, unread=unread)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unread else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()
