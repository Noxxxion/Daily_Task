# Datenbank-Query-Builder

Du bist Teil eines Teams, das eine Datenbankabfrage-Sprache für eine interne Anwendung entwickelt. Die Anwendung soll es ermöglichen, dynamisch SQL-Abfragen zu erstellen, die auf einer einfachen Datenbankstruktur basieren. Die Datenbank enthält eine Tabelle namens `users` mit folgenden Spalten: `id`, `name`, `email`, `age`, `department`, `salary`.

Deine Aufgabe ist es, einen Query-Builder zu implementieren, der folgende Funktionen unterstützt:

- `select(columns)` – Wählt Spalten aus
- `from_table(table)` – Gibt an, von welcher Tabelle gelesen werden soll
- `where(condition)` – Fügt eine WHERE-Bedingung hinzu
- `order_by(column, direction='asc')` – Sortiert nach einer Spalte (aufsteigend oder absteigend)
- `limit(count)` – Begrenzt die Anzahl der Ergebnisse
- `build()` – Erstellt den SQL-String

Die Abfragen müssen folgende Regeln einhalten:

1. Die Spaltennamen in `select` und `order_by` müssen in der Tabelle existieren.
2. Die WHERE-Bedingungen müssen in der Form `column operator value` sein, wobei `operator` eines der folgenden sein darf: `=`, `!=`, `>`, `<`, `>=`, `<=`, `LIKE`.
3. Die Werte in WHERE-Bedingungen müssen entweder Strings (in Anführungszeichen) oder Zahlen sein.
4. Die Sortierreihenfolge (`direction`) muss entweder `'asc'` oder `'desc'` sein.
5. Der Query-Builder soll eine Exception werfen, wenn ungültige Parameter übergeben werden.

## Beispiele

```python
query = QueryBuilder()
sql = query.select(['name', 'email']).from_table('users').where('age > 30').order_by('name').build()
# Soll folgende SQL-Abfrage erzeugen:
# SELECT name, email FROM users WHERE age > 30 ORDER BY name

query = QueryBuilder()
sql = query.select(['id', 'name']).from_table('users').where("name LIKE 'John%'").limit(5).build()
# Soll folgende SQL-Abfrage erzeugen:
# SELECT id, name FROM users WHERE name LIKE 'John%' LIMIT 5
```

## Edge-Cases

- `select` ohne Angabe von Spalten sollte alle Spalten auswählen (`*`)
- `where` ohne Bedingung sollte keine WHERE-Klausel erzeugen
- `order_by` ohne Angabe der Richtung sollte standardmäßig aufsteigend sortieren
- `limit` ohne Angabe sollte keine LIMIT-Klausel erzeugen

## Anforderungen

- Implementiere alle Methoden des QueryBuilders
- Verwende eine saubere und lesbare Implementierung
- Füge alle notwendigen Validierungen hinzu
- Die `build()`-Methode sollte einen vollständigen SQL-String zurückgeben
- Die Lösung muss alle Tests bestehen