from django_components import component
from components.button.model import ButtonModel, ButtonType
from typing import get_origin


@component.register("button")
class Button(component.Component):
    template_name = "template.html"

    def get_context_data(self, model: ButtonModel):
        if not model.get("type"):
            model["type"] = "default"

        if get_origin(model["type"] is not ButtonType):
            raise TypeError("Invalid button type")

        print(model)

        return {
            "model": model,
        }

    class Media:
        css = "style.css"
        js = "script.js"
