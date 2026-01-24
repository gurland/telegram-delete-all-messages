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


class UpdatesCombined(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Updates`.

    Details:
        - Layer: ``158``
        - ID: ``725B04C3``

    Parameters:
        updates (List of :obj:`Update <pyrogram.raw.base.Update>`):
            N/A

        users (List of :obj:`User <pyrogram.raw.base.User>`):
            N/A

        chats (List of :obj:`Chat <pyrogram.raw.base.Chat>`):
            N/A

        date (``int`` ``32-bit``):
            N/A

        seq_start (``int`` ``32-bit``):
            N/A

        seq (``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 87 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetNotifyExceptions
            contacts.DeleteContacts
            contacts.AddContact
            contacts.AcceptContact
            contacts.GetLocated
            contacts.BlockFromReplies
            messages.SendMessage
            messages.SendMedia
            messages.ForwardMessages
            messages.EditChatTitle
            messages.EditChatPhoto
            messages.AddChatUser
            messages.DeleteChatUser
            messages.CreateChat
            messages.ImportChatInvite
            messages.StartBot
            messages.MigrateChat
            messages.SendInlineBotResult
            messages.EditMessage
            messages.GetAllDrafts
            messages.SetGameScore
            messages.SendScreenshotNotification
            messages.SendMultiMedia
            messages.UpdatePinnedMessage
            messages.SendVote
            messages.GetPollResults
            messages.EditChatDefaultBannedRights
            messages.SendScheduledMessages
            messages.DeleteScheduledMessages
            messages.SetHistoryTTL
            messages.SetChatTheme
            messages.HideChatJoinRequest
            messages.HideAllChatJoinRequests
            messages.ToggleNoForwards
            messages.SendReaction
            messages.GetMessagesReactions
            messages.SetChatAvailableReactions
            messages.SendWebViewData
            messages.GetExtendedMedia
            messages.SendBotRequestedPeer
            messages.SetChatWallPaper
            help.GetAppChangelog
            channels.CreateChannel
            channels.EditAdmin
            channels.EditTitle
            channels.EditPhoto
            channels.JoinChannel
            channels.LeaveChannel
            channels.InviteToChannel
            channels.DeleteChannel
            channels.ToggleSignatures
            channels.EditBanned
            channels.DeleteHistory
            channels.TogglePreHistoryHidden
            channels.EditCreator
            channels.ToggleSlowMode
            channels.ConvertToGigagroup
            channels.ToggleJoinToSend
            channels.ToggleJoinRequest
            channels.ToggleForum
            channels.CreateForumTopic
            channels.EditForumTopic
            channels.UpdatePinnedForumTopic
            channels.ReorderPinnedForumTopics
            channels.ToggleAntiSpam
            channels.ToggleParticipantsHidden
            payments.AssignAppStoreTransaction
            payments.AssignPlayMarketTransaction
            phone.DiscardCall
            phone.SetCallRating
            phone.CreateGroupCall
            phone.JoinGroupCall
            phone.LeaveGroupCall
            phone.InviteToGroupCall
            phone.DiscardGroupCall
            phone.ToggleGroupCallSettings
            phone.ToggleGroupCallRecord
            phone.EditGroupCallParticipant
            phone.EditGroupCallTitle
            phone.ToggleGroupCallStartSubscription
            phone.StartScheduledGroupCall
            phone.JoinGroupCallPresentation
            phone.LeaveGroupCallPresentation
            folders.EditPeerFolders
            chatlists.JoinChatlistInvite
            chatlists.JoinChatlistUpdates
            chatlists.LeaveChatlist
    """

    __slots__: List[str] = ["updates", "users", "chats", "date", "seq_start", "seq"]

    ID = 0x725b04c3
    QUALNAME = "types.UpdatesCombined"

    def __init__(self, *, updates: List["raw.base.Update"], users: List["raw.base.User"], chats: List["raw.base.Chat"], date: int, seq_start: int, seq: int) -> None:
        self.updates = updates  # Vector<Update>
        self.users = users  # Vector<User>
        self.chats = chats  # Vector<Chat>
        self.date = date  # int
        self.seq_start = seq_start  # int
        self.seq = seq  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatesCombined":
        # No flags
        
        updates = TLObject.read(b)
        
        users = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        date = Int.read(b)
        
        seq_start = Int.read(b)
        
        seq = Int.read(b)
        
        return UpdatesCombined(updates=updates, users=users, chats=chats, date=date, seq_start=seq_start, seq=seq)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.updates))
        
        b.write(Vector(self.users))
        
        b.write(Vector(self.chats))
        
        b.write(Int(self.date))
        
        b.write(Int(self.seq_start))
        
        b.write(Int(self.seq))
        
        return b.getvalue()
