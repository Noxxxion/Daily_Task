# AufgabenSortierer

## Problemstellung

In modernen Workflow-Management-Systemen ist die effiziente Ressourcenallokation von entscheidender Bedeutung. Ein kritisches Problem in der aktuellen Systemlandschaft ist die unstrukturierte Verarbeitung von Aufgabenpaketen (Task-Batches), bei denen die Reihenfolge der Abarbeitung rein zufällig oder nach dem Zeitpunkt des Eintreffens erfolgt. Dies führt dazu, dass zeitkritische Prozesse (High-Priority) durch weniger wichtige Hintergrundaufgaben verzögert werden, was die Einhaltung von Service Level Agreements (SLAs) gefährdet.

Es besteht die dringende Notwendigkeit einer dedizierten Komponente, die in der Lage ist, eine Menge von Aufgabenobjekten zu analysieren und diese basierend auf einem numerischen Prioritätswert deterministisch neu zu ordnen. Das Ziel ist die Implementierung eines stabilen Sortier-Mechanismus, der sicherstellt, dass die Rechenressourcen stets die Aufgaben mit der höchsten numerischen Relevanz zuerst bearbeiten.

## Funktionale Anforderungen & Akzeptanzkriterien

- **AC 1: Numerische Priorisierung:** Die Komponente muss eine Liste von Obregjekten entgegennehmen und diese in absteigender Reihenfolge ihrer numerischen Priorität sortieren (höchster Wert = höchste Priorität).
- **AC 2: Erhalt der Datenintegrität (Stability):** Der Sortieralgorithmus muss "stabil" implementiert sein. Das bedeutet, dass zwei Aufgaben mit identischem Prioritätswert ihre relative Position zueinander aus der ursprünglichen Eingabeliste beibehalten müssen.
- **AC 3: Unveränderlichkeit der Quelldaten:** Die ursprüngliche Eingabeliste darf durch den Sortiervorgang nicht mutiert werden. Das Ergebnis muss als eine neue, sortierte Datenstruktur zurückgegeben werden.
- **AC 4: Validierung der Datentypen:** Das System muss sicherstellen, dass nur Objekte verarbeitet werden, die ein gültiges, vergleichbares numerisches Attribut für die Priorität besitzen.

## Software-Design- und Implementierungsrichtlinien

- **Single Responsibility Principle (SRP):** Die Verantwortung für die Sortierlogik muss strikt von der Datenstruktur der Aufgaben getrennt sein. Eine Klasse ist ausschließlich für den Sortiervorgang zuständig, eine andere definiert das Aufgabenmodell.
- **Kapselung:** Der Zugriff auf den Prioritätswert innerhalb des Aufgabenobjekts muss über kontrollierte Schnittstellen (z. B. Getter-Methoden) erfolgen, um die Integrität des Attributs zu schützen.
- **Exception Handling:** Die Implementierung muss ein robustes Error-Handling beinhalten. Es sind spezifische Ausnahmen definiert, wenn die Eingabedaten nicht den Anforderungen entsprechen (z. B. bei fehlerhaften Datentypen oder fehlenden Attributen). Ein stillschweigendes Ignorieren von Fehlern ist untersagt.
- **Interface-Design:** Die öffentliche API der Komponente muss präzise und leicht verständlich sein, sodass eine Integration in bestehende Workflow-Pipelines ohne tiefgreifende Kenntnis der internen Sortierlogik möglich ist.

## Zu berücksichtigende Edge-Cases

- **Leere Datenstrukturen:** Die Komponente muss den Fall einer leeren Liste handhaben können, ohne eine Exception auszulösen, und stattdessen eine leere Liste zurückgeben.
- **Identische Prioritätswerte:** Wie in AC 2 definiert, muss die relative Ordnung bei Gleichstand der Werte strikt gewahrt bleiben.
- **Nicht-numerische Prioritätswerte:** Das System muss erkenntlich machen, wenn ein Attribut, das als numerischer Wert erwartet wird, einen String oder ein anderes nicht vergleichbares Format aufweist, und dies über eine definierte Exception melden.
- **Null- oder None-Werte:** Das Auftreten von `None` (oder `null`) innerhalb der Liste oder als Wert für das Prioritätsattribut muss abgefangen werden, um Abstürze während des Vergleichsvorgangs zu verhindern.
- **Negative Prioritätswerte:** Die Logik muss korrekt mit negativen Zahlen arbeiten können, sofern diese im Rahmen der numerischen Skala liegen.
