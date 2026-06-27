# SchrittListe

## Problemstellung
In komplexen Geschäftsprozessen, wie beispielsweise der Onboarding-Phase neuer Mitarbeiter oder der Durchführung von Qualitätskontrollen in der Fertigung, ist die Einhaltung einer exakt definierten Abfolge von Arbeitsschritten kritisch für die Compliance und Prozessintegrität. Aktuell fehlt es an einer standardisierten Komponente, welche diese Sequenzen programmatisch verwaltet und sicherstellt, dass Schritte nicht übersprungen oder in einer unzulässigen Reihenfolge bearbeitet werden können.

Das Ziel der Entwicklung der 'SchrittListe' ist die Bereitstellung einer robusten Logik-Komponente, die eine Liste von sequenziellen Schritten kapselt. Diese Komponente muss die Integrität des Workflows garantieren, indem sie den Status jedes Schrittes verwaltet und Operationen verhindert, die die logische Abfolge der Prozesskette verletzen würden.

## Funktionale Anforderungen & Akzeptanzkriterien
- **Initialisierung und Struktur:** Die Komponente muss in der Lage sein, eine definierte Anzahl von Schritten zu initialisieren. Jeder Schritt muss eine eindeutige Identifikation und eine Beschreibung besitzen.
- **Sequenzielle Integrität:** Es muss sichergestellt werden, dass die Liste als strikt geordnete Sequenz behandelt wird. Operationen, die die logische Reihenfolge der bereits definierten Schritte verändern (außerhalb der zulässigen API), sind zu unterbinden.
- **Statusverwaltung:** Jeder Schritt innerhalb der Liste muss über einen Status verfügen (z. B. 'PENDING', 'IN_PROGRESS', 'COMPLETED'). Ein Wechsel des Status darf nur gemäß der vordefinierten Workflow-Logik erfolgen.
- **Validierung der Prozessfortschritte:** Das System muss eine Validierungslogik implementelle, die prüft, ob ein Schritt erst dann als 'COMPLETED' markiert werden kann, wenn der unmittelbar vorangehende Schritt ebenfalls den Status 'COMPLETED' aufweist.
- **Fortschrittsüberwachung:** Die Komponente muss eine Methode bereitstellen, die den aktuellen Fortschritt (z. B. als Prozentsatz oder Anzahl erledigter Schritte im Verhältnis zur Gesamtzahl) berechenbar macht.

## Software-Design-Richtlinien
- **Kapselung (Encapsulation):** Der interne Zustand der Liste und die einzelnen Schritt-Objekte müssen strikt gekapselt sein. Ein direkter Zugriff auf die zugrunde liegende Datenstruktur von außen ist untersagt; jegliche Manipulation muss über die bereitgestellte öffentliche API erfolgen.
- **Single Responsibility Principle (SRP):** Die Logik zur Verwaltung der Liste und die Logik zur Definition eines einzelnen Schrittes müssen in getrennten Verantwortungsbereichen liegen.
- **Exception Handling:** Verletzungen der Business-Logik (z. B. Versuch, einen Schritt zu überspringen) müssen durch spezifische, domänenspezifische Exceptions abgefangen und gemeldet werden. Ein "Silent Failure" ist nicht zulässig.
- **Immutabilität von Identifikatoren:** Einmal zugewiesene Identifikatern für Schritte dürfen während der Lebensdauer der Liste nicht verändert werden können.

## Zu berücksichtigende Edge-Cases
- **Leere Datenstrukturen:** Versuche, Operationen auf einer initial leeren Liste durchzuführen (z. B. Fortschrittsabfrage), müssen definiert behandelt werden.
- **Null- oder Leereingaben:** Die Übergabe von null oder leeren Strings als Schrittbezeichnung muss durch eine Validierung abgefangen werden.
- **Duplikate:** Das Hinzufügen von Schritten mit bereits existierenden Identifikatoren muss als Verletzung der Integrität gewertet werden.
- **Grenzwerte der Sequenz:** Der Versuch, den Status des ersten oder des letzten Elements in einer unzulässigen Weise zu manipulieren (z. B. Abschluss eines Schritts, bevor die Liste initialisiert wurde), muss durch das Exception-Handling abgefangen werden.
- **Inkonsistente Zustandsübergänge:** Versuche, einen Schritt direkt von 'PENDING' auf 'COMPLETED' zu setzen, ohne den Zwischenstatus 'IN_PROGRESS' zu durchlaufen (sofern dies als Anforderung definiert ist), müssen unterbunden werden.