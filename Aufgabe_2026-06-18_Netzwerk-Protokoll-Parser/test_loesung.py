# pyright: reportUnusedImport=false
import pytest
from loesung import parse_network_log, filter_by_protocol, get_statistics
from datetime import datetime
import tempfile
import os

def test_parse_network_log_valid_data():
    content = '''2023-05-15 10:30:00;192.168.1.1;10.0.0.1;TCP;80;1024;OK
2023-05-15 10:30:01;192.168.1.2;10.0.0.2;UDP;53;512;ERROR'''
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        f.write(content)
        temp_path = f.name
    
    try:
        result = parse_network_log(temp_path)
        assert len(result) == 2
        assert result[0]['timestamp'] == datetime(2023, 5, 15, 10, 30, 0)
        assert result[0]['source_ip'] == '192.168.1.1'
        assert result[0]['destination_ip'] == '10.0.0.1'
        assert result[0]['protocol'] == 'TCP'
        assert result[0]['port'] == 80
        assert result[0]['size'] == 1024
        assert result[0]['status'] == 'OK'
    finally:
        os.unlink(temp_path)

def test_parse_network_log_invalid_data():
    content = '''2023-05-15 10:30:00;192.168.1.1;10.0.0.1;TCP;80;1024;OK
invalid_line
2023-05-15 10:30:01;192.168.1.2;10.0.0.2;UDP;53;512;ERROR
invalid_ip;10.0.0.2;TCP;80;1024;OK'''
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.log') as f:
        f.write(content)
        temp_path = f.name
    
    try:
        result = parse_network_log(temp_path)
        assert len(result) == 2
    finally:
        os.unlink(temp_path)

def test_filter_by_protocol():
    log_data = [
        {'protocol': 'TCP', 'size': 100},
        {'protocol': 'UDP', 'size': 200},
        {'protocol': 'TCP', 'size': 300}
    ]
    
    result = filter_by_protocol(log_data, 'TCP')
    assert len(result) == 2
    assert all(entry['protocol'] == 'TCP' for entry in result)

def test_get_statistics_empty():
    result = get_statistics([])
    assert result['total_packets'] == 0
    assert result['protocol_distribution'] == {}
    assert result['total_bytes'] == 0
    assert result['error_packets'] == 0

def test_get_statistics():
    log_data = [
        {'protocol': 'TCP', 'size': 100, 'status': 'OK'},
        {'protocol': 'UDP', 'size': 200, 'status': 'ERROR'},
        {'protocol': 'TCP', 'size': 300, 'status': 'WARNING'},
        {'protocol': 'TCP', 'size': 400, 'status': 'ERROR'}
    ]
    
    result = get_statistics(log_data)
    assert result['total_packets'] == 4
    assert result['protocol_distribution'] == {'TCP': 3, 'UDP': 1}
    assert result['total_bytes'] == 1000
    assert result['error_packets'] == 2