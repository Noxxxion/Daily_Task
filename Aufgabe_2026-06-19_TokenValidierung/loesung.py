# Das finale, korrigierte Code-Grundgerüst für den Benutzer

```python
def is_valid_token(token):
    """
    Validiert einen Token im Format XYZ-123-ABC.
    
    Args:
        token (str): Der zu validierende Token
        
    Returns:
        bool: True wenn der Token gültig ist, sonst False
    """
    # Prüfe auf None oder nicht-string Typ
    if token is None or not isinstance(token, str):
        return False
    
    # Prüfe auf leere Strings
    if not token:
        return False
    
    # Teile den Token an den Bindestrichen
    parts = token.split('-')
    
    # Prüfe auf genau 3 Teile
    if len(parts) != 3:
        return False
    
    # Speichere die Teile
    part1, part2, part3 = parts
    
    # Prüfe ersten Teil: 3 Großbuchstaben
    if not (len(part1) == 3 and part1.isalpha() and part1.isupper()):
        return False
    
    # Prüfe zweiten Teil: 3 Ziffern
    if not (len(part2) == 3 and part2.isdigit()):
        return False
    
    # Prüfe dritten Teil: 3 Großbuchstaben
    if not (len(part3) == 3 and part3.isalpha() and part3.isupper()):
        return False
    
    return True
```