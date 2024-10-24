from django import template
from django.core.paginator import Page

from ..domain.paginate_results import PaginatedResults

# from pattern_library.monkey_utils import override_tag

register = template.Library()


@register.simple_tag
def get_previous_page_link(
    base_url: str, paginated_results: PaginatedResults, search: str
) -> str:
    link = "#"

    if paginated_results.has_previous:
        link = (
            base_url
            + "?page="
            + str(paginated_results.previous_page)
            + "&search="
            + search
        )

    return link


@register.simple_tag
def get_next_page_link(
    base_url: str, paginated_results: PaginatedResults, search: str
) -> str:
    link = "#"

    if paginated_results.has_next:
        link = (
            base_url + "?page=" + str(paginated_results.next_page) + "&search=" + search
        )

    return link


# override_tag(register, "get_previous_page_link", "")
# override_tag(register, "get_next_page_link", "")
