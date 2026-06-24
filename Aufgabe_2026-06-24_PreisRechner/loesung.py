import os
from typing import List

class InvalidInputException(Exception):
    """Custom exception for invalid input values."""
    pass

def calculate_net_payment(amounts: List[float], flat_fee: float, commission_rate: float) -> float:
    """
    Calculates the net payment amount after applying a flat fee and commission rate.
    
    Args:
        amounts: A list of individual payment amounts to be aggregated.
        flat_fee: The fixed fee to subtract from the total amount before applying commission.
        commission_rate: The percentage rate to apply as commission (e.g., 5.0 for 5%).
        
    Returns:
        The net payment amount after all deductions.
        
    Raises:
        InvalidInputException: If any input is invalid according to business rules.
    """
    pass