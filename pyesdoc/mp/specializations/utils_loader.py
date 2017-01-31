"""
.. module:: loader.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Loads CMIP6 specialization from file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import imp
import os



# Realm name overrides.
REALM_NAME_OVERRIDES = {
    "ocean-bgc": "oceanbgc"
}


def get_realm_specializations(input_dir, realm_name):
    """Returns specialization modules organized by type.

    :param str input_dir: Directory within which modules reside.
    :param str realm_name: Name of realm being processed.

    """
    # Reformat realm name when running from specializations repo.
    try:
        realm_name = REALM_NAME_OVERRIDES[realm_name]
    except KeyError:
        pass

    def get_module(modules, name):
        for module in modules:
            if module.__name__ == name:
                return module


    def is_target(filename):
        """Returns flag indicating whether a module is a specialization target or not.

        """
        return not filename.startswith('_') and \
               filename.endswith('.py') and \
               filename.startswith(realm_name)


    # Load specialization modules.
    modules = sorted([i for i in os.listdir(input_dir) if is_target(i)])
    modules = [os.path.join(input_dir, m) for m in modules]
    modules = [(m.split("/")[-1].split(".")[0], m) for m in modules]
    modules = [imp.load_source(name, fpath) for name, fpath in modules]
    if not modules:
        raise KeyError("Realm specializations not found")

    # Set specializations.
    realm = get_module(modules, realm_name)
    grid = get_module(modules, "{}_grid".format(realm_name))
    key_properties = get_module(modules, "{}_key_properties".format(realm_name))
    processes = [get_module(modules, p) for p in realm.PROCESSES]

    return realm, grid, key_properties, processes
