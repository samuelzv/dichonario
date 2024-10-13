from django import template
from django.urls import reverse
from django.utils.translation import gettext, gettext_lazy
from components.button.model import ButtonModel, ButtonType
import ast

# from quotes.domain.quote_session import QuoteSession
# from components.buttongroup.model import Button
from components.card.model import CardModel

register = template.Library()


@register.filter
def get_url_from_button(button):
    return reverse(button["url"]) + "?action=" + button["id"]

@register.simple_tag
def create_dict(str_dict):
    return ast.literal_eval(str_dict)

@register.simple_tag
def get_type_writer_dic(text: str, index: int) -> dict:

    return {
        "text": f'"{text}"',
        "filename": 'components-js/main-type-writer-' + str(index),
        "index": index,

    } 

@register.simple_tag
def map_quote_to_card(quote) -> CardModel:
    return {
        "id": quote.id,
        "header_text": "",
        "main_text": quote.quote,
    }


@register.simple_tag
def get_app_name() -> str:
    return "Dichonario"


@register.simple_tag
def get_button_config(
    type: ButtonType,
    title: str,
    tooltip: str,
    color: str,
    is_submit: bool,
    util_classes: str,
) -> ButtonModel:
    return {
        "type": type,
        "title": gettext_lazy(title),
        "tooltip": gettext_lazy(tooltip),
        "color": color,
        "is_submit": is_submit or False,
        "util_classes": util_classes,
    }

@register.simple_tag(takes_context=True)
def get_theme(context):
    theme = context['request'].COOKIES.get("theme", "dark")

    return {
        "theme": theme 
    } 

@register.simple_tag(takes_context=True)
def get_language(context):
    return {
        'is_english': context['request'].LANGUAGE_CODE == 'en',
        'is_spanish': context['request'].LANGUAGE_CODE == 'es',
        'i18n': {
            'english_code': 'en' ,
            'english_label': gettext_lazy('English'),
            'english_description': gettext_lazy('Switch to English'),
            'spanish_code': 'es',
            'spanish_label': gettext_lazy('Spanish'),
            'spanish_description': gettext_lazy('Switch to Spanish'),
        }
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
