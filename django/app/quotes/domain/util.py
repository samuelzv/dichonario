from collections.abc import Iterable
from typing import Any, Mapping
from django.urls import reverse
from django.db.models import QuerySet
from django.core.paginator import EmptyPage, Paginator
from .constants import command_buttons
from django.utils.translation import gettext
import copy


def setUrlButton(button):
    button["url"] = reverse(button["url"]) + "?action=" + button["id"]
    return button


def get_command_buttons():
    return list(map(setUrlButton, copy.deepcopy(command_buttons)))


def is_authorizer(user):
    return user.groups.filter(name="authorizer").exists()


def paginate_list(
    *,
    items_per_page: int,
    list_items,
    page_number: int,
    paginator_url: str,
    search: str,
    attrs={},
) -> Mapping[str, Any] | None:
    paginator = Paginator(list_items, items_per_page)

    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page_number = 1
        page = paginator.get_page(page_number)

    list_items = list(page.object_list)

    # some times list items is an array of arrays, dont' know why yet
    try:
        if len(list_items):
            iterator = iter(list_items[0])
            list_items = list_items[0]
    except:
        print("Not iterable")

    return {
        "list_items": list_items,
        "total_count": paginator.count,
        "current_page": page_number,
        "num_pages": paginator.num_pages,
        "search": search,
        "paginator_url": paginator_url,
        "has_next": page.has_next(),
        "has_previous": page.has_previous(),
        "attrs": attrs,
    }


def set_session_action(request):
    action = ""
    if request.GET.get("action", "") == "":
        if request.session.get("action", "") == "":
            action = "mine"
        else:
            action = request.session.get("action", "")
    else:
        action = request.GET.get("action", "")

    request.session["action"] = action
    request.session["search"] = request.GET.get("search", "")
    request.session["page"] = request.GET.get("page", 1)
