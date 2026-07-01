# RollenManager

## Problemstellung
In modernen Enterprise-Anwendungen ist eine präzise und konsistente Steuerung von Zugriffsberechtigungen eine kritische Anforderung an die Systemsicherheit. Das vorliegende Projekt adressiert das Problem der unstrukturierten Verwaltung von Berechtigungen innerhalb einer Identitätsarchitektur. 

Bisherige Implementierungen leiden unter einer mangelnden Trennung zwischen Identität (Identity) und Autorisierung (Role). Dies führt zu inkonsistenten Zuständen, bei der Berechtigungen nicht eindeutig einer Entität zugeordnet werden können oder Dubletten die Logik der Zugriffskontrolle korrumpieren. Das Ziel des 'RollenManager'-Moduls ist es, eine zentrale, zustandsbehaftete Komponente bereitzustellen, welche die Zuweisung, Entfernung und Verifizierung von Rollen für verschiedene Identitäten (z. B. Benutzer-IDs, Service-Accounts oder System-Identitäten) kapselt und die referenzielle Integrität der Zuordnungen sicherstellt.

## Funktionale Anforderungen & Akzeptanzkriterien
Die Implementierung muss folgende fachliche Logik erfüllen:

- **Rollen-Zuweisung (Assign Role):** Das System muss in der Lage sein, einer eindeutigen Identität eine spezifische Rolle zuzuweisen. Eine Zuweisung ist nur gültig, wenn die Identität und die Rolle valide Strings sind.
- **Rollen-Entfernung (Revoke Role):** Es muss möglich sein, eine bestehende Verbindung zwischen einer Identität und einer Rolle gezielt aufzuheben, ohne andere Rollen der Identität zu beeinflussen.
- **Berechtigungsprüfung (Role Verification):** Das Modul muss eine Abfragefunktion bereitstellen, die mit höchster Präzision beantwortet, ob eine spezifische Identität über eine bestimmte Rolle verfügt (Boolean Response).
- **Identitäts-Audit (Retrieve Roles):** Für jede hinterlegte Identität muss eine vollständung Liste aller aktuell zugewiesenen Rollen extrahierbar sein.
- **Vermeidung von Redundanz:** Das System muss sicherstellen, dass die Zuweisung derselben Rolle an dieselbe Identität keinen neuen Eintrag erzeugt (Idempotenz der Zuweisungsoperation).

## Software-Design-Richtlinien
Um eine wartbare und robuste Architektur zu gewährleisten, sind folgende Prinzipien zwingend einzuhalten:

- **Kapselung (Encapsulation):** Der interne Zustand der Rollen-Mapping-Struktur muss strikt vor externen Manipulationen geschützt werden. Der Zugriff auf die Daten darf ausschließlich über die definierten öffentlichen Methoden erfolgen.
- **Single Responsibility Principle (SRP):** Die Klasse `RollenManager` darf ausschließlich für die Verwaltung der Zuordnungen zuständig sein. Logik zur Identitätsverwaltung oder Rollendefinition ist außerhalb dieser Komponente zu belassen.
- **Defensives Programmieren:** Alle öffentlichen Methoden müssen Eingabewerte validieren, bevor sie die Domänenlogik verarbeiten.
- **Exception Handling:** Fehlerhafte Operationen (z. B. Manipulation nicht existierender Identitäten) dürfen nicht durch stille Fehlertoleranz unterdrückt werden, sondern müssen über spezifische, nachvollziehbare Ausnahmen kommuniziert werden.
- **Immutabilität der Rückgabewerte:** Bei der Abfrage von Rollenlisten muss sichergestellt werden, dass die zurückgegebene Datenstruktur nicht durch nachträgliche Modifikation der aufrufenden Komponente den internen Zustand des Managers verändert (Deep Copy oder unmodifizierbare Strukturen).

## Zu berücksichtigende Edge-Cases
Die Implementierung muss folgende Grenzfälle explizit behandeln:

- **Null- und Leere-Werte:** Versuche, eine Rolle oder eine Identität mit `None` bzw. einem leeren String (`""`) zuzuweisen, müssen als ungültige Operation erkannt und abgefangen werden.
- **Nicht existierende Entitäten:** Der Versuch, eine Rolle von einer Identität zu entfernen, die bisher keine Rollen besitzt, muss konsistent behandelt werden (kein Absturz, sondern definierte Fehlerbehandlung).
- **Duplikats-Zuweisung:** Das mehrfache Zuweisen derselben Rolle an dieselbe Identität darf nicht zu inkonsistenten Zuständen oder einer künstlichen Vergrößerung der Rollenliste führen.
- **Identitäts-Leeren:** Die Abfrage von Rollen für eine Identität, die im System noch nie registriert wurde, muss ein eindeutiges Ergebnis (leere Menge) liefern und darf keine Fehlermeldung provozieren, sofern dies fachlich als "keine Berechtigungen vorhanden" definiert ist.