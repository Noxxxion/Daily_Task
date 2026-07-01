import os
from typing import List, Dict, Set, Optional

class RollenManager:
    """
    Ein Rollenmanager zur Verwaltung von Rollenzuweisungen für Identitäten.
    
    Die Klasse kapselt die Zuweisung, Entfernung und Überprüfung von Rollen für verschiedene
    Identitäten (z. B. Benutzer-IDs, Service-Accounts). Sie gewährleistet die Integrität
    der Zuordnungen und verhindert Redundanzen.
    """
    
    def __init__(self) -> None:
        """
        Initialisiert einen neuen RollenManager mit leerem internen Zustand.
        
        Der interne Zustand ist ein Dictionary, das Identitäten auf Mengen von Rollen abbildet.
        """
        self._rollen_zuweisungen: Dict[str, Set[str]] = {}
    
    def zuweisen(self, identitaet: str, rolle: str) -> None:
        """
        Weist einer Identität eine Rolle zu.
        
        Args:
            identitaet (str): Die eindeutige Identität (z. B. Benutzer-ID).
            rolle (str): Die zuzuweisende Rolle.
            
        Raises:
            ValueError: Wenn identitaet oder rolle None oder leer sind.
        """
        pass
    
    def entfernen(self, identitaet: str, rolle: str) -> None:
        """
        Entfernt eine Rolle von einer Identität.
        
        Args:
            identitaet (str): Die Identität, von der die Rolle entfernt werden soll.
            rolle (str): Die zu entfernende Rolle.
            
        Raises:
            ValueError: Wenn identitaet oder rolle None oder leer sind.
            KeyError: Wenn die Identität nicht existiert oder die Rolle nicht zugewiesen ist.
        """
        pass
    
    def pruefen(self, identitaet: str, rolle: str) -> bool:
        """
        Prüft, ob eine Identität über eine bestimmte Rolle verfügt.
        
        Args:
            identitaet (str): Die Identität, die geprüft werden soll.
            rolle (str): Die Rolle, die geprüft werden soll.
            
        Returns:
            bool: True, wenn die Identität die Rolle besitzt, sonst False.
            
        Raises:
            ValueError: Wenn identitaet oder rolle None oder leer sind.
        """
        pass
    
    def abrufen(self, identitaet: str) -> Set[str]:
        """
        Ruft alle Rollen einer Identität ab.
        
        Args:
            identitaet (str): Die Identität, deren Rollen abgerufen werden sollen.
            
        Returns:
            Set[str]: Eine Menge aller Rollen der Identität. Gibt eine leere Menge zurück,
                      wenn die Identität nicht existiert oder keine Rollen hat.
                      
        Raises:
            ValueError: Wenn identitaet None oder leer ist.
        """
        pass