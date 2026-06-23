import pytest
from order_state_machine import OrderStateMachine, OrderState, InvalidTransitionError

def test_initialization():
    """Testet die Initialisierung der Zustandsmaschine mit gültigem Startzustand."""
    order = OrderStateMachine(OrderState.ERSTELLT)
    assert order.get_current_state() == OrderState.ERSTELLT

def test_valid_transition_from_created_to_processing():
    """Testet einen gültigen Übergang von ERSTELLT zu IN_BEARBEITUNG."""
    order = OrderStateMachine(OrderState.ERSTELLT)
    order.transition_to(OrderState.IN_BEARBEITUNG)
    assert order.get_current_state() == OrderState.IN_BEARBEITUNG

def test_valid_transition_from_processing_to_shipped():
    """Testet einen gültigen Übergang von IN_BEARBEITUNG zu VERSANDT."""
    order = OrderStateMachine(OrderState.IN_BEARBEITUNG)
    order.transition_to(OrderState.VERSANDT)
    assert order.get_current_state() == OrderState.VERSANDT

def test_valid_transition_from_shipped_to_completed():
    """Testet einen gültigen Übergang von VERSANDT zu ABGESCHLOSSEN."""
    order = OrderStateMachine(OrderState.VERSANDT)
    order.transition_to(OrderState.ABGESCHLOSSEN)
    assert order.get_current_state() == OrderState.ABGESCHLOSSEN

def test_valid_transition_from_created_to_cancelled():
    """Testet einen gültigen Übergang von ERSTELLT zu ABGEBROCHEN."""
    order = OrderStateMachine(OrderState.ERSTELLT)
    order.transition_to(OrderState.ABGEBROCHEN)
    assert order.get_current_state() == OrderState.ABGEBROCHEN

def test_valid_transition_from_processing_to_cancelled():
    """Testet einen gültigen Übergang von IN_BEARBEITUNG zu ABGEBROCHEN."""
    order = OrderStateMachine(OrderState.IN_BEARBEITUNG)
    order.transition_to(OrderState.ABGEBROCHEN)
    assert order.get_current_state() == OrderState.ABGEBROCHEN

def test_invalid_transition_from_created_to_shipped():
    """Testet einen ungültigen Übergang von ERSTELLT zu VERSANDT."""
    order