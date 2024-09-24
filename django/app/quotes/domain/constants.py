from typing import Literal
from django.utils.translation import gettext_lazy
from django.urls import reverse

QuoteScope = Literal["mine", "public"]

# reverse(button["url"]) + "?action=" + button["id"]

command_buttons = [
    {
        "id": "mine",
        "text": gettext_lazy("Mine"),
        "url": "quote-list",
        "selected": False,
        "class_name": "",
    },
    {
        "id": "public",
        "text": gettext_lazy("Public"),
        "url": "quote-list",
        "selected": False,
        "class_name": "",
    },
    {
        "id": "authors",
        "text": gettext_lazy("Authors"),
        "url": "author-list",
        "selected": False,
        "class_name": "",
    },
]

# for button in command_buttons:
#    button["url"] = reverse(button["url"]) + "?action=" + button["id"]
