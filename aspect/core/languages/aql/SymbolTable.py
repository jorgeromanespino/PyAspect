#
import copy

#
class SymbolTable:
    #
    class Meta:
        variable_key = '__variable__$'
        function_key = '__function__$'
    #
    def __init__(self):
        self.contexts = []
        self.push()

    #
    def push(self):
        self.contexts.append({})

    #
    def pop(self):
        if len(self.contexts) == 1:
            raise Exception('Trying to do a pop with only one contexts')
        self.contexts.pop()

    #
    def peek(self):
        return self.contexts[-1]

    def __setitem__(self, key, value):
        self.peek()[key] = value
        return self

    #
    def __getitem__(self, key):
         return self.peek()[key]

    #
    def __contains__(self, key):
         return key in self.peek()    

    # 
    def set_variable(self, name, value):
        env = SymbolTable.Meta.variable_key
        self[f"{env}{name}{env}"] = value

    # 
    def get_variable(self, name):
        env = SymbolTable.Meta.variable_key
        return self[f"{env}{name}{env}"]

    # 
    def set_function(self, name, value):
        env = SymbolTable.Meta.function_key
        self[f"{env}{name}{env}"] = value

    # 
    def get_function(self, name):
        env = SymbolTable.Meta.function_key
        return self[f"{env}{name}{env}"]

    #
    def clone(self):
        return copy.deepcopy(self)

    # TODO def get_function_instance(self, name):
    # TODO put_all
    # TODO clone
    # TODO copy????

