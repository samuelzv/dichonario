# In a file called [project root]/components/calendar/calendar.py
from __future__ import annotations
from django_components import component
from components.buttongroup.model import Link
from typing import List


class LinkButton(Link):
    is_selected: bool
    is_first: bool
    is_last: bool


@component.register("buttongroup")
class Datalist(component.Component):
    template_name = "template.html"

    def get_context_data(self, name: str, buttons: list[Link], selected: str, attrs={}):

        return {
            "name": name,
            "buttons": self.set_buttons(buttons, selected),
            "selected": selected,
            "attrs": attrs,
        }

    def set_buttons(self, buttons: list[Link], selected_id: str) -> list[LinkButton]:
        results: List[LinkButton] = []
        buttons_len = len(buttons)

        for i, v in enumerate(buttons):
            linkButton: LinkButton = {
                "id": v["id"],
                "text": v["text"],
                "url": v["url"],
                "is_selected": v["id"] == selected_id,
                "is_first": i == 0,
                "is_last": i == buttons_len - 1,
                "class_name": v["class_name"] or "",
            }
            if linkButton["is_first"]:
                linkButton["class_name"] = "first-button" + linkButton["class_name"]

            if linkButton["is_last"]:
                linkButton["class_name"] = "last-button " + linkButton["class_name"]

            if linkButton["is_selected"]:
                linkButton["class_name"] = "selected " + linkButton["class_name"]
            else:
                linkButton["class_name"] = " " + linkButton["class_name"]

            results.append(linkButton)

        return results

    def set_button(self, button: Link) -> Link:
        return button

    class Media:
        css = "style.css"
        js = "script.js"
