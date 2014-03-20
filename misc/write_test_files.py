# Module imports.
from os.path import abspath, join, dirname, exists

import tornado.template as template

import pyesdoc
import pyesdoc.ontologies.cim as cim
import test_utils as tu
import test_types as tt


# Output folder.
OP_FILES = join(join(dirname(dirname(abspath(__file__))), "tests"), "files")


def _get_file_name(doc, encoding):
    path = join(OP_FILES, doc.__class__.type_key)

    return path + "." + encoding


def _write_file(doc, encoding):
    encoded = pyesdoc.encode(doc, encoding)
    with open(_get_file_name(doc, encoding), 'w') as f:
        f.write(encoded)


def _main():
    for tm in tt.MODULES:
        doc = tu.get_doc(tm)
        for encoding in pyesdoc.ESDOC_ENCODINGS_FILE:
            try:
                _write_file(doc, encoding)
            except Exception as err:
                print "ERR ::", doc.type_key, " ::", err  


if __name__ == '__main__':
    _main()
