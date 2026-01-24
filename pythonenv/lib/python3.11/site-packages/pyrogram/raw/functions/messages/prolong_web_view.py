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


class ProlongWebView(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``7FF34309``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        query_id (``int`` ``64-bit``):
            N/A

        silent (``bool``, *optional*):
            N/A

        reply_to_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        top_msg_id (``int`` ``32-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "bot", "query_id", "silent", "reply_to_msg_id", "top_msg_id", "send_as"]

    ID = 0x7ff34309
    QUALNAME = "functions.messages.ProlongWebView"

    def __init__(self, *, peer: "raw.base.InputPeer", bot: "raw.base.InputUser", query_id: int, silent: Optional[bool] = None, reply_to_msg_id: Optional[int] = None, top_msg_id: Optional[int] = None, send_as: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.bot = bot  # InputUser
        self.query_id = query_id  # long
        self.silent = silent  # flags.5?true
        self.reply_to_msg_id = reply_to_msg_id  # flags.0?int
        self.top_msg_id = top_msg_id  # flags.9?int
        self.send_as = send_as  # flags.13?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ProlongWebView":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        peer = TLObject.read(b)
        
        bot = TLObject.read(b)
        
        query_id = Long.read(b)
        
        reply_to_msg_id = Int.read(b) if flags & (1 << 0) else None
        top_msg_id = Int.read(b) if flags & (1 << 9) else None
        send_as = TLObject.read(b) if flags & (1 << 13) else None
        
        return ProlongWebView(peer=peer, bot=bot, query_id=query_id, silent=silent, reply_to_msg_id=reply_to_msg_id, top_msg_id=top_msg_id, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 0) if self.reply_to_msg_id is not None else 0
        flags |= (1 << 9) if self.top_msg_id is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        b.write(Long(self.query_id))
        
        if self.reply_to_msg_id is not None:
            b.write(Int(self.reply_to_msg_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()
