# Daily Coding Practice — Automated LLM Challenge Pipeline

Dieses Repository ist ein vollautomatisiertes Trainingssystem für Softwareentwicklung und Softwaretesting. Es fungiert als lokales "Duolingo für IT-Spezialisten", um die logischen und algorithmischen Fähigkeiten kontinuierlich zu fordern und zu fördern.

Täglich wird hier beim Systemstart eine neue, praxisnahe Programmieraufgabe inklusive einer automatisierten Testumgebung generiert.

---

## Architektur und Funktionsweise

Die gesamte Pipeline läuft lokal auf eigener Hardware und ist wie folgt aufgebaut:

1. **Windows-Autostart & Umgebung**: Beim Hochfahren des PCs triggert eine Batch-Datei (`.bat`) die Aktivierung der dedizierten Conda-Umgebung und startet den Windows-SSH-Agenten zur schlüssellosen Git-Authentifizierung.
2. **Lokales LLM (Ollama)**: Ein Python-Skript kommuniziert mit einer lokal laufenden Instanz von Ollama. Als Engine wird das Modell `qwen3-coder:30b` genutzt.
3. **Lernkurven-Tracker & Zustand**: Das Skript scannt vor der Generierung die bereits vorhandenen Aufgabenordner. Die Anzahl und die Themen der gelösten Aufgaben werden an das Modell übergeben, um Redundanzen zu vermeiden und die algorithmische Komplexität dynamisch zu steigern (Einstieg -> Fortgeschritten -> Experte).
4. **Automatisierte Qualitätskontrolle (CI/CD im Kleinen)**: 
   - Das LLM generiert im JSON-Format die Aufgabenstellung (Markdown), das Code-Grundgerüst (`loesung.py`), eine funktionierende Referenzlösung sowie eine Testdatei (`test_loesung.py`) für das Test-Framework `pytest`.
   - Das Skript testet die generierte Referenzlösung im Hintergrund autonom gegen die generierten Test-Cases.
   - Schlagen die Tests fehl oder ist das JSON fehlerhaft, wird der Versuch verworfen und das Modell korrigiert sich in einem neuen Durchlauf selbst (bis zu 5 Versuche).
5. **Deployment & Git-Automatisierung**: Nach erfolgreichem Selbsttest wird die Referenzlösung wieder entfernt, das leere Code-Gerüst für den Benutzer bereitgestellt und der neue Tagesordner mit einer dynamischen Commit-Nachricht automatisch via SSH auf GitHub gepusht.

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

Um eine neu gespawnte Aufgabe zu lösen, wird folgender Workflow angewendet:

1. **Repository aktualisieren**:
   ```bash
   git pull origin main
   ```
2. **Aufgabe analysieren**: Die `README.md` im jeweiligen Tagesordner lesen, um die fachlichen Anforderungen und Edge-Cases zu verstehen.
3. **Code implementieren**: Die Funktionen in der `loesung.py` mit der entsprechenden Programmierlogik befüllen.
4. **Tests ausführen**: Im Terminal in den Tagesordner wechseln und die Validierung starten:
   ```bash
   pytest
   ```
   Die Aufgabe gilt als gelöst, sobald alle Test-Cases erfolgreich von Rot auf Grün springen.

---

## Technische Komponenten des Projekts

- **Laufzeitumgebung**: Python 3.11 innerhalb einer Anaconda/Miniconda-Umgebung
- **Test-Framework**: `pytest` (konfiguriert ohne Cache-Provider zur Vermeidung von Windows-Dateisperren)
- **Infrastruktur**: Ollama (Server-Modus via `ollama serve`)
- **LLM-Modell**: `qwen3-coder:30b` (ausgeführt auf einer NVIDIA RTX 4070 Ti SUPER via CUDA)
- **Versionsverwaltung**: Git mit SSH-Agent-Integration für Passphrase-Hinterlegung
