# -*- coding: utf-8 -*-

"""
.. module:: echo.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Outputs a document to stdout.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options

import pyesdoc



# Define command line options.
define("uid", help="Document unique identifer")
define("version", help="Document verstion", type=int)


def _main():
    """Main entry point.

    """
    pyesdoc.archive.init()

    document = pyesdoc.archive.load(options.uid, options.version)
    if not document:
        pyesdoc.rt.log("document not found")
    else:
        print document


# Entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
