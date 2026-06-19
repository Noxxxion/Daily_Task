import pytest
from loesung import QueryBuilder

def test_simple_select():
    query = QueryBuilder()
    query.select("name", "age").from_("users")
    assert str(query) == "SELECT name, age FROM users"

def test_select_all():
    query = QueryBuilder()
    query.from_("users")
    assert str(query) == "SELECT * FROM users"

def test_where_clause():
    query = QueryBuilder()
    query.select("name").from_("users").where("age > ?", 18)
    assert str(query) == "SELECT name FROM users WHERE age > ?"

def test_order_by():
    query = QueryBuilder()
    query.select("name").from_("users").order_by("name", "age")
    assert str(query) == "SELECT name FROM users ORDER BY name, age"

def test_limit():
    query = QueryBuilder()
    query.select("name").from_("users").limit(10)
    assert str(query) == "SELECT name FROM users LIMIT 10"

def test_full_query():
    query = QueryBuilder()
    query.select("name", "age").from_("users").where("age > ?", 18).order_by("age").limit(5)
    assert str(query) == "SELECT name, age FROM users WHERE age > ? ORDER BY age LIMIT 5"

def test_empty_order_by():
    query = QueryBuilder()
    query.select("name").from_("users").order_by()
    assert str(query) == "SELECT name FROM users"

def test_no_table_error():
    query = QueryBuilder()
    with pytest.raises(ValueError, match="FROM clause is required"):
        query.build()

def test_where_without_from_error():
    query = QueryBuilder()
    with pytest.raises(ValueError, match="FROM clause must be specified before WHERE"):
        query.where("age > ?", 18)

def test_limit_error():
    query = QueryBuilder()
    with pytest.raises(ValueError, match="Limit must be at least 1"):
        query.limit(0)

def test_empty_table_error():
    query = QueryBuilder()
    with pytest.raises(ValueError, match="Table name cannot be empty"):
        query.from_("")