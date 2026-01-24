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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

MessageAction = Union[raw.types.MessageActionBotAllowed, raw.types.MessageActionChannelCreate, raw.types.MessageActionChannelMigrateFrom, raw.types.MessageActionChatAddUser, raw.types.MessageActionChatCreate, raw.types.MessageActionChatDeletePhoto, raw.types.MessageActionChatDeleteUser, raw.types.MessageActionChatEditPhoto, raw.types.MessageActionChatEditTitle, raw.types.MessageActionChatJoinedByLink, raw.types.MessageActionChatJoinedByRequest, raw.types.MessageActionChatMigrateTo, raw.types.MessageActionContactSignUp, raw.types.MessageActionCustomAction, raw.types.MessageActionEmpty, raw.types.MessageActionGameScore, raw.types.MessageActionGeoProximityReached, raw.types.MessageActionGiftPremium, raw.types.MessageActionGroupCall, raw.types.MessageActionGroupCallScheduled, raw.types.MessageActionHistoryClear, raw.types.MessageActionInviteToGroupCall, raw.types.MessageActionPaymentSent, raw.types.MessageActionPaymentSentMe, raw.types.MessageActionPhoneCall, raw.types.MessageActionPinMessage, raw.types.MessageActionRequestedPeer, raw.types.MessageActionScreenshotTaken, raw.types.MessageActionSecureValuesSent, raw.types.MessageActionSecureValuesSentMe, raw.types.MessageActionSetChatTheme, raw.types.MessageActionSetChatWallPaper, raw.types.MessageActionSetMessagesTTL, raw.types.MessageActionSetSameChatWallPaper, raw.types.MessageActionSuggestProfilePhoto, raw.types.MessageActionTopicCreate, raw.types.MessageActionTopicEdit, raw.types.MessageActionWebViewDataSent, raw.types.MessageActionWebViewDataSentMe]


# noinspection PyRedeclaration
class MessageAction:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 39 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            MessageActionBotAllowed
            MessageActionChannelCreate
            MessageActionChannelMigrateFrom
            MessageActionChatAddUser
            MessageActionChatCreate
            MessageActionChatDeletePhoto
            MessageActionChatDeleteUser
            MessageActionChatEditPhoto
            MessageActionChatEditTitle
            MessageActionChatJoinedByLink
            MessageActionChatJoinedByRequest
            MessageActionChatMigrateTo
            MessageActionContactSignUp
            MessageActionCustomAction
            MessageActionEmpty
            MessageActionGameScore
            MessageActionGeoProximityReached
            MessageActionGiftPremium
            MessageActionGroupCall
            MessageActionGroupCallScheduled
            MessageActionHistoryClear
            MessageActionInviteToGroupCall
            MessageActionPaymentSent
            MessageActionPaymentSentMe
            MessageActionPhoneCall
            MessageActionPinMessage
            MessageActionRequestedPeer
            MessageActionScreenshotTaken
            MessageActionSecureValuesSent
            MessageActionSecureValuesSentMe
            MessageActionSetChatTheme
            MessageActionSetChatWallPaper
            MessageActionSetMessagesTTL
            MessageActionSetSameChatWallPaper
            MessageActionSuggestProfilePhoto
            MessageActionTopicCreate
            MessageActionTopicEdit
            MessageActionWebViewDataSent
            MessageActionWebViewDataSentMe
    """

    QUALNAME = "pyrogram.raw.base.MessageAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/message-action")
