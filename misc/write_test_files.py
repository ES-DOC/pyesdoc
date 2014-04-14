# Module imports.
from os.path import abspath, basename, join, dirname, exists, splitext

import tornado.template as template

import pyesdoc
import pyesdoc.ontologies.cim as cim
import test_utils as tu
import test_types as tt


# Output folder.
OP_FILES = join(join(dirname(dirname(abspath(__file__))), "tests"), "files")


def _get_file_name(mod, encoding):
    path = join(OP_FILES, mod.DOC_FILE)
    path = splitext(path)[0]
    path = path + "." + encoding

    return path


def _write_file(mod, doc, encoding):
    encoded = pyesdoc.encode(doc, encoding)
    with open(_get_file_name(mod, encoding), 'w') as f:
        f.write(encoded)


def _main():
    for mod in tt.MODULES:
        doc = tu.get_doc(mod)
        for encoding in pyesdoc.ESDOC_ENCODINGS_FILE:
            try:
                _write_file(mod, doc, encoding)
            except Exception as err:
                print "ERR ::", doc.type_key, " ::", err  


if __name__ == '__main__':
    _main()
