# IPRangeChecker - Aufgabenbeschreibung

## Ziel der Aufgabe
Implementiere eine Klasse `IPRangeChecker`, die prüft, ob eine gegebene IP-Adresse in einem angegebenen IP-Bereich (CIDR-Block) liegt.

## Funktionale Anforderungen
- Die Klasse muss eine Methode `is_ip_in_range` bereitstellen, die eine IP-Adresse und einen CIDR-Block entgegennimmt
- Die Methode soll einen booleschen Wert zurückgeben, der angibt, ob die IP-Adresse im CIDR-Block enthalten ist
- Die IP-Adresse und der CIDR-Block werden als Strings übergeben
- Die Klasse muss mit IPv4-Adressen arbeiten
- Die CIDR-Notation kann sowohl in der Form `192.168.1.0/24` als auch `192.168.1.0/255.255.255.0` angegeben werden

## Anforderungen an die Implementierung
- Die Implementierung muss robust gegenüber ungültigen Eingaben sein
- Es müssen alle relevanten Edge-Cases abgedeckt werden
- Fehlerhafte Eingaben sollen mit passenden Exceptions behandelt werden

## Edge-Cases und Spezifikationen
- Leere Strings als Eingabe
- None-Werte als Eingabe
- Ungültige IP-Adressen (z.B. 999.999.999.999)
- Ungültige CIDR-Blöcke (z.B. /33, negative Werte)
- Ungültige CIDR-Notation (z.B. /255.255.255.255.255)
- IPv6-Adressen (sollte nicht unterstützt werden)
- Überlauf bei der CIDR-Subnetzmaske
- Unterschiedliche Formate des CIDR-Blocks (CIDR-Notation vs. Netzmaske)

## Beispiele
- `is_ip_in_range("192.168.1.10", "192.168.1.0/24")` → `True`
- `is_ip_in_range("192.168.2.10", "192.168.1.0/24")` → `False`
- `is_ip_in_range("192.168.1.10", "192.168.1.0/255.255.255.0")` → `True`

## Abgabeformat
Die Implementierung soll in einer Datei `loesung.py` erfolgen, die eine Klasse `IPRangeChecker` mit der Methode `is_ip_in_range` enthält.

=== VORGABE ===
# Das finale, korrigierte Code-Grundgerüst für den Benutzer...

```python
# loesung.py
import ipaddress

class IPRangeChecker:
    def is_ip_in_range(self, ip_address, cidr_block):
        """
        Prüft, ob eine IP-Adresse in einem CIDR-Block enthalten ist.
        
        Args:
            ip_address (str): Die zu prüfende IP-Adresse als String
            cidr_block (str): Der CIDR-Block als String (z.B. "192.168.1.0/24" oder "192.168.1.0/255.255.255.0")
            
        Returns:
            bool: True, wenn die IP-Adresse im CIDR-Block liegt, sonst False
            
        Raises:
            ValueError: Bei ungültigen IP-Adressen oder CIDR-Blöcken
        """
        if not ip_address or not cidr_block:
            raise ValueError("IP-Adresse und CIDR-Block dürfen nicht leer sein")
        
        if ip_address is None or cidr_block is None:
            raise ValueError("IP-Adresse und CIDR-Block dürfen nicht None sein")
        
        try:
            # Prüfe, ob die IP-Adresse gültig ist
            ip_obj = ipaddress.IPv4Address(ip_address)
            
            # Prüfe, ob der CIDR-Block gültig ist
            network_obj = ipaddress.IPv4Network(cidr_block, strict=True)
            
            # Prüfe, ob die IP-Adresse im Netzwerk liegt
            return ip_obj in network_obj
            
        except (ValueError, ipaddress.AddressValueError, ipaddress.NetmaskValueError):
            raise ValueError("Ungültige IP-Adresse oder CIDR-Block")
```