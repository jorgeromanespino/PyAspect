#
from aspect.core.engines.Engine import Engine as CoreEngine, AspectException

#
class Engine(CoreEngine):
    #
    engines = {}
    #
    registry = {}

    #
    @staticmethod
    def __register(operation_name, operation_class):
        existed = operation_name in Engine.registry
        Engine.registry[operation_name] = operation_class
        return existed

    #
    def register(self, operation_name, operation_class):
        return Engine.__register(operation_name, operation_class)

    def get_operation(self, operation_name):
        return Engine.registry[operation_name]

    #        
    def __init__(self, args=None):
        super().__init__(args)
        self.operation_execution_engine = None

    #
    def new_instance(self, class_name, **kargs):
        instance = self.get_operation(class_name)()
        if (instance == None):
            raise AspectException('Class not found: ' + class_name)
        if len(kargs) != 0:
            Engine.copy_properties(kargs, instance)
        return instance

    #
    def execute(self, signature, args={}, modifiers=None, interprete=None):
        return self.new_instance(signature, **args).handle()

#
Engine.engines['standard'] = Engine()

        