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


class MessageService(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Message`.

    Details:
        - Layer: ``158``
        - ID: ``2B085862``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        peer_id (:obj:`Peer <pyrogram.raw.base.Peer>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        action (:obj:`MessageAction <pyrogram.raw.base.MessageAction>`):
            N/A

        out (``bool``, *optional*):
            N/A

        mentioned (``bool``, *optional*):
            N/A

        media_unread (``bool``, *optional*):
            N/A

        silent (``bool``, *optional*):
            N/A

        post (``bool``, *optional*):
            N/A

        legacy (``bool``, *optional*):
            N/A

        from_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            N/A

        reply_to (:obj:`MessageReplyHeader <pyrogram.raw.base.MessageReplyHeader>`, *optional*):
            N/A

        ttl_period (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "peer_id", "date", "action", "out", "mentioned", "media_unread", "silent", "post", "legacy", "from_id", "reply_to", "ttl_period"]

    ID = 0x2b085862
    QUALNAME = "types.MessageService"

    def __init__(self, *, id: int, peer_id: "raw.base.Peer", date: int, action: "raw.base.MessageAction", out: Optional[bool] = None, mentioned: Optional[bool] = None, media_unread: Optional[bool] = None, silent: Optional[bool] = None, post: Optional[bool] = None, legacy: Optional[bool] = None, from_id: "raw.base.Peer" = None, reply_to: "raw.base.MessageReplyHeader" = None, ttl_period: Optional[int] = None) -> None:
        self.id = id  # int
        self.peer_id = peer_id  # Peer
        self.date = date  # int
        self.action = action  # MessageAction
        self.out = out  # flags.1?true
        self.mentioned = mentioned  # flags.4?true
        self.media_unread = media_unread  # flags.5?true
        self.silent = silent  # flags.13?true
        self.post = post  # flags.14?true
        self.legacy = legacy  # flags.19?true
        self.from_id = from_id  # flags.8?Peer
        self.reply_to = reply_to  # flags.3?MessageReplyHeader
        self.ttl_period = ttl_period  # flags.25?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageService":
        
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        post = True if flags & (1 << 14) else False
        legacy = True if flags & (1 << 19) else False
        id = Int.read(b)
        
        from_id = TLObject.read(b) if flags & (1 << 8) else None
        
        peer_id = TLObject.read(b)
        
        reply_to = TLObject.read(b) if flags & (1 << 3) else None
        
        date = Int.read(b)
        
        action = TLObject.read(b)
        
        ttl_period = Int.read(b) if flags & (1 << 25) else None
        return MessageService(id=id, peer_id=peer_id, date=date, action=action, out=out, mentioned=mentioned, media_unread=media_unread, silent=silent, post=post, legacy=legacy, from_id=from_id, reply_to=reply_to, ttl_period=ttl_period)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out else 0
        flags |= (1 << 4) if self.mentioned else 0
        flags |= (1 << 5) if self.media_unread else 0
        flags |= (1 << 13) if self.silent else 0
        flags |= (1 << 14) if self.post else 0
        flags |= (1 << 19) if self.legacy else 0
        flags |= (1 << 8) if self.from_id is not None else 0
        flags |= (1 << 3) if self.reply_to is not None else 0
        flags |= (1 << 25) if self.ttl_period is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        b.write(self.peer_id.write())
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(Int(self.date))
        
        b.write(self.action.write())
        
        if self.ttl_period is not None:
            b.write(Int(self.ttl_period))
        
        return b.getvalue()
