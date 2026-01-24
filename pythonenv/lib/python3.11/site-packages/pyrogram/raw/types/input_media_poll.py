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


class InputMediaPoll(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``158``
        - ID: ``F94E5F1``

    Parameters:
        poll (:obj:`Poll <pyrogram.raw.base.Poll>`):
            N/A

        correct_answers (List of ``bytes``, *optional*):
            N/A

        solution (``str``, *optional*):
            N/A

        solution_entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["poll", "correct_answers", "solution", "solution_entities"]

    ID = 0xf94e5f1
    QUALNAME = "types.InputMediaPoll"

    def __init__(self, *, poll: "raw.base.Poll", correct_answers: Optional[List[bytes]] = None, solution: Optional[str] = None, solution_entities: Optional[List["raw.base.MessageEntity"]] = None) -> None:
        self.poll = poll  # Poll
        self.correct_answers = correct_answers  # flags.0?Vector<bytes>
        self.solution = solution  # flags.1?string
        self.solution_entities = solution_entities  # flags.1?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPoll":
        
        flags = Int.read(b)
        
        poll = TLObject.read(b)
        
        correct_answers = TLObject.read(b, Bytes) if flags & (1 << 0) else []
        
        solution = String.read(b) if flags & (1 << 1) else None
        solution_entities = TLObject.read(b) if flags & (1 << 1) else []
        
        return InputMediaPoll(poll=poll, correct_answers=correct_answers, solution=solution, solution_entities=solution_entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.correct_answers else 0
        flags |= (1 << 1) if self.solution is not None else 0
        flags |= (1 << 1) if self.solution_entities else 0
        b.write(Int(flags))
        
        b.write(self.poll.write())
        
        if self.correct_answers is not None:
            b.write(Vector(self.correct_answers, Bytes))
        
        if self.solution is not None:
            b.write(String(self.solution))
        
        if self.solution_entities is not None:
            b.write(Vector(self.solution_entities))
        
        return b.getvalue()
