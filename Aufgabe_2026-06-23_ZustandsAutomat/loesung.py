# Order State Machine - Code Skeleton

```python
import os
from typing import List, Dict, Set, Optional

class InvalidStateTransitionException(Exception):
    """Custom exception raised when an invalid state transition is attempted."""
    pass

class OrderStatus:
    """Enumeration of valid order statuses."""
    OFFEN = "OFFEN"
    IN_BEARBEITUNG = "IN_BEARBEITUNG"
    ABGESCHLOSSEN = "ABGESCHLOSSEN"
    STORNIERT = "STORNIERT"

class OrderStateMachine:
    """
    A finite state machine for managing order status transitions.
    
    The state machine ensures that order status can only be changed according to
    predefined rules, maintaining process integrity and preventing invalid transitions.
    """

    # Define valid transitions between states
    _TRANSITIONS: Dict[str, Set[str]] = {
        OrderStatus.OFFEN: {OrderStatus.IN_BEARBEITUNG, OrderStatus.STORNIERT},
        OrderStatus.IN_BEARBEITUNG: {OrderStatus.ABGESCHLOSSEN, OrderStatus.STORNIERT},
        OrderStatus.ABGESCHLOSSEN: set(),  # Terminal state
        OrderStatus.STORNIERT: set()       # Terminal state
    }

    def __init__(self, initial_status: str = OrderStatus.OFFEN):
        """
        Initialize the state machine with an initial status.
        
        Args:
            initial_status (str): The starting status of the order.
            
        Raises:
            InvalidStateTransitionException: If the initial status is not valid.
        """
        pass

    @property
    def current_status(self) -> str:
        """
        Get the current status of the order.
        
        Returns:
            str: The current status.
        """
        pass

    def transition_to(self, target_status: str) -> None:
        """
        Transition the order to a new status if allowed by the state machine rules.
        
        Args:
            target_status (str): The desired target status.
            
        Raises:
            InvalidStateTransitionException: If the transition is not allowed or invalid.
        """
        pass
```