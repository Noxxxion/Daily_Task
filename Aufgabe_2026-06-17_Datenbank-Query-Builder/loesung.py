import re
from typing import List, Optional


class QueryBuilder:
    def __init__(self):
        self._table: Optional[str] = None
        self._columns: List[str] = []
        self._where_conditions: List[str] = []
        self._order_by_column: Optional[str] = None
        self._order_by_direction: str = "asc"
        self._limit: Optional[int] = None

    _available_columns = {"id", "name", "age", "email", "department", "salary"}
    _available_tables = {"users"}

    def select(self, columns: List[str]) -> "QueryBuilder":
        # Validierung der ausgewählten Spalten
        for column in columns:
            if column not in self._available_columns:
                raise ValueError(f"Column '{column}' is not available")

        self._columns = columns
        return self

    def from_table(self, table: str) -> "QueryBuilder":
        # Validierung der Tabelle
        if table not in self._available_tables:
            raise ValueError(f"Table '{table}' is not available")

        self._table = table
        return self

    def where(self, condition: str) -> "QueryBuilder":
        # Einfache Validierung der WHERE-Bedingung
        pattern = r"^\s*(\w+)\s*(=|!=|>|<|>=|<=)\s*(.+)\s*$"
        match = re.match(pattern, condition)
        if not match:
            raise ValueError(f"Invalid where condition '{condition}'")

        column, operator, value = match.groups()

        # Validierung der Spalte in der WHERE-Bedingung
        if column not in self._available_columns:
            raise ValueError(
                f"Column '{column}' is not available in where condition"
            )

        # Validierung des Operators
        if operator not in ["=", "!=", ">", "<", ">=", "<="]:
            raise ValueError(
                f"Invalid operator '{operator}' in where condition"
            )

        self._where_conditions.append(condition)
        return self

    def order_by(self, column: str, direction: str = "asc") -> "QueryBuilder":
        # Validierung der Sortierspalte
        if column not in self._available_columns:
            raise ValueError(f"Column '{column}' is not available")

        # Validierung der Sortierrichtung
        if direction not in ["asc", "desc"]:
            raise ValueError(
                f"Invalid order direction '{direction}'. Use 'asc' or 'desc'"
            )

        self._order_by_column = column
        self._order_by_direction = direction
        return self

    def limit(self, count: int) -> "QueryBuilder":
        # Validierung des Limit-Werts
        if count <= 0:
            raise ValueError("Limit count must be a positive integer")

        self._limit = count
        return self

    def build(self) -> str:
        if not self._table:
            raise ValueError("Table name is required")

        columns_part = ", ".join(self._columns) if self._columns else "*"
        query = f"SELECT {columns_part} FROM {self._table}"

        if self._where_conditions:
            where_part = " AND ".join(self._where_conditions)
            query += f" WHERE {where_part}"

        if self._order_by_column:
            query += f" ORDER BY {self._order_by_column} {self._order_by_direction.upper()}"

        if self._limit is not None:
            query += f" LIMIT {self._limit}"

        return query
