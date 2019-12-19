#
class Command:
    #
    def __init__(self, value=None, result=None, symbol_table=None, children=[], parent={}, interpreter=None):
        self.value = value
        self.result = result
        self.symbol_table = symbol_table
        self.children = children
        self.parent = parent
        self.interpreter = interpreter
        self._runtime_interpreter = None

    #
    @property
    def runtime_interpreter(self):
        return self._runtime_interpreter

    @runtime_interpreter.setter
    def runtime_interpreter(self, value):
        self._runtime_interpreter = value

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

    # TODO test
    def execute_command(self, command):
        command.symbol_table = self.symbol_table
        command.execute()
        return command.result