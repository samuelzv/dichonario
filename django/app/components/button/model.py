from typing import TypedDict, Literal, Optional

# from typing_extensions import NotRequired
ButtonType = Literal["default", "outline"]


class ButtonModel(TypedDict):
    type: Optional[ButtonType]
    title: str
    color: str
    tooltip: Optional[str]
    is_submit: Optional[bool]
    util_classes: Optional[str]
