#
from aspect.core.engines.OperationExecutionEngine import OperationExecutionEngine as CoreOperationExecutionEngine
from aspect.core.entities.Entity import AspectException
from aspect.core.interpreters.Interpreter import Interpreter as CoreInterpreter
#
class OperationExecutionEngine(CoreOperationExecutionEngine):
    #
    def __init__(self):
        super().__init__()
    #
    def executeOperation(self, operation, interpreter=None, runtime_engine=None, args={}, modifiers={}):
        if runtime_engine == None or operation == None:
            raise AspectException("runtime_engine and/or operation are invalid")
        if not isinstance(interpreter, CoreInterpreter):
            interpreter_name = interpreter if interpreter != None else operation.Meta.interpreter
            interpreter_name = CoreInterpreter.Meta.model[interpreter_name].Meta.signature
            interpreter = runtime_engine.new_instance(interpreter_name, operation=operation, interpreter=interpreter, engine=runtime_engine, args=args, modifiers=modifiers)
        else:
            interpreter.operation = operation
            interpreter.engine = runtime_engine
            interpreter.args = args
            interpreter.modifiers = modifiers
        operation.runtime_interpreter = interpreter
        return interpreter.handle()