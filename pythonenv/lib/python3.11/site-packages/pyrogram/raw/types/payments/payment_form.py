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


class PaymentForm(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.payments.PaymentForm`.

    Details:
        - Layer: ``158``
        - ID: ``A0058751``

    Parameters:
        form_id (``int`` ``64-bit``):
            N/A

        bot_id (``int`` ``64-bit``):
            N/A

        title (``str``):
            N/A

        description (``str``):
            N/A

        invoice (:obj:`Invoice <pyrogram.raw.base.Invoice>`):
            N/A

        provider_id (``int`` ``64-bit``):
            N/A

        url (``str``):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        can_save_credentials (``bool``, *optional*):
            N/A

        password_missing (``bool``, *optional*):
            N/A

        photo (:obj:`WebDocument <pyrogram.raw.base.WebDocument>`, *optional*):
            N/A

        native_provider (``str``, *optional*):
            N/A

        native_params (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`, *optional*):
            N/A

        additional_methods (List of :obj:`PaymentFormMethod <pyrogram.raw.base.PaymentFormMethod>`, *optional*):
            N/A

        saved_info (:obj:`PaymentRequestedInfo <pyrogram.raw.base.PaymentRequestedInfo>`, *optional*):
            N/A

        saved_credentials (List of :obj:`PaymentSavedCredentials <pyrogram.raw.base.PaymentSavedCredentials>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetPaymentForm
    """

    __slots__: List[str] = ["form_id", "bot_id", "title", "description", "invoice", "provider_id", "url", "users", "can_save_credentials", "password_missing", "photo", "native_provider", "native_params", "additional_methods", "saved_info", "saved_credentials"]

    ID = 0xa0058751
    QUALNAME = "types.payments.PaymentForm"

    def __init__(self, *, form_id: int, bot_id: int, title: str, description: str, invoice: "raw.base.Invoice", provider_id: int, url: str, users: List["raw.base.User"], can_save_credentials: Optional[bool] = None, password_missing: Optional[bool] = None, photo: "raw.base.WebDocument" = None, native_provider: Optional[str] = None, native_params: "raw.base.DataJSON" = None, additional_methods: Optional[List["raw.base.PaymentFormMethod"]] = None, saved_info: "raw.base.PaymentRequestedInfo" = None, saved_credentials: Optional[List["raw.base.PaymentSavedCredentials"]] = None) -> None:
        self.form_id = form_id  # long
        self.bot_id = bot_id  # long
        self.title = title  # string
        self.description = description  # string
        self.invoice = invoice  # Invoice
        self.provider_id = provider_id  # long
        self.url = url  # string
        self.users = users  # Vector<User>
        self.can_save_credentials = can_save_credentials  # flags.2?true
        self.password_missing = password_missing  # flags.3?true
        self.photo = photo  # flags.5?WebDocument
        self.native_provider = native_provider  # flags.4?string
        self.native_params = native_params  # flags.4?DataJSON
        self.additional_methods = additional_methods  # flags.6?Vector<PaymentFormMethod>
        self.saved_info = saved_info  # flags.0?PaymentRequestedInfo
        self.saved_credentials = saved_credentials  # flags.1?Vector<PaymentSavedCredentials>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PaymentForm":
        
        flags = Int.read(b)
        
        can_save_credentials = True if flags & (1 << 2) else False
        password_missing = True if flags & (1 << 3) else False
        form_id = Long.read(b)
        
        bot_id = Long.read(b)
        
        title = String.read(b)
        
        description = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 5) else None
        
        invoice = TLObject.read(b)
        
        provider_id = Long.read(b)
        
        url = String.read(b)
        
        native_provider = String.read(b) if flags & (1 << 4) else None
        native_params = TLObject.read(b) if flags & (1 << 4) else None
        
        additional_methods = TLObject.read(b) if flags & (1 << 6) else []
        
        saved_info = TLObject.read(b) if flags & (1 << 0) else None
        
        saved_credentials = TLObject.read(b) if flags & (1 << 1) else []
        
        users = TLObject.read(b)
        
        return PaymentForm(form_id=form_id, bot_id=bot_id, title=title, description=description, invoice=invoice, provider_id=provider_id, url=url, users=users, can_save_credentials=can_save_credentials, password_missing=password_missing, photo=photo, native_provider=native_provider, native_params=native_params, additional_methods=additional_methods, saved_info=saved_info, saved_credentials=saved_credentials)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.can_save_credentials else 0
        flags |= (1 << 3) if self.password_missing else 0
        flags |= (1 << 5) if self.photo is not None else 0
        flags |= (1 << 4) if self.native_provider is not None else 0
        flags |= (1 << 4) if self.native_params is not None else 0
        flags |= (1 << 6) if self.additional_methods else 0
        flags |= (1 << 0) if self.saved_info is not None else 0
        flags |= (1 << 1) if self.saved_credentials else 0
        b.write(Int(flags))
        
        b.write(Long(self.form_id))
        
        b.write(Long(self.bot_id))
        
        b.write(String(self.title))
        
        b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        b.write(self.invoice.write())
        
        b.write(Long(self.provider_id))
        
        b.write(String(self.url))
        
        if self.native_provider is not None:
            b.write(String(self.native_provider))
        
        if self.native_params is not None:
            b.write(self.native_params.write())
        
        if self.additional_methods is not None:
            b.write(Vector(self.additional_methods))
        
        if self.saved_info is not None:
            b.write(self.saved_info.write())
        
        if self.saved_credentials is not None:
            b.write(Vector(self.saved_credentials))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
