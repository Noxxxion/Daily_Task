import pytest
from typing import List, Optional
from loesung import calculate_net_payment, InvalidInputException


def test_empty_amounts_list():
    """Test calculation with an empty list of amounts."""
    result = calculate_net_payment([], 10.0, 5.0)
    assert result == 0.0


def test_positive_values():
    """Test calculation with positive values. Corrected assertion: (300-50)*0.9 = 225."""
    result = calculate_net_payment([100.0, 200.0], 50.0, 10.0)
    assert result == 225.0


def test_flat_fee_larger_than_total():
    """Test behavior when flat fee exceeds total amount."""
    result = calculate_net_payment([10.0, 20.0], 40.0, 5.0)
    assert result == 0.0


def test_zero_commission_rate():
    """Test calculation with zero commission rate."""
    result = calculate_net_payment([100.0], 10.0, 0.0)
    assert result == 90.0


def test_negative_amounts():
    """Test that negative amounts raise an exception."""
    with pytest.raises(InvalidInputException):
        calculate_net_payment([-10.0], 5.0, 5.0)


def test_negative_flat_fee():
    """Test that negative flat fee raises an exception."""
    with pytest.raises(InvalidInputException):
        calculate_net_payment([100.0], -5.0, 5.0)


def test_invalid_commission_rate():
    """Test that commission rate outside [0, 100] raises an exception."""
    with pytest.raises(InvalidInputException):
        calculate_net_payment([100.0], 10.0, 105.0)

    with pytest.raises(InvalidInputException):
        calculate_net_payment([100.0], 10.0, -5.0)


def test_non_numeric_input():
    """Test that non-numeric inputs and None values raise an exception."""
    # Strings
    with pytest.raises(InvalidInputException):
        calculate_net_payment(["100"], 10.0, 5.0)

    with pytest.raises(InvalidInputException):
        calculate_net_payment([100.0], "10", 5.0)

    with pytest.raises(InvalidInputException):
        calculate_net_payment([100.0], 10.0, "5")

    # None values in list
    with pytest.raises(InvalidInputException):
        calculate_net_payment([100.0, None, 20.0], 10.0, 5.0)


def test_none_as_parameters():
    """Test that None as a parameter for fee or rate raises an exception."""
    with pytest.raises(InvalidInputException):
        calculate_net_payment([100.0], None, 5.0)  # type: ignore

    with pytest.raises(InvalidInputException):
        calculate_net_payment([100.0], 10.0, None)  # type: ignore


def test_precision_with_many_small_values():
    """Test precision with many small values."""
    small_amounts = [0.01] * 1000
    result = calculate_net_payment(small_amounts, 1.0, 2.0)
    expected = (10.0 - 1.0) * (1 - 0.02)
    assert abs(result - expected) < 1e-10


def test_exact_zero_total():
    """Test calculation when total amount is exactly zero."""
    result = calculate_net_payment([0.0, 0.0], 0.0, 5.0)
    assert result == 0.0


def test_large_numbers():
    """Test with large numbers to ensure no overflow issues."""
    result = calculate_net_payment([1e6, 2e6], 1e5, 3.5)
    expected = (3e6 - 1e5) * (1 - 0.035)
    assert result == expected


def test_commission_rate_exactly_100():
    """Test commission rate exactly at 100%."""
    result = calculate_net_payment([100.0], 10.0, 100.0)
    assert result == 0.0


def test_commission_rate_exactly_0():
    """Test commission rate exactly at 0%."""
    result = calculate_net_payment([100.0], 10.0, 0.0)
    assert result == 90.0
