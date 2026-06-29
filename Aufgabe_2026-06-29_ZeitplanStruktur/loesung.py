import os
from typing import List, Optional
from datetime import datetime

class InvalidIntervalError(Exception):
    """Exception raised when an interval has invalid start and end times."""
    pass

class OverlappingIntervalsError(Exception):
    """Exception raised when adding an interval that overlaps with existing intervals."""
    pass

class Interval:
    """Represents a time interval with a start and end datetime."""
    
    def __init__(self, start: datetime, end: datetime) -> None:
        """
        Initialize an interval with start and end times.
        
        Args:
            start: The start datetime of the interval.
            end: The end datetime of the interval.
            
        Raises:
            InvalidIntervalError: If start time is not before end time.
        """
        pass
    
    def __eq__(self, other) -> bool:
        """Check equality of two intervals."""
        pass
    
    def __hash__(self) -> int:
        """Return hash of the interval."""
        pass

class TimeSchedule:
    """Manages a collection of non-overlapping time intervals."""
    
    def __init__(self) -> None:
        """Initialize an empty time schedule."""
        pass
    
    def add_interval(self, interval: Interval) -> None:
        """
        Add an interval to the schedule.
        
        Args:
            interval: The interval to be added.
            
        Raises:
            OverlappingIntervalsError: If the interval overlaps with existing intervals.
        """
        pass
    
    def get_intervals(self) -> List[Interval]:
        """
        Get all intervals sorted by start time.
        
        Returns:
            A list of intervals sorted chronologically.
        """
        pass