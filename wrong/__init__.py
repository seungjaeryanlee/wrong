from .sort import *


name = "wrong"

def importer(module_name, function_id):
    """
    Imports a function from a module with given name and function id.
    """
    if module_name not in globals():
        raise ValueError('The module {} does not exist.'.format(module_name))
    
    module = globals()[module_name]
    function_name = '{}_{}'.format(module_name, function_id)

    if hasattr(module, function_name):
        return getattr(module, function_name)
    else:
        raise ValueError('The module {} has no function with id {}' \
            .format(module_name, function_id))
