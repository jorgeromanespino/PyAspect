#
from aspect.core.engines.Engine import Engine as CoreEngine

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
    def new_instance(self, operation_name, args):
        #todo simplify
        c = self.get_operation(operation_name)
        r = c()
        return r

    #
    def execute(self, signature, args):
        return 'echo hello world!'

#
Engine.engines['standard'] = Engine()

        