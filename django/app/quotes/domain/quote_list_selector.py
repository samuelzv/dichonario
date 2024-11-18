from abc import ABC, abstractmethod
from ..selectors import get_welcome_quote, quote_list_public, quote_list_created_by
from ..models import Quote
from typing import Iterable
from django.conf import settings


class Strategy(ABC):
    """
    Interface common to all strategies.
    """

    @abstractmethod
    def get_quotes(self, **params) -> Iterable[Quote]:
        pass


class CreatedByStrategy(Strategy):
    """
    Get just the quotes created by an specific user.
    """

    def get_quotes(self, **params):
        return quote_list_created_by(
            user=params.get("user"),
            search=params.get("search"),
        )


class PublicStrategy(Strategy):
    """
    Get just the public quotes.
    """

    def get_quotes(self, **params):
        return quote_list_public(params.get("search"))


class WelcomeStrategy(Strategy):
    """
    Get just the welcome public quote
    """

    def get_quotes(self, **params):
        id = settings.CUSTOM_WELCOME_ID
        return get_welcome_quote(id=id)


class QuoteListSelector:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def quotes(self, **params):
        return self._strategy.get_quotes(**params)


quote_list_welcome_selector = QuoteListSelector(WelcomeStrategy())
quote_list_public_selector = QuoteListSelector(PublicStrategy())
quote_list_created_by_selector = QuoteListSelector(CreatedByStrategy())
