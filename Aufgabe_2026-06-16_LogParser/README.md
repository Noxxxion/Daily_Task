# LogParser

Ein Unternehmen betreibt eine Webanwendung, die über ein Logging-System protokolliert. Die Logs werden in einer Datei gespeichert, wobei jede Zeile ein einzelnes Log-Ereignis darstellt. Jedes Log-Ereignis hat folgendes Format:

```
[YYYY-MM-DD HH:MM:SS] [LEVEL] [PID] [MESSAGE]
```

Beispiel:
```
[2023-10-15 14:30:45] [INFO] [1234] User login successful
[2023-10-15 14:31:22] [ERROR] [1234] Database connection failed
[2023-10-15 14:32:10] [DEBUG] [1235] Processing request
```

Die Aufgabe ist es, eine Python-Funktion zu implementieren, die eine Log-Datei liest und folgende Informationen extrahiert:

1. Anzahl der Einträge pro Log-Level (INFO, ERROR, DEBUG, WARN)
2. Die Anzahl der Einträge pro Prozess-ID (PID)
3. Die Anzahl der Einträge pro Tag

Außerdem soll eine Funktion zur Verfügung stehen, die nach einem bestimmten Suchbegriff in den Log-Meldungen sucht und die entsprechenden Einträge zurückgibt.

## Anforderungen

- Implementiere die Funktion `parse_log_file(file_path)`
- Implementiere die Funktion `search_logs(file_path, search_term)`
- Die Log-Datei kann leer sein oder fehlerhafte Einträge enthalten
- Fehlerhafte Log-Einträge sollen ignoriert werden
- Die Suchfunktion soll case-insensitive sein
- Die Ergebnisse sollen in Form von Dictionarys zurückgegeben werden

## Beispieldaten

```
[2023-10-15 14:30:45] [INFO] [1234] User login successful
[2023-10-15 14:31:22] [ERROR] [1234] Database connection failed
[2023-10-15 14:32:10] [DEBUG] [1235] Processing request
[2023-10-16 09:15:30] [WARN] [1236] Memory usage high
[2023-10-16 09:16:45] [INFO] [1234] User logout successful
[2023-10-16 09:17:00] [ERROR] [1237] File not found
```

## Edge-Cases

- Leere Log-Datei
- Log-Einträge mit fehlerhaftem Format
- Suchbegriff nicht gefunden
- Mehrere Suchbegriffe im selben Eintrag
