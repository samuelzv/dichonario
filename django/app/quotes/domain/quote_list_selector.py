from abc import ABC, abstractmethod
from ..selectors import quote_list_public, quote_list_created_by


class Strategy(ABC):
    """
    Interface common to all strategies.
    """
    @abstractmethod
    def get_quotes(self, **params):
        pass 

class CreatedByStrategy(Strategy):
    """
    Get just the quotes created by an specific user.
    """
    def get_quotes(self, **params):
        return quote_list_created_by(user=params.get('user'), search=params.get('search')) 

class PublicStrategy(Strategy):
    """
    Get just the public quotes.
    """
    def get_quotes(self, **params):
        return quote_list_public(params.get('search')) 


class QuoteListSelector():
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def quotes(self, **params):
        return self._strategy.get_quotes(**params)

quote_list_public_selector = QuoteListSelector(PublicStrategy())
quote_list_created_by_selector = QuoteListSelector(CreatedByStrategy())

