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


class WebPageNotModified(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.WebPage`.

    Details:
        - Layer: ``158``
        - ID: ``7311CA11``

    Parameters:
        cached_page_views (``int`` ``32-bit``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPage
    """

    __slots__: List[str] = ["cached_page_views"]

    ID = 0x7311ca11
    QUALNAME = "types.WebPageNotModified"

    def __init__(self, *, cached_page_views: Optional[int] = None) -> None:
        self.cached_page_views = cached_page_views  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "WebPageNotModified":
        
        flags = Int.read(b)
        
        cached_page_views = Int.read(b) if flags & (1 << 0) else None
        return WebPageNotModified(cached_page_views=cached_page_views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.cached_page_views is not None else 0
        b.write(Int(flags))
        
        if self.cached_page_views is not None:
            b.write(Int(self.cached_page_views))
        
        return b.getvalue()
