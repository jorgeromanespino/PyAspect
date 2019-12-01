#
from ..Operation import Operation
#
class Ping(Operation):
    # Static properties. Class metadata
    class Meta:
        name = 'common.ping'
        signature = 'common.ping'
        interpreter = 'StandardInterpreter'
    #
    def __init__(self, message=''):
        super().__init__()
    #
    def execute(self):
        return 'ack'

# Initialization
Operation.register(Ping)