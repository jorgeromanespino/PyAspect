#
import pytest
import aspect
from aspect.standard.engines.Engine import Engine
import aspect.standard.operations
from aspect.core.operations.Operation import Operation as CoreOperation
from aspect.standard.operations.common.Echo import Echo as EchoOperation

@pytest.fixture
def engine():
    engine = Engine()
    # Two ways of importing operations
    Engine.import_operations(module=aspect, submodule_path='standard/interpreters', recursive=True)
    Engine.import_operations(module=aspect.standard.operations, recursive=True)
    return engine

def test_engine_metadata():
    assert Engine.Meta.model['StandardEngine'] == Engine
    assert Engine.Meta.model['StandardEngine'].__name__ == 'Engine'

#
def test_engine_instantiation(engine):
    assert engine.operation_execution_engine != None

#
def test_engine_new_instance(engine):
    r = engine.new_instance("common.echo")
    assert type(r) == EchoOperation

#
def test_engine_new_instance(engine):
    r = engine.new_instance("common.echo")
    assert type(r) == EchoOperation

#
def test_engine_new_instance_not_exits(engine):
    with pytest.raises(Exception):
        engine.new_instance("echo", message="hi!")

#
def test_engine_execute_echo(engine):
    r = engine.execute('common.echo', args={'message':'hello world!'})
    assert r == 'echo hello world!'
#
def test_engine_execute_ping(engine):
    r = engine.execute('common.ping')
    assert r == 'ack'
#
def test_package_importing_by_path():
    # local_namespace, local_name
    operation = __import__('aspect.standard.operations.common.Ping', fromlist=['Ping'])
    instance = getattr(operation, 'Ping')()
    r = instance.execute()
    assert r == 'ack'
#
def test_engine_execute_reverse(engine):
    r = engine.execute('common.reverse', args={'message':'hello world!'})
    assert r == 'hello world!'[::-1]

def test_engine_execute_exec(engine):
    r = engine.execute('common.execute', args={'signature':'common.echo', 'args':{'message': 'hi'}})
    assert r == 'echo hi'

