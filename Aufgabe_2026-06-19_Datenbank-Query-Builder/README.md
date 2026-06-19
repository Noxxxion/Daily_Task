# Datenbank-Query-Builder

Du bist Teil eines Software-Teams, das eine interne Datenbankabfrage-Schnittstelle für eine Unternehmensanwendung entwickelt. Die Anwendung erfordert dynamische SQL-Abfragen, die auf Benutzereingaben basieren und gleichzeitig Sicherheitsaspekte wie SQL-Injection-Attacken verhindern müssen.

Deine Aufgabe ist es, eine Klasse `QueryBuilder` zu implementieren, die SQL-SELECT-Abfragen dynamisch aufbaut. Die Klasse soll folgende Funktionen unterstützen:

1. `select(*columns)` – Legt fest, welche Spalten ausgewählt werden.
2. `from_(table)` – Gibt an, aus welcher Tabelle gelesen wird.
3. `where(condition, *params)` – Fügt eine WHERE-Bedingung hinzu. Die Parameter müssen sicher eingefügt werden, um SQL-Injection zu verhindern.
4. `order_by(*columns)` – Sortiert das Ergebnis nach den angegebenen Spalten.
5. `limit(n)` – Begrenzt die Anzahl der Ergebnisse auf `n`.
6. `build()` – Erstellt den finalen SQL-String.

Die Abfragen müssen folgende Anforderungen erfüllen:

- Die WHERE-Bedingungen werden mit Parametern aufgebaut, um SQL-Injection zu verhindern.
- Die Abfrage muss sichere Platzhalter für Parameter verwenden (z.B. `?` oder `%s`).
- Die Klasse soll eine Methode `__str__()` implementieren, die den SQL-String zurückgibt, wenn die Klasse als String verwendet wird.

Beachte folgende Edge-Cases:

- Wenn keine Spalten in `select()` angegeben sind, soll `*` verwendet werden.
- Wenn keine Tabelle in `from_()` angegeben ist, soll eine `ValueError` geworfen werden.
- Wenn `where()` aufgerufen wird, ohne dass `from_()` zuvor aufgerufen wurde, soll eine `ValueError` geworfen werden.
- Wenn `order_by()` mit leerer Liste aufgerufen wird, soll keine ORDER-Bedingung hinzugefügt werden.
- Wenn `limit()` mit einem Wert kleiner als 1 aufgerufen wird, soll eine `ValueError` geworfen werden.

## Beispiel:

```python
query = QueryBuilder()
query.select("name", "age")
query.from_("users")
query.where("age > ?", 18)
query.order_by("age", "name")
query.limit(10)
print(query)
```

Sollte folgende Ausgabe erzeugen:

```sql
SELECT name, age FROM users WHERE age > ? ORDER BY age, name LIMIT 10
```

## Hinweis:

Verwende keine externe Bibliothek zur SQL-Generierung. Implementiere die gesamte Logik selbst.