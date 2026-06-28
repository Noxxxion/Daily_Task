# TextFragmenter

## Problemstellung
Im Rahmen der Skalierung unserer Datenverarbeitungs-Pipelines stehen wir vor der Herausforderung, unstrukturierte und großformatige Textdaten (z. B. Log-Dateien, Rohdaten-Exports oder konfigurative String-Blöcke) effizient zu verarbeiten. Derzeit werden diese Texte als monolithische Einheiten behandelt, was die nachgelagerte Verarbeitung in spezialisierten Mikroservices erschwert, da diese eine granulare Strukturierung der Daten benötigen.

Es fehlt eine standardisierte, robuste Komponente, die in der Lage ist, vorgegebene Textblöcke zuverlässig anhand definierter Trennzeichen (Delimiters) in atomare Fragmente zu zerlegen. Das Ziel des "TextFragmenter"-Moduls ist es, diese Zerlegung als isolierte, hochgradig testbare und wiederverwendbare Logik-Einheit bereitzustellen, um die Datenintegrität beim Übergang von der Rohdaten-Phase zur Strukturierungs-Phase sicherzustellen.

## Funktionale Anforderungen & Akzeptanzkriterien
- **AC 1: Primäre Fragmentierung:** Das System muss eine Methode bereitstellen, die einen Eingabestring anhand eines einzelnen, spezifizierten Trennzeichens (String oder Character) in eine Liste von Teilstring-Fragmenten zerlegt.
- **AC 2: Multi-Delimiter-Unterstützung:** Die Komponente muss in der Lage sein, eine Liste von verschiedenen Trennzeichen entgegenzunehmen und den Textblock zu fragmentieren, sobald eines der definierten Zeichen im Text gefunden wird.
- **AC 3: Bereinigung der Fragmente (Trimming):** Alle resultierenden Fragmente müssen nach der Zerlegung automatisch von führenden und abschließenden Whitespaces (Leerzeichen, Tabs, Zeilenumbrüche) bereinigt werden, um die Datenreinheit zu gewährleisten.
- **AC 4: Filterung leerer Segmente:** Das Ergebnis darf keine leeren Strings enthalten. Wenn durch aufeinanderfolgende Trennzeichen "leere" Bereiche entstehen, müssen diese im finalen Output unterdrückt werden.
- **AC 5: Rückgabetyp:** Die Funktion muss konsistent eine geordnete Sammlung (List/Array) von Strings zurückgeben, die der zeitlichen Abfolge der Trennung im Originaltext entspricht.

## Software-Design- und Implementierungsrichtlinien
- **Encapsulation (Kapselung):** Die Fragmentierungs-Logik muss in einer dedizierten Klasse gekapselt sein. Der interne Mechanismus der Zerlegung darf für den Aufrufer nicht einsehbar sein (Black-Box-Prinzip).
- **Single Responsibility Principle (SRP):** Die Komponente ist ausschließlich für die Zerlegung und Bereinigung zuständig. Seiteneffekte wie das Schreiben von Dateien oder Logging in externe Systeme sind strikt untersagt.
- **Exception Handling:** Ein robustes Error-Handling muss implementiert werden. Es sind spezifische Ausnahmen zu definieren (z. B. bei ungültigen Trennzeichen-Definitionen), anstatt generische Systemfehler durchzulassen.
- **Input Validation:** Jede Methode muss eine Validierung der Eingabeparameter vornehmen, bevor die eigentliche Geschäftslogik ausgeführt wird.

## Zu berücksichtigende Edge-Cases
- **Null/None-Eingabe:** Der Input-String darf nicht `null` oder `None` sein; in diesem Fall ist ein definierter Fehlerzustand auszulösen.
- **Leerer Eingabestring:** Ein leerer String (`""`) muss ohne Fehlermeldung verarbeitet werden und eine leere Liste als Ergebnis liefern.
- **Nicht vorhandene Trennzeichen:** Wenn das angegebene Trennzeichen im Textblock nicht existiert, muss der ursprüngliche (bereinigte) Text als einzelnes Element in einer Liste zurückgegeben werden.
- **Leeres Trennzeichen:** Das Bereitstellen eines leeren Strings als Trennzeichen muss als ungültige Konfiguration erkannt und abgefangen werden.
- **Consecutive Delimiters:** Mehrfache, direkt aufeinanderfolgende Trennzeichen im Quelltext dürfen nicht zu leeren Einträgen in der Ergebnisliste führen.
- **Nur Trennzeichen:** Ein Input-String, der ausschließlich aus Trennzeichen besteht, muss eine leere Liste zurückgeben.