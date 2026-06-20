# ConfigMerger - Aufgabenbeschreibung

## Ziel der Aufgabe
Implementiere eine Funktion `merge_configs`, die zwei Konfigurationsobjekte (Dictionary) zusammenführt. Dabei haben Werte aus dem zweiten Objekt Vorrang vor Werten aus dem ersten. Die Funktion soll rekursiv arbeiten, um verschachtelte Konfigurationen korrekt zusammenzufügen.

## Funktionale Anforderungen
- Die Funktion `merge_configs(config1: dict, config2: dict) -> dict` nimmt zwei Dictionary-Objekte entgegen.
- Werte aus `config2` überschreiben Werte aus `config1` bei identischen Schlüsseln.
- Bei verschachtelten Dictionaries wird die Merge-Logik rekursiv angewandt.
- Die Funktion muss sicher mit leeren oder None-Werten umgehen.
- Die Funktion darf keine Auswirkungen auf die ursprünglichen Eingabedaten haben (deep copy).

## Edge-Cases und Spezifikationen
- **Leere Eingaben**: `merge_configs({}, {})` sollte `{}` zurückgeben.
- **None-Werte**: `merge_configs(None, {})` und `merge_configs({}, None)` sollten jeweils ein leeres Dictionary zurückgeben.
- **Ungültige Datentypen**: Wenn eines der Argumente kein Dictionary ist, sollte eine `TypeError`-Exception geworfen werden.
- **Verschachtelte Strukturen**: Verschachtelte Dictionary-Objekte müssen rekursiv zusammengeführt werden.
- **Mischung von Typen**: Wenn ein Schlüssel in beiden Konfigurationen verschiedene Typen hat (z.B. ein String in `config1` und ein Dictionary in `config2`), sollte `config2` Vorrang haben.

## Beispiele

```python
config1 = {"a": 1, "b": {"c": 2, "d": 3}}
config2 = {"b": {"c": 4}, "e": 5}
result = merge_configs(config1, config2)
# Erwartet: {"a": 1, "b": {"c": 4, "d": 3}, "e": 5}
```

```python
config1 = {"a": 1}
config2 = {"a": 2}
result = merge_configs(config1, config2)
# Erwartet: {"a": 2}
```

## Hinweise
- Die Funktion sollte eine tiefe Kopie der Eingaben erstellen, um Seiteneffekte zu vermeiden.
- Die Rekursion muss korrekt mit verschachtelten Dictionaries umgehen.
- Fehlerbehandlung ist erforderlich, um sicherzustellen, dass nur Dictionary-Objekte übergeben werden.