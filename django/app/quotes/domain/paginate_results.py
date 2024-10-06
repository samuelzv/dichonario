from django.core.paginator import Paginator, EmptyPage

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