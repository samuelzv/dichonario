# In a file called [project root]/components/calendar/calendar.py
from __future__ import annotations
from django_components import component
from .model import CardModel


@component.register("card")
class Card(component.Component):
    template_name = "template.html"

    def get_context_data(self, attrs={}):
        return {
            "attrs": attrs,
        }

    class Media:
        css = "style.css"
        js = "script.js"
