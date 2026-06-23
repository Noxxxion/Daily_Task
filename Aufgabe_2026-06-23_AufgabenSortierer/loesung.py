import os
from typing import List, Dict, Set, Optional

class Task:
    def __init__(self, id: str, priority: int):
        self.id = id
        self.priority = priority

def sort_tasks_by_priority(tasks: List[Task]) -> List[Task]:
    """
    Sortiert eine Liste von Aufgabenobjekten nach ihrem Prioritätswert absteigend.
    
    Args:
        tasks: Liste von Task-Objekten mit einem 'priority'-Attribut
        
    Returns:
        Eine neue, sortierte Kopie der Eingabeliste
        
    Raises:
        TypeError: Wenn die Eingabe keine Liste ist oder ein Element kein Task-Objekt
        ValueError: Wenn ein Task-Objekt kein gültiges priority-Attribut besitzt
    """
    pass