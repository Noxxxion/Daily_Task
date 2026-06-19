# Die finalen, korrigierten und absolut robusten pytest-Funktionen

import pytest
from loesung import is_valid_token

def test_valid_token():
    """Testet gültige Tokens."""
    assert is_valid_token("ABC-123-DEF") == True
    assert is_valid_token("XYZ-456-UVW") == True
    assert is_valid_token("AAA-000-BBB") == True

def test_invalid_token_format():
    """Testet ungültige Token-Formate."""
    assert is_valid_token("abc-123-DEF") == False  # Kleine Buchstaben
    assert is_valid_token("AB-123-DEF") == False   # Zu kurz
    assert is_valid_token("ABC-12-DEF") == False   # Zu kurz
    assert is_valid_token("ABC-123-DE") == False   # Zu kurz
    assert is_valid_token("ABC-123-DEF-123") == False  # Zu viele Teile
    assert is_valid_token("ABC-123") == False      # Zu wenig Teile
    assert is_valid_token("ABC-123-DEF-GHI") == False  # Zu viele Teile
    assert is_valid_token("ABC 123 DEF") == False  # Leerzeichen statt Bindestrich
    assert is_valid_token("ABC--123-DEF") == False  # Doppelte Bindestriche
    assert is_valid_token("ABC-123--DEF") == False  # Doppelte Bindestriche

def test_empty_and_none():
    """Testet leere und None-Werte."""
    assert is_valid_token("") == False
    assert is_valid_token(None) == False

def test_non_string_types():
    """Testet nicht-string Datentypen."""
    assert is_valid_token(123) == False
    assert is_valid_token([]) == False
    assert is_valid_token({}) == False
    assert is_valid_token(True) == False

def test_whitespace_handling():
    """Testet Umgang mit Leerzeichen."""
    assert is_valid_token("ABC-123-DEF ") == False  # Leerzeichen am Ende
    assert is_valid_token(" ABC-123-DEF") == False  # Leerzeichen am Anfang
    assert is_valid_token("ABC 123 DEF") == False  # Leerzeichen in Teilen

def test_special_characters():
    """Testet Sonderzeichen."""
    assert is_valid_token("ABC-123-DEF!") == False  # Sonderzeichen
    assert is_valid_token("ABC-123-DEF@") == False  # Sonderzeichen
    assert is_valid_token("ABC-123-DEF#") == False  # Sonderzeichen
    assert is_valid_token("ABC-123-DEF$") == False  # Sonderzeichen

def test_edge_cases():
    """Testet weitere Edge-Cases."""
    assert is_valid_token("   ") == False  # Nur Leerzeichen
    assert is_valid_token("A1C-123-DEF") == False  # Erster Teil enthält Zahl
    assert is_valid_token("ABC-123-DE4") == False  # Dritter Teil enthält Zahl
    assert is_valid_token("ABC-12A-DEF") == False  # Zweiter Teil enthält Buchstabe