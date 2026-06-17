# pyright: reportUnusedImport=false
import pytest
from loesung import QueryBuilder

def test_simple_select():
    query = QueryBuilder()
    sql = query.select(['name']).from_table('users').build()
    assert sql == 'SELECT name FROM users'

def test_select_all():
    query = QueryBuilder()
    sql = query.select([]).from_table('users').build()
    assert sql == 'SELECT * FROM users'

def test_where_condition():
    query = QueryBuilder()
    sql = query.select(['name']).from_table('users').where('age > 25').build()
    assert sql == "SELECT name FROM users WHERE age > 25"

def test_order_by():
    query = QueryBuilder()
    sql = query.select(['name']).from_table('users').order_by('name', 'desc').build()
    assert sql == 'SELECT name FROM users ORDER BY name DESC'

def test_limit():
    query = QueryBuilder()
    sql = query.select(['name']).from_table('users').limit(10).build()
    assert sql == 'SELECT name FROM users LIMIT 10'

def test_complex_query():
    query = QueryBuilder()
    sql = query.select(['name', 'email']).from_table('users').where('age > 30').order_by('name').limit(5).build()
    assert sql == 'SELECT name, email FROM users WHERE age > 30 ORDER BY name ASC LIMIT 5'

def test_invalid_column_in_where():
    query = QueryBuilder()
    with pytest.raises(ValueError):
        query.select(['name']).from_table('users').where('invalid_column = 10').build()

def test_invalid_operator_in_where():
    query = QueryBuilder()
    with pytest.raises(ValueError):
        query.select(['name']).from_table('users').where('age INVALID 10').build()

def test_invalid_direction_in_order_by():
    query = QueryBuilder()
    with pytest.raises(ValueError):
        query.select(['name']).from_table('users').order_by('name', 'invalid').build()

def test_invalid_limit():
    query = QueryBuilder()
    with pytest.raises(ValueError):
        query.select(['name']).from_table('users').limit(-1).build()

def test_no_table_specified():
    query = QueryBuilder()
    with pytest.raises(ValueError):
        query.select(['name']).build()
