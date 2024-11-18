from typing import Iterable, Union
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Favorite, Quote, Author, Language
from django.db.models import Count
from .domain.embedding import get_embedding
from pgvector.django import L2Distance


def get_favorite_quote_from_user(*, quote: Quote, created_by: User):
    favorite = None
    try:
        favorite = Favorite.objects.get(
            quote=quote,
            created_by=created_by,
        )
    except Favorite.DoesNotExist:
        print("Favorite does not exist")

    return favorite


def quote_list_created_by(*, user: User, search: str) -> Iterable[Quote]:
    filter_dict = {"created_by": user}
    results = []

    if search:
        embedding = get_embedding(search)
        results = (
            Quote.objects.annotate(
                distance=L2Distance("embedding", embedding),
            )
            .filter(distance__lt=0.7)
            .filter(**filter_dict)
            .order_by("distance")
        )
    else:
        results = Quote.objects.filter(**filter_dict).order_by("-created_at")

    return list(results)


def quote_list_public(search: str) -> Iterable[Quote]:
    filter_dict = {"is_private": False}
    results = []

    if search:
        embedding = get_embedding(search)
        results = (
            Quote.objects.annotate(
                distance=L2Distance("embedding", embedding),
            )
            .filter(distance__lt=0.7)
            .filter(**filter_dict)
            .order_by("distance")
        )
    else:
        results = Quote.objects.filter(**filter_dict).order_by("-created_at")

    return list(results)


def author_by_id(*, id: int) -> Author:
    found = Author.objects.get(id=id)

    if found is None:
        raise ValidationError("Invalid author id")

    return found


def quote_by_id(*, id: int) -> Union[Quote, None]:
    quote = None

    try:
        quote = Quote.objects.get(id=id)
    except Quote.DoesNotExist:
        print("Quote does not exist")

    return quote


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
