from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Favorite, Quote, Author, Language
from .domain import embedding


def quote_create(
    *,
    quote: str,
    author: Author,
    is_private: bool,
    created_by: User,
    language: Language
) -> Quote:
    new_quote = Quote.objects.create(
        quote=quote,
        author=author,
        language=language,
        is_private=is_private,
        embedding=embedding.get_embeddeing(quote),
        created_by=created_by,
    )

    return new_quote


def quote_update(*, id: int, quote: str, author: Author, is_private: bool) -> Quote:
    found_quote = Quote.objects.get(id=id)

    if found_quote is None:
        raise ValidationError("Invalid quote id")

    found_quote.quote = quote
    found_quote.author = author
    found_quote.is_private = is_private

    found_quote.save()

    return found_quote


def author_create(*, name: str, created_by: User) -> Author:
    author = Author.objects.create(name=name, created_by=created_by)

    return author


def favorite_create(*, quote: Quote, created_by: User) -> Favorite:
    favorite = Favorite.objects.create(quote=quote, created_by=created_by)

    return favorite
