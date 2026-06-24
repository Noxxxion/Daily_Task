# ZustandsWandler

## Problemstellung
In komplexen Geschäftsprozessen ist die Integrität von Objekten über ihren gesamten Lebenszyklus hinweg von entscheidender Bedeutung. Ein häufig auftretendes Problem in Enterprise-Anwendungen ist das unkontrollierte Ändern von Statuswerten (z. B. bei Bestellungen, Dokumenten oder Benutzerkonten). Ohne eine strikte Validierung der Übergänge können Objekte in technisch ungültige oder geschäftlich nicht zulässige Zustände gelangen – beispielsweise kann eine Bestellung den Status "Versendet" erreichen, ohne dass der Status "Bezahlt" durchlaufen wurde.

Das Projekt 'ZustandsWandler' adressiert dieses Problem durch die Implementierung einer zentralen Logik-Komponente. Ziel ist es, einen deterministischen Mechanismus bereitzustellen, der Übergänge zwischen vordefinierten Prozessstufen ausschließlich auf Basis autorisierter Trigger (Events) erlaubt und die Einhaltung der Geschäftsregeln sicherstellt. Die Komponente muss als Single Source of Primärquelle (Single Source of Truth) für die Zustandslogik innerhalb eines Objekts fungieren und jegliche unzulässige Manipulation unterbinden.

## Funktionale Anforderungen & Akzeptanzkriterien
- **Definition von Zustandsraum und Übergangsmatrix**: Das System muss in der Lage sein, eine Menge von gültigen Ausgangszuständen, Zielzuständen und die dazugehörigen Auslöser (Events/Trigger) zu definieren.
- **Validierung von Zustandsübergängen**: Bei einem Trigger-Aufruf muss das System prüfen, ob der Übergang vom aktuellen Zustand zum neuen Zustand gemäß der vordefinierten Matrix zulässig ist.
- **Atomarität der Statusänderung**: Ein Zustandswechsel darf nur dann vollzogen werden, wenn die Validierung erfolgreich war. Der interne Status des Objekts darf nicht in einem unvollständigen oder invaliden Zustand verbleiben.
- **Reaktion auf illegale Übergänge**: Jeder Versuch, einen nicht autorisierten Übergang einzuleiten (z. B. ein Event, das für den aktuellen Zustand nicht definiert ist), muss explizit blockiert und durch eine entsprechende Fehlermeldung signalisiert werden.
- **Status-Abfrage**: Es muss eine zuverlässige Methode bereitgestellt werden, um den aktuellen, gültigen Status des Objekts jederzeit abzufragen.

## Design- und Architekturrichtlinien
- **Kapselung (Encapsulation)**: Der interne Zustand des Objekts darf nicht von außen direkt manipulierbar sein. Änderungen dürfen ausschließlich über die kontrollierte Schnittstelle des ZustandsWandlers erfolgen.
- **Single Responsibility Principle (SRP)**: Die Logik der Übergangsvalidierung muss strikt von der eigentlichen Geschäftslogik der Objekte getrennt sein. Der ZustandsWandler ist rein für die Überwachung der Transitionsregeln zuständig.
- **Exception Handling**: Es ist ein robustes Error-Handling zu implementieren. Für geschäftsrelevante Verstöße (z. B. `InvalidTransitionError`) müssen spezifische, benutzerdefinierte Ausnahmen definiert werden, um eine präzise Fehlerdiagnose zu ermöglichen.
- **Immutability der Konfiguration**: Die Definition der Übergangsmatrix sollte nach der Initialisierung als unveränderlich betrachtet werden, um Seiteneffekte während der Laufzeit zu vermeiden.

## Zu berücksichtigende Edge-Cases
- **Identische Zustandsübergänge**: Behandlung von Versuchen, ein Event auszulösen, das den aktuellen Zustand nicht verändert (Self-Transitions).
- **Initialisierung ohne Startzustand**: Absicherung gegen eine unvollständige Konfiguration, bei der kein gültiger Ausgangszustand definiert wurde.
- **Leere Event- oder Zustandslisten**: Validierung der Konfiguration gegen leere Datenstrukturen, um einen undefinierten Prozessverlauf zu verhindern.
- **Null- oder None-Werte**: Explizites Abfangen von Null-Eingaben bei der Definition von Zuständen oder beim Auslösen von Events, um Abstürze der Logik-Engine zu vermeiden.
- **Nicht definierte Trigger**: Sicherstellung, dass ein Event, das zwar existiert, aber nicht für den aktuellen Zustand registriert ist, korrekt als unzulässig erkannt wird.