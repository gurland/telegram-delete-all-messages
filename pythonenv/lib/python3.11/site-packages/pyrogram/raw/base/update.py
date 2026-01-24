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

Update = Union[raw.types.UpdateAttachMenuBots, raw.types.UpdateAutoSaveSettings, raw.types.UpdateBotCallbackQuery, raw.types.UpdateBotChatInviteRequester, raw.types.UpdateBotCommands, raw.types.UpdateBotInlineQuery, raw.types.UpdateBotInlineSend, raw.types.UpdateBotMenuButton, raw.types.UpdateBotPrecheckoutQuery, raw.types.UpdateBotShippingQuery, raw.types.UpdateBotStopped, raw.types.UpdateBotWebhookJSON, raw.types.UpdateBotWebhookJSONQuery, raw.types.UpdateChannel, raw.types.UpdateChannelAvailableMessages, raw.types.UpdateChannelMessageForwards, raw.types.UpdateChannelMessageViews, raw.types.UpdateChannelParticipant, raw.types.UpdateChannelPinnedTopic, raw.types.UpdateChannelPinnedTopics, raw.types.UpdateChannelReadMessagesContents, raw.types.UpdateChannelTooLong, raw.types.UpdateChannelUserTyping, raw.types.UpdateChannelWebPage, raw.types.UpdateChat, raw.types.UpdateChatDefaultBannedRights, raw.types.UpdateChatParticipant, raw.types.UpdateChatParticipantAdd, raw.types.UpdateChatParticipantAdmin, raw.types.UpdateChatParticipantDelete, raw.types.UpdateChatParticipants, raw.types.UpdateChatUserTyping, raw.types.UpdateConfig, raw.types.UpdateContactsReset, raw.types.UpdateDcOptions, raw.types.UpdateDeleteChannelMessages, raw.types.UpdateDeleteMessages, raw.types.UpdateDeleteScheduledMessages, raw.types.UpdateDialogFilter, raw.types.UpdateDialogFilterOrder, raw.types.UpdateDialogFilters, raw.types.UpdateDialogPinned, raw.types.UpdateDialogUnreadMark, raw.types.UpdateDraftMessage, raw.types.UpdateEditChannelMessage, raw.types.UpdateEditMessage, raw.types.UpdateEncryptedChatTyping, raw.types.UpdateEncryptedMessagesRead, raw.types.UpdateEncryption, raw.types.UpdateFavedStickers, raw.types.UpdateFolderPeers, raw.types.UpdateGeoLiveViewed, raw.types.UpdateGroupCall, raw.types.UpdateGroupCallConnection, raw.types.UpdateGroupCallParticipants, raw.types.UpdateGroupInvitePrivacyForbidden, raw.types.UpdateInlineBotCallbackQuery, raw.types.UpdateLangPack, raw.types.UpdateLangPackTooLong, raw.types.UpdateLoginToken, raw.types.UpdateMessageExtendedMedia, raw.types.UpdateMessageID, raw.types.UpdateMessagePoll, raw.types.UpdateMessagePollVote, raw.types.UpdateMessageReactions, raw.types.UpdateMoveStickerSetToTop, raw.types.UpdateNewChannelMessage, raw.types.UpdateNewEncryptedMessage, raw.types.UpdateNewMessage, raw.types.UpdateNewScheduledMessage, raw.types.UpdateNewStickerSet, raw.types.UpdateNotifySettings, raw.types.UpdatePeerBlocked, raw.types.UpdatePeerHistoryTTL, raw.types.UpdatePeerLocated, raw.types.UpdatePeerSettings, raw.types.UpdatePendingJoinRequests, raw.types.UpdatePhoneCall, raw.types.UpdatePhoneCallSignalingData, raw.types.UpdatePinnedChannelMessages, raw.types.UpdatePinnedDialogs, raw.types.UpdatePinnedMessages, raw.types.UpdatePrivacy, raw.types.UpdatePtsChanged, raw.types.UpdateReadChannelDiscussionInbox, raw.types.UpdateReadChannelDiscussionOutbox, raw.types.UpdateReadChannelInbox, raw.types.UpdateReadChannelOutbox, raw.types.UpdateReadFeaturedEmojiStickers, raw.types.UpdateReadFeaturedStickers, raw.types.UpdateReadHistoryInbox, raw.types.UpdateReadHistoryOutbox, raw.types.UpdateReadMessagesContents, raw.types.UpdateRecentEmojiStatuses, raw.types.UpdateRecentReactions, raw.types.UpdateRecentStickers, raw.types.UpdateSavedGifs, raw.types.UpdateSavedRingtones, raw.types.UpdateServiceNotification, raw.types.UpdateStickerSets, raw.types.UpdateStickerSetsOrder, raw.types.UpdateTheme, raw.types.UpdateTranscribedAudio, raw.types.UpdateUser, raw.types.UpdateUserEmojiStatus, raw.types.UpdateUserName, raw.types.UpdateUserPhone, raw.types.UpdateUserStatus, raw.types.UpdateUserTyping, raw.types.UpdateWebPage, raw.types.UpdateWebViewResultSent]


# noinspection PyRedeclaration
class Update:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 111 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            UpdateAttachMenuBots
            UpdateAutoSaveSettings
            UpdateBotCallbackQuery
            UpdateBotChatInviteRequester
            UpdateBotCommands
            UpdateBotInlineQuery
            UpdateBotInlineSend
            UpdateBotMenuButton
            UpdateBotPrecheckoutQuery
            UpdateBotShippingQuery
            UpdateBotStopped
            UpdateBotWebhookJSON
            UpdateBotWebhookJSONQuery
            UpdateChannel
            UpdateChannelAvailableMessages
            UpdateChannelMessageForwards
            UpdateChannelMessageViews
            UpdateChannelParticipant
            UpdateChannelPinnedTopic
            UpdateChannelPinnedTopics
            UpdateChannelReadMessagesContents
            UpdateChannelTooLong
            UpdateChannelUserTyping
            UpdateChannelWebPage
            UpdateChat
            UpdateChatDefaultBannedRights
            UpdateChatParticipant
            UpdateChatParticipantAdd
            UpdateChatParticipantAdmin
            UpdateChatParticipantDelete
            UpdateChatParticipants
            UpdateChatUserTyping
            UpdateConfig
            UpdateContactsReset
            UpdateDcOptions
            UpdateDeleteChannelMessages
            UpdateDeleteMessages
            UpdateDeleteScheduledMessages
            UpdateDialogFilter
            UpdateDialogFilterOrder
            UpdateDialogFilters
            UpdateDialogPinned
            UpdateDialogUnreadMark
            UpdateDraftMessage
            UpdateEditChannelMessage
            UpdateEditMessage
            UpdateEncryptedChatTyping
            UpdateEncryptedMessagesRead
            UpdateEncryption
            UpdateFavedStickers
            UpdateFolderPeers
            UpdateGeoLiveViewed
            UpdateGroupCall
            UpdateGroupCallConnection
            UpdateGroupCallParticipants
            UpdateGroupInvitePrivacyForbidden
            UpdateInlineBotCallbackQuery
            UpdateLangPack
            UpdateLangPackTooLong
            UpdateLoginToken
            UpdateMessageExtendedMedia
            UpdateMessageID
            UpdateMessagePoll
            UpdateMessagePollVote
            UpdateMessageReactions
            UpdateMoveStickerSetToTop
            UpdateNewChannelMessage
            UpdateNewEncryptedMessage
            UpdateNewMessage
            UpdateNewScheduledMessage
            UpdateNewStickerSet
            UpdateNotifySettings
            UpdatePeerBlocked
            UpdatePeerHistoryTTL
            UpdatePeerLocated
            UpdatePeerSettings
            UpdatePendingJoinRequests
            UpdatePhoneCall
            UpdatePhoneCallSignalingData
            UpdatePinnedChannelMessages
            UpdatePinnedDialogs
            UpdatePinnedMessages
            UpdatePrivacy
            UpdatePtsChanged
            UpdateReadChannelDiscussionInbox
            UpdateReadChannelDiscussionOutbox
            UpdateReadChannelInbox
            UpdateReadChannelOutbox
            UpdateReadFeaturedEmojiStickers
            UpdateReadFeaturedStickers
            UpdateReadHistoryInbox
            UpdateReadHistoryOutbox
            UpdateReadMessagesContents
            UpdateRecentEmojiStatuses
            UpdateRecentReactions
            UpdateRecentStickers
            UpdateSavedGifs
            UpdateSavedRingtones
            UpdateServiceNotification
            UpdateStickerSets
            UpdateStickerSetsOrder
            UpdateTheme
            UpdateTranscribedAudio
            UpdateUser
            UpdateUserEmojiStatus
            UpdateUserName
            UpdateUserPhone
            UpdateUserStatus
            UpdateUserTyping
            UpdateWebPage
            UpdateWebViewResultSent
    """

    QUALNAME = "pyrogram.raw.base.Update"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/update")
