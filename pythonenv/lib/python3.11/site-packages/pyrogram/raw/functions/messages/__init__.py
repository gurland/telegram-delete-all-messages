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

from .get_messages import GetMessages
from .get_dialogs import GetDialogs
from .get_history import GetHistory
from .search import Search
from .read_history import ReadHistory
from .delete_history import DeleteHistory
from .delete_messages import DeleteMessages
from .received_messages import ReceivedMessages
from .set_typing import SetTyping
from .send_message import SendMessage
from .send_media import SendMedia
from .forward_messages import ForwardMessages
from .report_spam import ReportSpam
from .get_peer_settings import GetPeerSettings
from .report import Report
from .get_chats import GetChats
from .get_full_chat import GetFullChat
from .edit_chat_title import EditChatTitle
from .edit_chat_photo import EditChatPhoto
from .add_chat_user import AddChatUser
from .delete_chat_user import DeleteChatUser
from .create_chat import CreateChat
from .get_dh_config import GetDhConfig
from .request_encryption import RequestEncryption
from .accept_encryption import AcceptEncryption
from .discard_encryption import DiscardEncryption
from .set_encrypted_typing import SetEncryptedTyping
from .read_encrypted_history import ReadEncryptedHistory
from .send_encrypted import SendEncrypted
from .send_encrypted_file import SendEncryptedFile
from .send_encrypted_service import SendEncryptedService
from .received_queue import ReceivedQueue
from .report_encrypted_spam import ReportEncryptedSpam
from .read_message_contents import ReadMessageContents
from .get_stickers import GetStickers
from .get_all_stickers import GetAllStickers
from .get_web_page_preview import GetWebPagePreview
from .export_chat_invite import ExportChatInvite
from .check_chat_invite import CheckChatInvite
from .import_chat_invite import ImportChatInvite
from .get_sticker_set import GetStickerSet
from .install_sticker_set import InstallStickerSet
from .uninstall_sticker_set import UninstallStickerSet
from .start_bot import StartBot
from .get_messages_views import GetMessagesViews
from .edit_chat_admin import EditChatAdmin
from .migrate_chat import MigrateChat
from .search_global import SearchGlobal
from .reorder_sticker_sets import ReorderStickerSets
from .get_document_by_hash import GetDocumentByHash
from .get_saved_gifs import GetSavedGifs
from .save_gif import SaveGif
from .get_inline_bot_results import GetInlineBotResults
from .set_inline_bot_results import SetInlineBotResults
from .send_inline_bot_result import SendInlineBotResult
from .get_message_edit_data import GetMessageEditData
from .edit_message import EditMessage
from .edit_inline_bot_message import EditInlineBotMessage
from .get_bot_callback_answer import GetBotCallbackAnswer
from .set_bot_callback_answer import SetBotCallbackAnswer
from .get_peer_dialogs import GetPeerDialogs
from .save_draft import SaveDraft
from .get_all_drafts import GetAllDrafts
from .get_featured_stickers import GetFeaturedStickers
from .read_featured_stickers import ReadFeaturedStickers
from .get_recent_stickers import GetRecentStickers
from .save_recent_sticker import SaveRecentSticker
from .clear_recent_stickers import ClearRecentStickers
from .get_archived_stickers import GetArchivedStickers
from .get_mask_stickers import GetMaskStickers
from .get_attached_stickers import GetAttachedStickers
from .set_game_score import SetGameScore
from .set_inline_game_score import SetInlineGameScore
from .get_game_high_scores import GetGameHighScores
from .get_inline_game_high_scores import GetInlineGameHighScores
from .get_common_chats import GetCommonChats
from .get_all_chats import GetAllChats
from .get_web_page import GetWebPage
from .toggle_dialog_pin import ToggleDialogPin
from .reorder_pinned_dialogs import ReorderPinnedDialogs
from .get_pinned_dialogs import GetPinnedDialogs
from .set_bot_shipping_results import SetBotShippingResults
from .set_bot_precheckout_results import SetBotPrecheckoutResults
from .upload_media import UploadMedia
from .send_screenshot_notification import SendScreenshotNotification
from .get_faved_stickers import GetFavedStickers
from .fave_sticker import FaveSticker
from .get_unread_mentions import GetUnreadMentions
from .read_mentions import ReadMentions
from .get_recent_locations import GetRecentLocations
from .send_multi_media import SendMultiMedia
from .upload_encrypted_file import UploadEncryptedFile
from .search_sticker_sets import SearchStickerSets
from .get_split_ranges import GetSplitRanges
from .mark_dialog_unread import MarkDialogUnread
from .get_dialog_unread_marks import GetDialogUnreadMarks
from .clear_all_drafts import ClearAllDrafts
from .update_pinned_message import UpdatePinnedMessage
from .send_vote import SendVote
from .get_poll_results import GetPollResults
from .get_onlines import GetOnlines
from .edit_chat_about import EditChatAbout
from .edit_chat_default_banned_rights import EditChatDefaultBannedRights
from .get_emoji_keywords import GetEmojiKeywords
from .get_emoji_keywords_difference import GetEmojiKeywordsDifference
from .get_emoji_keywords_languages import GetEmojiKeywordsLanguages
from .get_emoji_url import GetEmojiURL
from .get_search_counters import GetSearchCounters
from .request_url_auth import RequestUrlAuth
from .accept_url_auth import AcceptUrlAuth
from .hide_peer_settings_bar import HidePeerSettingsBar
from .get_scheduled_history import GetScheduledHistory
from .get_scheduled_messages import GetScheduledMessages
from .send_scheduled_messages import SendScheduledMessages
from .delete_scheduled_messages import DeleteScheduledMessages
from .get_poll_votes import GetPollVotes
from .toggle_sticker_sets import ToggleStickerSets
from .get_dialog_filters import GetDialogFilters
from .get_suggested_dialog_filters import GetSuggestedDialogFilters
from .update_dialog_filter import UpdateDialogFilter
from .update_dialog_filters_order import UpdateDialogFiltersOrder
from .get_old_featured_stickers import GetOldFeaturedStickers
from .get_replies import GetReplies
from .get_discussion_message import GetDiscussionMessage
from .read_discussion import ReadDiscussion
from .unpin_all_messages import UnpinAllMessages
from .delete_chat import DeleteChat
from .delete_phone_call_history import DeletePhoneCallHistory
from .check_history_import import CheckHistoryImport
from .init_history_import import InitHistoryImport
from .upload_imported_media import UploadImportedMedia
from .start_history_import import StartHistoryImport
from .get_exported_chat_invites import GetExportedChatInvites
from .get_exported_chat_invite import GetExportedChatInvite
from .edit_exported_chat_invite import EditExportedChatInvite
from .delete_revoked_exported_chat_invites import DeleteRevokedExportedChatInvites
from .delete_exported_chat_invite import DeleteExportedChatInvite
from .get_admins_with_invites import GetAdminsWithInvites
from .get_chat_invite_importers import GetChatInviteImporters
from .set_history_ttl import SetHistoryTTL
from .check_history_import_peer import CheckHistoryImportPeer
from .set_chat_theme import SetChatTheme
from .get_message_read_participants import GetMessageReadParticipants
from .get_search_results_calendar import GetSearchResultsCalendar
from .get_search_results_positions import GetSearchResultsPositions
from .hide_chat_join_request import HideChatJoinRequest
from .hide_all_chat_join_requests import HideAllChatJoinRequests
from .toggle_no_forwards import ToggleNoForwards
from .save_default_send_as import SaveDefaultSendAs
from .send_reaction import SendReaction
from .get_messages_reactions import GetMessagesReactions
from .get_message_reactions_list import GetMessageReactionsList
from .set_chat_available_reactions import SetChatAvailableReactions
from .get_available_reactions import GetAvailableReactions
from .set_default_reaction import SetDefaultReaction
from .translate_text import TranslateText
from .get_unread_reactions import GetUnreadReactions
from .read_reactions import ReadReactions
from .search_sent_media import SearchSentMedia
from .get_attach_menu_bots import GetAttachMenuBots
from .get_attach_menu_bot import GetAttachMenuBot
from .toggle_bot_in_attach_menu import ToggleBotInAttachMenu
from .request_web_view import RequestWebView
from .prolong_web_view import ProlongWebView
from .request_simple_web_view import RequestSimpleWebView
from .send_web_view_result_message import SendWebViewResultMessage
from .send_web_view_data import SendWebViewData
from .transcribe_audio import TranscribeAudio
from .rate_transcribed_audio import RateTranscribedAudio
from .get_custom_emoji_documents import GetCustomEmojiDocuments
from .get_emoji_stickers import GetEmojiStickers
from .get_featured_emoji_stickers import GetFeaturedEmojiStickers
from .report_reaction import ReportReaction
from .get_top_reactions import GetTopReactions
from .get_recent_reactions import GetRecentReactions
from .clear_recent_reactions import ClearRecentReactions
from .get_extended_media import GetExtendedMedia
from .set_default_history_ttl import SetDefaultHistoryTTL
from .get_default_history_ttl import GetDefaultHistoryTTL
from .send_bot_requested_peer import SendBotRequestedPeer
from .get_emoji_groups import GetEmojiGroups
from .get_emoji_status_groups import GetEmojiStatusGroups
from .get_emoji_profile_photo_groups import GetEmojiProfilePhotoGroups
from .search_custom_emoji import SearchCustomEmoji
from .toggle_peer_translations import TogglePeerTranslations
from .get_bot_app import GetBotApp
from .request_app_web_view import RequestAppWebView
from .set_chat_wall_paper import SetChatWallPaper
