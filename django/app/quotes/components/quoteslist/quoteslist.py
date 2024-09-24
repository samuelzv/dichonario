# In a file called [project root]/components/calendar/calendar.py
from django.core.paginator import EmptyPage, Paginator
from django.db.models import QuerySet
from django_components import component
from typing import List

from components.card.model import CardModel


@component.register("quoteslist")
class Datalist(component.Component):
    template_name = "template.html"
    ITEMS_PER_PAGE = 4

    def get_context_data(
        self,
        name: str,
        list: QuerySet,
        page_number: int,
        paginator_url: str,
        search: str,
        attrs={},
    ):
        paginator = Paginator(list, self.ITEMS_PER_PAGE)

        try:
            page = paginator.page(page_number)
        except EmptyPage:
            page_number = 1
            page = paginator.page(page_number)

        return {
            "name": name,
            "page": page,
            "total_count": paginator.count,
            "current_page": page_number,
            "num_pages": paginator.num_pages,
            "search": search,
            "paginator_url": paginator_url,
            "attrs": attrs,
        }

    # Both `css` and `js` can be relative to dir where `calendar.py` is, or relative to STATICFILES_DIRS
    class Media:
        css = "style.css"
        js = "script.js"
