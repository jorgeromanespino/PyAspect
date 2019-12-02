#
from ..entities.Entity import AspectException
from ..operations.Operation import Operation
#
class Interpreter(Operation):
    # Static properties. Class metadata
    class Meta:
        name = 'CoreInterpreter'
        signature = 'core_interpreter.interpret'
        interpreter = None
        model = {}
    #
    @staticmethod
    def register(clazz):
        existed = Operation.register(clazz)
        Interpreter.Meta.model[clazz.Meta.name] = clazz
        return existed

    #
    def __init__(self, **kargs):
        super().__init__()
        self.engine = kargs['engine'] if 'engine' in kargs else None
        self.operation = kargs['operation'] if 'operation' in kargs else None
        self. interpreter = kargs['interpreter'] if 'interpreter' in kargs else None
        self.args = kargs['args'] if 'args' in kargs else None
        self.modifiers = kargs['modifiers'] if 'modifiers' in kargs else None
    #
    def init(self):
        if self.operation == None:
            raise AspectException('operation is None')
        if self.engine == None:
            raise AspectException('engine is None')

    #
    def execute(self):
        operation_impl = self.engine.new_instance(self.operation.Meta.signature, **self.args)
        operation_impl.runtime_interpreter = self
        Operation.copy_properties(self.args, operation_impl)
        if isinstance(operation_impl, Interpreter):
            operation_impl.engine = self.engine
        #
        return operation_impl.handle()

    #
    def exec(self, **kargs):
        return self.engine.execute(**kargs)        


