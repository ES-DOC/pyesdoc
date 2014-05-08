"""
.. module:: write_demo_files.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Writes demo files to the file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from os.path import abspath, join, dirname

import tornado.template as template

import pyesdoc
import test_utils as tu
import test_types as tt



# Output folder.
OP = dirname(abspath(__file__))
OP = dirname(OP)
OP = dirname(OP)
OP = join(OP, "esdoc-viewer")
OP = join(OP, "src")
OP = join(OP, "media")
OP = join(OP, "html")

# Demo document template.
_TEMPLATE = dirname(abspath(__file__))
_TEMPLATE = template.Loader(_TEMPLATE).load("demo_document_TEMPLATE.html")


def _get_file_name(doc):
    """Gets document file name in readiness for io."""
    path = join(OP, doc.meta.project.upper())
    path += '-'
    path += doc.__class__.type_key.upper().replace(".", "-")
    path += '.'
    path += pyesdoc.ESDOC_ENCODING_HTML

    return path


def _write(doc):
    """Writes a document html file."""
    as_html = pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_HTML)
    with open(_get_file_name(doc), 'w') as op_file:
        op_file.write(_TEMPLATE.generate(body=as_html))


def _main():
    """Main entry point."""
    for mod in tt.MODULES:
        doc = tu.get_doc(mod)
        try:
            _write(doc)
        except Exception as err:
            print "ERR ::", doc.type_key, " ::", err


# Entry point.
if __name__ == '__main__':
    _main()
