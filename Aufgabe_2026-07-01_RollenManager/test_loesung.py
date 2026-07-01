import pytest
from typing import Set
# Annahme: Die Implementierung befindet sich in einer Datei namens loesung.py
from loesung import RollenManager

def test_zuweisen_gueltig() -> None:
    """Testet die Zuweisung einer Rolle zu einer Identität."""
    rm = RollenManager()
    rm.zuweisen("user123", "admin")
    assert rm.pruefen("user123", "admin") is True

def test_zuweisen_duplikat() -> None:
    """Testet, dass das mehrfache Zuweisen derselben Rolle keine Duplikate erzeugt (Idempotenz)."""
    rm = RollenManager()
    rm.zuweisen("user123", "admin")
    rm.zuweisen("user123", "admin")
    assert len(rm.abrufen("user123")) == 1

def test_zuweisen_leer_oder_none() -> None:
    """Testet, dass das Zuweisen von leeren Strings oder None-Werten fehlschlägt (Defensives Programmieren)."""
    rm = RollenManager()
    invalid_inputs = [("", "admin"), ("user123", ""), (None, "admin"), ("user123", None)]
    for ident, rolle in invalid_inputs:
        with pytest.raises(ValueError):
            rm.zuweisen(ident, rolle)

def test_entfernen_gueltig() -> None:
    """Testet das Entfernen einer existierenden Rolle."""
    rm = RollenManager()
    rm.zuweisen("user123", "admin")
    rm.entfernen("user123", "admin")
    assert rm.pruefen("user123", "admin") is False

def test_entfernen_identitaet_nicht_vorhanden() -> None:
    """Testet das Entfernen einer Rolle von einer Identität, die nicht existiert."""
    rm = RollenManager()
    with pytest.raises(KeyError):
        rm.entfernen("user123", "admin")

def test_entfernen_rolle_nicht_zugewiesen() -> None:
    """Testet das Entfernen einer Rolle, die der Identität nicht zugewiesen ist."""
    rm = RollenManager()
    rm.zuweisen("user123", "admin")
    with pytest.raises(KeyError):
        rm.entfernen("user123", "editor")

def test_pruefen_nicht_vorhandene_identitaet() -> None:
    """Testet die Prüfung einer Rolle für eine Identität, die nicht existiert."""
    rm = RollenManager()
    assert rm.pruefen("user123", "admin") is False

def test_abrufen_nicht_vorhandene_identitaet() -> None:
    """Testet das Abrufen aller Rollen einer Identität, die nicht existiert."""
    rm = RollenManager()
    result = rm.abrufen("user123")
    assert isinstance(result, set)
    assert len(result) == 0

def test_abrufen_leere_identitaet() -> None:
    """Testet das Abrufen aller Rollen einer Identität, die keine Rollen hat."""
    rm = RollenManager()
    rm.zuweisen("user123", "admin")
    rm.entfernen("user123", "admin")
    result = rm.abrufen("user123")
    assert isinstance(result, set)
    assert len(result) == 0

def test_pruefen_leer_oder_none() -> None:
    """Testet die Prüfung mit leerem String oder None-Wert."""
    rm = RollenManager()
    with pytest.raises(ValueError):
        rm.pruefen("", "admin")
    with pytest.raises(ValueError):
        rm.pruefen("user123", "")
    with pytest.raises(ValueError):
        rm.pruefen(None, "admin")
    with pytest.raises(ValueError):
        rm.pruefen("user123", None)

def test_abrufen_leer_oder_none() -> None:
    """Testet das Abrufen mit leerem String oder None-Wert."""
    rm = RollenManager()
    with pytest.raises(ValueError):
        rm.abrufen("")
    with pytest.raises(ValueError):
        rm.abrufen(None)

def test_zuweisen_mehrere_rollen() -> None:
    """Testet das Zuweisen mehrerer Rollen an dieselbe Identität."""
    rm = RollenManager()
    rm.zuweisen("user123", "admin")
    rm.zuweisen("user123", "editor")
    rm.zuweisen("user123", "viewer")
    assert len(rm.abrufen("user123")) == 3
    assert rm.pruefen("user123", "admin") is True
    assert rm.pruefen("user123", "editor") is True
    assert rm.pruefen("user123", "viewer") is True

def test_zuweisen_und_entfernen_mischung() -> None:
    """Testet das Mischen von Zuweisungen und Entfernungen."""
    rm = RollenManager()
    rm.zuweisen("user123", "admin")
    rm.zuweisen("user123", "editor")
    rm.entfernen("user123", "admin")
    assert len(rm.abrufen("user123")) == 1
    assert rm.pruefen("user123", "admin") is False
    assert rm.pruefen("user123", "editor") is True

def test_immutabilitaet_rueckgabewerte() -> None:
    """Testet, dass Rückgabewerte nicht modifizierbar sind."""
    rm = RollenManager()
    rm.zuweisen("user123", "admin")
    result = rm.abrufen("user123")
    original_len = len(result)
    try:
        result.add("editor")  # Versuch, die Menge zu modifizieren
    except AttributeError:
        pass  # Erwartet, da Sets unveränderbar sein sollten
    assert len(rm.abrufen("user123")) == original_len