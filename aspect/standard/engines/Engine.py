#
from aspect.core.engines.Engine import Engine as CoreEngine

#
class Engine(CoreEngine):
    #
    engines = {}
    #        
    def __init__(self, args=None):
        super().__init__(args)
        self.operation_execution_engine = None

    #
    def execute(self, signature, args):
        return 'echo hello world!'

#
Engine.engines['standard'] = Engine()
        