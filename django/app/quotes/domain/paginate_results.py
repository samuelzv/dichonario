from django.core.paginator import Paginator, EmptyPage
from dataclasses import dataclass
from typing import Any, Union

from collections.abc import Iterable


def paginate_results(queryset, current_page, page_size):
    paginator = Paginator(queryset, page_size)

    try:
        page_number = current_page
    except ValueError:
        page_number = 1

    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page_number = 1
        page = paginator.page(page_number)

    items = list(page.object_list)
    pagination = {
        "current_page": page_number,
        "has_next": page.has_next(),
        "has_previous": page.has_previous(),
        "num_pages": paginator.num_pages,
        "total_records": paginator.count,
        "previous_page": page.previous_page_number() if page.has_previous() else None,
        "next_page": page.next_page_number() if page.has_next() else None,
    }

    return (items, pagination)


@dataclass()
class PaginatedResults:
    list_items: Any
    current_page: int
    has_next: bool
    has_previous: bool
    num_pages: int
    total_records: int
    previous_page: Union[int, None]
    next_page: Union[int, None]


@dataclass()
class Paginated:
    queryset: Any
    current_page: int
    page_size: int

    def paginate(self) -> PaginatedResults:
        paginator = Paginator(self.queryset, self.page_size)

        try:
            page_number = self.current_page
            page = paginator.page(page_number)
        except EmptyPage:
            page_number = 1
            page = paginator.page(page_number)

        self.paginated_results = PaginatedResults(
            list_items=page.object_list,
            current_page=page_number,
            has_next=page.has_next(),
            has_previous=page.has_previous(),
            num_pages=paginator.num_pages,
            total_records=paginator.count,
            previous_page=page.previous_page_number() if page.has_previous() else None,
            next_page=page.next_page_number() if page.has_next() else None,
        )

        return self.paginated_results
