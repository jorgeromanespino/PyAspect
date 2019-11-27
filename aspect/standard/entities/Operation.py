#
from .Entity import Entity
#
class Operation(Entity):
    class meta:
        type = 'operation'
        name = 'operation'
        model = {}
        addToModel = False    
    #
    def __init__(self, args={}):
        super().__init__(args)
        self.signature = ""
        self.local_namespace = ""
        self.local_name = ""
        self.interpreter = None
