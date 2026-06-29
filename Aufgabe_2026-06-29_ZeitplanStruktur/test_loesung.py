import pytest
from loesung import *
from datetime import datetime

def test_interval_creation_valid() -> None:
    """Test that valid intervals can be created."""
    start = datetime(2023, 1, 1, 10, 0)
    end = datetime(2023, 1, 1, 12, 0)
    interval = Interval(start, end)
    assert interval is not None

def test_interval_creation_invalid() -> None:
    """Test that invalid intervals (end before start) raise InvalidIntervalError."""
    start = datetime(2023, 1, 1, 12, 0)
    end = datetime(2023, 1, 1, 10, 0)
    with pytest.raises(InvalidIntervalError):
        Interval(start, end)

def test_interval_equality() -> None:
    """Test that intervals are equal if they have the same start and end times."""
    start = datetime(2023, 1, 1, 10, 0)
    end = datetime(2023, 1, 1, 12, 0)
    interval1 = Interval(start, end)
    interval2 = Interval(start, end)
    assert interval1 == interval2

def test_interval_hash() -> None:
    """Test that intervals can be hashed."""
    start = datetime(2023, 1, 1, 10, 0)
    end = datetime(2023, 1, 1, 12, 0)
    interval = Interval(start, end)
    assert hash(interval) is not None

def test_schedule_empty_initialization() -> None:
    """Test that a new schedule is empty."""
    schedule = TimeSchedule()
    assert schedule.get_intervals() == []

def test_schedule_add_single_interval() -> None:
    """Test adding a single interval to the schedule."""
    schedule = TimeSchedule()
    start = datetime(2023, 1, 1, 10, 0)
    end = datetime(2023, 1, 1, 12, 0)
    interval = Interval(start, end)
    schedule.add_interval(interval)
    intervals = schedule.get_intervals()
    assert len(intervals) == 1
    assert intervals[0] == interval

def test_schedule_add_overlapping_intervals() -> None:
    """Test that adding overlapping intervals raises OverlappingIntervalsError."""
    schedule = TimeSchedule()
    start1 = datetime(2023, 1, 1, 10, 0)
    end1 = datetime(2023, 1, 1, 12, 0)
    interval1 = Interval(start1, end1)
    schedule.add_interval(interval1)
    
    start2 = datetime(2023, 1, 1, 11, 0)
    end2 = datetime(2023, 1, 1, 13, 0)
    interval2 = Interval(start2, end2)
    
    with pytest.raises(OverlappingIntervalsError):
        schedule.add_interval(interval2)

def test_schedule_add_non_overlapping_intervals() -> None:
    """Test that adding non-overlapping intervals works correctly."""
    schedule = TimeSchedule()
    start1 = datetime(2023, 1, 1, 10, 0)
    end1 = datetime(2023, 1, 1, 12, 0)
    interval1 = Interval(start1, end1)
    schedule.add_interval(interval1)
    
    start2 = datetime(2023, 1, 1, 13, 0)
    end2 = datetime(2023, 1, 1, 15, 0)
    interval2 = Interval(start2, end2)
    schedule.add_interval(interval2)
    
    intervals = schedule.get_intervals()
    assert len(intervals) == 2
    assert intervals[0] == interval1
    assert intervals[1] == interval2

def test_schedule_get_intervals_sorted() -> None:
    """Test that intervals are returned sorted by start time."""
    schedule = TimeSchedule()
    s1 = datetime(2023, 1, 1, 15, 0)
    e1 = datetime(2023, 1, 1, 17, 0)
    interval1 = Interval(s1, e1)
    schedule.add_interval(interval1)
    
    s2 = datetime(2023, 1, 1, 10, 0)
    e2 = datetime(2023, 1, 1, 12, 0)
    interval2 = Interval(s2, e2)
    schedule.add_interval(interval2)
    
    intervals = schedule.get_intervals()
    assert len(intervals) == 2
    assert intervals[0] == interval2  # Should be sorted by start time
    assert intervals[1] == interval1

def test_schedule_add_duplicate_interval() -> None:
    """Test that adding a duplicate interval raises OverlappingIntervalsError."""
    schedule = TimeSchedule()
    start = datetime(2023, 1, 1, 10, 0)
    end = datetime(2023, 1, 1, 12, 0)
    interval = Interval(start, end)
    schedule.add_interval(interval)
    
    with pytest.raises(OverlappingIntervalsError):
        schedule.add_interval(interval)

def test_schedule_add_adjacent_intervals() -> None:
    """Test that adjacent intervals (touching at endpoints) do not overlap."""
    schedule = TimeSchedule()
    start1 = datetime(2023, 1, 1, 10, 0)
    end1 = datetime(2023, 1, 1, 12, 0)
    interval1 = Interval(start1, end1)
    schedule.add_interval(interval1)
    
    start2 = datetime(2023, 1, 1, 12, 0)
    end2 = datetime(2023, 1, 1, 14, 0)
    interval2 = Interval(start2, end2)
    schedule.add_interval(interval2)
    
    intervals = schedule.get_intervals()
    assert len(intervals) == 2
    assert intervals[0] == interval1
    assert intervals[1] == interval2

def test_schedule_add_none_interval() -> None:
    """Test that adding a None interval raises TypeError."""
    schedule = TimeSchedule()
    with pytest.raises(TypeError):
        schedule.add_interval(None)

def test_interval_with_zero_duration_is_invalid() -> None:
    """Test that intervals with zero duration raise InvalidIntervalError per requirements."""
    start = datetime(2023, 1, 1, 10, 0)
    end = datetime(2023, 1, 1, 10, 0)
    with pytest.raises(InvalidIntervalError):
        Interval(start, end)