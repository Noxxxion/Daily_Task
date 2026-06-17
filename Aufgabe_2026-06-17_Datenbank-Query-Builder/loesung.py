import re
from typing import List, Optional

class QueryBuilder:
    def __init__(self):
        self._table: Optional[str] = None
        self._columns: List[str] = []
        self._where_conditions: List[str] = []
        self._order_by_column: Optional[str] = None
        self._order_by_direction: str = 'asc'
        self._limit: Optional[int] = None

    def select(self, columns: List[str]) -> 'QueryBuilder':
        # TODO: Implementierung
        pass

    def from_table(self, table: str) -> 'QueryBuilder':
        # TODO: Implementierung
        pass

    def where(self, condition: str) -> 'QueryBuilder':
        # TODO: Implementierung
        pass

    def order_by(self, column: str, direction: str = 'asc') -> 'QueryBuilder':
        # TODO: Implementierung
        pass

    def limit(self, count: int) -> 'QueryBuilder':
        # TODO: Implementierung
        pass

    def build(self) -> str:
        # TODO: Implementierung
        pass