# Die finalen, korrigierten und absolut robusten pytest-Funktionen...

import pytest
from loesung import merge_configs

def test_merge_configs_empty_dicts():
    """Testet das Zusammenführen leerer Dictionaries."""
    assert merge_configs({}, {}) == {}

def test_merge_configs_none_inputs():
    """Testet das Zusammenführen mit None-Eingaben."""
    assert merge_configs(None, {}) == {}
    assert merge_configs({}, None) == {}
    assert merge_configs(None, None) == {}

def test_merge_configs_simple_merge():
    """Testet das Zusammenführen einfacher Werte."""
    config1 = {"a": 1, "b": 2}
    config2 = {"b": 3, "c": 4}
    expected = {"a": 1, "b": 3, "c": 4}
    assert merge_configs(config1, config2) == expected

def test_merge_configs_nested_dicts():
    """Testet das Zusammenführen verschachtelter Dictionaries."""
    config1 = {"a": 1, "b": {"c": 2, "d": 3}}
    config2 = {"b": {"c": 4}, "e": 5}
    expected = {"a": 1, "b": {"c": 4, "d": 3}, "e": 5}
    assert merge_configs(config1, config2) == expected

def test_merge_configs_deep_nested():
    """Testet das Zusammenführen tief verschachtelter Dictionaries."""
    config1 = {"a": {"b": {"c": 1}}}
    config2 = {"a": {"b": {"c": 2, "d": 3}}}
    expected = {"a": {"b": {"c": 2, "d": 3}}}
    assert merge_configs(config1, config2) == expected

def test_merge_configs_overwrite_with_different_types():
    """Testet das Überschreiben mit unterschiedlichen Datentypen."""
    config1 = {"a": 1, "b": "string"}
    config2 = {"a": {"nested": "dict"}, "b": 2}
    expected = {"a": {"nested": "dict"}, "b": 2}
    assert merge_configs(config1, config2) == expected

def test_merge_configs_with_none_values():
    """Testet das Zusammenführen mit None-Werten."""
    config1 = {"a": None, "b": 1}
    config2 = {"a": 2, "c": None}
    expected = {"a": 2, "b": 1, "c": None}
    assert merge_configs(config1, config2) == expected

def test_merge_configs_invalid_input_type():
    """Testet das Werfen von TypeError bei ungültigen Eingabetypen."""
    with pytest.raises(TypeError):
        merge_configs("not_a_dict", {})
    
    with pytest.raises(TypeError):
        merge_configs({}, "not_a_dict")
    
    with pytest.raises(TypeError):
        merge_configs(123, {})
    
    with pytest.raises(TypeError):
        merge_configs({}, 123)

def test_merge_configs_original_dicts_unchanged():
    """Testet, dass die Original-Dictionaries nicht verändert werden."""
    config1 = {"a": 1, "b": {"c": 2}}
    config2 = {"b": {"d": 3}}
    
    original_config1 = {"a": 1, "b": {"c": 2}}
    original_config2 = {"b": {"d": 3}}
    
    merge_configs(config1, config2)
    
    assert config1 == original_config1
    assert config2 == original_config2

def test_merge_configs_complex_scenario():
    """Testet ein komplexes Zusammenführen mit mehreren Ebenen."""
    config1 = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "credentials": {
                "user": "admin",
                "password": "secret"
            }
        },
        "api": {
            "timeout": 30,
            "retries": 3
        }
    }
    config2 = {
        "database": {
            "port": 3306,
            "credentials": {
                "password": "newpass"
            }
        },
        "cache": {
            "enabled": True
        }
    }
    expected = {
        "database": {
            "host": "localhost",
            "port": 3306,
            "credentials": {
                "user": "admin",
                "password": "newpass"
            }
        },
        "api": {
            "timeout": 30,
            "retries": 3
        },
        "cache": {
            "enabled": True
        }
    }
    
    assert merge_configs(config1, config2) == expected

def test_merge_configs_single_level():
    """Testet Zusammenführen auf einfacher Ebene."""
    config1 = {"key1": "value1", "key2": "value2"}
    config2 = {"key2": "new_value", "key3": "value3"}
    result = merge_configs(config1, config2)
    assert result["key1"] == "value1"
    assert result["key2"] == "new_value"
    assert result["key3"] == "value3"

def test_merge_configs_deep_copy_behavior():
    """Testet, dass verschachtelte Objekte nicht referenziert werden."""
    config1 = {"a": {"b": {"c": 1}}}
    config2 = {"a": {"b": {"d": 2}}}
    
    result = merge_configs(config1, config2)
    
    # Ändere das Original, um sicherzustellen, dass result nicht beeinflusst wird
    config1["a"]["b"]["c"] = 999
    
    assert result["a"]["b"]["c"] == 1
    assert result["a"]["b"]["d"] == 2
    assert "c" in result["a"]["b"]
    assert "d" in result["a"]["b"]
    assert result["a"]["b"]["d"] == 2
    assert result["a"]["b"]["c"] == 1

def test_merge_configs_mixed_types():
    """Testet Zusammenführen mit gemischten Datentypen."""
    config1 = {"a": 1, "b": [1, 2, 3], "c": "string"}
    config2 = {"a": 2, "b": [4, 5], "d": {"nested": "dict"}}
    expected = {"a": 2, "b": [4, 5], "c": "string", "d": {"nested": "dict"}}
    assert merge_configs(config1, config2) == expected