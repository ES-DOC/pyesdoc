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

import pyesdoc


_FILEPATHS = [
    "/Users/macg/Documents/cim-simulation.xml",
    "/Users/macg/Documents/cim-experiment.xml"
    ]



def _main():
    """Main entry point."""
    for fp in _FILEPATHS:
        print pyesdoc.read(fp, pyesdoc.METAFOR_CIM_XML_ENCODING)


# Entry point.
if __name__ == '__main__':
    _main()
