"""
.. module:: config.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Configuration utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# -*- coding: utf-8 -*-

# Module imports.
import os

from ..utils import convert as convertor



# Configuration file name.
_CONFIG_FILENAME = "config.json"

# Configuration file path.
_CONFIG_FILEPATH = os.path.dirname(os.path.abspath(__file__))
_CONFIG_FILEPATH = os.path.join(_CONFIG_FILEPATH, _CONFIG_FILENAME)

# Configuration file info.
_cfg = convertor.json_file_to_namedtuple(_CONFIG_FILEPATH)

# Default archive location.
_DEFAULT_ARCHIVE_LOCATION = "./documents"

# Archive root directory.
if _cfg.location != _DEFAULT_ARCHIVE_LOCATION:
    DIR_ARCHIVE = _cfg.location
else:
    DIR_ARCHIVE = os.path.dirname(os.path.abspath(__file__))
    DIR_ARCHIVE = os.path.join(DIR_ARCHIVE, "documents")
if not os.path.exists(DIR_ARCHIVE):
    raise IOError("Archive directory does not exist: {0}".format(DIR_ARCHIVE))


# Set of supported projects.
projects = _cfg.projects

# Set of supported sources.
sources = _cfg.sources


def get_project_sources():
    """Returns iterable of unique project/source pairs."""
    result = []
    for project in _cfg.projects:
        for source in (f.source for f in project.feeds):
            if (project.name, source) not in result:
                result.append((project.name, source))

    return tuple(result)