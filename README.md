# Daily Coding Practice — Interactive LLM Challenge Pipeline

Dieses Repository ist ein vollautomatisiertes, interaktives Trainingssystem für Softwareentwicklung und Softwaretesting. Es fungiert als lokales "Duolingo für IT-Spezialisten", um die logischen und algorithmischen Fähigkeiten kontinuierlich zu fordern und zu fördern.

Das System generiert nicht mehr blind Aufgaben, sondern verwaltet den Lernfortschritt über eine Wissensdatenbank, bietet ein interaktives Auswahlmenü im Terminal und steuert die Lernkurve über ein Zwei-KI-System.

---

## Architektur und Funktionsweise

Die gesamte Pipeline läuft lokal auf eigener Hardware und ist in vier klare Phasen unterteilt:

### 1. Synchronisation & Inventur (Zustands-Erkennung)

- Beim Systemstart zieht das Skript via `git pull` den neuesten Stand von GitHub.
- Das Skript scannt die Festplatte nach Aufgabenordnern. Neue, unregistrierte Ordner werden automatisch migriert: Ein LLM-Prompt liest die `README.md` ein, bestimmt das Thema und extrahiert 3–5 spezifische technische Stichwörter (Tags).
- Das System führt im Hintergrund autonom `pytest` für alle ungelösten Aufgaben aus. Ist ein Test erfolgreich, wird der Status in der `progress_db.json` permanent von `"ungeloest"` auf `"geloest"` umgeschaltet.

### 2. Der Chef-Lehrer (Strategie-KI)

- Alle Tags von Aufgaben, die aktuell noch ungelöst auf der Festplatte liegen, werden temporär gesperrt.
- Eine KI-Instanz (Chef-Lehrer) analysiert die gesperrten Tags sowie die Historie aller bereits verwendeten Themen (Stories), um redundante Aufgaben zu vermeiden.
- Er generiert eine Auswahl aus exakt 3 neuen, vollkommen unterschiedlichen Fachgebieten (z. B. Kryptographie, Cloud-Infrastruktur oder Algorithmen), die keine gesperrten Tags enthalten.

### 3. Interaktive Benutzer-Eingabe (Gamification)

- Die Pipeline blockiert den Autostart und präsentiert dem Benutzer im Terminal ein formatiertes Auswahlmenü mit den 3 Vorschlägen und deren IT-Szenarien.
- Über eine fehlerabgesicherte Terminal-Eingabe (Tasten 1, 2 oder 3) wählt der Benutzer seine heutige Mission.

### 4. Der Coder & Deployment (Code-KI)

- Das große Code-Modell `qwen3-coder:30b` erhält das gewählte Thema und arbeitet die vollständige Challenge aus.
- **Qualitätssicherung**: Das Modell generiert die Aufgabe, ein Code-Gerüst, die Unittests (`pytest`) und eine Referenzlösung. Python testet die Referenzlösung im Hintergrund. Besteht sie den Test nicht, wird der Versuch verworfen und ein neuer Durchlauf gestartet (Self-Correction Loop).
- Nach erfolgreichem Test wird das leere Gerüst bereitgestellt und der Stand automatisch via SSH auf GitHub gepusht.

---

## Die Wissensdatenbank (`progress_db.json`)

Der Fortschritt wird in einer zentralen JSON-Datei protokolliert, die als Gedächtnis des Systems dient:

```json
{
  "letztes_update": "2026-06-19",
  "aktuelle_streak": 0,
  "aufgaben": {
    "Aufgabe_2026-06-16_LogParser": {
      "datum": "2026-06-16",
      "thema": "LogParser",
      "tags": ["string-parsing", "log-analysis", "file-processing"],
      "status": "ungeloest"
    }
  }
}
```

---

## Verzeichnisstruktur

Jede tägliche Aufgabe wird in einem eigenen Unterverzeichnis abgelegt:

```text
Aufgabe_YYYY-MM-DD_ThemenName/
├── README.md        # Ausführliche Aufgabenstellung, Anforderungen und Edge-Cases
├── loesung.py       # Das zu befüllende Code-Gerüst inklusive Type Hints
└── test_loesung.py  # Die automatisierten pytest-Test-Cases zur Validierung
```

---

## Workflow für das tägliche Training

1. **Repository aktualisieren**: `git pull origin main`
2. **PC-Start / Menü-Wahl**: Passphrase für den SSH-Key eingeben, im Menü die Option 1, 2 oder 3 wählen und Generierung abwarten.
3. **Aufgabe lösen**: Code in der `loesung.py` implementieren.
4. **Validieren**: Im Tagesordner `pytest` ausführen, bis alle Tests grün sind. Beim nächsten Systemstart wird die Aufgabe automatisch als gelöst verbucht.

---

## Technische Komponenten

- **Laufzeitumgebung**: Python 3.11 innerhalb einer Anaconda/Miniconda-Umgebung
- **Test-Framework**: `pytest` (konfiguriert ohne Cache-Provider zur Vermeidung von Windows-Dateisperren)
- **Infrastruktur**: Ollama (`ollama serve` im Hintergrundmodus via Batch-Steuerung)
- **LLM-Modell**: `qwen3-coder:30b` (ausgeführt auf einer NVIDIA RTX 4070 Ti SUPER via CUDA)
- **Authentifizierung**: Git über den Windows-eigenen OpenSSH-Agenten zur sicheren Session-Hinterlegung
