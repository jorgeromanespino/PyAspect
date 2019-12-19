#
import pytest
#
from aspect.core.languages.aql.SymbolTable import SymbolTable

#
def test_symbol_table_instantiation():
    st = SymbolTable()
    assert st != None and len(st.contexts) == 1 and st.contexts[0] == {}

@pytest.fixture
def symbol_table():
    st = SymbolTable()
    return st

#
def test_symbol_table_push(symbol_table):
    symbol_table.push()
    assert len(symbol_table.contexts) == 2
    assert symbol_table.contexts[0] == symbol_table.contexts[1] == {}

#
def test_symbol_table_push_and_pop(symbol_table):
    symbol_table.push()
    symbol_table.pop()
    assert len(symbol_table.contexts) == 1 and symbol_table.contexts[0] == {}

#
def test_symbol_table_pop_exception(symbol_table):
    with pytest.raises(Exception):
        symbol_table.pop()

#
def test_symbol_table_peek(symbol_table):
    assert symbol_table.peek() == symbol_table.contexts[0]

#
def test_symbol_table_set_and_get(symbol_table):
    symbol_table['my_symbol'] = 1
    assert symbol_table['my_symbol'] == 1

#
def test_symbol_table_in(symbol_table):
    symbol_table['my_symbol'] = 1
    assert 'my_symbol' in symbol_table
    assert not 'my_symbol_' in symbol_table

#
def test_symbol_table_getting_symbol_dont_exist(symbol_table):
    with pytest.raises(KeyError):
        symbol_table['my_symbol']

#
def test_symbol_table_set_and_get_variable(symbol_table):
    symbol_table.set_variable('my_variable', 1)
    assert symbol_table.get_variable('my_variable') == 1

#
def test_symbol_table_set_and_get_variable(symbol_table):
    f = lambda x: x + 1 
    symbol_table.set_function('my_function', f)
    assert symbol_table.get_function('my_function') == f

#
def test_symbol_table_clone_with_1_context(symbol_table):
    symbol_table['my_symbol_1'] = 1
    symbol_table['my_symbol_2'] = 2
    new_st = symbol_table.clone()
    assert id(new_st.peek()) != id(symbol_table.peek())
    assert symbol_table['my_symbol_1'] == 1 and symbol_table['my_symbol_2'] == 2
    assert new_st['my_symbol_1'] == 1 and new_st['my_symbol_2'] == 2
