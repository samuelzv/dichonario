# In a file called [project root]/components/calendar/calendar.py
from django_components import component


@component.register("datalist")
class Datalist(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir
    # will be automatically found. To customize which template to use based on context
    # you can override method `get_template_name` instead of specifying `template_name`.
    #
    # `template_name` can be relative to dir where `calendar.py` is, or relative to STATICFILES_DIRS
    template_name = "template.html"

    # This component takes one parameter, a date string to show in the template
    def get_context_data(
        self,
        name: str,
        data: list,
        initial_value: None,
        external_class: str = "",
        attrs={},
    ):
        return {
            "name": name,
            "data": data,
            "initial_value": initial_value,
            "external_class": external_class,
            "attrs": attrs,
        }

    # Both `css` and `js` can be relative to dir where `calendar.py` is, or relative to STATICFILES_DIRS
    class Media:
        css = "style.css"
        js = "script.js"
