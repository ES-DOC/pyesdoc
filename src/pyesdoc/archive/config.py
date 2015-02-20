# -*- coding: utf-8 -*-
"""
.. module:: config.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Configuration utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

from ..utils import config



# Archive location comes from config.
DIR_ARCHIVE = config.archive.location
if not os.path.exists(DIR_ARCHIVE):
    raise IOError("Archive directory does not exist: {0}".format(DIR_ARCHIVE))


# Set of supported projects.
projects = config.archive.projects

# Set of supported sources.
sources = config.archive.sources


def get_project_sources():
    """Returns iterable of unique project/source pairs.

    """
    result = []
    for project in projects:
        for source in (f.source for f in project.feeds):
            if (project.name, source) not in result:
                result.append((project.name, source))

    return tuple(result)
  