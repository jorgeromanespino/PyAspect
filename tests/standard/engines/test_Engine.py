#
import pytest
from aspect.standard.engines.Engine import Engine
from aspect.standard.operations.common.Echo import Echo as EchoOperation
from aspect.standard.operations.common.Ping import Ping as PingOperation

@pytest.fixture
def engine():
    engine = Engine()
    engine.import_classes("aspect/standard/operations/common")
    engine.import_classes("aspect/standard/interpreters")
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

#
def test_directory_navigation():
    import glob
    path ="./aspect/standard/operations"
    files = [f for f in glob.glob(path + '/**/*.py', recursive=True)]
    assert len(files) > 0

#
def test_get_local_namespace_and_local_name():
    import glob
    path ="aspect/standard/operations/common"
    file_list = glob.glob(path + '/Ping.py')
    assert len(file_list) == 1

    file_path = file_list[0]
    assert file_path.endswith('Ping.py')

    file_name = file_path.split('/')[-1]
    assert file_name == 'Ping.py'

    import re
    local_namespace = re.sub('.py$', '', file_path)
    local_namespace = re.sub('^\.', '', local_namespace).replace('/','.')
    local_name = re.sub('.py$', '', file_name)
    assert local_namespace == 'aspect.standard.operations.common.Ping' and local_name == "Ping"
    
    operation = __import__(local_namespace, fromlist=[local_name])
    instance = getattr(operation, local_name)()
    r = instance.execute()
    assert r == 'ack'

#
def test_importing_all_files():
    import glob
    import re

    path = "aspect/standard/operations/common"
    files = [f for f in glob.glob(path + '/**/*.py', recursive=True)]
    for file_path in files:
        file_name = file_path.split('/')[-1]        
        if file_name == '__init__.py': continue
        #
        local_namespace = re.sub('.py$', '', file_path)
        local_namespace = re.sub('^\.', '', local_namespace).replace('/','.')
        local_name = re.sub('.py$', '', file_name)
        operation = __import__(local_namespace, fromlist=[local_name])
        instance = getattr(operation, local_name)()
        r = instance.execute()
        r = r
