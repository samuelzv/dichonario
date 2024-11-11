from django import template
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext, gettext_lazy
from quotes.models import Quote
from django.core.exceptions import ObjectDoesNotExist
import ast

register = template.Library()


@register.filter
def get_url_from_button(button):
    return reverse(button["url"]) + "?action=" + button["id"]


@register.simple_tag
def create_dict(str_dict):
    return ast.literal_eval(str_dict)


@register.simple_tag(takes_context=True)
def get_is_favorite(context, quote: Quote) -> bool:
    try:
        if context["request"].user.is_authenticated:
            print("quote is: ", quote.quote)
            print("quote id: ", quote.id)
            print("user is: ", context["request"].user.id)
            if quote.favorites.get(id=context["request"].user.id):
                return True
    except ObjectDoesNotExist as e:
        print("Object does not exist")
        print(e)

    return False


@register.simple_tag
def get_text_by_section(section: str) -> str:
    if section == "mine":
        return gettext("Mine")

    if section == "public":
        return gettext("Public")

    if section == "authors":
        return gettext("Authors")

    return ""


@register.simple_tag
def get_type_writer_dic(text: str, index: int) -> dict:

    return {
        "text": f'"{text}"',
        "filename": "components-js/main-type-writer-" + str(index),
        "index": index,
    }


@register.simple_tag
def get_app_name() -> str:
    return "Dichonario"


@register.simple_tag(takes_context=True)
def get_theme(context):
    theme = context["request"].COOKIES.get("theme", "dark")

    return {"theme": theme}


@register.simple_tag(takes_context=True)
def get_language(context):
    return {
        "is_english": context["request"].LANGUAGE_CODE == "en",
        "is_spanish": context["request"].LANGUAGE_CODE == "es",
        "i18n": {
            "english_code": "en",
            "english_label": gettext_lazy("English"),
            "english_description": gettext_lazy("Switch to English"),
            "spanish_code": "es",
            "spanish_label": gettext_lazy("Spanish"),
            "spanish_description": gettext_lazy("Switch to Spanish"),
        },
    }


@register.simple_tag(takes_context=True)
def get_quote_groups(context):
    request = context["request"]
    # quote_session = QuoteSession(request)

    buttons = [
        {
            "id": "mine",
            "text": gettext("Mine"),
            "url": "quote-list",
            "selected": False,  # quote_session.scope == "mine",
            "class_name": "",
        },
        {
            "id": "public",
            "text": gettext("Public"),
            "url": "quote-list",
            "selected": False,  # quote_session.scope == "public",
            "class_name": "",
        },
        {
            "id": "new",
            "text": gettext("New"),
            "url": "quote-new",
            "selected": False,
            "class_name": "",
        },
    ]
    return buttons


@register.simple_tag(takes_context=True)
def get_current_url(context) -> str:
    request = context["request"]
    params = request.GET.dict()

    query_string = request.path + "?"
    for key in params:
        query_string += str(key) + "=" + str(params[key]) + "&"

    return query_string
