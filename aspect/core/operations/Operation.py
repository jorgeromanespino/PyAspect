#
from ..entities.Entity import Entity
#
class Operation:
    #
    registry = {}
    #
    @staticmethod
    def register(clazz):
        existed = clazz.Meta.signature in Operation.registry
        Operation.registry[clazz.Meta.signature] = clazz
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
