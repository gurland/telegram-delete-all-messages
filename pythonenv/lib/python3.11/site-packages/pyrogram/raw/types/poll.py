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


class Poll(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Poll`.

    Details:
        - Layer: ``158``
        - ID: ``86E18161``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        question (``str``):
            N/A

        answers (List of :obj:`PollAnswer <pyrogram.raw.base.PollAnswer>`):
            N/A

        closed (``bool``, *optional*):
            N/A

        public_voters (``bool``, *optional*):
            N/A

        multiple_choice (``bool``, *optional*):
            N/A

        quiz (``bool``, *optional*):
            N/A

        close_period (``int`` ``32-bit``, *optional*):
            N/A

        close_date (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "question", "answers", "closed", "public_voters", "multiple_choice", "quiz", "close_period", "close_date"]

    ID = 0x86e18161
    QUALNAME = "types.Poll"

    def __init__(self, *, id: int, question: str, answers: List["raw.base.PollAnswer"], closed: Optional[bool] = None, public_voters: Optional[bool] = None, multiple_choice: Optional[bool] = None, quiz: Optional[bool] = None, close_period: Optional[int] = None, close_date: Optional[int] = None) -> None:
        self.id = id  # long
        self.question = question  # string
        self.answers = answers  # Vector<PollAnswer>
        self.closed = closed  # flags.0?true
        self.public_voters = public_voters  # flags.1?true
        self.multiple_choice = multiple_choice  # flags.2?true
        self.quiz = quiz  # flags.3?true
        self.close_period = close_period  # flags.4?int
        self.close_date = close_date  # flags.5?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Poll":
        
        id = Long.read(b)
        
        flags = Int.read(b)
        
        closed = True if flags & (1 << 0) else False
        public_voters = True if flags & (1 << 1) else False
        multiple_choice = True if flags & (1 << 2) else False
        quiz = True if flags & (1 << 3) else False
        question = String.read(b)
        
        answers = TLObject.read(b)
        
        close_period = Int.read(b) if flags & (1 << 4) else None
        close_date = Int.read(b) if flags & (1 << 5) else None
        return Poll(id=id, question=question, answers=answers, closed=closed, public_voters=public_voters, multiple_choice=multiple_choice, quiz=quiz, close_period=close_period, close_date=close_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        flags = 0
        flags |= (1 << 0) if self.closed else 0
        flags |= (1 << 1) if self.public_voters else 0
        flags |= (1 << 2) if self.multiple_choice else 0
        flags |= (1 << 3) if self.quiz else 0
        flags |= (1 << 4) if self.close_period is not None else 0
        flags |= (1 << 5) if self.close_date is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.question))
        
        b.write(Vector(self.answers))
        
        if self.close_period is not None:
            b.write(Int(self.close_period))
        
        if self.close_date is not None:
            b.write(Int(self.close_date))
        
        return b.getvalue()
