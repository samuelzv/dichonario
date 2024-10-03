from abc import ABC, abstractmethod
from .quote_list_selector import quote_list_created_by_selector, quote_list_public_selector, QuoteListSelector 


class QuoteListBaseFactory(ABC):
    """
    Interface common to all creators.
    """
    @abstractmethod
    def create(self, type: str) -> QuoteListSelector:
        pass

class QuoteListFactory(QuoteListBaseFactory):
    """
    Get just the quotes created by an specific user.
    """
    def create(self, type: str) -> QuoteListSelector:
        if type == "mine":
            return quote_list_created_by_selector
        else:
            return quote_list_public_selector