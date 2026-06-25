# BestandsVergleich

## Problemstellung
In der Logistik- und Bestandsverwaltung unserer Organisation tritt regelmäßig das Problem auf, dass Diskrepanzen zwischen dem theoretischen Soll-Bestand (aus dem ERP-System) und dem tatsächlichen Ist-Bestand (aus physischen Scans oder Wareneingangsprotokollen) existieren. Diese Differenzen führen zu Fehlplanungen in der Lieferkette, ungenauen Lagerbestandsanzeigen und potenziellen Umsatzverlusten durch nicht verfügbare Artikel.

Bisher erfolgt die manuelle Abgleich dieser Listen über zeitintensive und fehleranfällige Excel-Vergleiche. Es besteht die dringende Notwendigkeit eines automatisierten, hochperformanten Logik-Moduls, das zwei Datensätze (Soll-Bestand vs. Ist-Bestand) verarbeitet und präzise identifiziert, welche Artikel im physischen Bestand fehlen (Abwesenheitsanalyse). Das Modul muss als Kernkomponente für zukünftige Automatisierungsprozesse dienen und eine absolut verlässliche Identifikation von Differenzen gewährleisten.

## Funktionale Anforderungen & Akritanzkriterien
- **AC 1: Definition der Eingangsdaten:** Das System muss zwei separate Listen von eindeutigen Identifikatoren (z. B. SKU, Artikelnummer oder UUID) entgegennehmen können. Die Eingabe muss als iterierbare Datenstruktur (z. B. Liste oder Set) definiert sein.
- **AC 2: Logik der Differenzermittlung:** Das Modul muss die Menge der Elemente bestimmen, die im ersten Datensatz (Soll-Bestand/Master-Liste) vorhanden sind, jedoch im zweiten Datensatz (Ist-Bestand/Scan-Liste) fehlen.
- **AC 3: Eindeutigkeit des Ergebnisses:** Die Ausgabe der fehlenden Elemente muss eine Menge von eindeutigen Werten sein. Duplikate innerhalb der Ausgangslisten dürfen das Ergebnis der Differenzermittlung nicht verfälschen.
- **AC 4: Unabhängigkeit von der Reihenfolge:** Der Vergleichsprozess muss unabhängig von der ursprünglichen Sortierung oder Anordnung der Elemente in den Eingangslisten ein konsistentes Ergebnis liefern.
- **AC 5: Rückgabewert:** Das Modul muss eine Liste (oder ein vergleichbares iterierbares Objekt) zurückgeben, welche ausschließlich die identifizierten fehlenden Elemente enthält. Im Falle einer vollständigen Übereinstimmung ist eine leere Struktur zurückzugeben.

## Software-Design & Implementierungsrichtlinien
- **Single Responsibility Principle (SRP):** Die Logik für den Vergleich muss strikt von der Logik der Datenbeschaffung oder der Formatierung getrennt sein. Eine dedizierte Klasse/Funktion darf ausschließlich die mathematische Mengen-Differenz berechnen.
- **Kapselung:** Der interne Prozess der Differenzbildung muss gekapselt sein. Die Schnittstelle nach außen darf nur die finalen Ergebnisse liefern, ohne den internen Zustand der Vergleichsoperation preiszugeben.
- **Exception Handling & Robustness:** Das System muss ein robustes Error-Handling implementieren. Ungültige Eingabetypen oder strukturelle Fehler in den Datenmustern müssen durch definierte Exceptions abgefangen werden, anstatt einen unkontrollierte Programmabbruch zu verursachen.
- **Immutability (Unveränderlichkeit):** Die ursprünglichen Eingangslisten dürfen während des Vergleichsprozesses zu keinem Zeitpunkt modifiziert werden. Der Prozess muss als reine Funktion betrachtet werden, die neue Daten erzeugt, ohne den Ausgangszustand zu verändern.

## Zu berücksichtigende Edge-Cases
- **Leere Datensätze:** Es muss definiert sein, wie das System reagiert, wenn die Soll-Liste leer ist (Ergebnis muss leer sein) oder wenn die Ist-Liste leer ist (alle Elemente der Soll-Liste müssen als fehlend markiert werden).
- **Identische Datensätze:** Bei vollständiger Deckungsgleichheit beider Listen muss das Ergebnis zwingend eine leere Menge sein.
- **Null-Werte/None-Werte:** Das Auftreten von `None` oder `Null` innerhalb der Listen muss abgefangen werden. Diese Werte dürfen weder die Logik korrumpieren noch zu Laufzeitfehlern führen; sie sind als ungültige Identifikatoren zu behandeln (auszufiltern).
- **Duplikate in den Eingangslisten:** Die Logik muss sicherstellen, dass mehrfache Nennungen desselben Elements in der Soll-Liste nicht zu einer multiplen Auflistung im Ergebnis führen.
- **Typ-Inkonsistenz:** Das System muss mit unterschiedlichen, aber vergleichbaren Datentypen (z. B. String vs. Integer bei numerischen IDs) umgehen können oder einen expliziten Validierungsfehler werfen, falls die Vergleichbarkeit nicht gewährleistet ist.