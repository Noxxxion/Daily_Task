# PreisRechner

## Problemstellung
Innerhalb unseres Abrechnungsmoduls für Dienstleister-Provisionen besteht aktuell das Problem, dass die manuelle Berechnung von Netto-Auszahlungsbeträgen fehleranfällig und zeitaufwendig ist. Das Unternehmen muss bei jedem Abrechnungszyklus eine Liste von Einzelbeträgen (Leistungshonorare) aggregieren. Von dieser Gesamtsumme muss vor der finalen Überweisung eine fixe Bearbeit_gebühr (Pauschalgebühr) abgezogen werden. Anschließend muss auf den verbleibenden Restbetrag eine vertraglich vereinbarte Provisionsgebühr in Prozent angewendet werden.

Um die finanzielle Integrität unserer Abrechnungsprozesse zu gewährleisten, wird eine automatisierte, robuste und mathematisch präzierte Komponente benötigt. Diese Komponente muss sicherstellen, dass alle Berechnungen nachvollziehbar sind und keine negativen oder unlogischen Auszahlungsbeträge generiert werden, die den Buchhaltungsprozess korrumpieren könnten.

## Funktionale Anforderungen & Akzeptanzkriterien
- **Aggregation der Einzelposten**: Die Komponente muss in der Lage sein, eine Liste von numerischen Einzelwerten als Eingabe zu akzeptieren und deren Summe präzise zu berechnen.
- **Subtraktion der Pauschalgebühr**: Nach der Aggregation der Einzelbeträge muss die definierte Pauschalgebühr vom Gesamtwert abgezogen werden.
- **Anwendung des Prozentsatzes**: Auf den nach Abzug der Pauschalgebühr verbleibenden Betrag muss ein fester Prozentsatz (Provisionssatz) angewendet werden, um den finalen Netto-Auszahlungsbetrag zu ermitteln. Der Prozentsatz ist als Reduktion des Wertes zu interpretieren (z. B. 5 % Abzug).
- **Präzision der Berechnung**: Die Berechnung muss eine hohe numerische Genauigkeit aufweisen, um Rundungsfehler bei der Aggregation von vielen kleinen Beträgen zu vermeiden.
- **Validierung der Eingabewerte**: Das System muss sicherstellen, dass alle Eingabewerte (Einzelbeträge, Pauschalgebühr, Prozentsatz) mathematisch sinnvoll sind.

## Software-Design & Implementierungsrichtlinien
- **Single Responsibility Principle (SRP)**: Die Logik zur Berechnung darf nicht mit Logiken zur Dateneingabe oder Ausgabe vermischt werden. Eine dedizierte Klasse oder Funktion ist für die reine Rechenlogik verantwortlich.
- **Encapsulation**: Der interne Zustand der Berechnung (z. B. Zwischenschritte) muss vor externen Manipulationen geschützt werden.
- **Exception Handling**: Es ist ein robustes Error-Handling zu implementieren. Anstatt unkontrollierte Systemabstürs zu verursachen, müssen spezifische, benutzerdefinierte Exceptions geworfen werden, wenn die Geschäftsregeln verletzt werden (z. B. `InvalidInputException`).
- **Type Safety**: Die Verwendung von Typ-Annotationen ist zwingend erforderlich, um die Integrität der numerischen Datenströme zu garantieren.
- **Immutability**: Die Eingabedaten (die Liste der Einzelbeträge) dürfen während des Berechnungsprozesses nicht verändert werden.

## Zu berücksichtigende Edge-Cases
- **Leere Datenstruktur**: Das Verhalten bei einer leeren Liste von Einzelbeträgen muss definiert sein (Erwartetes Ergebnis: 0 oder Exception).
- **Negative Eingabewerte**: Einzelbeträge, Pauschalgebühren oder Prozentsätze, die negativ sind, müssen als ungültig erkannt und abgefangen werden.
- **Pauschalgebühr größer als Gesamtsumme**: Falls die Pauschalgebühr den aggregierten Wert der Einzelposten übersteigt, muss das System verhindern, dass ein negativer Auszahlungsbetrag entsteht (Erwartung: Begrenzung auf 0 oder Fehlerwerfen).
- **Prozentsatz außerhalb des Bereichs [0, 100]**: Ein Prozentsatz, der kleiner als 0 oder größer als 100 ist, muss durch eine Validierung ausgeschlossen werden.
- **Nicht-numerische Datentypen**: Das System muss auf Eingaben reagieren, die keine validen Zahlenwerte repräsentieren (z. B. Strings oder Null-Werte innerhalb der Liste).