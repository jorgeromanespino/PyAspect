#
from aspect.core.engines.Engine import Engine as CoreEngine, AspectException
from aspect.core.operations.Operation import Operation as CoreOperation
from .OperationExecutionEngine import OperationExecutionEngine
import pkgutil
from pathlib import Path
from importlib import import_module   
#import glob
#import re

#
class Engine(CoreEngine):
    # Static metadata
    class Meta:
        name = 'StandardEngine'
        model = {}

    #
    @staticmethod
    def register(clazz):
        existed = clazz.Meta.name in Engine.Meta.model
        Engine.Meta.model[clazz.Meta.name] = clazz
        return existed

    #
    def get_operation(self, operation_name):
        return CoreOperation.Meta.model[operation_name]

    #        
    def __init__(self, **kargs):
        super().__init__(kargs)
        self.operation_execution_engine = OperationExecutionEngine()

    #
    def new_instance(self, class_name, **kargs):
        instance = self.get_operation(class_name)(**kargs)
        if (instance == None):
            raise AspectException('Class not found: ' + class_name)
        if len(kargs) != 0:
            Engine.copy_properties(kargs, instance)
        return instance

    #
    def execute(self, operation=None, signature=None, args={}, modifiers=None, interpreter=None):
        operation = operation if signature == None else signature
        o = operation if isinstance(operation, CoreOperation) else self.new_instance(operation, **args)
        r = self.operation_execution_engine.executeOperation(runtime_engine=self, operation=o, interpreter=interpreter, args=args, modifiers=modifiers)
        return r
        
    # #
    # def import_classes(self, path):
    #     files = [f for f in glob.glob(path + '/**/*.py', recursive=True)]
    #     for file_path in files:
    #         file_name = file_path.split('/')[-1]        
    #         if file_name == '__init__.py': continue
    #         #
    #         class_name = re.sub('.py$', '', file_name)
    #         module_name = re.sub('.py$', '', file_path)
    #         module_name = re.sub(r'^\.', '', module_name).replace('/','.')
    #         module = __import__(module_name, fromlist=[class_name])
    #         clazz = getattr(module, class_name)
    #         Engine.register(clazz)

    #
    staticmethod
    def import_operations(module=None, path=None, recursive=False):
        if path != None:
            path = Path(path)
            module_name_dotted = '.'.join(path.parts)
        else:
            path = Path(module.__path__[0])
            module_name_dotted = module.__name__
        modules = {'packages':{}, 'modules':{}}
        for (loader, module_name, is_pkg) in pkgutil.walk_packages([path]):
            imported_module = import_module(module_name_dotted + '.' + module_name)
            if is_pkg: # Package registration
                modules['packages'][module_name] = {'module':imported_module}
            else: # Module initialization
                class_instance = getattr(imported_module, module_name)
                modules['modules'][module_name_dotted + '.' + module_name] = class_instance
                instance = class_instance()
        if recursive: # Importing subpackages recursively
            for package_name, package_info in modules['packages'].items():
                packages = Engine.import_operations(module=package_info['module'], recursive=recursive)
                package_info['packages'] = packages
        return modules
#
Engine.register(Engine)
