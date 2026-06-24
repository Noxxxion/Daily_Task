import os
from typing import List, Dict, Set, Optional, Any

class InvalidTransitionError(Exception):
    """Exception raised when an invalid state transition is attempted."""
    pass

class StateMachine:
    """
    A state machine that manages valid transitions between states based on triggers.
    
    The state machine ensures that state changes are only allowed according to a 
    predefined transition matrix. It enforces encapsulation by not allowing direct
    access to the internal state, and provides atomic state changes.
    
    Attributes:
        _initial_state: The initial state of the machine.
        _transitions: A dictionary mapping (current_state, trigger) to next_state.
        _valid_states: A set of all valid states.
        _current_state: The current state of the machine.
    """
    
    def __init__(self, 
                 initial_state: str,
                 transitions: Dict[str, Dict[str, str]],
                 valid_states: Optional[Set[str]] = None):
        """
        Initialize the StateMachine with an initial state, transition rules, and valid states.
        
        Args:
            initial_state: The starting state of the machine.
            transitions: A nested dictionary mapping (current_state, trigger) to next_state.
            valid_states: Set of all valid states. If None, derived from transitions.
            
        Raises:
            ValueError: If initial_state is not in valid_states or if transitions are invalid.
        """
        pass
    
    def trigger(self, trigger: str) -> None:
        """
        Attempt to transition to a new state based on the given trigger.
        
        Args:
            trigger: The event that triggers a state change.
            
        Raises:
            InvalidTransitionError: If the transition is not allowed.
            ValueError: If trigger is None or empty string.
        """
        pass
    
    def get_current_state(self) -> str:
        """
        Get the current state of the machine.
        
        Returns:
            The current state as a string.
        """
        pass