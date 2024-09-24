from __future__ import annotations
from typing import TypedDict, NotRequired


class Link(TypedDict):
    id: str
    text: str
    url: str
    class_name: NotRequired[str]
