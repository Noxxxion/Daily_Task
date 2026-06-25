import os
from typing import List, Set, Optional

def bestands_vergleich(soll_liste: List[Optional[str]], ist_liste: List[Optional[str]]) -> List[str]:
    """
    Vergleicht zwei Listen von Identifikatoren (Soll- und Ist-Bestand) und gibt die fehlenden Elemente aus dem Soll-Bestand zurück.
    
    Args:
        soll_liste: Liste der Identifikatoren im Soll-Bestand (z. B. Artikelnummern).
        ist_liste: Liste der Identifikatoren im Ist-Bestand (z. B. gescannte Artikelnummern).
        
    Returns:
        Eine Liste der Identifikatoren, die im Soll-Bestand vorhanden sind, aber im Ist-Bestand fehlen.
        
    Raises:
        TypeError: Wenn eine der Eingaben keine iterierbare Struktur ist.
    """
    pass