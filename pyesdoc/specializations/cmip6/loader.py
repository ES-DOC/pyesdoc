"""
.. module:: utils.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: CMIP6 specialization validation utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import imp
import os



def get_specializations(input_dir, realm):
    """Returns specialization modules organized by type.

    :param str input_dir: Directory within which modules reside.
    :param str realm: Name of realm being processed.

    """
    def is_target(filename):
        """Returns flag indicating whether a module is a specialization target or not.

        """
        return not filename.startswith('_') and \
               filename.endswith('.py') and \
               filename.startswith(realm)

    # Load specialization modules.
    modules = sorted([i for i in os.listdir(input_dir) if is_target(i)])
    modules = [os.path.join(input_dir, m) for m in modules]
    modules = [(m.split("/")[-1].split(".")[0], m) for m in modules]
    modules = [imp.load_source(name, fpath) for name, fpath in modules]

    # Organize specialization modules.
    realm = grid = key_properties = None
    processes = []
    for module in modules:
        if realm is None:
            realm = module
        elif module.__name__.endswith('_grid'):
            grid = module
        elif module.__name__.endswith('_key_properties'):
            key_properties = module
        else:
            processes.append(module)

    return realm, grid, key_properties, processes


