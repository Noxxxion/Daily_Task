# ObjektKoppler

## Problemstellung
In modernen, dezentralen Enterprise-Systemen liegen Informationen oft in fragmentierten Domänenmodellen vor. Ein typisches Szenario ist die Trennung von Stammdaten (z. B. ein 'Kunden'-Objekt) und transaktionalen Daten (z. B. ein 'Bestell'-Objekt). Um geschäftskritische Prozesse wie die Rechnungsstellung oder die Logistiksteuerung durchzuführen, müssen diese technisch separaten Objekte logisch miteinander verknüpft werden, ohne die Integrität der ursprünglichen Domänenmodelle zu gefährden.

Das Modul 'ObjektKoppler' hat die Aufgabe, eine Brücke zwischen zwei unabhängigen Objekten zu schlagen, indem es ein gemeinsames Identifikationsmerkmal (Key) identifiziert und eine funktionale Verbindung herstellt. Das Ziel ist es, eine konsistente Sicht auf verknüpfte Datenstrukturen zu ermöglichen, ohne die ursprünglichen Objekte durch invasive Vererbung oder direkte Mutationen zu verändern.

## Funktionale Anforderungen & Akzeptanzkriterien
- **Identifikation von Kopplungsschlüsseln:** Der Dienst muss in der Lage sein, ein definiertes Attribut aus zwei unterschiedlichen Objekten als primäres Bindeglied zu verwenden.
- **Erstellung einer Kopplungsinstanz:** Bei erfolgreicher Identifizierung eines identischen Schlüssels muss eine neue, dedikative Struktur (`CouplingResult`) erstellt werden, die den Zugriff auf beide Ausgangsobjekte ermöglicht.
- **Unveränderlichkeit der Quellobjekte (Immutability):** Der Kopplungsprozess darf keine Seiteneffekte auf den Zuständen der ursprünglichen Objekte haben. Die Originaldaten müssen nach dem Vorgang bitidentisch zu ihrem Zustand vor der Kopplung sein.
- **Validierung der Schlüsselintegrität:** Vor der Erstellung der Verbindung muss eine Validierung stattfinden, ob die Typen der verglichenen Attribute kompatibel sind. Es wird ein striktes Typing-Modell angewandt (keine implizite Konvertierung).
- **Software-Design-Richtlinien:**
    - **Encapsulation:** Die Logik zur Extraktion und zum Vergleich der Schlüssel muss vollständig gekapselt sein; die aufrufende Komponente darf keine Details über den internen Vergleichsalgorithmus kennen.
    - **Single Responsibility Principle (SRP):** Der Koppler ist ausschließlich für die Logik der Verbindung zuständig, nicht für die Datenbeschaffung oder die nachgelagerte Geschäftslogik.
    - **Exception Handling:** Es muss ein striktes Error-Handling implementiert werden. Fehlgeschlagene Kopplungsversuche aufgrund fehlender Schlüssel müssen über spezifische, benutzerdefinierte Business-Exceptions gemeldet werden.

## Zu berücksichtigende Edge-Cases
- **Fehlende Schlüsselattribute:** Eines oder beide Objekte verfügen nicht über das für die Kopplung erforderliche Attribut; hier muss eine `KeyAttributeNotFoundError` erfolgen.
- **Typen-Mismatch:** Der Schlüssel in Objekt A ist ein String (z. B. "100"), während der Schlüssel in Objekt B ein Integer (z. B. 100) ist. Um Datenkorruption zu vermeiden, wird dies als `IncompatibleKeyTypesError` gewertet.
- **Null- und None-Werte:** Eines der Schlüsselattribute ist `null` oder `None`. Eine Kopplung unter Verwendung von Null-Werten muss explizit unterbunden werden (`NullKeyError`), um fehlerhafte Datenverknüpfungen zu vermeiden.
- **Leere Datensätze:** Die Eingabe besteht aus leeren Objekten oder leeren Listen von Objekten; der Dienst muss robust reagieren (Rückgabe einer leeren Liste bei Listen-Eingabe, ohne Exception).
- **Duplikate im Schlüsselraum:** Bei der Verarbeitung von Listen wird ein One-to-Many-Verhalten unterstützt. Wenn ein Schlüssel in der linken Liste mehrfach vorkommt oder in der rechten Liste mehrere Treffer findet, werden alle gültigen Kombinationen als separate `CouplingResult`-Instanzen zurückgegeben.