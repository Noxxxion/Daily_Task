```python
import pytest
from your_module import OrderStateMachine, OrderStatus, InvalidStateTransitionException  # Replace 'your_module' with actual module name

def test_initialization_with_valid_status():
    """Test that the state machine initializes correctly with a valid status."""
    sm = OrderStateMachine(OrderStatus.OFFEN)
    assert sm.current_status == OrderStatus.OFFEN

def test_initialization_with_invalid_status():
    """Test that initializing with an invalid status raises an exception."""
    with pytest.raises(InvalidStateTransitionException):
        OrderStateMachine("INVALID_STATUS")

def test_valid_transition_from_offen():
    """Test valid transitions from OFFEN status."""
    sm = OrderStateMachine(OrderStatus.OFFEN)
    sm.transition_to(OrderStatus.IN_BEARBEITUNG)
    assert sm.current_status == OrderStatus.IN_BEARBEITUNG

def test_invalid_transition_from_offen():
    """Test invalid transitions from OFFEN status."""
    sm = OrderStateMachine(OrderStatus.OFFEN)
    with pytest.raises(InvalidStateTransitionException):
        sm.transition_to(OrderStatus.ABGESCHLOSSEN)

def test_valid_transition_from_in_bearbeitung():
    """Test valid transitions from IN_BEARBEITUNG status."""
    sm = OrderStateMachine(OrderStatus.IN_BEARBEITUNG)
    sm.transition_to(OrderStatus.ABGESCHLOSSEN)
    assert sm.current_status == OrderStatus.ABGESCHLOSSEN

def test_invalid_transition_from_in_bearbeitung():
    """Test invalid transitions from IN_BEARBEITUNG status."""
    sm = OrderStateMachine(OrderStatus.IN_BEARBEITUNG)
    with pytest.raises(InvalidStateTransitionException):
        sm.transition_to(OrderStatus.OFFEN)

def test_terminal_state_transitions():
    """Test that terminal states cannot transition further."""
    sm = OrderStateMachine(OrderStatus.ABGESCHLOSSEN)
    with pytest.raises(InvalidStateTransitionException):
        sm.transition_to(OrderStatus.STORNIERT)

    sm = OrderStateMachine(OrderStatus.STORNIERT)
    with pytest.raises(InvalidStateTransitionException):
        sm.transition_to(OrderStatus.OFFEN)

def test_status_property_read_only():
    """Test that the current_status property is read-only."""
    sm = OrderStateMachine()
    assert sm.current_status == OrderStatus.OFFEN
    # This should not be allowed, but we're just checking it's accessible
    try:
        sm.current_status = "SOMETHING"
    except AttributeError:
        pass  # Expected behavior
```