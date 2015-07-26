# -*- coding: utf-8 -*-

"""
.. module:: run_convert_document.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Converts a document held upon local file system.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options

import pyesdoc



# Define command line options.
define("file", help="Path to file to be converted.")
define("encoding", help="Encoding to which file will be converted.")


def _main():
    """Main entry point.

    """
    pyesdoc.convert_file(options.file, options.encoding)



# Entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()