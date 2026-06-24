import os
from typing import List, Dict, Set, Optional


class Task:
    """
    Repräsentiert eine Aufgabe mit einem numerischen Prioritätswert.

    Attributes:
        id (str): Eindeutige Identifikation der Aufgabe.
        priority (int): Numerischer Wert zur Bestimmung der Priorität.
    """

    def __init__(self, id: str, priority: int):
        self.id = id
        self.priority = priority

    def get_priority(self) -> int:
        """
        Gibt den Prioritätswert der Aufgabe zurück.

        Returns:
            int: Der numerische Prioritätswert.
        """
        return self.priority


def sort_tasks_by_priority(tasks: List[Task]) -> List[Task]:
    """
    Sortiert eine Liste von Task-Objekten nach ihrem Prioritätswert in absteigender Reihenfolge.

    Die Sortierung ist stabil, d.h. Aufgaben mit gleicher Priorität behalten ihre
    relative Reihenfolge aus der ursprünglichen Liste bei.

    Args:
        tasks (List[Task]): Liste von Task-Objekten zur Sortierung.

    Returns:
        List[Task]: Eine neue, sortierte Liste der Aufgaben.

    Raises:
        TypeError: Wenn die Eingabeliste oder ein Task-Objekt nicht korrekt ist.
        AttributeError: Wenn ein Task-Objekt kein 'get_priority'-Attribut besitzt.
    """
    pass
