#
import pytest
from aspect.core.engines.Engine import Engine

@pytest.fixture
def engine():
    return Engine()

def test_engine_instantiation(engine):
    assert engine.target == "PythonMemoryModel"
