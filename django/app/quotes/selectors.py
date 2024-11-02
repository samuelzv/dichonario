from typing import Iterable
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Quote, Author, Language
from django.db.models import Count


def quote_list_created_by(*, user: User, search: str) -> Iterable[Quote]:
    filter_dict = {"created_by": user}

    if search:
        filter_dict |= {"quote__icontains": search}

    results = list(Quote.objects.filter(**filter_dict).order_by("-created_at"))
    print("Results:", results)
    print("Length:", len(results))

    return results


def quote_list_public(search: str) -> Iterable[Quote]:
    filter_dict = {"is_private": False}

    if search:
        filter_dict |= {"quote__icontains": search}

    results = list(Quote.objects.filter(**filter_dict).order_by("-created_at"))
    print("Results:", results)
    print("Length:", len(results))

    return results


def author_by_id(*, id: int) -> Author:
    found = Author.objects.get(id=id)

    if found is None:
        raise ValidationError("Invalid author id")

    return found


def quote_by_id(*, id: int) -> Quote:
    found = Quote.objects.get(id=id)

    if found is None:
        raise ValidationError("Invalid quote id")

    return found


def quote_delete_by_id(*, id: int) -> Quote:
    found = Quote.objects.get(id=id)

    if found is None:
        raise ValidationError("Invalid quote id")
    else:
        found.delete()

    return found


def get_author_list() -> Iterable[Author]:
    return Author.objects.all().order_by("name")


def get_author_list_count_quotes() -> Iterable[Author]:
    authors = (
        Author.objects.annotate(num_quotes=Count("quotes"))
        .filter(num_quotes__gt=0)
        .order_by("name")
    )

    return authors


def language_by_code(*, code: str) -> Language:
    found = Language.objects.get(code=code)

    if found is None:
        raise ValidationError("Invalid language code")

    return found


def get_welcome_quote(*, id: int) -> Iterable[Quote]:
    return [quote_by_id(id=id)]
