# -*- coding: utf-8 -*-

"""
.. module:: run_delete_ingest_files.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Deletes ingest files from document archive.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc



def _main():
    """Main entry point.

    """
    pyesdoc.archive.delete_ingested_files()


# Entry point.
if __name__ == '__main__':
    _main()
