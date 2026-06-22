import os
from typing import Dict, Optional

class SerialNumberChecker:
    def __init__(self) -> None:
        pass

    def is_valid(self, serial_number: str) -> bool:
        """
        Prüft, ob eine Seriennummer gültig ist.
        
        Args:
            serial_number (str): Die zu prüfende Seriennummer
            
        Returns:
            bool: True, wenn die Seriennummer gültig ist, sonst False
        """
        # TODO: Implementierung
        pass

    def parse(self, serial_number: str) -> Dict[str, str]:
        """
        Zerlegt eine gültige Seriennummer in ihre Komponenten.
        
        Args:
            serial_number (str): Die zu zerlegende Seriennummer
            
        Returns:
            Dict[str, str]: Dictionary mit den Komponenten 'prefix', 'number_sequence', 'check_digit'
            
        Raises:
            ValueError: Wenn die Seriennummer ungültig ist
        """
        # TODO: Implementierung
        pass