"""
.. module:: loader.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Loads CMIP6 specialization from file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import imp
import os



def get_modules(input_dir, typeof):
    """Returns specialization modules.

    :param str input_dir: Directory within which modules reside.
    :param str typeof: Type of specialization being processed.

    """
    # Load specialization modules.
    modules = _get_modules(input_dir, typeof)
    if not modules:
        raise KeyError("Specializations not found")

    # Set specializations.
    root = _get_module(modules, typeof)
    try:
        root.GRID
    except AttributeError:
        grid = None
    else:
        grid = _get_module(modules, root.GRID)
    key_properties = _get_module(modules, root.KEY_PROPERTIES)
    processes = [_get_module(modules, p) for p in root.PROCESSES]

    return root, grid, key_properties, processes


def _get_modules(input_dir, specialization_type):
    """Returns a set of specialization modules.

    """
    modules = sorted([i for i in os.listdir(input_dir) if _is_target(i, specialization_type)])
    modules = [os.path.join(input_dir, m) for m in modules]
    modules = [(m.split("/")[-1].split(".")[0], m) for m in modules]

    return [imp.load_source(name, fpath) for name, fpath in modules]


def _get_module(modules, name):
    """Returns a specialization module.

    """
    for module in modules:
        if module.__name__ == name:
            return module


def _is_target(filename, specialization_type):
    """Returns flag indicating whether a module is a specialization target or not.

    """
    return not filename.startswith('_') and \
           filename.endswith('.py') and \
           filename.startswith(specialization_type)
