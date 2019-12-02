#
from ..entities.Entity import Entity
#
class Operation:
    # Static properties. Class metadata
    class Meta:
        name = 'core_operation.execute'
        interpreter = None
        model = {}

    #
    @staticmethod
    def register(clazz):
        clazz.Meta.signature = clazz.Meta.signature if hasattr(clazz.Meta, 'signature') else clazz.Meta.name
        existed = clazz.Meta.signature in Operation.Meta.model
        Operation.Meta.model[clazz.Meta.signature] = clazz
        return existed
    #
    @staticmethod
    def copy_properties(source, target, deep=False):
        Entity.copy_properties(source, target, deep)
    #
    def __init__(self):
        self.runtime_interpreter = None
        self.result = None
    #
    def init(self):
        return self.result
    #
    def execute(self):
        return self.result
    #
    def finish(self):
        return self.result
    #
    def handle(self):
        self.result = self.init()
        self.result = self.execute()
        self.result = self.finish()
        return self.result

    #
    def exec(self, **kargs):
        return self.runtime_interpreter.exec(**kargs)
