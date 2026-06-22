# SerialNumberChecker - Aufgabenbeschreibung

## Ziel der Aufgabe
Implementiere eine Klasse `SerialNumberChecker`, die Seriennummern auf korrektes Format prüft. Die Seriennummer soll aus einem Präfix, einer alphanumerischen Zahlenfolge und einer Prüfziffer bestehen.

## Funktionale Anforderungen

Die Seriennummer muss folgende Struktur haben:
1. **Präfix**: Ein String mit mindestens 2 Zeichen, maximal 10 Zeichen
2. **Zahlenfolge**: Eine alphanumerische Zeichenkette mit mindestens 5 Zeichen, maximal 20 Zeichen
3. **Prüfziffer**: Eine einzelne Ziffer (0-9), die als letztes Zeichen der Seriennummer steht

Die Seriennummer soll folgendes Format haben: `PRÄFIXZAHLENFOLGEPRÜFZIFFER`

Beispiele für gültige Seriennummern:
- `ABC12345678901234567899`
- `XYZ987654321098765432100`

Beispiele für ungültige Seriennummern:
- `AB12345678901234567890` (Präfix zu kurz)
- `ABC1234567890123456789` (Zahlenfolge zu kurz)
- `ABC1234567890123456789A` (Prüfziffer ist kein Digit)
- `ABC123456789012345678901` (Zahlenfolge zu lang)

## Technische Anforderungen

Die Klasse `SerialNumberChecker` muss folgende Methoden bereitstellen:
- `is_valid(serial_number: str) -> bool`: Prüft, ob eine Seriennummer gültig ist
- `parse(serial_number: str) -> dict`: Gibt ein Dictionary mit den aufgeteilten Komponenten zurück (Präfix, Zahlenfolge, Prüfziffer), wenn die Seriennummer gültig ist

## Edge-Cases und Spezifikationen

- Leere Strings oder `None` als Eingabe führen zu `False` bei `is_valid()` und sollten eine Exception bei `parse()` auslösen
- Ungültige Datentypen (z.B. Integer, Liste) sollten zu einer Exception führen
- Die Zahlenfolge darf sowohl Ziffern als auch Buchstaben enthalten
- Das Präfix darf keine Ziffern enthalten
- Die Prüfziffer muss genau eine Ziffer sein (0-9)
- Alle Zeichen außer der Prüfziffer müssen alphanumerisch sein

## Hinweise zur Implementierung

Die Implementierung sollte robust gegenüber fehlerhaften Eingaben sein und klare Fehlermeldungen liefern.

=== VORGABE ===
# Das finale, korrigierte Code-Grundgerüst für den Benutzer...

```python
class SerialNumberChecker:
    def is_valid(self, serial_number: str) -> bool:
        # Implementiere die Validierung hier
        pass

    def parse(self, serial_number: str) -> dict:
        # Implementiere das Parsen hier
        pass
```