from enum import Enum
from typing import get_origin
from .constants import QuoteScope


class QuoteSession:
    def __init__(self, request):
        if self.validate(request.session):
            self._scope: QuoteScope = "mine"
            self.session = request.session

            self.scope = self.session.get("quote_scope", "")

    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, scope: QuoteScope):
        self._scope = scope
        self.save()

    def validate(self, session) -> bool:
        if get_origin(session.get("quote_scope") is not QuoteScope):
            raise TypeError("scope is not a QuoteScope type")

        return True

    def save(self):
        self.session["quote_scope"] = self.scope
