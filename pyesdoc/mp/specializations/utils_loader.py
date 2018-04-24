"""
.. module:: utils_loader.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Loads CMIP6 specialization from file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import imp
import json
import os
import glob



def get_short_tables_definitions(input_dir, typeof):
    """Returns specialization short tables.

    :param str input_dir: Directory within which modules reside.
    :param str typeof: Type of specialization being processed.

    :returns: Tuple of decoded short tables.
    :rtype: tuple

    """
    def _decode(fpath):
        name = fpath.split("/")[-1].split(".")[0].replace("_short_table", "")
        with open(fpath, 'r') as fstream:
            return name, json.loads(fstream.read())

    fpaths = os.path.join(input_dir, "short_tables")
    fpaths = os.path.join(fpaths, "{}_*.json".format(typeof))
    tables = [_decode(i) for i in glob.glob(fpaths)]

    return sorted(tables, key=lambda i: i[0])


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
    children = [_get_module(modules, i) for i in [
        '{}_key_properties'.format(typeof),
        '{}_grid'.format(typeof)
    ] + root.PROCESSES]

    return [root] + [i for i in children if i is not None]


def _get_modules(input_dir, typeof):
    """Returns a set of specialization modules.

    """
    def _is_target(fname):
        return not fname.startswith('_') and \
               fname.endswith('.py') and \
               fname.startswith(typeof)

    modules = sorted([i for i in os.listdir(input_dir) if _is_target(i)])
    modules = [os.path.join(input_dir, m) for m in modules]
    modules = [(m.split("/")[-1].split(".")[0], m) for m in modules]
    modules = [imp.load_source(i, j) for i, j in modules]

    return modules


def _get_module(modules, name):
    """Returns a specialization module.

    """
    for module in modules:
        if module.__name__ == name:
            return module
