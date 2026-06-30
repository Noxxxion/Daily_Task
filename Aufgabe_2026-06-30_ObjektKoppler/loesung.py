import os
from typing import List, Dict, Set, Optional, Any, Union

class ObjectCouplingError(Exception):
    """Benutzerdefinierte Exception für Fehler bei der Objekt-Kopplung."""
    pass

class KeyAttributeNotFoundError(ObjectCouplingError):
    """Exception, die geworfen wird, wenn ein benötigtes Schlüsselattribut nicht gefunden wurde."""
    pass

class IncompatibleKeyTypesError(ObjectCouplingError):
    """Exception, die geworfen wird, wenn die Typen der Schlüssel nicht kompatibel sind."""
    pass

class NullKeyError(ObjectCouplingError):
    """Exception, die geworfen wird, wenn ein Schlüsselwert None oder null ist."""
    pass

class CouplingResult:
    """
    Repräsentiert das Ergebnis einer erfolgreichen Kopplung zweier Objekte.
    
    Attributes:
        left_object: Das erste ursprüngliche Objekt.
        right_object: Das zweite ursprüngliche Objekt.
        key_attribute: Der gemeinsame Schlüssel, der zur Kopplung verwendet wurde.
        key_value: Der Wert des gemeinsamen Schlüssels.
    """
    
    def __init__(self, left_object: Dict[str, Any], right_object: Dict[str, Any], 
                 key_attribute: str, key_value: Union[str, int, float]) -> None:
        self.left_object = left_object
        self.right_object = right_object
        self.key_attribute = key_attribute
        self.key_value = key_value

def couple_objects(left_object: Dict[str, Any], right_object: Dict[str, Any], 
                   key_attribute: str) -> CouplingResult:
    """
    Kopplt zwei Objekte basierend auf einem gemeinsamen Schlüsselattribut.
    
    Args:
        left_object: Das erste Objekt als Dictionary.
        right_object: Das zweite Objekt als Dictionary.
        key_attribute: Der Name des Schlüsselattributs, das in beiden Objekten vorhanden sein muss.
        
    Returns:
        Ein CouplingResult-Objekt mit den kopplten Objekten und dem gemeinsamen Schlüssel.
        
    Raises:
        KeyAttributeNotFoundError: Wenn das Schlüsselattribut in einem der Objekte fehlt.
        IncompatibleKeyTypesError: Wenn die Typen der Schlüsselwerte nicht kompatibel sind.
        NullKeyError: Wenn einer der Schlüsselwerte None oder null ist.
    """
    pass

def couple_object_lists(left_objects: List[Dict[str, Any]], 
                        right_objects: List[Dict[str, Any]], 
                        key_attribute: str) -> List[CouplingResult]:
    """
    Kopplt zwei Listen von Objekten basierend auf einem gemeinsamen Schlüsselattribut.
    
    Args:
        left_objects: Liste der ersten Objekte als Dictionarys.
        right_objects: Liste der zweiten Objekte als Dictionarys.
        key_attribute: Der Name des Schlüsselattributs, das in beiden Objekten vorhanden sein muss.
        
    Returns:
        Eine Liste von CouplingResult-Objekten mit den kopplten Objekten und dem gemeinsamen Schlüssel.
        
    Raises:
        KeyAttributeNotFoundError: Wenn das Schlüsselattribut in einem der Objekte fehlt.
        IncompatibleKeyTypesError: Wenn die Typen der Schlüsselwerte nicht kompatibel sind.
        NullKeyError: Wenn einer der Schlüsselwerte None oder null ist.
    """
    pass