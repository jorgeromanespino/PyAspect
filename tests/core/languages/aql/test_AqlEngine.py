#
import pytest
#
from aspect.core.languages.aql.AqlEngine import AqlEngine

#
def test_aql_engine():
    aql_engine = AqlEngine()
    assert aql_engine != None

#
@pytest.fixture
def aql_engine():
    engine = AqlEngine()
    return engine

#
def test_aql_engine_parse_entity(aql_engine):
    ast = aql_engine.parse('entity')
    assert ast.getText() == 'entity' and  ast.children[0].getText() == 'entity'
