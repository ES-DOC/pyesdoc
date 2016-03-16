# -*- coding: utf-8 -*-

"""
.. module:: write_test_files.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Writes test files to the file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from os.path import join, splitext

from tornado.options import define, options

import pyesdoc
import pyesdoc.ontologies.cim as cim
import test_utils as tu
import test_types as tt



# Define command line options.
define("outdir", help="Path to directory to which to write outputs")


def _get_file_path(mod, encoding):
    """Returns test file path in readiness for io.

    """
    path = join(options.outdir, mod.DOC_FILE)
    path = splitext(path)[0]
    path = path + "." + encoding

    return path


def _write_file(mod, doc, encoding):
    """Writes test file to file system.

    """
    fpath = _get_file_path(mod, encoding)
    with open(fpath, 'w') as op_file:
        encoded = pyesdoc.encode(doc, encoding)
        op_file.write(encoded)


def _main():
    """Main entry point.

    """
    for mod in tt.MODULES:
        doc = tu.get_doc(mod)
        for encoding in pyesdoc.ENCODINGS_FILE:
            try:
                _write_file(mod, doc, encoding)
            except Exception as err:
                msg = "ERR:: {0} :: {1}".format(doc.type_key, err)
                print(msg)


# Entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
