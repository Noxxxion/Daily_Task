import pytest
from loesung import StateMachine, InvalidTransitionError

@pytest.fixture
def valid_config():
    """Fixture für eine standardmäßig gültige Konfiguration."""
    return {
        "initial_state": "OPEN",
    "transitions": {
        "OPEN": {"PAY": "PAID", "CANCEL": "CLOSED"},
        "PAID": {"SHIP": "SHIPPED"},
        "SHIPPED": {"DELIVER": "DELIVERED"},
        "CLOSED": {},
        "DELIVERED": {}
    },
    "valid_states": {"OPEN", "PAID", "SHIPPED", "DELIVERED", "CLOSED"}
    }

def test_initialization_with_valid_config(valid_config):
    """Test, dass die StateMachine mit einer gültigen Konfiguration korrekt initialisiert wird."""
    sm = StateMachine(
        initial_state=valid_config["initial_state"],
        transitions=valid_config["transitions"],
        valid_states=valid_config["valid_states"]
    )
    assert sm.get_current_state() == "OPEN"

def test_initialization_with_invalid_initial_state(valid_config):
    """Test, dass ein ValueError geworfen wird, wenn der Startzustand nicht in den validen Zuständen liegt."""
    with pytest.raises(ValueError, match="Initial state not in valid states"):
        StateMachine(
            initial_state="NON_EXISTENT",
  	        transitions=valid_config["transitions"],
            valid_states=valid_config["valid_states"]
        )

def test_trigger_valid_transition(valid_config):
    """Test, dass ein gültiger Übergang erfolgreich ausgeführt wird."""
    sm = StateMachine(
        initial_state="OPEN",
        transitions=valid_config["transitions"],
        valid_states=valid_config["valid_states"]
    )
    sm.trigger("PAY")
    assert sm.get_current_state() == "PAID"

def test_trigger_invalid_transition(valid_config):
    """Test, dass ein nicht definierter Übergang für den aktuellen Zustand einen InvalidTransitionError auslöst."""
    sm = StateMachine(
        initial_state="OPEN",
        transitions=valid_config["transitions"],
        valid_states=valid_config["valid_states"]
    )
    # 'SHIP' ist zwar in der Matrix, aber nicht von 'OPEN' aus erreichbar
    with pytest.raises(InvalidTransitionError):
        sm.trigger("SHIP")

def test_get_current_state(valid_config):
    """Test, dass der aktuelle Zustand korrekt zurückgegeben wird."""
    sm = StateMachine(
        initial_state="OPEN",
        transitions=valid_config["transitions"],
        valid_states=valid_config["valid_states"]
    )
    assert sm.get_current_state() == "OPEN"

def test_self_transition():
    """Test, dass ein Übergang in den gleichen Zustand (Self-Transition) erlaubt ist, sofern definiert."""
    transitions = {"STABLE": {"STAY": "STABLE"}}
    sm = StateMachine(initial_state="STABLE", transitions=transitions, valid_states={"STABLE"})
    sm.trigger("STAY")
    assert sm.get_current_state() == "STABLE"

def test_empty_transitions():
    """Test das Verhalten bei einer leeren Transitions-Matrix."""
    with pytest.raises(ValueError):
        # Initialisierung mit leerer Matrix sollte gegen die Anforderung 'keine leere Liste' verstoßen
        StateMachine(initial_state="START", transitions={}, valid_states={"START"})

def test_none_initial_state():
    """Test, dass None als initialer Zustand einen ValueError auslöst."""
    with pytest.raises(ValueError):
        StateMachine(initial_state=None, transitions={}, valid_states=None)

def test_none_trigger():
    """Test, dass ein None-Trigger einen ValueError auslöst."""
    sm = StateMachine(initial_state="OPEN", transitions={"OPEN": {"PAY": "PAID"}}, valid_states={"OPEN", "PAID"})
    with pytest.raises(ValueError):
        sm.trigger(None)

def test_empty_trigger():
    """Test, dass ein leerer String als Trigger einen ValueError auslucht."""
    sm = StateMachine(initial_state="OPEN", transitions={"OPEN": {"PAY": "PAID"}}, valid_states={"OPEN", "PAID"})
    with pytest.raises(ValueError):
        sm.trigger("")

def test_transition_to_none_state():
    """Test, dass ein Übergang in einen None-Zustand als unzulässig erkannt wird."""
    transitions = {"OPEN": {"BAD_EVENT": None}}
    sm = StateMachine(initial_state="OPEN", transitions=transitions, valid_states={"OPEN"})
    with pytest.raises(InvalidTransitionError):
        sm.trigger("BAD_EVENT")

def test_multiple_transitions(valid_config):
    """Test eine Sequenz von mehreren aufeinanderfolgenden Übergängen."""
    sm = StateMachine(
        initial_state="OPEN",
        transitions=valid_config["transitions"],
        valid_states=valid_config["valid_states"]
    )
    sm.trigger("PAY")
    sm.trigger("SHIP")
    sm.trigger("DELIVER")
    assert sm.get_current_state() == "DELIVERED"

def test_invalid_trigger_for_current_state(valid_config):
    """Test, dass ein Trigger, der zwar existiert, aber nicht für den aktuellen Zustand registriert ist, blockiert wird."""
    sm = StateMachine(
        initial_state="PAID",
        transitions=valid_config["transitions"],
        valid_states=valid_config["valid_states"]
    )
    # 'CANCEL' existiert in der Matrix für 'OPEN', aber nicht für 'PAID'
    with pytest.raises(InvalidTransitionError):
        sm.trigger("CANCEL")

def test_transition_matrix_immutability(valid_config):
    """Test, dass eine nachträgliche Änderung der externen Transitions-Dictionary die interne Logik nicht beeinflusst."""
    transitions = {"OPEN": {"PAY": "PAID"}}
    sm = StateMachine(initial_state="OPEN", transitions=transitions, valid_states={"OPEN", "PAID"})
    
    # Manipulation des ursprünglichen Objekts
    transitions["OPEN"]["PAY"] = "BROKEN"
    
    # Der Übergang muss weiterhin zum korrekten Zielzustand führen (Deep Copy/Immutability Check)
    sm.trigger("PAY")
    assert sm.get_current_state() == "PAID"

def test_atomicity_on_failure(valid_config):
    """Test, dass der Zustand bei einem fehlgeschlagenen Trigger nicht verändert wird (Atomarität)."""
    sm = StateMachine(
        initial_state="OPEN",
        transitions=valid_config["transitions"],
        valid_states=valid_config["valid_states"]
    )
    with pytest.raises(InvalidTransitionError):
        sm.trigger("NON_EXISTENT_EVENT")
    # Der Zustand muss nach dem Fehler weiterhin 'OPEN' sein
    assert sm.get_current_state() == "OPEN"