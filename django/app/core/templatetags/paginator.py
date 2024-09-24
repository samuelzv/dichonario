from django import template
from django.core.paginator import Page

from pattern_library.monkey_utils import override_tag

register = template.Library()


@register.simple_tag
def get_previous_page_link(base_url: str, page: Page, search: str) -> str:
    link = "#"

    if page.has_previous():
        link = (
            base_url + "?page=" + str(page.previous_page_number()) + "&search=" + search
        )

    return link


@register.simple_tag
def get_next_page_link(base_url: str, page: Page, search: str) -> str:
    link = "#"

    if page.has_next():
        link = base_url + "?page=" + str(page.next_page_number()) + "&search=" + search

    return link


override_tag(register, "get_previous_page_link", "")
override_tag(register, "get_next_page_link", "")
