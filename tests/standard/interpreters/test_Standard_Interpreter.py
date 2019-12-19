#
import pytest
from aspect.standard.engines.Engine import Engine
from aspect.standard.operations.common.Echo import Echo as EchoOperation
from aspect.standard.interpreters.Interpreter import Interpreter
#
@pytest.fixture
def standard_engine():
    engine = Engine()
    engine.register(EchoOperation)
    return engine
#
@pytest.fixture
def echo_operation():
    echo = EchoOperation()
    return echo
#
@pytest.fixture
def interpreter():
    interpreter = Interpreter(engine=None, operation=None, interpreter=None, args=None, modifiers=None)
    return interpreter
#
def test_interpreter_metadata(interpreter):
    assert interpreter.engine == None
    assert interpreter.operation == None
    assert interpreter.interpreter == None
    assert interpreter.args == None
    assert interpreter.modifiers == None
#
#
def test_interpret_echo_operation(standard_engine, interpreter, echo_operation):
    interpreter = Interpreter(engine=standard_engine, operation=echo_operation, args={'message':'hi!'})
    r = interpreter.handle()
    assert r == 'echo hi!'

