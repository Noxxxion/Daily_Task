import os
from typing import List, Optional

class TextFragmenter:
    """
    Ein TextFragmenter-Modul zur Zerlegung von Textblöcken anhand definierter Trennzeichen.
    
    Die Komponente ermöglicht die Fragmentierung von Texten in atomare Segmente,
    wobei automatisch Whitespaces bereinigt und leere Segmente gefiltert werden.
    """
    
    def __init__(self) -> None:
        """Initialisiert einen neuen TextFragmenter."""
        pass
    
    def fragment(self, text: str, delimiter: str) -> List[str]:
        """
        Zerlegt einen Text anhand eines einzelnen Trennzeichens in Fragment-Strings.
        
        Args:
            text (str): Der zu zerlegende Text.
            delimiter (str): Das Trennzeichen für die Fragmentierung.
            
        Returns:
            List[str]: Eine Liste der Fragment-Strings, bereinigt und ohne leere Einträge.
            
        Raises:
            ValueError: Wenn der Text None ist oder das Trennzeichen leer ist.
        """
        pass
    
    def fragment_multiple(self, text: str, delimiters: List[str]) -> List[str]:
        """
        Zerlegt einen Text anhand mehrerer Trennzeichen in Fragment-Strings.
        
        Args:
            text (str): Der zu zerlegende Text.
            delimiters (List[str]): Eine Liste von Trennzeichen für die Fragmentierung.
            
        Returns:
            List[str]: Eine Liste der Fragment-Strings, bereinigt und ohne leere Einträge.
            
        Raises:
            ValueError: Wenn der Text None ist oder eine leere Liste von Trennzeichen übergeben wird.
        """
        pass