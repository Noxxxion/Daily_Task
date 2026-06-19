# Die finale, korrigierte und präzise Markdown-Beschreibung der TokenValidierung

## Beschreibung
Implementiere eine Funktion zur Validierung von Tokens im Format `XYZ-123-ABC`, wobei die einzelnen Teile den folgenden Regeln entsprechen müssen:

1. **Erster Teil (XYZ)**: 
   - Muss aus genau 3 Großbuchstaben bestehen
   - Keine Leerzeichen oder Sonderzeichen erlaubt

2. **Zweiter Teil (123)**: 
   - Muss aus genau 3 Ziffern bestehen
   - Keine Leerzeichen oder Sonderzeichen erlaubt

3. **Dritter Teil (ABC)**: 
   - Muss aus genau 3 Großbuchstaben bestehen
   - Keine Leerzeichen oder Sonderzeichen erlaubt

## Anforderungen
- Die Funktion `is_valid_token(token)` soll einen Boolean zurückgeben
- Ungültige Eingaben (z.B. None, nicht-string Typen, falsche Länge) sollen als `False` gewertet werden
- Die Funktion muss robust gegenüber Edge-Cases sein

## Beispiele
- `is_valid_token("ABC-123-DEF")` → `True`
- `is_valid_token("abc-123-DEF")` → `False` (kleine Buchstaben)
- `is_valid_token("AB-123-DEF")` → `False` (zu kurz)
- `is_valid_token("ABC-12-DEF")` → `False` (zu kurz)
- `is_valid_token("ABC-123-DE")` → `False` (zu kurz)
- `is_valid_token("ABC-123-DEF-123")` → `False` (zu lang)
- `is_valid_token("")` → `False` (leer)
- `is_valid_token(None)` → `False` (None-Wert)
- `is_valid_token(123)` → `False` (nicht-string)
- `is_valid_token("ABC-123")` → `False` (zu wenig Teile)
- `is_valid_token("ABC-123-DEF-GHI")` → `False` (zu viele Teile)
- `is_valid_token("ABC-123-DEF ")` → `False` (Leerzeichen am Ende)
- `is_valid_token(" ABC-123-DEF")` → `False` (Leerzeichen am Anfang)

## Edge-Cases
- Leere Strings
- None-Werte
- Nicht-string Datentypen
- Strings mit Leerzeichen
- Ungültige Zeichen (kleine Buchstaben, Sonderzeichen, Leerzeichen)
- Falsche Anzahl an Teilen
- Falsche Länge der Teile
- Zeichen außerhalb der erlaubten Menge