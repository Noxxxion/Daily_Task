import pytest
from loesung import (
    couple_objects, 
    couple_object_lists, 
    CouplingResult, 
    KeyAttributeNotFoundError, 
    IncompatibleKeyTypesError, 
    NullKeyError
)

def test_couple_objects_success() -> None:
    """Testet erfolgreiche Kopplung zweier Objekte mit kompatiblen Schlüsseln."""
    obj_a = {"uid": 100, "data": "A"}
    obj_b = {"uid": 100, "data": "B"}
    
    result = couple_objects(obj_a, obj_b, "uid")
    
    assert isinstance(result, CouplingResult)
    assert result.key_value == 100
    assert result.left_object["data"] == "A"
    assert result.right_object["data"] == "B"

def test_couple_objects_missing_key_attribute() -> None:
    """Testet, dass eine KeyAttributeNotFoundError geworfen wird, wenn ein Schlüssel fehlt."""
    obj_a = {"id": 1}
    obj_b = {"name": "Kein ID Attribut"}
    with pytest.raises(KeyAttributeNotFoundError):
        couple_objects(obj_a, obj_b, "id")

def test_couple_objects_incompatible_types() -> None:
    """Testet, dass eine IncompatibleKeyTypesError geworfen wird bei inkompatiblen Typen (String vs Int)."""
    obj_a = {"uid": "100"}
    obj_b = {"uid": 100}
    with pytest.raises(IncompatibleKeyTypesError):
        couple_objects(obj_a, obj_b, "uid")

def test_couple_objects_null_key() -> None:
    """Testet, dass eine NullKeyError geworfen wird, wenn ein Schlüsselwert None ist."""
    obj_a = {"uid": None}
    obj_b = {"uid": 100}
    with pytest.raises(NullKeyError):
        couple_objects(obj_a, obj_b, "uid")

def test_immutability_requirement() -> None:
    """Verifiziert die Anforderung der Unveränderlichkeit (Immutability) der Quellobjekte."""
    original_a = {"uid": 1, "meta": "unchanged"}
    original_b = {"uid": 1, "meta": "unchanged"}
    # Kopie für den Vergleich nach dem Prozess
    copy_a = original_a.copy()
    copy_b = original_b.copy()
    
    couple_objects(original_a, original_b, "uid")
    
    assert original_a == copy_a, "Das Quellobjekt A wurde mutiert!"
    assert original_b == copy_b, "Das Quellobjekt B wurde mutiert!"

def test_couple_object_lists_success() -> None:
    """Testet erfolgreiche Kopplung von Listen mit mehreren Treffern (One-to-Many)."""
    list_a = [{"uid": 1, "val": "A"}, {"uid": 2, "val": "B"}]
    list_b = [{"uid": 1, "info": "X"}, {"uid": 1, "info": "Y"}]
    
    results = couple_object_lists(list_a, list_b, "uid")
    
    # Erwartet: 2 Ergebnisse (1-X und 1-Y)
    assert len(results) == 2
    keys = [r.key_value for r in results]
    assert keys == [1, 1]

def test_couple_object_lists_empty_inputs() -> None:
    """Testet das Verhalten bei leeren Eingabelisten (sollte leere Liste zurückgeben, keine Exception)."""
    assert couple_object_lists([], [{"uid": 1}], "uid") == []
    assert couple_object_lists([{"uid": 1}], [], "uid") == []

def test_couple_object_lists_duplicate_keys() -> None:
    """Testet das Verhalten bei Duplikaten in der linken Liste (One-to-Many)."""
    list_a = [{"uid": 1, "tag": "first"}, {"uid": 1, "tag": "second"}]
    list_b = [{"uid": 1, "data": "target"}]
    
    results = couple_object_lists(list_a, list_b, "uid")
    
    assert len(results) == 2
    assert results[0].left_object["tag"] == "first"
    assert results[1].left_object["tag"] == "second"