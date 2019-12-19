#
import pytest
#
from aspect.sql.languages.aql.AqlEngine import AqlEngine
from aspect.sql.languages.aql.translators.sqlalchemy.Translator import Translator as SqlAlchemyTranslator

#
def test_SqlAqlEngine_instantiation():
    aql_engine = AqlEngine()
    sqlalchemy_translator = SqlAlchemyTranslator()
    #
    assert aql_engine != None and sqlalchemy_translator != None

#
@pytest.fixture
def aql_engine():
    engine = AqlEngine()
    return engine
#
def test_aql_engine_parse_entity(aql_engine):
    ast = aql_engine.parse('entity')
    assert ast.getText() == 'entity' and  ast.children[0].getText() == 'entity'

#
def test_aql_engine_parse_and_translate_entity(aql_engine):
    ast = aql_engine.parse('entity')
    translator = aql_engine.translate(ast)
    assert ast.getText() == 'entity' and  ast.children[0].getText() == 'entity'
    assert translator != None and translator.visited == True