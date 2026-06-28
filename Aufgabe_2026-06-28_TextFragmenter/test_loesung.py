import pytest
from loesung import TextFragmenter

def test_fragment_single_delimiter() -> None:
    """Testet die Fragmentierung mit einem einzelnen Trennzeichen."""
    fragmenter = TextFragmenter()
    result = fragmenter.fragment("a,b,c", ",")
    assert result == ["a", "b", "c"]

def test_fragment_with_whitespace() -> None:
    """Testet die Bereinigung von Whitespaces in Fragmenten (AC 3)."""
    fragmenter = TextFragmenter()
    result = fragmenter.fragment(" a , b , c ", ",")
    assert result == ["a", "b", "c"]

def test_fragment_empty_string() -> None:
    """Testet die Verarbeitung eines leeren Strings (Edge Case)."""
    fragmenter = TextFragmenter()
    result = fragmenter.fragment("", ",")
    assert result == []

def test_fragment_none_input() -> None:
    """Testet das Verhalten bei None-Elegabe des Textes (Edge Case)."""
    fragmenter = TextFragmenter()
    with pytest.raises(ValueError):
        fragmenter.fragment(None, ",")

def test_fragment_empty_delimiter() -> None:
    """Testet das Verhalten bei leerem Trennzeichen (Edge Case)."""
    fragmenter = TextFragmenter()
    with pytest.raises(ValueError):
        fragmenter.fragment("a,b,c", "")

def test_fragment_no_delimiter_found() -> None:
    """Testet die Fragmentierung, wenn das Trennzeichen nicht gefunden wird (Edge Case)."""
    fragmenter = TextFragmenter()
    result = fragmenter.fragment("abc", ",")
    assert result == ["abc"]

def test_fragment_consecutive_delimiters() -> None:
    """Testet die Handhabung aufeinanderfolgender Trennzeichen (AC 4 / Edge Case)."""
    fragmenter = TextFragmenter()
    result = fragmenter.fragment("a,,b,,,c", ",")
    assert result == ["a", "b", "c"]

def test_fragment_only_delimiters() -> None:
    """Testet die Verarbeitung eines Strings, der nur aus Trennzeichen besteht (Edge Case)."""
    fragmenter = TextFragmenter()
    result = fragmenter.fragment(",,, , ,", ",")
    assert result == []

def test_fragment_multiple_delimiters() -> None:
    """Testet die Fragmentierung mit mehreren verschiedenen Trennzeichen (AC 2)."""
    fragmenter = TextFragmenter()
    result = fragmenter.fragment_multiple("a,b;c.d", [",", ";", "."])
    assert result == ["a", "b", "c", "d"]

def test_fragment_multiple_delimiters_empty_list() -> None:
    """Testet das Verhalten bei einer leeren Liste von Trennzeichen (Edge Case)."""
    fragmenter = TextFragmenter()
    with pytest.raises(ValueError):
        fragmenter.fragment_multiple("a,b,c", [])

def test_fragment_multiple_delimiters_none_input() -> None:
    """Testet das Verhalten bei None-Eingabe des Textes in fragment_multiple."""
    fragmenter = TextFragmenter()
    with pytest.raises(ValueError):
        fragmenter.fragment_multiple(None, [","])

def test_fragment_multiple_no_delimiter_found() -> None:
    """Testet die Fragmentierung mit mehreren Trennzeichen, wenn keines im Text existiert."""
    fragmenter = TextFragmenter()
    result = fragmenter.fragment_multiple("abc", [",", ";"])
    assert result == ["abc"]

def test_fragment_multiple_consecutive_delimiters() -> None:
    """Testet die Handhabung aufeinanderfolgender verschiedener Trennzeichen (AC 4)."""
    fragmenter = TextFragmenter()
    result = fragmenter.fragment_multiple("a,,b;;c..d", [",", ";", "."])
    assert result == ["a", "b", "c", "d"]