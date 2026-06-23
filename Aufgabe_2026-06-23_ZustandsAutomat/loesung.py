import os
from typing import List, Dict, Set, Optional

class OrderState:
    ERSTELLT = "ERSTELLT"
    IN_BEARBEITUNG = "IN_BEARBEITUNG"
    VERSANDT = "VERSANDT"
    ABGESCHLOSSEN = "ABGESCHLOSSEN"
    ABGEBROCHEN = "ABGEBROCHEN"

class InvalidTransitionError(Exception):
    """Exception raised when an invalid state transition is attempted."""
    pass

class OrderStateMachine:
    """
    A finite state machine for managing order states according to defined business rules.
    
    The state machine ensures that transitions between order states follow strict business logic,
    preventing invalid state changes such as moving from 'ERSTELLT' directly to 'VERSANDT'.
    """
    
    def __init__(self, initial_state: str):
        """
        Initialize the state machine with an initial state.
        
        Args:
            initial_state (str): The starting state of the order.
            
        Raises:
            InvalidTransitionError: If the initial state is not a valid order state.
        """
        pass
    
    def transition_to(self, target_state: str) -> None:
        """
        Transition the order to a new state according to business rules.
        
        Args:
            target_state (str): The desired target state.
            
        Raises:
            InvalidTransitionError: If the transition is not allowed by business rules
                                    or if the target state is invalid.
        """
        pass
    
    def get_current_state(self) -> str:
        """
        Get the current state of the order.
        
        Returns:
            str: The current state of the order.
        """
        pass