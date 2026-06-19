import re

class QueryBuilder:
    def __init__(self):
        self._columns = []
        self._table = None
        self._where_condition = None
        self._where_params = []
        self._order_by = []
        self._limit = None

    def select(self, *columns):
        # TODO: Implementierung
        pass

    def from_(self, table):
        # TODO: Implementierung
        pass

    def where(self, condition, *params):
        # TODO: Implementierung
        pass

    def order_by(self, *columns):
        # TODO: Implementierung
        pass

    def limit(self, n):
        # TODO: Implementierung
        pass

    def build(self):
        # TODO: Implementierung
        pass

    def __str__(self):
        # TODO: Implementierung
        pass