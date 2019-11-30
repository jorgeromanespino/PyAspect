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
    def executeOperation(self, operation, interpreter, runtime_engine, args={}, modifiers={}):
        if runtime_engine == None or operation == None:
            raise AspectException("runtime_engine and/or operation are invalid")
        interpreter_name = interpreter.Meta.name if isinstance(interpreter, CoreInterpreter) else operation.Meta.name
        interpreter_impl = runtime_engine.new_instance(interpreter_name, operation=operation, interpreter=interpreter, engine=runtime_engine, args=args, modifiers=modifiers)
        return interpreter_impl.handle()