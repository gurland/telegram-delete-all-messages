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


class PeerSettings(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PeerSettings`.

    Details:
        - Layer: ``158``
        - ID: ``A518110D``

    Parameters:
        report_spam (``bool``, *optional*):
            N/A

        add_contact (``bool``, *optional*):
            N/A

        block_contact (``bool``, *optional*):
            N/A

        share_contact (``bool``, *optional*):
            N/A

        need_contacts_exception (``bool``, *optional*):
            N/A

        report_geo (``bool``, *optional*):
            N/A

        autoarchived (``bool``, *optional*):
            N/A

        invite_members (``bool``, *optional*):
            N/A

        request_chat_broadcast (``bool``, *optional*):
            N/A

        geo_distance (``int`` ``32-bit``, *optional*):
            N/A

        request_chat_title (``str``, *optional*):
            N/A

        request_chat_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["report_spam", "add_contact", "block_contact", "share_contact", "need_contacts_exception", "report_geo", "autoarchived", "invite_members", "request_chat_broadcast", "geo_distance", "request_chat_title", "request_chat_date"]

    ID = 0xa518110d
    QUALNAME = "types.PeerSettings"

    def __init__(self, *, report_spam: Optional[bool] = None, add_contact: Optional[bool] = None, block_contact: Optional[bool] = None, share_contact: Optional[bool] = None, need_contacts_exception: Optional[bool] = None, report_geo: Optional[bool] = None, autoarchived: Optional[bool] = None, invite_members: Optional[bool] = None, request_chat_broadcast: Optional[bool] = None, geo_distance: Optional[int] = None, request_chat_title: Optional[str] = None, request_chat_date: Optional[int] = None) -> None:
        self.report_spam = report_spam  # flags.0?true
        self.add_contact = add_contact  # flags.1?true
        self.block_contact = block_contact  # flags.2?true
        self.share_contact = share_contact  # flags.3?true
        self.need_contacts_exception = need_contacts_exception  # flags.4?true
        self.report_geo = report_geo  # flags.5?true
        self.autoarchived = autoarchived  # flags.7?true
        self.invite_members = invite_members  # flags.8?true
        self.request_chat_broadcast = request_chat_broadcast  # flags.10?true
        self.geo_distance = geo_distance  # flags.6?int
        self.request_chat_title = request_chat_title  # flags.9?string
        self.request_chat_date = request_chat_date  # flags.9?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerSettings":
        
        flags = Int.read(b)
        
        report_spam = True if flags & (1 << 0) else False
        add_contact = True if flags & (1 << 1) else False
        block_contact = True if flags & (1 << 2) else False
        share_contact = True if flags & (1 << 3) else False
        need_contacts_exception = True if flags & (1 << 4) else False
        report_geo = True if flags & (1 << 5) else False
        autoarchived = True if flags & (1 << 7) else False
        invite_members = True if flags & (1 << 8) else False
        request_chat_broadcast = True if flags & (1 << 10) else False
        geo_distance = Int.read(b) if flags & (1 << 6) else None
        request_chat_title = String.read(b) if flags & (1 << 9) else None
        request_chat_date = Int.read(b) if flags & (1 << 9) else None
        return PeerSettings(report_spam=report_spam, add_contact=add_contact, block_contact=block_contact, share_contact=share_contact, need_contacts_exception=need_contacts_exception, report_geo=report_geo, autoarchived=autoarchived, invite_members=invite_members, request_chat_broadcast=request_chat_broadcast, geo_distance=geo_distance, request_chat_title=request_chat_title, request_chat_date=request_chat_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.report_spam else 0
        flags |= (1 << 1) if self.add_contact else 0
        flags |= (1 << 2) if self.block_contact else 0
        flags |= (1 << 3) if self.share_contact else 0
        flags |= (1 << 4) if self.need_contacts_exception else 0
        flags |= (1 << 5) if self.report_geo else 0
        flags |= (1 << 7) if self.autoarchived else 0
        flags |= (1 << 8) if self.invite_members else 0
        flags |= (1 << 10) if self.request_chat_broadcast else 0
        flags |= (1 << 6) if self.geo_distance is not None else 0
        flags |= (1 << 9) if self.request_chat_title is not None else 0
        flags |= (1 << 9) if self.request_chat_date is not None else 0
        b.write(Int(flags))
        
        if self.geo_distance is not None:
            b.write(Int(self.geo_distance))
        
        if self.request_chat_title is not None:
            b.write(String(self.request_chat_title))
        
        if self.request_chat_date is not None:
            b.write(Int(self.request_chat_date))
        
        return b.getvalue()
