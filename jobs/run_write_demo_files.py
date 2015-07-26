# -*- coding: utf-8 -*-

"""
.. module:: write_demo_files.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Writes demo files to the file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from os.path import abspath, join, dirname

import tornado.template as template
from tornado.options import define, options

import pyesdoc
import test_utils as tu
import test_types as tt



# Define command line options.
define("outdir", help="Path to directory to which to write outputs")


# Demo document template.
_TEMPLATE = dirname(abspath(__file__))
_TEMPLATE = template.Loader(_TEMPLATE).load("run_write_demo_files_template.html")


def _get_file_path(doc):
    """Gets document file path in readiness for io.

    """
    fpath = "{0}-{1}.{2}".format(
        doc.meta.project.upper(),
        doc.__class__.type_key.upper().replace(".", "-"),
        pyesdoc.ESDOC_ENCODING_HTML)

    return join(options.outdir, fpath)


def _write(doc):
    """Writes a document html file.

    """
    with open(_get_file_path(doc), 'w') as op_file:
        doc = pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_HTML)
        doc = _TEMPLATE.generate(body=doc)
        op_file.write(doc)


def _main():
    """Main entry point.

    """
    for doc in [tu.get_doc(m) for m in tt.MODULES]:
        try:
            _write(doc)
        except Exception as err:
            msg = "ERR:: {0} :: {1}".format(doc.type_key, err)
            print(msg)


# Entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
