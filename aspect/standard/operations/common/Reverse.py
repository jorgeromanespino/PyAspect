#
from ..Operation import Operation
#
class Reverse(Operation):
    # Static properties. Class metadata
    class Meta:
        name = 'common.reverse'
        signature = 'common.reverse'
        interpreter = 'StandardInterpreter'
    #
    def __init__(self, message=''):
        super().__init__()
        self.message = message
    #
    def execute(self):
        return self.message[::-1]

# Initialization
Operation.register(Reverse)