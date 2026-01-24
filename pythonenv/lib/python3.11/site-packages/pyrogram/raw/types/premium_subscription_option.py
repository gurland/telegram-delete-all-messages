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


class PremiumSubscriptionOption(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.PremiumSubscriptionOption`.

    Details:
        - Layer: ``158``
        - ID: ``5F2D1DF2``

    Parameters:
        months (``int`` ``32-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        bot_url (``str``):
            N/A

        current (``bool``, *optional*):
            N/A

        can_purchase_upgrade (``bool``, *optional*):
            N/A

        transaction (``str``, *optional*):
            N/A

        store_product (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["months", "currency", "amount", "bot_url", "current", "can_purchase_upgrade", "transaction", "store_product"]

    ID = 0x5f2d1df2
    QUALNAME = "types.PremiumSubscriptionOption"

    def __init__(self, *, months: int, currency: str, amount: int, bot_url: str, current: Optional[bool] = None, can_purchase_upgrade: Optional[bool] = None, transaction: Optional[str] = None, store_product: Optional[str] = None) -> None:
        self.months = months  # int
        self.currency = currency  # string
        self.amount = amount  # long
        self.bot_url = bot_url  # string
        self.current = current  # flags.1?true
        self.can_purchase_upgrade = can_purchase_upgrade  # flags.2?true
        self.transaction = transaction  # flags.3?string
        self.store_product = store_product  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PremiumSubscriptionOption":
        
        flags = Int.read(b)
        
        current = True if flags & (1 << 1) else False
        can_purchase_upgrade = True if flags & (1 << 2) else False
        transaction = String.read(b) if flags & (1 << 3) else None
        months = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        bot_url = String.read(b)
        
        store_product = String.read(b) if flags & (1 << 0) else None
        return PremiumSubscriptionOption(months=months, currency=currency, amount=amount, bot_url=bot_url, current=current, can_purchase_upgrade=can_purchase_upgrade, transaction=transaction, store_product=store_product)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.current else 0
        flags |= (1 << 2) if self.can_purchase_upgrade else 0
        flags |= (1 << 3) if self.transaction is not None else 0
        flags |= (1 << 0) if self.store_product is not None else 0
        b.write(Int(flags))
        
        if self.transaction is not None:
            b.write(String(self.transaction))
        
        b.write(Int(self.months))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        b.write(String(self.bot_url))
        
        if self.store_product is not None:
            b.write(String(self.store_product))
        
        return b.getvalue()
