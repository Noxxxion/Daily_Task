import pytest
from typing import List, Optional

# Annahme: Die Implementierung befindet sich in loesung.py
from loesung import bestands_vergleich

def test_leere_soll_liste():
    """AC 5 & Edge-Case: Wenn die Soll-Liste leer ist, muss das Ergebnis leer sein."""
    assert bestands_vergleich([], ["A", "B"]) == []

def test_leere_ist_liste():
    """Edge-Case: Wenn die Ist-Liste leer ist, sind alle Elemente der Soll-Liste fehlend."""
    assert bestands_vergleich(["A", "B"], []) == ["A", "B"]

def test_identische_listen():
    """AC 5 & Edge-Case: Identische Listen liefern eine leere Liste zurück."""
    assert bestands_vergleich(["A", "B"], ["A", "B"]) == []

def test_fehlende_elemente():
    """AC 2: Korrekte Identifikation der Differenz (Soll minus Ist)."""
    result = bestands_vergleich(["A", "B", "C"], ["A", "B"])
    assert "C" in result and len(result) == 1

def test_duplikate_in_soll_liste():
    """AC 3: Duplikate in der Soll-Liste dürfen das Ergebnis nicht verfälschen (Eindeutigkeit)."""
    result = bestands_vergleich(["A", "A", "B"], ["A"])
    assert result == ["B"]

def test_duplikate_in_ist_liste():
    """AC 3: Duplikate in der Ist-Liste dürfen das Ergebnis nicht verfälschen."""
    result = bestands_vergleich(["A", "B"], ["A", "A", "A"])
    assert result == ["B"]

def test_ordnungsunabhaengigkeit():
    """AC 4: Der Vergleich muss unabhängig von der Sortierung sein."""
    assert sorted(bestands_vergleich(["A", "B", "C"], ["C", "A"])) == sorted(["B"])
    assert sorted(bestands_vergleich(["C", "A", "B"], ["A", "B", "C"])) == []

def test_none_werte_filterung():
    """Edge-Case: None-Werte sind ungültige Identifikatoren und dürfen die Logik nicht korrumpieren."""
    # Die Anforderung besagt, None als ungültig zu behandeln. 
    # Das Ergebnis sollte nur valide, fehlende IDs enthalten.
    result = bestands_vergleich(["A", None, "B"], ["A", "C"])
    assert "B" in result
    assert None not in result
    assert len(result) == 1

def test_typfehler_eingabe():
    """Exception Handling: Nicht-iterierbare Eingaben müssen einen TypeError auslösen."""
    with pytest.raises(TypeError):
        bestands_vergleich(None, ["A"]) # type: ignore
    with pytest.raises(TypeError):
        bestands_vergleich(["A"], 123) # type: ignore

def test_typ_inkonsistenz_vergleichbar():
    """AC: Vergleichbare Typen (int/float) sollten funktionieren, sofern die Logik dies erlaubt."""
    # Wenn das System robust ist, erkennt es 1 == 1.0
    assert bestands_vergleich([1, 2], [1.0]) == [2]

def test_typ_inkonsistenz_nicht_vergleichbar():
    """AC: Expliziter Fehler bei nicht vergleichbaren Typen (z.B. String vs Liste/Objekt)."""
    # Ein Vergleich zwischen einem String und einer Liste als Element ist logisch unsinnig
    with pytest.raises((TypeError, ValueError)):
        bestands_vergleich(["A", "B"], [["A"]])