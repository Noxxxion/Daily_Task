import os
from typing import Dict, Any, Optional

def merge_configs(config1: Optional[Dict[str, Any]], config2: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Führt zwei Konfigurationsobjekte zusammen, wobei Werte aus config2 Vorrang haben.
    
    Args:
        config1: Erste Konfiguration als Dictionary oder None
        config2: Zweite Konfiguration als Dictionary oder None
        
    Returns:
        Ein kombiniertes Dictionary mit Werten aus beiden Konfigurationen
        
    Raises:
        TypeError: Wenn eines der Argumente kein Dictionary ist
    """
    # TODO: Implementierung hier einfügen
    pass