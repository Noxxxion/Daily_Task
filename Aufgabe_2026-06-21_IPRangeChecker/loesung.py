import os
from typing import Tuple

class IPRangeChecker:
    def __init__(self):
        pass

    def is_ip_in_range(self, ip_address: str, cidr_block: str) -> bool:
        """
        Prüft, ob eine IP-Adresse in einem CIDR-Block liegt.
        
        Args:
            ip_address: IP-Adresse als String (z.B. "192.168.1.1")
            cidr_block: CIDR-Block als String (z.B. "192.168.1.0/24" oder "192.168.1.0/255.255.255.0")
            
        Returns:
            bool: True, wenn die IP-Adresse im CIDR-Block liegt, sonst False
            
        Raises:
            ValueError: Bei ungültigen IP-Adressen oder CIDR-Blöcken
        """
        # TODO: Implementierung
        pass