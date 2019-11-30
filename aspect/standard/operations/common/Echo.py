#
from ..Operation import Operation
#
class Echo(Operation):
    # Static properties. Class metadata
    class Meta:
        name = 'common.echo'
        signature = 'common.echo'
        interpreter = 'StandardInterpreter'
    #
    def __init__(self, message=''):
        super().__init__()
        self.message = message
    #
    def execute(self):
        return 'echo ' + self.message

# Initialization
Operation.register(Echo)