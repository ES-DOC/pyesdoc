# -*- coding: utf-8 -*-

"""
.. module:: populate.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Populates archive with documents pulled from remote sources.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import pyesdoc



# Define command line options.
_ARGS = argparse.ArgumentParser("Emits a validation report over an ontology schema.")
_ARGS.add_argument(
    "--throttle",
    help="Limit upon number of documents to populate.",
    dest="throttle",
    type=int,
    default=0
    )
_ARGS.add_argument(
    "--project",
    help="Project code of documents to be populated.",
    dest="project",
    type=str,
    default=None
    )


def _main(args):
    """Main entry point.

    """
    pyesdoc.archive.init()
    pyesdoc.archive.populate(args.throttle, args.project)



# Main entry point.
if __name__ == '__main__':
    _main(_ARGS.parse_args())
