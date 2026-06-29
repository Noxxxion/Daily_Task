# ZeitplanStruktur

## Problemstellung
Im Rahmen der Entwicklung unserer neuen Ressourcenmanagement-Plattform steht die Implementierung einer Kernkomponente zur Verwaltung von Zeitintervallen an. Derzeit existiert keine standardisierte Logik, um zeitlich befristete Ereignisse (z. B. Termine, Wartungsfenster oder Schichtplanungen) konsistent zu erfassen und gegen logische Fehler zu validieren.

Das Hauptproblem besteht darin, dass unkontrollierte Eingaben von Zeitspannen zu Überschneidungen in der Ressourcenplanung führen können, was die Integrität der gesamten Planungsdatenbank gefährdet. Es wird eine modulare, leicht testbare Logik benötigt, welche die Definition, Validierung und die Prüfung auf zeitliche Kollisionen innerhalb einer strukturiert verwalteten Menge von Zeitintervallen übernimmt. Die Komponente muss als verlässliches Fundament für höherrangige Scheduling-Dienste dienen.

## Funktionale Anforderungen & Akzeptanzkriterien
- **Erstellung von Zeitintervallen**: Das System muss in der Lage sein, ein Zeitintervall aus einem eindeutigen Startzeitpunkt und einem eindeutigen Endzeitpunkt zu initialisieren.
- **Chronologische Validierung**: Bei der Erstellung eines Intervalls muss zwingend geprüft werden, dass der Startzeitpunkt zeitlich vor dem Endzeitpunkt liegt. Ein Verstoß gegen diese Regel führt zur Ablehnung des Objekts.
- **Kollisionsprüfung (Overlap Detection)**: Die Struktur muss eine Methode bereitstellen, die prüft, ob ein neu hinzugefügtes Intervall mit bereits existierenden Intervallen in der Sammlung kollidiert (Überschneidung von Zeitspannen).
- **Sortierte Bereitstellung**: Die Verwaltungskomponente muss die Fähigkeit besitzen, alle gespeicherten Intervalle in einer chronologisch aufsteigenden Reihenfolge (nach Startzeitpunkt) zurückzugeben.
- **Einhaltung der Software-Design-Richtlinien**:
    - **Encapsulation**: Der interne Zustand der Zeitplan-Struktur (die Liste der Intervalle) darf von außen nicht direkt manipulierbar sein; Änderungen müssen ausschließlich über definierte Methoden erfolgen.
    - **Single Responsibility Principle**: Die Logik zur Repräsentation eines einzelnen Intervalls muss strikt von der Logik zur Verwaltung der Sammlung getrennt sein.
    - **Exception Handling**: Für alle geschäftskritischen Fehler (z. B. ungültige Zeitspannen oder unerwünschte Überschneidungen) müssen spezifische, fachlich aussagekräftige Exceptions definiert und geworfen werden.
    - **Immutability**: Einmal erstellte Intervalle sollten nach Möglichkeit als unveränderliche Objekte behandelt werden, um Seiteneffekte bei der Berechnung zu vermeiden.

## Zu berücksende Edge-Cases
- **Null-/None-Werte**: Eingaben von leeren oder nicht definierten Zeitstempeln müssen abgefangen und durch eine entsprechende Fehlermeldung behandelt werden.
- **Identische Start- und Endpunkte**: Ein Intervall, bei dem Startzeitpunkt und Endzeitpunkt identisch sind (Dauer = 0), muss als ungültig markiert oder gemäß den Business-Regeln explizit ausgeschlossen werden.
- **Leere Datenstruktur**: Operationen auf einer initial leeren Zeitplan-Struktur (z. B. die Suche nach Überschneidungen) müssen ohne Systemabsturz und mit einem definierten Ergebnis (z. B. "keine Kollision") erfolgen.
- **Berührungslose Intervalle**: Es muss sichergestellt werden, dass ein Intervall, das exakt zum Endzeitpunkt eines anderen Intervalls endet, nicht fälscherweise als Überschneidung gewertet wird (Grenzwertprüfung).
- **Duplikate**: Das Hinzufügen eines identischen Zeitintervalls, das bereits in der Struktur existiert, muss durch die Validierungslogik erkannt werden.