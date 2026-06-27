import pytest
from loesung import *

def test_step_initialization():
    """Testet die Initialisierung eines Steps."""
    step = Step("step1", "Beschreibung des Schritts")
    assert step.step_id == "step1"
    assert step.description == "Beschreibung des Schritts"
    assert step.status == "PENDING"

def test_step_invalid_initialization():
    """Testet die Initialisierung mit ungültigen Werten (leere Strings und None)."""
    with pytest.raises(ValueError):
        Step("", "Beschreibung")
    
    with pytest.raises(ValueError):
        Step("step1", "")

    with pytest.raises(ValueError):
        Step(None, "Beschreibung") # type: ignore

    with pytest.raises(ValueError):
        Step("step1", None) # type: ignore

def test_step_id_immutability():
    """Testet die Immutabilität der Schritt-ID."""
    step = Step("step1", "Beschreibung")
    with pytest.raises(AttributeError):
        step.step_id = "new_id" # type: ignore

def test_step_status_transitions():
    """Testet die Statusübergänge eines Steps (PENDING -> IN_PROGRESS -> COMPLETED)."""
    step = Step("step1", "Beschreibung")
    
    # Starten des Schritts
    step.start()
    assert step.status == "IN_PROGRESS"
    
    # Abschluss des Schritts
    step.complete()
    assert step.status == "COMPLETED"
    
    # Weitere Änderungen sollten fehlschlagen (Schritt ist bereits abgeschlossen)
    with pytest.raises(ValueError):
        step.start()
    
    with pytest.raises(ValueError):
        step.complete()

def test_step_invalid_completion():
    """Testet ungültige Zustandsübergänge (Überspringen von IN_PROGRESS)."""
    step = Step("step1", "Beschreibung")
    
    # Versuch, direkt abzuschließen ohne zu starten (PENDING -> COMPLETED ist verboten)
    with pytest.raises(ValueError):
        step.complete()

def test_step_list_initialization():
    """Testet die Initialisierung einer SchrittListe."""
    step1 = Step("step1", "Schritt 1")
    step2 = Step("step2", "Schritt 2")
    
    step_list = StepList([step1, step2])
    assert step_list.get_completed_steps() == 0

def test_step_list_empty_initialization():
    """Testet die Initialisierung mit leerer Liste."""
    with pytest.raises(ValueError):
        StepList([])

def test_step_list_duplicate_ids():
    """Testet die Initialisierung mit doppelten IDs."""
    step1 = Step("step1", "Schritt 1")
    step2 = Step("step1", "Schritt 2")  # gleiche ID
    
    with pytest.raises(ValueError):
        StepList([step1, step2])

def test_step_list_get_step():
    """Testet das Abrufen eines Schritts."""
    step1 = Step("step1", "Schritt 1")
    step2 = Step("step2", "Schritt 2")
    
    step_list = StepList([step1, step2])
    
    assert step_list.get_step("step1") == step1
    assert step_list.get_step("step2") == step2
    assert step_list.get_step("nonexistent") is None

def test_step_list_progress():
    """Testet die Fortschrittsberechnung."""
    step1 = Step("step1", "Schrit 1")
    step2 = Step("step2", "Schritt 2")
    
    step_list = StepList([step1, step2])
    
    # Initialer Fortschritt
    assert step_list.get_progress() == 0.0
    assert step_list.get_completed_steps() == 0
    
    # Einen Schritt abgeschlossen
    step1.start()
    step1.complete()
    
    assert step_list.get_progress() == 50.0
    assert step_list.get_completed_steps() == 1

def test_step_list_status_validation():
    """Testet die Validierung der sequenziellen Integrität (Schritt-Überspringen)."""
    pass