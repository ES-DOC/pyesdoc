# -*- coding: utf-8 -*-
"""
.. module:: config.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Configuration utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.utils import config



def get_project_sources():
    """Returns iterable of unique project/source pairs.

    """
    config.init()

    result = []
    for project in get_projects():
        for source in (f.source for f in project.feeds):
            if (project.name, source) not in result:
                result.append((project.name, source))

    return tuple(result)


def get_directory():
    """Returns archive directory as defined withn pyesdoc.conf.

    """
    config.init()

    return config.data.archive.location


def get_projects():
    """Returns set of archive projects.

    """
    config.init()

    return config.data.archive.projects


def get_sources():
    """Returns set of archive sources.

    """
    config.init()

    return config.data.archive.sources

