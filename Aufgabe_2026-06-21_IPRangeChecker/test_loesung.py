import pytest
from loesung import IPRangeChecker

def test_valid_ipv4_in_range():
    """Testet gültige IPv4-Adressen in einem CIDR-Block"""
    checker = IPRangeChecker()
    assert checker.is_ip_in_range("192.168.1.10", "192.168.1.0/24") == True
    assert checker.is_ip_in_range("192.168.1.255", "192.168.1.0/24") == True
    assert checker.is_ip_in_range("192.168.1.0", "192.168.1.0/24") == True
    assert checker.is_ip_in_range("192.168.2.10", "192.168.1.0/24") == False

def test_valid_ipv4_in_range_with_netmask():
    """Testet gültige IPv4-Adressen mit Netzmaske statt CIDR"""
    checker = IPRangeChecker()
    assert checker.is_ip_in_range("192.168.1.10", "192.168.1.0/255.255.255.0") == True
    assert checker.is_ip_in_range("192.168.1.255", "192.168.1.0/255.255.255.0") == True
    assert checker.is_ip_in_range("192.168.1.0", "192.168.1.0/255.255.255.0") == True
    assert checker.is_ip_in_range("192.168.2.10", "192.168.1.0/255.255.255.0") == False

def test_edge_cases():
    """Testet Edge-Cases"""
    checker = IPRangeChecker()
    
    # Teste mit verschiedenen CIDR-Werten
    assert checker.is_ip_in_range("10.0.0.1", "10.0.0.0/8") == True
    assert checker.is_ip_in_range("172.16.0.1", "172.16.0.0/12") == True
    assert checker.is_ip_in_range("192.168.0.1", "192.168.0.0/16") == True
    
    # Teste mit /32 CIDR
    assert checker.is_ip_in_range("192.168.1.1", "192.168.1.1/32") == True
    assert checker.is_ip_in_range("192.168.1.2", "192.168.1.1/32") == False

def test_invalid_inputs():
    """Testet ungültige Eingaben"""
    checker = IPRangeChecker()
    
    # Teste None-Werte
    with pytest.raises(ValueError):
        checker.is_ip_in_range(None, "192.168.1.0/24")
    
    with pytest.raises(ValueError):
        checker.is_ip_in_range("192.168.1.1", None)
    
    # Teste leere Strings
    with pytest.raises(ValueError):
        checker.is_ip_in_range("", "192.168.1.0/24")
    
    with pytest.raises(ValueError):
        checker.is_ip_in_range("192.168.1.1", "")
    
    # Teste ungültige IP-Adressen
    with pytest.raises(ValueError):
        checker.is_ip_in_range("999.999.999.999", "192.168.1.0/24")
    
    with pytest.raises(ValueError):
        checker.is_ip_in_range("192.168.1.1", "192.168.1.0/33")
    
    with pytest.raises(ValueError):
        checker.is_ip_in_range("192.168.1.1", "192.168.1.0/255.255.255.255.255")

def test_ipv6_not_supported():
    """Testet, dass IPv6-Adressen nicht unterstützt werden"""
    checker = IPRangeChecker()
    
    with pytest.raises(ValueError):
        checker.is_ip_in_range("2001:0db8::1", "2001:0db8::/32")