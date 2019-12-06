#
import pytest
from aspect.standard.engines.Engine import Engine

# References:
# https://stackoverflow.com/questions/1707709/list-all-the-modules-that-are-part-of-a-python-package
# https://www.bnmetrics.com/blog/dynamic-import-in-python3

#
def test_directory_recursive_navigation():
    import glob
    path ="./aspect/standard/operations"
    files = [f for f in glob.glob(path + '/**/*.py', recursive=True)]
    assert './aspect/standard/operations/Operation.py' in files
    assert './aspect/standard/operations/common/Execute.py' in files
    assert './aspect/standard/operations/common/Reverse.py' in files
    assert './aspect/standard/operations/common/Ping.py' in files
    assert './aspect/standard/operations/__init__.py' in files
    assert len(files) > 0

def test_directory_recursive_navigation():
    import glob
    path ="./aspect/standard/operations"
    files = [f for f in glob.glob(path + '/*.py')]
    assert './aspect/standard/operations/Operation.py' in files
    assert not './aspect/standard/operations/common/Execute.py' in files
    assert not './aspect/standard/operations/common/Reverse.py' in files
    assert not './aspect/standard/operations/common/Ping.py' in files
    assert './aspect/standard/operations/__init__.py' in files
    assert len(files) > 0

#
def test_instantiate_operation_by_relative_path():
    import glob
    path = "aspect/standard/operations/common"
    file_list = glob.glob(path + '/Ping.py')
    assert len(file_list) == 1

    file_path = file_list[0]
    assert file_path.endswith('Ping.py')

    file_name = file_path.split('/')[-1]
    assert file_name == 'Ping.py'

    import re
    local_namespace = re.sub('.py$', '', file_path)
    local_namespace = re.sub('^\.', '', local_namespace).replace('/','.')
    local_name = re.sub('.py$', '', file_name)
    assert local_namespace == 'aspect.standard.operations.common.Ping' and local_name == "Ping"
    
    operation = __import__(local_namespace, fromlist=[local_name])
    instance = getattr(operation, local_name)()
    r = instance.execute()
    assert r == 'ack'


#
def test_importing_all_files_relative_files():
    import glob
    import re

    path = "aspect/standard/operations/common"
    files = [f for f in glob.glob(path + '/**/*.py', recursive=True)]
    for file_path in files:
        file_name = file_path.split('/')[-1]        
        if file_name == '__init__.py': continue
        #
        local_namespace = re.sub('.py$', '', file_path)
        local_namespace = re.sub('^\.', '', local_namespace).replace('/','.')
        local_name = re.sub('.py$', '', file_name)
        operation = __import__(local_namespace, fromlist=[local_name])
        instance = getattr(operation, local_name)()
        r = instance.execute()
        r = r

#
def test_walk_packages_by_module_path():
    import pkgutil
    from pathlib import Path
    from importlib import import_module   
    import aspect.standard.operations as Operations

    # path = Path('aspect/standard/operations')
    # module_name = '.'.join(path.parts)
    path = Path(Operations.__path__[0])
    module_name_dotted = Operations.__name__

    modules = {}
    for (loader, module_name, is_pkg) in pkgutil.walk_packages([path]):
        imported_module = import_module(module_name_dotted + '.' + module_name)
        if is_pkg:
            modules[module_name] = {'module':imported_module, 'path': imported_module.__path__[0]}
        else: # Module initialization
            class_instance = getattr(imported_module, module_name)
            instance = class_instance()

    assert not 'Operation' in modules
    assert 'common' in modules
    assert len(modules) > 0

#
def import_operations(module=None, path=None, recursive=False):
    import pkgutil
    from pathlib import Path
    from importlib import import_module   
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
            packages = import_operations(module=package_info['module'], recursive=recursive)
            package_info['packages'] = packages
    return modules

#
def test_import_operations_common():
    import aspect.standard.operations.common as CommonOperation
    modules = import_operations(module=CommonOperation)
    assert len(modules['modules']) > 0

#
def test_import_operations_recursive():
    import aspect.standard.operations as Operation
    modules = import_operations(module=Operation, recursive=True)
    assert len(modules['modules']) > 0

def test_import_operations_by_path_recursive():
    modules = import_operations(path='aspect/standard/operations', recursive=True)
    assert len(modules['modules']) > 0
