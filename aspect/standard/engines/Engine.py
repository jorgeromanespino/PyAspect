#
from aspect.core.engines.Engine import Engine as CoreEngine, AspectException
from aspect.core.operations.Operation import Operation as CoreOperation
from .OperationExecutionEngine import OperationExecutionEngine
#
class Engine(CoreEngine):
    #
    engines = {}
    #
    registry = {}

    #
    @staticmethod
    def register(clazz):
        existed = clazz.Meta.name in Engine.registry
        Engine.registry[clazz.Meta.name] = clazz
        return existed

    #
    @staticmethod
    def register_operations():
        for k, v in CoreOperation.registry.items():
            Engine.register(v)
    #
    def get_operation(self, operation_name):
        return Engine.registry[operation_name] #if operation_name in Engine.registry else None

    #        
    def __init__(self, **kargs):
        super().__init__(kargs)
        self.operation_execution_engine = OperationExecutionEngine()

    #
    def new_instance(self, class_name, **kargs):
        instance = self.get_operation(class_name)()
        if (instance == None):
            raise AspectException('Class not found: ' + class_name)
        if len(kargs) != 0:
            Engine.copy_properties(kargs, instance)
        return instance

    #
    def execute(self, operation, args={}, modifiers=None, interpreter=None):
        o = operation if isinstance(operation, CoreOperation) else self.new_instance(operation, **args)
        r = self.operation_execution_engine.executeOperation(runtime_engine=self, operation=o, interpreter=interpreter, args=args, modifiers=modifiers)
        return o.handle()

#
Engine.engines['standard'] = Engine()
