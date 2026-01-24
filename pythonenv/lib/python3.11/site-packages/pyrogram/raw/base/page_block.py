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

PageBlock = Union[raw.types.PageBlockAnchor, raw.types.PageBlockAudio, raw.types.PageBlockAuthorDate, raw.types.PageBlockBlockquote, raw.types.PageBlockChannel, raw.types.PageBlockCollage, raw.types.PageBlockCover, raw.types.PageBlockDetails, raw.types.PageBlockDivider, raw.types.PageBlockEmbed, raw.types.PageBlockEmbedPost, raw.types.PageBlockFooter, raw.types.PageBlockHeader, raw.types.PageBlockKicker, raw.types.PageBlockList, raw.types.PageBlockMap, raw.types.PageBlockOrderedList, raw.types.PageBlockParagraph, raw.types.PageBlockPhoto, raw.types.PageBlockPreformatted, raw.types.PageBlockPullquote, raw.types.PageBlockRelatedArticles, raw.types.PageBlockSlideshow, raw.types.PageBlockSubheader, raw.types.PageBlockSubtitle, raw.types.PageBlockTable, raw.types.PageBlockTitle, raw.types.PageBlockUnsupported, raw.types.PageBlockVideo]


# noinspection PyRedeclaration
class PageBlock:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 29 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            PageBlockAnchor
            PageBlockAudio
            PageBlockAuthorDate
            PageBlockBlockquote
            PageBlockChannel
            PageBlockCollage
            PageBlockCover
            PageBlockDetails
            PageBlockDivider
            PageBlockEmbed
            PageBlockEmbedPost
            PageBlockFooter
            PageBlockHeader
            PageBlockKicker
            PageBlockList
            PageBlockMap
            PageBlockOrderedList
            PageBlockParagraph
            PageBlockPhoto
            PageBlockPreformatted
            PageBlockPullquote
            PageBlockRelatedArticles
            PageBlockSlideshow
            PageBlockSubheader
            PageBlockSubtitle
            PageBlockTable
            PageBlockTitle
            PageBlockUnsupported
            PageBlockVideo
    """

    QUALNAME = "pyrogram.raw.base.PageBlock"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/page-block")
