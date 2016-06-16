# -*- coding: utf-8 -*-

"""
.. module:: run_archive_cmip6_documents.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Writes CMIP6 documents to archive.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import argparse
import glob
import hashlib
import os
import shutil



# Define command line options.
_parser = argparse.ArgumentParser("Archives CIM documents extracted from CMIP6 experiment spreadsheet.")
_parser.add_argument(
    "--source-dir",
    help="Path to a directory from which documents will be archived.",
    dest="source_dir",
    type=str
    )
_parser.add_argument(
    "--target-dir",
    help="Path to archive directory.",
    dest="target_dir",
    type=str
    )


def _main(source_dir, target_dir):
    """Main entry point.

    """
    if not os.path.isdir(source_dir):
        raise ValueError("Source directory does not exist")
    if not os.path.isdir(target_dir):
        raise ValueError("Target directory does not exist")

    for src in glob.iglob(os.path.join(source_dir, "*.json")):
        dest = hashlib.md5(src.split("/")[-1]).hexdigest()
        dest += ".json"
        dest = os.path.join(target_dir, dest)
        shutil.copyfile(src, dest)


# Entry point.
if __name__ == '__main__':
    args = _parser.parse_args()
    _main(args.source_dir, args.target_dir)