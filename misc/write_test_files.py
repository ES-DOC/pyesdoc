"""
.. module:: write_test_files.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Writes test files to the file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from os.path import abspath, join, dirname, splitext

import pyesdoc
import pyesdoc.ontologies.cim as cim
import test_utils as tu
import test_types as tt



# Output folder.
OP = dirname(abspath(__file__))
OP = dirname(OP)
OP = join(OP, "tests")
OP = join(OP, "files")


def _get_file_name(mod, encoding):
    """Returns test file name in readiness for io."""
    path = join(OP, mod.DOC_FILE)
    path = splitext(path)[0]
    path = path + "." + encoding

    return path


def _write_file(mod, doc, encoding):
    """Writes test file to file system."""
    encoded = pyesdoc.encode(doc, encoding)
    with open(_get_file_name(mod, encoding), 'w') as op_file:
        op_file.write(encoded)


def _main():
    """Main entry point."""
    for mod in tt.MODULES:
        doc = tu.get_doc(mod)
        for encoding in pyesdoc.ESDOC_ENCODINGS_FILE:
            try:
                _write_file(mod, doc, encoding)
            except Exception as err:
                print "ERR ::", doc.type_key, " ::", err


# Entry point.
if __name__ == '__main__':
    _main()
