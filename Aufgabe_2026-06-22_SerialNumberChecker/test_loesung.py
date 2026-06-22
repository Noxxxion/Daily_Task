import pytest
from loesung import SerialNumberChecker

def test_is_valid_with_valid_serial_numbers():
    """Testet gültige Seriennummern"""
    checker = SerialNumberChecker()
    
    valid_numbers = [
        "ABC12345678901234567899",
        "XYZ987654321098765432100",
        "TEST123456789012345678901",
        "AB123456789012345678909"
    ]
    
    for number in valid_numbers:
        assert checker.is_valid(number) is True

def test_is_valid_with_invalid_serial_numbers():
    """Testet ungültige Seriennummern"""
    checker = SerialNumberChecker()
    
    invalid_numbers = [
        "AB12345678901234567890",  # Präfix zu kurz
        "ABC1234567890123456789",  # Zahlenfolge zu kurz
        "ABC1234567890123456789A", # Prüfziffer ist kein Digit
        "ABC123456789012345678901", # Zahlenfolge zu lang
        "",                         # Leere Zeichenkette
        "ABC12345678901234567890X", # Prüfziffer ist kein Digit
        "ABC1234567890123456789010", # Zahlenfolge zu lang
        "123456789012345678901234567890" # Kein Präfix
    ]
    
    for number in invalid_numbers:
        assert checker.is_valid