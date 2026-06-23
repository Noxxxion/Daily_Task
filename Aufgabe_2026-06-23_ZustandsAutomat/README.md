# Bestell-Zustandsmaschine

Diese Anwendung implementiert eine endliche Zustandsmaschine zur Verwaltung von Bestellzuständen gemäß festgelegter Geschäftsregeln.

## Zustände

Die Bestellung kann folgende Zustände durchlaufen:
- `ERSTELLT`: Die Bestellung wurde erstellt.
- `IN_BEARBEITUNG`: Die Bestellung wird bearbeitet.
- `VERSANDT`: Die Bestellung wurde versandt.
- `ABGESCHLOSSEN`: Die Bestellung ist abgeschlossen.
- `ABGEBROCHEN`: Die Bestellung wurde abgebrochen.

## Zustandsübergänge

Die folgenden Übergänge sind erlaubt:
- `ERSTELLT` → `IN_BEARBEITUNG`
- `IN_BEARBEITUNG` → `VERSANDT`
- `VERSANDT` → `ABGESCHLOSSEN`
- `ERSTELLT` → `ABGEBROCHEN`
- `IN_BEARBEITUNG` → `ABGEBROCHEN`

Alle anderen Übergänge sind nicht erlaubt und führen zu einer `InvalidTransitionError`.

## Implementierungsdetails

Die Zustandsmaschine ist so konzipiert, dass sie nur gültige Zustandsübergänge zulässt. Jeder Versuch, einen ungültigen Zustand zu erreichen, löst eine Ausnahme aus.

### Klasse `OrderState`

Diese Klasse definiert die möglichen Zustände als Klassenkonstanten.

### Klasse `InvalidTransitionError`

Eine benutzerdefinierte Ausnahme, die geworfen wird, wenn ein ungültiger Zustandsübergang versucht wird.

### Klasse `OrderStateMachine`

Die Hauptklasse zur Verwaltung der Bestellzustände. Sie verwaltet den aktuellen Zustand und erlaubt nur gültige Übergänge.

#### Methoden

- `__init__(self, initial_state: str)`: Initialisiert die Zustandsmaschine mit einem Startzustand.
- `transition_to(self, target_state: str) -> None`: Führt einen Zustandsübergang durch, wenn er gültig ist.
- `get_current_state(self) -> str`: Gibt den aktuellen Zustand zurück.

## Beispiel

```python
from order_state_machine import OrderStateMachine, OrderState

# Erstelle eine neue Bestellung im Zustand "ERSTELLT"
order = OrderStateMachine(OrderState.ERSTELLT)

# Übergang zu "IN_BEARBEITUNG"
order.transition_to(OrderState.IN_BEARBEITUNG)

# Aktueller Zustand
print(order.get_current_state())  # Gibt "IN_BEARBEITUNG" aus

# Übergang zu "VERSANDT"
order.transition_to(OrderState.VERSANDT)

# Übergang zu "ABGESCHLOSSEN"
order.transition_to(OrderState.ABGESCHLOSSEN)
```

## Fehlerbehandlung

Wenn ein ungültiger Zustandsübergang versucht wird, wird eine `InvalidTransitionError` ausgelöst.