# Netzwerk-Protokoll-Parser

Du bist als Softwareentwickler für ein Netzwerk-Analyzer-System tätig. Deine Aufgabe ist es, einen Parser für ein spezifisches Protokoll zu implementieren, das in einer Datei gespeicherte Netzwerkdatenpakete analysiert.

Das Protokoll verwendet folgende Formatierung:

- Jede Zeile ist ein Datensatz
- Datensätze sind durch Semikolon getrennt
- Die Felder sind: `timestamp`, `source_ip`, `destination_ip`, `protocol`, `port`, `size`, `status`
- `timestamp` ist im Format `YYYY-MM-DD HH:MM:SS`
- `source_ip` und `destination_ip` sind IPv4-Adressen
- `protocol` ist ein String (z.B. `TCP`, `UDP`)
- `port` ist eine Zahl
- `size` ist die Größe des Pakets in Bytes
- `status` ist ein String (`OK`, `ERROR`, `WARNING`)

## Anforderungen

Implementiere folgende Funktionen:

1. `parse_network_log(log_file_path: str) -> list[dict]`
   - Liest die Datei und gibt eine Liste von Dictionaries mit den geparsten Daten zurück
   - Jedes Dictionary enthält die Keys: `timestamp`, `source_ip`, `destination_ip`, `protocol`, `port`, `size`, `status`
   - Die Werte müssen korrekt typisiert sein (z.B. `port` und `size` als Integer)
   - Fehlerhafte Zeilen sollen übersprungen werden

2. `filter_by_protocol(log_data: list[dict], protocol: str) -> list[dict]`
   - Filtert die Logdaten nach dem angegebenen Protokoll

3. `get_statistics(log_data: list[dict]) -> dict`
   - Gibt eine Zusammenfassung der Logdaten zurück mit folgenden Keys:
     - `total_packets`: Anzahl der Pakete
     - `protocol_distribution`: Dictionary mit der Anzahl der Pakete pro Protokoll
     - `total_bytes`: Summe aller Paketgrößen
     - `error_packets`: Anzahl der Pakete mit Status `ERROR`

## Edge-Cases

- Leere Zeilen sollen übersprungen werden
- Zeilen mit fehlenden Feldern sollen übersprungen werden
- Ungültige IP-Adressen sollen übersprungen werden
- Ungültige Werte für `port` oder `size` sollen übersprungen werden
- Ungültige Timestamps sollen übersprungen werden
- `status` muss genau `OK`, `ERROR` oder `WARNING` sein

## Beispiel-Datei

```
2023-05-15 10:30:00;192.168.1.1;10.0.0.1;TCP;80;1024;OK
2023-05-15 10:30:01;192.168.1.2;10.0.0.2;UDP;53;512;ERROR
2023-05-15 10:30:02;192.168.1.3;10.0.0.3;TCP;443;2048;WARNING
2023-05-15 10:30:03;invalid_ip;10.0.0.4;TCP;80;1024;OK
2023-05-15 10:30:04;192.168.1.5;10.0.0.5;TCP;80;invalid_size;OK
```

## Hinweise

- Nutze `ipaddress` für IP-Validierung
- Nutze `datetime` für Timestamp-Validierung
- Verwende `try-except` für die Typkonvertierung
