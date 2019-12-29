#
from aspect.core.languages.aql.translators.Command import Command as CoreCommand
#
class Command(CoreCommand):
    #
    def __init__(self, value=None, result=None, symbol_table=None, children=[], parent={}, interpreter=None):
        super().__init__(value, result, symbol_table, children, parent, interpreter)

    # TODO
    def push_context(self, context):
        raise NotImplementedError

    # TODO
    def pop_context(self):
        raise NotImplementedError

    # TODO
    def peek_context(self, level):
        raise NotImplementedError

    # TODO
    def execute(self):
        return self.result
