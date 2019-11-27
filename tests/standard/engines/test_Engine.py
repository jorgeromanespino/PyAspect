#
import pytest
from aspect.standard.engines.Engine import Engine

@pytest.fixture
def engine():
    return Engine()

def test_engine_metadata():
    assert type(Engine.engines['standard']) == Engine
    assert type(Engine.engines['standard']).__name__ == 'Engine'
    assert Engine.engines['standard'].__class__ == Engine
    assert Engine.engines['standard'].__class__.__name__ == 'Engine'

#
def test_engine_instantiation(engine):
    assert engine.operation_execution_engine == None

#
def test_engine_execute(engine):
    r = engine.execute(signature='common.echo', args={'message': 'hello world!'})
    assert r == 'echo hello world!'