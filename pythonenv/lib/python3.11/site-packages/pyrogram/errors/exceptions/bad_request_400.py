# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from ..rpc_error import RPCError


class BadRequest(RPCError):
    """Bad Request"""
    CODE = 400
    """``int``: RPC Error Code"""
    NAME = __doc__


class AboutTooLong(BadRequest):
    """The provided about/bio text is too long"""
    ID = "ABOUT_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AccessTokenExpired(BadRequest):
    """The bot token has expired"""
    ID = "ACCESS_TOKEN_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AccessTokenInvalid(BadRequest):
    """The bot access token is invalid"""
    ID = "ACCESS_TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AdminsTooMuch(BadRequest):
    """The chat has too many administrators"""
    ID = "ADMINS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AdminRankEmojiNotAllowed(BadRequest):
    """Emoji are not allowed in custom administrator titles"""
    ID = "ADMIN_RANK_EMOJI_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AdminRankInvalid(BadRequest):
    """The custom administrator title is invalid or too long"""
    ID = "ADMIN_RANK_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AlbumPhotosTooMany(BadRequest):
    """Too many photos were included in the album"""
    ID = "ALBUM_PHOTOS_TOO_MANY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ApiIdInvalid(BadRequest):
    """The api_id/api_hash combination is invalid"""
    ID = "API_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ApiIdPublishedFlood(BadRequest):
    """You are using an API key that is limited on the server side because it was published somewhere"""
    ID = "API_ID_PUBLISHED_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ArticleTitleEmpty(BadRequest):
    """The article title is empty"""
    ID = "ARTICLE_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AudioTitleEmpty(BadRequest):
    """The title attribute of the audio is empty"""
    ID = "AUDIO_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AuthBytesInvalid(BadRequest):
    """The authorization bytes are invalid"""
    ID = "AUTH_BYTES_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AuthTokenAlreadyAccepted(BadRequest):
    """The authorization token was already used"""
    ID = "AUTH_TOKEN_ALREADY_ACCEPTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AuthTokenExpired(BadRequest):
    """The provided authorization token has expired and the updated QR-code must be re-scanned"""
    ID = "AUTH_TOKEN_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AuthTokenInvalid(BadRequest):
    """An invalid authorization token was provided"""
    ID = "AUTH_TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class AutoarchiveNotAvailable(BadRequest):
    """This feature is not yet enabled for your account due to it not receiving too many private messages from strangers"""
    ID = "AUTOARCHIVE_NOT_AVAILABLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BankCardNumberInvalid(BadRequest):
    """The credit card number is invalid"""
    ID = "BANK_CARD_NUMBER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BannedRightsInvalid(BadRequest):
    """You provided a set of restrictions that is invalid"""
    ID = "BANNED_RIGHTS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BasePortLocInvalid(BadRequest):
    """The base port location is invalid"""
    ID = "BASE_PORT_LOC_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotsTooMuch(BadRequest):
    """The chat has too many bots"""
    ID = "BOTS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotChannelsNa(BadRequest):
    """Bots can't edit admin privileges"""
    ID = "BOT_CHANNELS_NA"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotCommandDescriptionInvalid(BadRequest):
    """The command description was empty, too long or had invalid characters"""
    ID = "BOT_COMMAND_DESCRIPTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotDomainInvalid(BadRequest):
    """The domain used for the auth button does not match the one configured in @BotFather"""
    ID = "BOT_DOMAIN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotGamesDisabled(BadRequest):
    """Bot games cannot be used in this type of chat"""
    ID = "BOT_GAMES_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotGroupsBlocked(BadRequest):
    """This bot can't be added to groups"""
    ID = "BOT_GROUPS_BLOCKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotInlineDisabled(BadRequest):
    """The inline feature of the bot is disabled"""
    ID = "BOT_INLINE_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotInvalid(BadRequest):
    """This is not a valid bot"""
    ID = "BOT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotMethodInvalid(BadRequest):
    """The method can't be used by bots"""
    ID = "BOT_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotMissing(BadRequest):
    """This method can only be run by a bot"""
    ID = "BOT_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotOnesideNotAvail(BadRequest):
    """Bots can't pin messages for one side only in private chats"""
    ID = "BOT_ONESIDE_NOT_AVAIL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotPaymentsDisabled(BadRequest):
    """This method can only be run by a bot"""
    ID = "BOT_PAYMENTS_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotPollsDisabled(BadRequest):
    """Sending polls by bots has been disabled"""
    ID = "BOT_POLLS_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotResponseTimeout(BadRequest):
    """The bot did not answer to the callback query in time"""
    ID = "BOT_RESPONSE_TIMEOUT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BotScoreNotModified(BadRequest):
    """The bot score was not modified"""
    ID = "BOT_SCORE_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BroadcastIdInvalid(BadRequest):
    """The channel is invalid"""
    ID = "BROADCAST_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BroadcastPublicVotersForbidden(BadRequest):
    """Polls with public voters cannot be sent in channels"""
    ID = "BROADCAST_PUBLIC_VOTERS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class BroadcastRequired(BadRequest):
    """The request can only be used with a channel"""
    ID = "BROADCAST_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ButtonDataInvalid(BadRequest):
    """The button callback data is invalid or too large"""
    ID = "BUTTON_DATA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ButtonTypeInvalid(BadRequest):
    """The type of one of the buttons you provided is invalid"""
    ID = "BUTTON_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ButtonUrlInvalid(BadRequest):
    """The button url is invalid"""
    ID = "BUTTON_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ButtonUserPrivacyRestricted(BadRequest):
    """The privacy settings of the user specified in a keyboard button do not allow creating such button"""
    ID = "BUTTON_USER_PRIVACY_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CallAlreadyAccepted(BadRequest):
    """The call is already accepted"""
    ID = "CALL_ALREADY_ACCEPTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CallAlreadyDeclined(BadRequest):
    """The call is already declined"""
    ID = "CALL_ALREADY_DECLINED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CallPeerInvalid(BadRequest):
    """The provided call peer object is invalid"""
    ID = "CALL_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CallProtocolFlagsInvalid(BadRequest):
    """Call protocol flags invalid"""
    ID = "CALL_PROTOCOL_FLAGS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CdnMethodInvalid(BadRequest):
    """The method can't be used on CDN DCs"""
    ID = "CDN_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelsAdminPublicTooMuch(BadRequest):
    """You are an administrator of too many public channels"""
    ID = "CHANNELS_ADMIN_PUBLIC_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelsTooMuch(BadRequest):
    """You have joined too many channels or supergroups, leave some and try again"""
    ID = "CHANNELS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelAddInvalid(BadRequest):
    """Internal error."""
    ID = "CHANNEL_ADD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelBanned(BadRequest):
    """The channel is banned"""
    ID = "CHANNEL_BANNED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelInvalid(BadRequest):
    """The channel parameter is invalid"""
    ID = "CHANNEL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelPrivate(BadRequest):
    """The channel/supergroup is not accessible"""
    ID = "CHANNEL_PRIVATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelTooLarge(BadRequest):
    """The channel is too large"""
    ID = "CHANNEL_TOO_LARGE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatAboutNotModified(BadRequest):
    """The chat about text was not modified because you tried to edit it using the same content"""
    ID = "CHAT_ABOUT_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatAboutTooLong(BadRequest):
    """The chat about text is too long"""
    ID = "CHAT_ABOUT_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatAdminRequired(BadRequest):
    """The method requires chat admin privileges"""
    ID = "CHAT_ADMIN_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatForwardsRestricted(BadRequest):
    """The chat restricts forwarding content"""
    ID = "CHAT_FORWARDS_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatIdEmpty(BadRequest):
    """The provided chat id is empty"""
    ID = "CHAT_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatIdInvalid(BadRequest):
    """The chat id being used is invalid or not known yet. Make sure you see the chat before interacting with it"""
    ID = "CHAT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatInvalid(BadRequest):
    """The chat is invalid"""
    ID = "CHAT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatInvitePermanent(BadRequest):
    """The chat invite link is primary"""
    ID = "CHAT_INVITE_PERMANENT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatLinkExists(BadRequest):
    """The action failed because the supergroup is linked to a channel"""
    ID = "CHAT_LINK_EXISTS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatNotModified(BadRequest):
    """The chat settings (title, permissions, photo, etc..) were not modified because you tried to edit them using the same content"""
    ID = "CHAT_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatRestricted(BadRequest):
    """The chat is restricted and cannot be used"""
    ID = "CHAT_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendInlineForbidden(BadRequest):
    """You cannot use inline bots to send messages in this chat"""
    ID = "CHAT_SEND_INLINE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatTitleEmpty(BadRequest):
    """The chat title is empty"""
    ID = "CHAT_TITLE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatTooBig(BadRequest):
    """The chat is too big for this action"""
    ID = "CHAT_TOO_BIG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CodeEmpty(BadRequest):
    """The provided code is empty"""
    ID = "CODE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CodeHashInvalid(BadRequest):
    """The provided code hash invalid"""
    ID = "CODE_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class CodeInvalid(BadRequest):
    """The provided code is invalid (i.e. from email)"""
    ID = "CODE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ConnectionApiIdInvalid(BadRequest):
    """The provided API id is invalid"""
    ID = "CONNECTION_API_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ConnectionAppVersionEmpty(BadRequest):
    """App version is empty"""
    ID = "CONNECTION_APP_VERSION_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ConnectionDeviceModelEmpty(BadRequest):
    """The device model is empty"""
    ID = "CONNECTION_DEVICE_MODEL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ConnectionLangPackInvalid(BadRequest):
    """The specified language pack is not valid"""
    ID = "CONNECTION_LANG_PACK_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ConnectionLayerInvalid(BadRequest):
    """The connection layer is invalid. Missing InvokeWithLayer-InitConnection call"""
    ID = "CONNECTION_LAYER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ConnectionNotInited(BadRequest):
    """The connection was not initialized"""
    ID = "CONNECTION_NOT_INITED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ConnectionSystemEmpty(BadRequest):
    """The connection to the system is empty"""
    ID = "CONNECTION_SYSTEM_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ConnectionSystemLangCodeEmpty(BadRequest):
    """The system language code is empty"""
    ID = "CONNECTION_SYSTEM_LANG_CODE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ContactAddMissing(BadRequest):
    """Contact to add is missing"""
    ID = "CONTACT_ADD_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ContactIdInvalid(BadRequest):
    """The provided contact id is invalid"""
    ID = "CONTACT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ContactNameEmpty(BadRequest):
    """The provided contact name is empty"""
    ID = "CONTACT_NAME_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ContactReqMissing(BadRequest):
    """Missing contact request"""
    ID = "CONTACT_REQ_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class DataInvalid(BadRequest):
    """The encrypted data is invalid"""
    ID = "DATA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class DataJsonInvalid(BadRequest):
    """The provided JSON data is invalid"""
    ID = "DATA_JSON_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class DataTooLong(BadRequest):
    """Data too long"""
    ID = "DATA_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class DateEmpty(BadRequest):
    """The date argument is empty"""
    ID = "DATE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class DcIdInvalid(BadRequest):
    """The dc_id parameter is invalid"""
    ID = "DC_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class DhGAInvalid(BadRequest):
    """The g_a parameter invalid"""
    ID = "DH_G_A_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class DocumentInvalid(BadRequest):
    """The document is invalid"""
    ID = "DOCUMENT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EmailHashExpired(BadRequest):
    """The email hash expired and cannot be used to verify it"""
    ID = "EMAIL_HASH_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EmailInvalid(BadRequest):
    """The email provided is invalid"""
    ID = "EMAIL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EmailUnconfirmed(BadRequest):
    """Email unconfirmed"""
    ID = "EMAIL_UNCONFIRMED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EmailUnconfirmed(BadRequest):
    """The provided email isn't confirmed, {value} is the length of the verification code that was just sent to the email"""
    ID = "EMAIL_UNCONFIRMED_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EmailVerifyExpired(BadRequest):
    """The verification email has expired"""
    ID = "EMAIL_VERIFY_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EmoticonEmpty(BadRequest):
    """The emoticon parameter is empty"""
    ID = "EMOTICON_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EmoticonInvalid(BadRequest):
    """The emoticon parameter is invalid"""
    ID = "EMOTICON_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EmoticonStickerpackMissing(BadRequest):
    """The emoticon sticker pack you are trying to obtain is missing"""
    ID = "EMOTICON_STICKERPACK_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EncryptedMessageInvalid(BadRequest):
    """The special binding message (bind_auth_key_inner) contains invalid data"""
    ID = "ENCRYPTED_MESSAGE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EncryptionAlreadyAccepted(BadRequest):
    """The secret chat is already accepted"""
    ID = "ENCRYPTION_ALREADY_ACCEPTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EncryptionAlreadyDeclined(BadRequest):
    """The secret chat is already declined"""
    ID = "ENCRYPTION_ALREADY_DECLINED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EncryptionDeclined(BadRequest):
    """The secret chat was declined"""
    ID = "ENCRYPTION_DECLINED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EncryptionIdInvalid(BadRequest):
    """The provided secret chat id is invalid"""
    ID = "ENCRYPTION_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EntitiesTooLong(BadRequest):
    """The entity provided contains data that is too long, or you passed too many entities to this message"""
    ID = "ENTITIES_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EntityBoundsInvalid(BadRequest):
    """The message entity bounds are invalid"""
    ID = "ENTITY_BOUNDS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EntityMentionUserInvalid(BadRequest):
    """The mentioned entity is not an user"""
    ID = "ENTITY_MENTION_USER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ErrorTextEmpty(BadRequest):
    """The provided error message is empty"""
    ID = "ERROR_TEXT_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ExpireDateInvalid(BadRequest):
    """The expiration date is invalid"""
    ID = "EXPIRE_DATE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ExportCardInvalid(BadRequest):
    """The provided card is invalid"""
    ID = "EXPORT_CARD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ExternalUrlInvalid(BadRequest):
    """The external media URL is invalid"""
    ID = "EXTERNAL_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FieldNameEmpty(BadRequest):
    """The field with the name FIELD_NAME is missing"""
    ID = "FIELD_NAME_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FieldNameInvalid(BadRequest):
    """The field with the name FIELD_NAME is invalid"""
    ID = "FIELD_NAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FileIdInvalid(BadRequest):
    """The file id is invalid"""
    ID = "FILE_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FileMigrate(BadRequest):
    """The file is in Data Center No. {value}"""
    ID = "FILE_MIGRATE_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartsInvalid(BadRequest):
    """Invalid number of parts."""
    ID = "FILE_PARTS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartEmpty(BadRequest):
    """The file part sent is empty"""
    ID = "FILE_PART_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartInvalid(BadRequest):
    """The file part number is invalid."""
    ID = "FILE_PART_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartLengthInvalid(BadRequest):
    """The length of a file part is invalid"""
    ID = "FILE_PART_LENGTH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartSizeChanged(BadRequest):
    """The part size is different from the size of one of the previous parts in the same file"""
    ID = "FILE_PART_SIZE_CHANGED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartSizeInvalid(BadRequest):
    """The file part size is invalid"""
    ID = "FILE_PART_SIZE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartTooBig(BadRequest):
    """The size limit for the content of the file part has been exceeded"""
    ID = "FILE_PART_TOO_BIG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilePartMissing(BadRequest):
    """Part {value} of the file is missing from storage"""
    ID = "FILE_PART_X_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FileReferenceEmpty(BadRequest):
    """The file id contains an empty file reference, you must obtain a valid one by fetching the message from the origin context"""
    ID = "FILE_REFERENCE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FileReferenceExpired(BadRequest):
    """The file id contains an expired file reference, you must obtain a valid one by fetching the message from the origin context"""
    ID = "FILE_REFERENCE_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FileReferenceInvalid(BadRequest):
    """The file id contains an invalid file reference, you must obtain a valid one by fetching the message from the origin context"""
    ID = "FILE_REFERENCE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FilterIdInvalid(BadRequest):
    """The specified filter ID is invalid"""
    ID = "FILTER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FirstnameInvalid(BadRequest):
    """The first name is invalid"""
    ID = "FIRSTNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FolderIdEmpty(BadRequest):
    """The folder you tried to delete was already empty"""
    ID = "FOLDER_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FolderIdInvalid(BadRequest):
    """The folder id is invalid"""
    ID = "FOLDER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FreshChangeAdminsForbidden(BadRequest):
    """You can't change administrator settings in this chat because your session was logged-in recently"""
    ID = "FRESH_CHANGE_ADMINS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FromMessageBotDisabled(BadRequest):
    """Bots can't use fromMessage min constructors"""
    ID = "FROM_MESSAGE_BOT_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class FromPeerInvalid(BadRequest):
    """The from peer value is invalid"""
    ID = "FROM_PEER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GameBotInvalid(BadRequest):
    """You cannot send that game with the current bot"""
    ID = "GAME_BOT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GeoPointInvalid(BadRequest):
    """Invalid geo point provided"""
    ID = "GEO_POINT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GifContentTypeInvalid(BadRequest):
    """GIF content-type invalid"""
    ID = "GIF_CONTENT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GifIdInvalid(BadRequest):
    """The provided gif/animation id is invalid"""
    ID = "GIF_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GraphInvalidReload(BadRequest):
    """Invalid graph token provided, please reload the stats and provide the updated token"""
    ID = "GRAPH_INVALID_RELOAD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GraphOutdatedReload(BadRequest):
    """The graph data is outdated"""
    ID = "GRAPH_OUTDATED_RELOAD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GroupcallSsrcDuplicateMuch(BadRequest):
    """Too many group call synchronization source duplicates"""
    ID = "GROUPCALL_SSRC_DUPLICATE_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GroupedMediaInvalid(BadRequest):
    """The album contains invalid media"""
    ID = "GROUPED_MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class GroupCallInvalid(BadRequest):
    """The group call is invalid"""
    ID = "GROUP_CALL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class HashInvalid(BadRequest):
    """The provided hash is invalid"""
    ID = "HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ImageProcessFailed(BadRequest):
    """The server failed to process your image"""
    ID = "IMAGE_PROCESS_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ImportFileInvalid(BadRequest):
    """The imported file is invalid"""
    ID = "IMPORT_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ImportFormatUnrecognized(BadRequest):
    """The imported format is unrecognized"""
    ID = "IMPORT_FORMAT_UNRECOGNIZED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ImportIdInvalid(BadRequest):
    """The import id is invalid"""
    ID = "IMPORT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InlineResultExpired(BadRequest):
    """The inline bot query expired"""
    ID = "INLINE_RESULT_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputConstructorInvalid(BadRequest):
    """The provided constructor is invalid"""
    ID = "INPUT_CONSTRUCTOR_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputFetchError(BadRequest):
    """An error occurred while deserializing TL parameters"""
    ID = "INPUT_FETCH_ERROR"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputFetchFail(BadRequest):
    """Failed deserializing TL payload"""
    ID = "INPUT_FETCH_FAIL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputFilterInvalid(BadRequest):
    """The filter is invalid for this query"""
    ID = "INPUT_FILTER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputLayerInvalid(BadRequest):
    """The provided layer is invalid"""
    ID = "INPUT_LAYER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputMethodInvalid(BadRequest):
    """The method invoked is invalid in the current schema"""
    ID = "INPUT_METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputRequestTooLong(BadRequest):
    """The input request is too long"""
    ID = "INPUT_REQUEST_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InputUserDeactivated(BadRequest):
    """The target user has been deleted/deactivated"""
    ID = "INPUT_USER_DEACTIVATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InviteHashEmpty(BadRequest):
    """The invite hash is empty"""
    ID = "INVITE_HASH_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InviteHashExpired(BadRequest):
    """The chat invite link is no longer valid"""
    ID = "INVITE_HASH_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InviteHashInvalid(BadRequest):
    """The invite link hash is invalid"""
    ID = "INVITE_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InviteRequestSent(BadRequest):
    """The request to join this chat or channel has been successfully sent"""
    ID = "INVITE_REQUEST_SENT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InviteRevokedMissing(BadRequest):
    """The action required a chat invite link to be revoked first"""
    ID = "INVITE_REVOKED_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LangPackInvalid(BadRequest):
    """The provided language pack is invalid"""
    ID = "LANG_PACK_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LastnameInvalid(BadRequest):
    """The last name is invalid"""
    ID = "LASTNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LimitInvalid(BadRequest):
    """The limit parameter is invalid"""
    ID = "LIMIT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LinkNotModified(BadRequest):
    """The chat link was not modified because you tried to link to the same target"""
    ID = "LINK_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class LocationInvalid(BadRequest):
    """The file location is invalid"""
    ID = "LOCATION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MaxIdInvalid(BadRequest):
    """The max_id parameter is invalid"""
    ID = "MAX_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MaxQtsInvalid(BadRequest):
    """The provided QTS is invalid"""
    ID = "MAX_QTS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class Md5ChecksumInvalid(BadRequest):
    """The file's checksum did not match the md5_checksum parameter"""
    ID = "MD5_CHECKSUM_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MediaCaptionTooLong(BadRequest):
    """The media caption is too long"""
    ID = "MEDIA_CAPTION_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MediaEmpty(BadRequest):
    """The media you tried to send is invalid"""
    ID = "MEDIA_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MediaInvalid(BadRequest):
    """The media is invalid"""
    ID = "MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MediaNewInvalid(BadRequest):
    """The new media to edit the message with is invalid"""
    ID = "MEDIA_NEW_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MediaPrevInvalid(BadRequest):
    """The previous media cannot be edited with anything else"""
    ID = "MEDIA_PREV_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MegagroupIdInvalid(BadRequest):
    """The supergroup is invalid"""
    ID = "MEGAGROUP_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MegagroupPrehistoryHidden(BadRequest):
    """The action failed because the supergroup has the pre-history hidden"""
    ID = "MEGAGROUP_PREHISTORY_HIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MegagroupRequired(BadRequest):
    """The request can only be used with a supergroup"""
    ID = "MEGAGROUP_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageEditTimeExpired(BadRequest):
    """You can no longer edit this message because too much time has passed"""
    ID = "MESSAGE_EDIT_TIME_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageEmpty(BadRequest):
    """The message sent is empty or contains invalid characters"""
    ID = "MESSAGE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageIdsEmpty(BadRequest):
    """The requested message doesn't exist or you provided no message id"""
    ID = "MESSAGE_IDS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageIdInvalid(BadRequest):
    """The message id is invalid"""
    ID = "MESSAGE_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageNotModified(BadRequest):
    """The message was not modified because you tried to edit it using the same content"""
    ID = "MESSAGE_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessagePollClosed(BadRequest):
    """You can't interact with a closed poll"""
    ID = "MESSAGE_POLL_CLOSED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageTooLong(BadRequest):
    """The message text is too long"""
    ID = "MESSAGE_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MethodInvalid(BadRequest):
    """The API method is invalid and cannot be used"""
    ID = "METHOD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MsgIdInvalid(BadRequest):
    """The message ID used in the peer was invalid"""
    ID = "MSG_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MsgWaitFailed(BadRequest):
    """A waiting call returned an error"""
    ID = "MSG_WAIT_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MultiMediaTooLong(BadRequest):
    """The album/media group contains too many items"""
    ID = "MULTI_MEDIA_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class NewSaltInvalid(BadRequest):
    """The new salt is invalid"""
    ID = "NEW_SALT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class NewSettingsInvalid(BadRequest):
    """The new settings are invalid"""
    ID = "NEW_SETTINGS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class NextOffsetInvalid(BadRequest):
    """The next offset value is invalid"""
    ID = "NEXT_OFFSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class OffsetInvalid(BadRequest):
    """The offset parameter is invalid"""
    ID = "OFFSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class OffsetPeerIdInvalid(BadRequest):
    """The provided offset peer is invalid"""
    ID = "OFFSET_PEER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class OptionsTooMuch(BadRequest):
    """The poll options are too many"""
    ID = "OPTIONS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class OptionInvalid(BadRequest):
    """The option specified is invalid and does not exist in the target poll"""
    ID = "OPTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PackShortNameInvalid(BadRequest):
    """Invalid sticker pack name. It must begin with a letter, can't contain consecutive underscores and must end in '_by_<bot username>'."""
    ID = "PACK_SHORT_NAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PackShortNameOccupied(BadRequest):
    """A sticker pack with this name already exists"""
    ID = "PACK_SHORT_NAME_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PackTitleInvalid(BadRequest):
    """The sticker pack title is invalid"""
    ID = "PACK_TITLE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ParticipantsTooFew(BadRequest):
    """The chat doesn't have enough participants"""
    ID = "PARTICIPANTS_TOO_FEW"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ParticipantVersionOutdated(BadRequest):
    """The other participant is using an outdated Telegram app version"""
    ID = "PARTICIPANT_VERSION_OUTDATED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PasswordEmpty(BadRequest):
    """The password provided is empty"""
    ID = "PASSWORD_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PasswordHashInvalid(BadRequest):
    """The two-step verification password is invalid"""
    ID = "PASSWORD_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PasswordMissing(BadRequest):
    """The account is missing the two-step verification password"""
    ID = "PASSWORD_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PasswordRecoveryNa(BadRequest):
    """The password recovery e-mail is not available"""
    ID = "PASSWORD_RECOVERY_NA"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PasswordRequired(BadRequest):
    """The two-step verification password is required for this method"""
    ID = "PASSWORD_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PasswordTooFresh(BadRequest):
    """The two-step verification password was added recently and you are required to wait {value} seconds"""
    ID = "PASSWORD_TOO_FRESH_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PaymentProviderInvalid(BadRequest):
    """The payment provider was not recognised or its token was invalid"""
    ID = "PAYMENT_PROVIDER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PeerFlood(BadRequest):
    """The method can't be used because your account is currently limited"""
    ID = "PEER_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PeerIdInvalid(BadRequest):
    """The peer id being used is invalid or not known yet. Make sure you meet the peer before interacting with it"""
    ID = "PEER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PeerIdNotSupported(BadRequest):
    """The provided peer id is not supported"""
    ID = "PEER_ID_NOT_SUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PersistentTimestampEmpty(BadRequest):
    """The pts argument is empty"""
    ID = "PERSISTENT_TIMESTAMP_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PersistentTimestampInvalid(BadRequest):
    """The persistent timestamp is invalid"""
    ID = "PERSISTENT_TIMESTAMP_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneCodeEmpty(BadRequest):
    """The phone code is missing"""
    ID = "PHONE_CODE_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneCodeExpired(BadRequest):
    """The confirmation code has expired"""
    ID = "PHONE_CODE_EXPIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneCodeHashEmpty(BadRequest):
    """The phone code hash is missing"""
    ID = "PHONE_CODE_HASH_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneCodeInvalid(BadRequest):
    """The confirmation code is invalid"""
    ID = "PHONE_CODE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberAppSignupForbidden(BadRequest):
    """You can't sign up using this app"""
    ID = "PHONE_NUMBER_APP_SIGNUP_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberBanned(BadRequest):
    """The phone number is banned from Telegram and cannot be used"""
    ID = "PHONE_NUMBER_BANNED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberFlood(BadRequest):
    """This number has tried to login too many times"""
    ID = "PHONE_NUMBER_FLOOD"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberInvalid(BadRequest):
    """The phone number is invalid"""
    ID = "PHONE_NUMBER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberOccupied(BadRequest):
    """The phone number is already in use"""
    ID = "PHONE_NUMBER_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhoneNumberUnoccupied(BadRequest):
    """The phone number is not yet being used"""
    ID = "PHONE_NUMBER_UNOCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhonePasswordProtected(BadRequest):
    """The phone is password protected"""
    ID = "PHONE_PASSWORD_PROTECTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoContentTypeInvalid(BadRequest):
    """The photo content type is invalid"""
    ID = "PHOTO_CONTENT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoContentUrlEmpty(BadRequest):
    """The photo content URL is empty"""
    ID = "PHOTO_CONTENT_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoCropFileMissing(BadRequest):
    """Photo crop file missing"""
    ID = "PHOTO_CROP_FILE_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoCropSizeSmall(BadRequest):
    """The photo is too small"""
    ID = "PHOTO_CROP_SIZE_SMALL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoExtInvalid(BadRequest):
    """The photo extension is invalid"""
    ID = "PHOTO_EXT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoFileMissing(BadRequest):
    """Profile photo file missing"""
    ID = "PHOTO_FILE_MISSING"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoIdInvalid(BadRequest):
    """The photo id is invalid"""
    ID = "PHOTO_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoInvalid(BadRequest):
    """The photo is invalid"""
    ID = "PHOTO_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoInvalidDimensions(BadRequest):
    """The photo dimensions are invalid"""
    ID = "PHOTO_INVALID_DIMENSIONS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoSaveFileInvalid(BadRequest):
    """The photo you tried to send cannot be saved by Telegram"""
    ID = "PHOTO_SAVE_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoThumbUrlEmpty(BadRequest):
    """The photo thumb URL is empty"""
    ID = "PHOTO_THUMB_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PhotoThumbUrlInvalid(BadRequest):
    """The photo thumb URL is invalid"""
    ID = "PHOTO_THUMB_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PinnedDialogsTooMuch(BadRequest):
    """Too many pinned dialogs"""
    ID = "PINNED_DIALOGS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PinRestricted(BadRequest):
    """You can't pin messages in private chats with other people"""
    ID = "PIN_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PollAnswersInvalid(BadRequest):
    """The poll answers are invalid"""
    ID = "POLL_ANSWERS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PollOptionDuplicate(BadRequest):
    """A duplicate option was sent in the same poll"""
    ID = "POLL_OPTION_DUPLICATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PollOptionInvalid(BadRequest):
    """A poll option used invalid data (the data may be too long)"""
    ID = "POLL_OPTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PollQuestionInvalid(BadRequest):
    """The poll question is invalid"""
    ID = "POLL_QUESTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PollUnsupported(BadRequest):
    """This layer does not support polls in the invoked method"""
    ID = "POLL_UNSUPPORTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PollVoteRequired(BadRequest):
    """Cast a vote in the poll before calling this method"""
    ID = "POLL_VOTE_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PrivacyKeyInvalid(BadRequest):
    """The privacy key is invalid"""
    ID = "PRIVACY_KEY_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PrivacyTooLong(BadRequest):
    """Your privacy exception list has exceeded the maximum capacity"""
    ID = "PRIVACY_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PrivacyValueInvalid(BadRequest):
    """The privacy value is invalid"""
    ID = "PRIVACY_VALUE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class QueryIdEmpty(BadRequest):
    """The query ID is empty"""
    ID = "QUERY_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class QueryIdInvalid(BadRequest):
    """The callback query id is invalid"""
    ID = "QUERY_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class QueryTooShort(BadRequest):
    """The query is too short"""
    ID = "QUERY_TOO_SHORT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class QuizCorrectAnswersEmpty(BadRequest):
    """The correct answers of the quiz are empty"""
    ID = "QUIZ_CORRECT_ANSWERS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class QuizCorrectAnswersTooMuch(BadRequest):
    """The quiz contains too many correct answers"""
    ID = "QUIZ_CORRECT_ANSWERS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class QuizCorrectAnswerInvalid(BadRequest):
    """The correct answers of the quiz are invalid"""
    ID = "QUIZ_CORRECT_ANSWER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class QuizMultipleInvalid(BadRequest):
    """A quiz can't have multiple answers"""
    ID = "QUIZ_MULTIPLE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RandomIdEmpty(BadRequest):
    """The random ID is empty"""
    ID = "RANDOM_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RandomIdInvalid(BadRequest):
    """The provided random ID is invalid"""
    ID = "RANDOM_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RandomLengthInvalid(BadRequest):
    """The random length is invalid"""
    ID = "RANDOM_LENGTH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RangesInvalid(BadRequest):
    """Invalid range provided"""
    ID = "RANGES_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ReactionEmpty(BadRequest):
    """The reaction provided is empty"""
    ID = "REACTION_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ReactionInvalid(BadRequest):
    """Invalid reaction provided (only valid emoji are allowed)"""
    ID = "REACTION_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ReflectorNotAvailable(BadRequest):
    """The call reflector is not available"""
    ID = "REFLECTOR_NOT_AVAILABLE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ReplyMarkupBuyEmpty(BadRequest):
    """Reply markup for buy button empty"""
    ID = "REPLY_MARKUP_BUY_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ReplyMarkupGameEmpty(BadRequest):
    """The provided reply markup for the game is empty"""
    ID = "REPLY_MARKUP_GAME_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ReplyMarkupInvalid(BadRequest):
    """The provided reply markup is invalid"""
    ID = "REPLY_MARKUP_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ReplyMarkupTooLong(BadRequest):
    """The reply markup is too long"""
    ID = "REPLY_MARKUP_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ResultsTooMuch(BadRequest):
    """The result contains too many items"""
    ID = "RESULTS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ResultIdDuplicate(BadRequest):
    """The result contains items with duplicated identifiers"""
    ID = "RESULT_ID_DUPLICATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ResultIdEmpty(BadRequest):
    """Result ID empty"""
    ID = "RESULT_ID_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ResultIdInvalid(BadRequest):
    """The given result cannot be used to send the selection to the bot"""
    ID = "RESULT_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ResultTypeInvalid(BadRequest):
    """The result type is invalid"""
    ID = "RESULT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RevoteNotAllowed(BadRequest):
    """You cannot change your vote"""
    ID = "REVOTE_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RsaDecryptFailed(BadRequest):
    """Internal RSA decryption failed"""
    ID = "RSA_DECRYPT_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ScheduleBotNotAllowed(BadRequest):
    """Bots are not allowed to schedule messages"""
    ID = "SCHEDULE_BOT_NOT_ALLOWED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ScheduleDateInvalid(BadRequest):
    """Invalid schedule date provided"""
    ID = "SCHEDULE_DATE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ScheduleDateTooLate(BadRequest):
    """The date you tried to schedule is too far in the future (more than one year)"""
    ID = "SCHEDULE_DATE_TOO_LATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ScheduleStatusPrivate(BadRequest):
    """You cannot schedule a message until the person comes online if their privacy does not show this information"""
    ID = "SCHEDULE_STATUS_PRIVATE"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ScheduleTooMuch(BadRequest):
    """You tried to schedule too many messages in this chat"""
    ID = "SCHEDULE_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SearchQueryEmpty(BadRequest):
    """The search query is empty"""
    ID = "SEARCH_QUERY_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SecondsInvalid(BadRequest):
    """The seconds interval is invalid"""
    ID = "SECONDS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SendMessageMediaInvalid(BadRequest):
    """The message media is invalid"""
    ID = "SEND_MESSAGE_MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SendMessageTypeInvalid(BadRequest):
    """The message type is invalid"""
    ID = "SEND_MESSAGE_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SessionTooFresh(BadRequest):
    """You can't do this action because the current session was logged-in recently"""
    ID = "SESSION_TOO_FRESH_X"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SettingsInvalid(BadRequest):
    """Invalid settings were provided"""
    ID = "SETTINGS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class Sha256HashInvalid(BadRequest):
    """The provided SHA256 hash is invalid"""
    ID = "SHA256_HASH_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ShortnameOccupyFailed(BadRequest):
    """An error occurred when trying to register the short-name used for the sticker pack. Try a different name"""
    ID = "SHORTNAME_OCCUPY_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SlowmodeMultiMsgsDisabled(BadRequest):
    """Slowmode is enabled, you cannot forward multiple messages to this group"""
    ID = "SLOWMODE_MULTI_MSGS_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SmsCodeCreateFailed(BadRequest):
    """An error occurred while creating the SMS code"""
    ID = "SMS_CODE_CREATE_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SrpIdInvalid(BadRequest):
    """Invalid SRP ID provided"""
    ID = "SRP_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SrpPasswordChanged(BadRequest):
    """The password has changed"""
    ID = "SRP_PASSWORD_CHANGED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StartParamEmpty(BadRequest):
    """The start parameter is empty"""
    ID = "START_PARAM_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StartParamInvalid(BadRequest):
    """The start parameter is invalid"""
    ID = "START_PARAM_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StartParamTooLong(BadRequest):
    """The start parameter is too long"""
    ID = "START_PARAM_TOO_LONG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickersetInvalid(BadRequest):
    """The requested sticker set is invalid"""
    ID = "STICKERSET_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickersetNotModified(BadRequest):
    """The sticker set is not modified"""
    ID = "STICKERSET_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickersEmpty(BadRequest):
    """The sticker provided is empty"""
    ID = "STICKERS_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickersTooMuch(BadRequest):
    """Too many stickers in the set"""
    ID = "STICKERS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerDocumentInvalid(BadRequest):
    """The sticker document is invalid"""
    ID = "STICKER_DOCUMENT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerEmojiInvalid(BadRequest):
    """The sticker emoji is invalid"""
    ID = "STICKER_EMOJI_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerFileInvalid(BadRequest):
    """The sticker file is invalid"""
    ID = "STICKER_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerIdInvalid(BadRequest):
    """The provided sticker id is invalid"""
    ID = "STICKER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerInvalid(BadRequest):
    """The provided sticker is invalid"""
    ID = "STICKER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerPngDimensions(BadRequest):
    """The sticker png dimensions are invalid"""
    ID = "STICKER_PNG_DIMENSIONS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerPngNopng(BadRequest):
    """Stickers must be png files but the provided image was not a png"""
    ID = "STICKER_PNG_NOPNG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerTgsNotgs(BadRequest):
    """A tgs sticker file was expected, but something else was provided"""
    ID = "STICKER_TGS_NOTGS"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerThumbPngNopng(BadRequest):
    """A png sticker thumbnail file was expected, but something else was provided"""
    ID = "STICKER_THUMB_PNG_NOPNG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class StickerVideoNowebm(BadRequest):
    """A webm video file was expected, but something else was provided"""
    ID = "STICKER_VIDEO_NOWEBM"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutInvalid(BadRequest):
    """The takeout id is invalid"""
    ID = "TAKEOUT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutRequired(BadRequest):
    """The method must be invoked inside a takeout session"""
    ID = "TAKEOUT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TempAuthKeyEmpty(BadRequest):
    """The temporary auth key provided is empty"""
    ID = "TEMP_AUTH_KEY_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ThemeFileInvalid(BadRequest):
    """Invalid theme file provided"""
    ID = "THEME_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ThemeFormatInvalid(BadRequest):
    """Invalid theme format provided"""
    ID = "THEME_FORMAT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ThemeInvalid(BadRequest):
    """Invalid theme provided"""
    ID = "THEME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ThemeMimeInvalid(BadRequest):
    """You cannot create this theme because the mime-type is invalid"""
    ID = "THEME_MIME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TmpPasswordDisabled(BadRequest):
    """The temporary password is disabled"""
    ID = "TMP_PASSWORD_DISABLED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TmpPasswordInvalid(BadRequest):
    """The temporary password is invalid"""
    ID = "TMP_PASSWORD_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TokenInvalid(BadRequest):
    """The provided token is invalid"""
    ID = "TOKEN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TtlDaysInvalid(BadRequest):
    """The provided TTL days is invalid"""
    ID = "TTL_DAYS_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TtlMediaInvalid(BadRequest):
    """The media does not support self-destruction"""
    ID = "TTL_MEDIA_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TypesEmpty(BadRequest):
    """The types parameter is empty"""
    ID = "TYPES_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TypeConstructorInvalid(BadRequest):
    """The type constructor is invalid"""
    ID = "TYPE_CONSTRUCTOR_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UntilDateInvalid(BadRequest):
    """That date parameter is invalid"""
    ID = "UNTIL_DATE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UrlInvalid(BadRequest):
    """The URL provided is invalid"""
    ID = "URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsageLimitInvalid(BadRequest):
    """The usage limit is invalid"""
    ID = "USAGE_LIMIT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsernameInvalid(BadRequest):
    """The username is invalid"""
    ID = "USERNAME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsernameNotModified(BadRequest):
    """The username was not modified because you tried to edit it using the same one"""
    ID = "USERNAME_NOT_MODIFIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsernameNotOccupied(BadRequest):
    """The username is not occupied by anyone"""
    ID = "USERNAME_NOT_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsernameOccupied(BadRequest):
    """The username is already in use by someone else"""
    ID = "USERNAME_OCCUPIED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserpicUploadRequired(BadRequest):
    """You are required to upload a profile picture for this action"""
    ID = "USERPIC_UPLOAD_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsersTooFew(BadRequest):
    """Not enough users (to create a chat, for example)"""
    ID = "USERS_TOO_FEW"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UsersTooMuch(BadRequest):
    """The maximum number of users has been exceeded (to create a chat, for example)"""
    ID = "USERS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserAdminInvalid(BadRequest):
    """The action requires admin privileges. Probably you tried to edit admin privileges on someone you don't have rights to"""
    ID = "USER_ADMIN_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserAlreadyParticipant(BadRequest):
    """The user is already a participant of this chat"""
    ID = "USER_ALREADY_PARTICIPANT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserBannedInChannel(BadRequest):
    """You are limited from sending messages in supergroups/channels, check @SpamBot for details"""
    ID = "USER_BANNED_IN_CHANNEL"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserBlocked(BadRequest):
    """The user is blocked"""
    ID = "USER_BLOCKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserBot(BadRequest):
    """Bots in channels can only be administrators, not members."""
    ID = "USER_BOT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserBotInvalid(BadRequest):
    """This method can only be used by a bot"""
    ID = "USER_BOT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserBotRequired(BadRequest):
    """The method can be used by bots only"""
    ID = "USER_BOT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserChannelsTooMuch(BadRequest):
    """The user is already in too many channels or supergroups"""
    ID = "USER_CHANNELS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserCreator(BadRequest):
    """You can't leave this channel because you're its creator"""
    ID = "USER_CREATOR"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserIdInvalid(BadRequest):
    """The user id being used is invalid or not known yet. Make sure you meet the user before interacting with it"""
    ID = "USER_ID_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserInvalid(BadRequest):
    """The provided user is invalid"""
    ID = "USER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserIsBlocked(BadRequest):
    """The user blocked you"""
    ID = "USER_IS_BLOCKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserIsBot(BadRequest):
    """A bot cannot send messages to other bots or to itself"""
    ID = "USER_IS_BOT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserKicked(BadRequest):
    """This user was kicked from this chat"""
    ID = "USER_KICKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserNotMutualContact(BadRequest):
    """The user is not a mutual contact"""
    ID = "USER_NOT_MUTUAL_CONTACT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserNotParticipant(BadRequest):
    """The user is not a member of this chat"""
    ID = "USER_NOT_PARTICIPANT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class VideoContentTypeInvalid(BadRequest):
    """The video content type is invalid (i.e.: not streamable)"""
    ID = "VIDEO_CONTENT_TYPE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class VideoFileInvalid(BadRequest):
    """The video file is invalid"""
    ID = "VIDEO_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class VoiceMessagesForbidden(BadRequest):
    """Voice messages are restricted"""
    ID = "VOICE_MESSAGES_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class VolumeLocNotFound(BadRequest):
    """The volume location can't be found"""
    ID = "VOLUME_LOC_NOT_FOUND"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WallpaperFileInvalid(BadRequest):
    """The provided file cannot be used as a wallpaper"""
    ID = "WALLPAPER_FILE_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WallpaperInvalid(BadRequest):
    """The input wallpaper was not valid"""
    ID = "WALLPAPER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WallpaperMimeInvalid(BadRequest):
    """The wallpaper mime type is invalid"""
    ID = "WALLPAPER_MIME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WcConvertUrlInvalid(BadRequest):
    """WC convert URL invalid"""
    ID = "WC_CONVERT_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebdocumentInvalid(BadRequest):
    """The web document is invalid"""
    ID = "WEBDOCUMENT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebdocumentMimeInvalid(BadRequest):
    """The web document mime type is invalid"""
    ID = "WEBDOCUMENT_MIME_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebdocumentSizeTooBig(BadRequest):
    """The web document is too big"""
    ID = "WEBDOCUMENT_SIZE_TOO_BIG"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebdocumentUrlEmpty(BadRequest):
    """The web document URL is empty"""
    ID = "WEBDOCUMENT_URL_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebdocumentUrlInvalid(BadRequest):
    """The web document URL is invalid"""
    ID = "WEBDOCUMENT_URL_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebpageCurlFailed(BadRequest):
    """Telegram server could not fetch the provided URL"""
    ID = "WEBPAGE_CURL_FAILED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class WebpageMediaEmpty(BadRequest):
    """The URL doesn't contain any valid media"""
    ID = "WEBPAGE_MEDIA_EMPTY"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class YouBlockedUser(BadRequest):
    """You blocked this user"""
    ID = "YOU_BLOCKED_USER"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


