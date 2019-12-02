#
from ..Operation import Operation
#
class Execute(Operation):
    # Static properties. Class metadata
    class Meta:
        name = 'common.execute'
        interpreter = 'StandardInterpreter'
    #
    def __init__(self, operation=None, signature=None, args={}, modifiers=None, interpreter=None):
        super().__init__()
        self.operation = operation if signature == None else signature
        self.args = args
    #
    def execute(self):
        if self.operation == None: return None
        r = self.exec(operation=self.operation, args=self.args)
        return r

# Initialization
Operation.register(Execute)