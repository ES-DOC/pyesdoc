# -*- coding: utf-8 -*-

"""
.. module:: run_archive_populate.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Populates archive with documents pulled from remote sources.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from tornado.options import define, options

import pyesdoc


# Define command line options.
define("throttle", help="Limit upon number of documents to populate", type=int, default=0)
define("project", help="Project code of documents to be populated", type=str, default=None)



def _main():
    """Main entry point.

    """
    pyesdoc.archive.init()
    pyesdoc.archive.populate(options.throttle, options.project)



# Entry point.
if __name__ == '__main__':
    options.parse_command_line()
    _main()
