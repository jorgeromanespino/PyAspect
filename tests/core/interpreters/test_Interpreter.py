#
import pytest
from aspect.core.interpreters.Interpreter import Interpreter
from aspect.core.entities.Entity import AspectException

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
def test_interpret_echo_operation(interpreter):
    with pytest.raises(AspectException):
        interpreter.handle()


