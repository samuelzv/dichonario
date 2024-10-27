from abc import ABC, abstractmethod
from typing import Union
from .quote_list_selector import (
    quote_list_created_by_selector,
    quote_list_public_selector,
    quote_list_welcome_selector,
    QuoteListSelector,
)


class QuoteListBaseFactory(ABC):
    """
    Interface common to all creators.
    """

    @abstractmethod
    def create(self, type: str) -> Union[QuoteListSelector, None]:
        pass


class QuoteListFactory(QuoteListBaseFactory):
    """
    Based on the query type gets the proper quotes query selector
    """

    def create(self, type: str) -> Union[QuoteListSelector, None]:
        if type == "mine":
            return quote_list_created_by_selector

        if type == "public":
            return quote_list_public_selector

        if type == "welcome":
            return quote_list_welcome_selector

        return None

