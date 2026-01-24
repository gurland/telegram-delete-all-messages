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


class Forbidden(RPCError):
    """Forbidden"""
    CODE = 403
    """``int``: RPC Error Code"""
    NAME = __doc__


class BroadcastForbidden(Forbidden):
    """The request can't be used in channels"""
    ID = "BROADCAST_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChannelPublicGroupNa(Forbidden):
    """The channel/supergroup is not available"""
    ID = "CHANNEL_PUBLIC_GROUP_NA"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatAdminInviteRequired(Forbidden):
    """You don't have rights to invite other users"""
    ID = "CHAT_ADMIN_INVITE_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatAdminRequired(Forbidden):
    """The method requires chat admin privileges"""
    ID = "CHAT_ADMIN_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatForbidden(Forbidden):
    """You cannot write in this chat"""
    ID = "CHAT_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendGifsForbidden(Forbidden):
    """You can't send animations in this chat"""
    ID = "CHAT_SEND_GIFS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendInlineForbidden(Forbidden):
    """You cannot use inline bots to send messages in this chat"""
    ID = "CHAT_SEND_INLINE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendMediaForbidden(Forbidden):
    """You can't send media messages in this chat"""
    ID = "CHAT_SEND_MEDIA_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendPollForbidden(Forbidden):
    """You can't send polls in this chat"""
    ID = "CHAT_SEND_POLL_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatSendStickersForbidden(Forbidden):
    """You can't send stickers in this chat"""
    ID = "CHAT_SEND_STICKERS_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class ChatWriteForbidden(Forbidden):
    """You don't have rights to send messages in this chat"""
    ID = "CHAT_WRITE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class EditBotInviteForbidden(Forbidden):
    """Bots' chat invite links can't be edited"""
    ID = "EDIT_BOT_INVITE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class InlineBotRequired(Forbidden):
    """The action must be performed through an inline bot callback"""
    ID = "INLINE_BOT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageAuthorRequired(Forbidden):
    """You are not the author of this message"""
    ID = "MESSAGE_AUTHOR_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class MessageDeleteForbidden(Forbidden):
    """You don't have rights to delete messages in this chat, most likely because you are not the author of them"""
    ID = "MESSAGE_DELETE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PollVoteRequired(Forbidden):
    """Cast a vote in the poll before calling this method"""
    ID = "POLL_VOTE_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class PremiumAccountRequired(Forbidden):
    """This action requires a premium account"""
    ID = "PREMIUM_ACCOUNT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class RightForbidden(Forbidden):
    """You don't have enough rights for this action, or you tried to set one or more admin rights that can't be applied to this kind of chat (channel or supergroup)"""
    ID = "RIGHT_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class SensitiveChangeForbidden(Forbidden):
    """Your sensitive content settings can't be changed at this time"""
    ID = "SENSITIVE_CHANGE_FORBIDDEN"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class TakeoutRequired(Forbidden):
    """The method must be invoked inside a takeout session"""
    ID = "TAKEOUT_REQUIRED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserBotInvalid(Forbidden):
    """This method can only be called by a bot"""
    ID = "USER_BOT_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserChannelsTooMuch(Forbidden):
    """One of the users you tried to add is already in too many channels/supergroups"""
    ID = "USER_CHANNELS_TOO_MUCH"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserInvalid(Forbidden):
    """The provided user is invalid"""
    ID = "USER_INVALID"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserIsBlocked(Forbidden):
    """The user is blocked"""
    ID = "USER_IS_BLOCKED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserNotMutualContact(Forbidden):
    """The provided user is not a mutual contact"""
    ID = "USER_NOT_MUTUAL_CONTACT"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserPrivacyRestricted(Forbidden):
    """The user's privacy settings is preventing you to perform this action"""
    ID = "USER_PRIVACY_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


class UserRestricted(Forbidden):
    """You are limited/restricted. You can't perform this action"""
    ID = "USER_RESTRICTED"
    """``str``: RPC Error ID"""
    MESSAGE = __doc__


