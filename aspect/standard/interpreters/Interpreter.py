#
from aspect.core.interpreters.Interpreter import Interpreter as CoreInterpreter
#
class Interpreter(CoreInterpreter):
    # Static properties. Class metadata
    class Meta:
        name = 'StandardInterpreter'
        signature = "StandardInterpreter.interpret"
        interpreter = None

    #
    @staticmethod
    def register(clazz):
        return CoreInterpreter.register(clazz)     

    #
    def __init__(self, **kargs):
        super().__init__(**kargs)

#
Interpreter.register(Interpreter)