#
import pytest
from aspect.standard.engines.Engine import Engine
from aspect.standard.operations.common.Echo import Echo as EchoOperation
from aspect.standard.operations.common.Ping import Ping as PingOperation

@pytest.fixture
def engine():
    engine = Engine()
    Engine.register_operations()
    return engine

def test_engine_metadata():
    assert type(Engine.engines['standard']) == Engine
    assert type(Engine.engines['standard']).__name__ == 'Engine'
    assert Engine.engines['standard'].__class__ == Engine
    assert Engine.engines['standard'].__class__.__name__ == 'Engine'

#
def test_engine_instantiation(engine):
    assert engine.operation_execution_engine != None

#
def test_engine_new_instance(engine):
    r = engine.new_instance("common.echo", args=None)
    assert type(r) == EchoOperation

#
def test_engine_new_instance(engine):
    r = engine.new_instance("common.echo", args=None)
    assert type(r) == EchoOperation

#
def test_engine_new_instance_not_exits(engine):
    with pytest.raises(Exception):
        engine.new_instance("echo", message="hi!")

#
def test_engine_execute_echo(engine):
    r = engine.execute('common.echo', args={'message':'hello world!'})
    assert r == 'echo hello world!'

def test_engine_execute_ping(engine):
    r = engine.execute('common.ping')
    assert r == 'ack'


def test_package_loading():
    # local_namespace, local_name
    operation = __import__('aspect.standard.operations.common.Ping', fromlist=['Ping'])
    instance = getattr(operation, 'Ping')()
    r = instance.execute()
    assert r == 'ack'
