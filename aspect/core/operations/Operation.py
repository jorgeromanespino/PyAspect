#
class Operation:
    #
    def __init__(self):
        self.runtime_interpreter = None
        self.result = None
    #
    def init(self):
        return None
    #
    def execute(self):
        return None
    #
    def finish(self):
        return None
    #
    def handle(self):
        result = self.result = self.init()
        #
        result = self.execute()
        self.result = result if result != None else self.result
        #
        result = self.finish()
        self.result = result if result != None else self.result
        #
        return self.result
