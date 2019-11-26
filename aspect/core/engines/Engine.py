
class Engine:
    def __init__(self, args=None):
        self.store = None #args.store if args.store else None #Store()
        self.target = "PythonMemoryModel"
        self.aqlEngine = None #AqlEngine()

    def getOperationImpl(self, args):
        #operation = self.getOperation(args);
        #return Engine.newInstance(operation.localFullName, args);
        raise NotImplemented()

    #
    def getOperation(self, args):
        raise NotImplemented()

    #
    def query(self, q):
        # return self.aqlEngine.execute(q)
        raise NotImplemented()

    #
    def register(self, clazz):
        #return this.aqlEngine.registerByName(clazz.meta.name, clazz);
        raise NotImplemented()
        