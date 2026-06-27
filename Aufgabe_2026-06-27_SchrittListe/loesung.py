import os
from typing import List, Dict, Set, Optional

class Step:
    """
    Repräsentiert einen einzelnen Schritt in der SchrittListe.
    
    Jeder Schritt hat eine eindeutige ID, eine Beschreibung und einen Status.
    Der Status kann PENDING, IN_PROGRESS oder COMPLETED sein.
    """
    
    def __init__(self, step_id: str, description: str):
        """
        Initialisiert einen neuen Schritt.
        
        Args:
            step_id: Eindeutige Identifikation des Schritts
            description: Beschreibung des Schritts
            
        Raises:
            ValueError: Wenn step_id oder description leer sind
        """
        pass
    
    @property
    def step_id(self) -> str:
        """Gibt die eindeutige ID des Schritts zurück."""
        pass
    
    @property
    def description(self) -> str:
        """Gibt die Beschreibung des Schritts zurück."""
        pass
    
    @property
    def status(self) -> str:
        """Gibt den Status des Schritts zurück."""
        pass
    
    def start(self) -> None:
        """
        Setzt den Status des Schritts auf IN_PROGRESS.
        
        Raises:
            ValueError: Wenn der Schritt bereits abgeschlossen ist oder 
                        wenn der Status nicht korrekt geändert werden kann
        """
        pass
    
    def complete(self) -> None:
        """
        Setzt den Status des Schritts auf COMPLETED.
        
        Raises:
            ValueError: Wenn der Schritt noch nicht gestartet wurde oder
                        wenn der Status nicht korrekt geändert werden kann
        """
        pass

class StepList:
    """
    Verwaltet eine sequenzielle Liste von Schritten mit Statusverwaltung.
    
    Die Liste gewährleistet die Integrität der Abfolge und validiert 
    Zustandsübergänge gemäß der definierten Workflow-Logik.
    """
    
    def __init__(self, steps: List[Step]):
        """
        Initialisiert eine neue SchrittListe mit gegebenen Schritten.
        
        Args:
            steps: Liste von Step-Objekten
            
        Raises:
            ValueError: Wenn die Liste leer ist oder Duplikate enthält
        """
        pass
    
    def get_step(self, step_id: str) -> Optional[Step]:
        """
        Gibt den Schritt mit der gegebenen ID zurück.
        
        Args:
            step_id: Eindeutige Identifikation des Schritts
            
        Returns:
            Der entsprechende Step oder None, wenn nicht gefunden
        """
        pass
    
    def get_progress(self) -> float:
        """
        Berechnet den Fortschritt der Liste als Prozentsatz.
        
        Returns:
            Fortschritt in Prozent (0.0 bis 100.0)
            
        Raises:
            ValueError: Wenn die Liste leer ist
        """
        pass
    
    def get_completed_steps(self) -> int:
        """
        Gibt die Anzahl der abgeschlossenen Schritte zurück.
        
        Returns:
            Anzahl der COMPLETED Schritte
            
        Raises:
            ValueError: Wenn die Liste leer ist
        """
        pass