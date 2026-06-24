import pytest
from loesung import *


def test_sort_empty_list():
    """AC 1, AC 3: Leere Liste sollte eine leere Liste zurückgeben."""
    assert sort_tasks_by_priority([]) == []


def test_sort_single_task():
    """AC 1: Einzelne Aufgabe sollte unverändert zurückgegeben werden."""
    task = Task("1", 5)
    result = sort_tasks_by_priority([task])
    assert result == [task]


def test_sort_multiple_tasks_descending_priority():
    """AC 1: Mehrere Aufgaben sollten nach absteigender Priorität sortiert werden."""
    task1 = Task("1", 3)
    task2 = Task("2", 7)
    task3 = Task("3", 1)
    tasks = [task1, task2, task3]
    result = sort_tasks_by_priority(tasks)
    expected = [task2, task1, task3]
    assert result == expected


def test_sort_stable_order():
    """AC 2: Stabilität der Sortierung bei gleichen Prioritäten."""
    task1 = Task("1", 5)
    task2 = Task("2", 5)
    task3 = Task("3", 5)
    tasks = [task1, task2, task3]
    result = sort_tasks_by_priority(tasks)
    # Da die Sortierung stabil ist, sollte die ursprüngliche Reihenfolge erhalten bleiben
    assert result[0] is task1
    assert result[1] is task2
    assert result[2] is task3


def test_sort_with_same_priority_mixed_order():
    """AC 2: Stabilität bei gemischter Prioritätsvergabe."""
    task1 = Task("1", 10)
    task2 = Task("2", 5)
    task3 = Task("3", 10)  # gleiche Priorität wie task1
    tasks = [task1, task2, task3]
    result = sort_tasks_by_priority(tasks)
    assert result[0] is task1  # Höchste Priorität zuerst
    assert (
        result[1] is task3
    )  # Gleiche Priorität, daher in Originalreihenfolge
    assert result[2] is task2


def test_sort_preserves_original_list():
    """AC 3: Ursprüngliche Liste darf nicht verändert werden."""
    task1 = Task("1", 3)
    task2 = Task("2", 7)
    original_tasks = [task1, task2]
    # Kopie erstellen, um die Identität der Liste zu prüfen
    result = sort_tasks_by_priority(original_tasks)
    assert result == [task2, task1]
    assert original_tasks == [task1, task2]


def test_sort_with_negative_priorities():
    """Edge Case: Negative Prioritätswerte sollten korrekt sortiert werden."""
    task1 = Task("1", -1)
    task2 = Task("<0xA0>2", -5)
    task3 = Task("3", 0)
    tasks = [task1, task2, task3]
    result = sort_tasks_by_priority(tasks)
    expected = [task3, task1, task2]
    assert result == expected


def test_sort_with_invalid_task_type():
    """AC 4: Nicht-Task Objekte (z.B. Dict) sollten eine TypeError auslösen."""
    with pytest.raises(TypeError):
        sort_tasks_by_priority([{"id": "1", "priority": 5}])


def test_sort_with_none_element_in_list():
    """Edge Case: None-Werte innerhalb der Liste müssen abgefangen werden."""
    task = Task("1", 5)
    with pytest.raises(TypeError):
        sort_tasks_by_priority([task, None])


def test_sort_with_none_priority_value():
    """Edge Case: None als Prioritätswert muss einen TypeError (Vergleichsfehler) auslösen."""

    class TaskWithNonePriority:
        def __init__(self, id, priority):
            self.id = id
            self.priority = priority

        def get_priority(self):
            return self.priority

    task = TaskWithNonePriority("1", None)
    with pytest.raises(TypeError):
        sort_tasks_by_priority([task])


def test_sort_with_non_numeric_priority():
    """AC 4: Nicht-numerische Prioritätswerte sollten eine TypeError auslösen."""

    class InvalidTask:
        def __init__(self, id: str, priority: str):
            self.id = id
            self.priority = priority

        def get_priority(self) -> str:
            return self.priority

    task = InvalidTask("1", "high")
    with pytest.raises(TypeError):
        sort_tasks_by_priority([task])


def test_sort_with_missing_get_priority_method():
    """AC 4/Design Rule: Fehlende get_priority-Methode sollte eine AttributeError auslösen."""

    class TaskWithoutGetter:
        def __init__(self, id: str, priority: int):
            self.id = id
            self.priority = priority

    task = TaskWithoutGetter("1", 5)
    with pytest.raises(AttributeError):
        sort_tasks_by_priority([task])


def test_sort_with_mixed_valid_invalid_tasks():
    """AC 4: Mischung aus gültigen und ungültigen Tasks sollte Fehler werfen."""
    valid_task = Task("1", 5)
    # Ein Objekt, das kein Task ist (z.B. int)
    with pytest.raises(TypeError):
        sort_tasks_by_priority([valid_task, 123])
