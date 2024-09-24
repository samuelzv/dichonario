from __future__ import annotations
from typing import TypedDict, NotRequired


class CardModel(TypedDict):
    id: str
    header_text: NotRequired[str]
    main_text: str
