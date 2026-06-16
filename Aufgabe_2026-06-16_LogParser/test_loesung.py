# pyright: reportUnusedImport=false
import pytest
from loesung import parse_log_file, search_logs


def test_parse_log_file_normal_case(tmp_path):
    log_content = '''[2023-10-15 14:30:45] [INFO] [1234] User login successful
[2023-10-15 14:31:22] [ERROR] [1234] Database connection failed
[2023-10-15 14:32:10] [DEBUG] [1235] Processing request
[2023-10-16 09:15:30] [WARN] [1236] Memory usage high
[2023-10-16 09:16:45] [INFO] [1234] User logout successful
[2023-10-16 09:17:00] [ERROR] [1237] File not found'''
    
    file_path = tmp_path / "test.log"
    file_path.write_text(log_content, encoding='utf-8')
    
    result = parse_log_file(str(file_path))
    
    assert result['level_count']['INFO'] == 2
    assert result['level_count']['ERROR'] == 2
    assert result['level_count']['DEBUG'] == 1
    assert result['level_count']['WARN'] == 1
    assert result['pid_count']['1234'] == 3
    assert result['pid_count']['1235'] == 1
    assert result['pid_count']['1236'] == 1
    assert result['pid_count']['1237'] == 1
    assert result['date_count']['2023-10-15'] == 3
    assert result['date_count']['2023-10-16'] == 3


def test_parse_log_file_empty_file(tmp_path):
    file_path = tmp_path / "empty.log"
    file_path.write_text('', encoding='utf-8')
    
    result = parse_log_file(str(file_path))
    
    assert result['level_count']['INFO'] == 0
    assert result['level_count']['ERROR'] == 0
    assert result['level_count']['DEBUG'] == 0
    assert result['level_count']['WARN'] == 0
    assert result['pid_count'] == {}
    assert result['date_count'] == {}


def test_parse_log_file_invalid_entries(tmp_path):
    log_content = '''[2023-10-15 14:30:45] [INFO] [1234] User login successful
invalid log entry
[2023-10-15 14:31:22] [ERROR] [1234] Database connection failed
[2023-10-15 14:32:10] [INVALID] [1235] Processing request
[2023-10-16 09:15:30] [WARN] [1236] Memory usage high'''
    
    file_path = tmp_path / "invalid.log"
    file_path.write_text(log_content, encoding='utf-8')
    
    result = parse_log_file(str(file_path))
    
    assert result['level_count']['INFO'] == 1
    assert result['level_count']['ERROR'] == 1
    assert result['level_count']['DEBUG'] == 0
    assert result['level_count']['WARN'] == 1
    assert result['pid_count']['1234'] == 2
    assert result['pid_count']['1236'] == 1
    assert result['date_count']['2023-10-15'] == 2
    assert result['date_count']['2023-10-16'] == 1


def test_search_logs_normal_case(tmp_path):
    log_content = '''[2023-10-15 14:30:45] [INFO] [1234] User login successful
[2023-10-15 14:31:22] [ERROR] [1234] Database connection failed
[2023-10-15 14:32:10] [DEBUG] [1235] Processing request'''
    
    file_path = tmp_path / "search.log"
    file_path.write_text(log_content, encoding='utf-8')
    
    results = search_logs(str(file_path), 'user')
    
    assert len(results) == 1
    assert 'User login successful' in results[0]
    
    results = search_logs(str(file_path), 'database')
    
    assert len(results) == 1
    assert 'Database connection failed' in results[0]


def test_search_logs_case_insensitive(tmp_path):
    log_content = '''[2023-10-15 14:30:45] [INFO] [1234] User login successful'''
    
    file_path = tmp_path / "case.log"
    file_path.write_text(log_content, encoding='utf-8')
    
    results = search_logs(str(file_path), 'USER')
    
    assert len(results) == 1
    assert 'User login successful' in results[0]


def test_search_logs_not_found(tmp_path):
    log_content = '''[2023-10-15 14:30:45] [INFO] [1234] User login successful'''
    
    file_path = tmp_path / "notfound.log"
    file_path.write_text(log_content, encoding='utf-8')
    
    results = search_logs(str(file_path), 'xyz')
    
    assert len(results) == 0