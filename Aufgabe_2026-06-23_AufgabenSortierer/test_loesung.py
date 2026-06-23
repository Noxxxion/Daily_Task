import pytest
from typing import List, Optional

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
    # Überprüfe, ob die Eingabe eine Liste ist
    if not isinstance(tasks, list):
        raise TypeError("Die Eingabe muss eine Liste sein.")
    
    # Erstelle eine Kopie der Liste, um Mutation zu verhindern
    result = []
    
    for task in tasks:
        # Überprüfe, ob das Element None ist
        if task is None:
            raise TypeError("Elemente in der Liste dürfen nicht None sein.")
        
        # Überprüfe, ob das Element ein Task-Objekt ist
        if not isinstance(task, Task):
            raise TypeError("Alle Elemente in der Liste müssen Task-Objekte sein.")
        
        # Überprüfe, ob das priority-Attribut vorhanden ist
        if not hasattr(task, 'priority'):
            raise ValueError("Task-Objekte müssen ein 'priority'-Attribut besitzen.")
        
        # Überprüfe, ob das priority-Attribut None ist
        if task.priority is None:
            raise ValueError("Das 'priority'-Attribut darf nicht None sein.")
        
        # Überprüfe, ob das priority-Attribut numerisch ist
        if not isinstance(task.priority, (int, float)):
            raise ValueError("Das 'priority'-Attribut muss numerisch sein.")
        
        result.append(task)
    
    # Sortiere die Liste nach Priorität absteigend und behalte die Stabilität bei
    return sorted(result, key=lambda x: x.priority, reverse=True)

def test_sort_empty_list():
    """Testet das Sortieren einer leeren Liste."""
    assert sort_tasks_by_priority([]) == []

def test_sort_single_task():
    """Testet das Sortieren einer Liste mit einem Task."""
    task = Task("1", 5)
    result = sort_tasks_by_priority([task])
    assert result == [task]

def test_sort_multiple_tasks():
    """Testet das Sortieren mehrerer Tasks mit unterschiedlichen Prioritäten."""
    task1 = Task("1", 3)
    task2 = Task("2", 1)
    task3 = Task("3", 5)
    
    tasks = [task1, task2, task3]
    result = sort_tasks_by_priority(tasks)
    
    assert len(result) == 3
    assert result[0].priority == 5  # Höchste Priorität zuerst
    assert result[1].priority == 3
    assert result[2].priority == 1

def test_sort_stable():
    """Testet, dass die Sortierung stabil ist (gleiche Prioritäten behalten Reihenfolge)."""
    task1 = Task("1", 5)
    task2 = Task("2", 5)
    task3 = Task("3", 3)
    
    tasks = [task1, task2, task3]
    result = sort_tasks_by_priority(tasks)
    
    # task1 sollte vor task2 stehen, da es im Original-Array zuerst stand
    assert result[0] is task1
    assert result[1] is task2
    assert result[2].priority == 3

def test_sort_with_none_priority():
    """Testet das Verhalten bei None-Werten im priority-Attribut."""
    task1 = Task("1", 5)
    task2 = Task("2", None)
    
    tasks = [task1, task2]
    
    with pytest.raises(ValueError):
        sort_tasks_by_priority(tasks)

def test_sort_with_invalid_priority_type():
    """Testet das Verhalten bei nicht-numerischen Prioritätswerten."""
    task1 = Task("1", 5)
    task2 = Task("2", "high") # type: ignore
    
    tasks = [task1, task2]
    
    with pytest.raises(ValueError):
        sort_tasks_by_priority(tasks)

def test_sort_with_none_element():
    """Testet das Verhalten, wenn ein Element der Liste selbst None ist."""
    task1 = Task("1", 5)
    tasks = [task1, None]
    
    with pytest.raises(TypeError):
        sort_tasks_by_priority(tasks)

def test_sort_with_invalid_element_type():
    """Testet das Verhalten bei Elementen, die keine Task-Objekte sind."""
    task1 = Task("1", 5)
    tasks = [task1, "not a task object"] # type: ignore
    
    with pytest.raises(TypeError):
        sort_tasks_by_priority(tasks)

def test_sort_mutates_original_list():
    """Testet, dass die Originalliste nicht mutiert wird und ein neues Objekt zurückgegeben wird."""
    task1 = Task("1", 3)
    task2 = Task("2", 1)
    
    original_tasks = [task1, task2]
    original_copy = [t for t in original_tasks]
    
    result = sort_tasks_by_priority(original_tasks)
    
    # Die Inhalt der Original-Liste muss identisch mit dem Snapshot vor der Sortierung sein
    assert original_tasks == original_copy
    # Das Ergebnis muss ein anderes Objekt (neue Liste) sein
    assert result is not original_tasks

def test_sort_with_missing_priority_attribute():
    """Testet das Verhalten bei fehlendem priority-Attribut."""
    class TaskWithoutPriority:
        def __init__(self, id: str):
            self.id = id
    
    task1 = Task("1", 5)
    task2 = TaskWithoutPriority("2")
    
    tasks = [task1, task2] # type: ignore
    
    with pytest.raises(ValueError):
        sort_tasks_by_priority(tasks)

def test_sort_with_negative_priorities():
    """Testet das Sortieren mit negativen Prioritäten."""
    task1 = Task("1", -1)
    task2 = Task("2", -5)
    task3 = Task("3", 0)
    
    tasks = [task1, task2, task3]
    result = sort_tasks_by_priority(tasks)
    
    assert result[0].priority == 0  # Höchste Priorität
    assert result[1].priority == -1
    assert result[2].priority == -5

def test_sort_with_large_priorities():
    """Testet das Sortieren mit sehr hohen Prioritäten."""
    task1 = Task("1", 1000000)
    task2 = Task("2", 999999)
    
    tasks = [task1, task2]
    result = sort_tasks_by_priority(tasks)
    
    assert result[0].priority == 1000000