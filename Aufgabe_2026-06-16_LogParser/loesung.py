from typing import Dict, List


def parse_log_file(file_path: str) -> Dict[str, Dict[str, int]]:
    """
    Parst eine Log-Datei und liefert Statistiken zu Log-Level, PID und Tag.

    Args:
        file_path: Pfad zur Log-Datei

    Returns:
        Dictionary mit Statistiken
    """

    log_level_count = {"INFO": 0, "ERROR": 0, "DEBUG": 0, "WARN": 0}
    pid_count: Dict[str, int] = {}
    date_count: Dict[str, int] = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # Log-Einträge haben das Format: [YYYY-MM-DD HH:MM:SS] [LOG_LEVEL] [PID] Message
            # Wir splitten die Zeile anhand von "] " und entfernen die vordere eckige Klammer bei den ersten drei Teilen
            parts = line.strip().split("] ")

            # Edge-Case: Ungültige Zeilen überspringen, die nicht das erwartete Format haben
            if len(parts) < 4:
                continue

            # Extrahieren der relevanten Informationen
            date_time = parts[0].lstrip("[")  # "2023-10-15 14:30:45"
            log_level = parts[1].lstrip("[")  # "INFO"
            pid = parts[2].lstrip("[")  # "1234"

            # Edge-Case: Log-Level, die nicht in unserem Zähler sind, überspringen
            if log_level in log_level_count:
                log_level_count[log_level] += 1

                # PID als reinen String-Key zählen
                pid_count[pid] = pid_count.get(pid, 0) + 1

                # Datum extrahieren: Wir nehmen einfach die ersten 10 Zeichen (YYYY-MM-DD)
                tag_string = date_time[:10]
                date_count[tag_string] = date_count.get(tag_string, 0) + 1

    return {
        "level_count": log_level_count,
        "pid_count": pid_count,
        "date_count": date_count,
    }


def search_logs(file_path: str, search_term: str) -> List[str]:
    """
    Durchsucht eine Log-Datei nach einem Suchbegriff.

    Args:
        file_path: Pfad zur Log-Datei
        search_term: Suchbegriff (case-insensitive)

    Returns:
        Liste der passenden Log-Einträge
    """
    # Wir machen die Suche case-insensitive, indem wir den Suchbegriff und die Zeile in Kleinbuchstaben umwandeln
    search_term_lower = search_term.lower()
    matching_entries: List[str] = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if search_term_lower in line.lower():
                matching_entries.append(line.strip())

    return matching_entries
