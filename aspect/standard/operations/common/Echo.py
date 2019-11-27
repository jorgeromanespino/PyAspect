#
from ..Operation import Operation
#
class Echo(Operation):
    #
    def __init__(self, message=''):
        super().__init__()
        self.message = message
    #
    def execute(self):
        return 'echo ' + self.message