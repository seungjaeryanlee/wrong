# A mini version of the wrong package. Chose one wrong implementation for
# each module. Allows for a simpler syntax (from wrong import sort). The
# wrong implementation that is most informative to the user should be selected.
from .sort import sort_3 as sort

# Import all wrong implementations of each module for the importer function.
from .sort import *


name = "wrong"

def importer(module_name, function_id):
    """
    Imports a function from a module with given name and function id.
    """
    function_name = '{}_{}'.format(module_name, function_id)

    if module_name not in globals():
        raise ValueError('The module {} does not exist.'.format(module_name))
    if function_name not in globals():
        raise ValueError('The module {} has no function with id {}' \
            .format(module_name, function_id))
    else:
        return globals()[function_name]
