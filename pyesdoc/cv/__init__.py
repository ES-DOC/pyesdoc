# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.cv.__init__.py

   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL / CeCILL
   :platform: Unix
   :synopsis: Python earth science standard vocabulary package intializer.

.. moduleauthor:: IPSL (ES-DOC) <dev@esdocumentation.org>

"""
from pyesdoc.cv.codecs import decode
from pyesdoc.cv.codecs import encode
from pyesdoc.cv.constants import *
from pyesdoc.cv.exceptions import *
from pyesdoc.cv.partition import Partition
from pyesdoc.cv.term import Term
from pyesdoc.cv.termset import Termset



# Synonyms for the masses.
Facet = Term

# Synonyms for the masses.
Facetset = Termset


# Managed partitions.
_PARTITIONS = dict()


def create_partition(domain, io_dir):
    """Creates & returns a partition.

    :param str domain: Partition domain.
    :param str io_dir: Partition io directory.

    :returns: A partition ready for action.
    :rtype: pyesdoc.cv.partition.Partition

    """
    namespace = u"{}".format(domain).lower()

    _PARTITIONS[namespace] = Partition(domain, io_dir)

    return _PARTITIONS[namespace]


def get_partition(domain):
    """Returns a vocabulary partition.

    :param str domain: Partition domain.

    :returns: Partition information.
    :rtype: pyesdoc.cv.partitions.Partition

    """
    namespace = "{}".format(domain).lower()

    return _PARTITIONS[namespace]


def show_partitions():
    """Writes to stdout the set of partitions.

    """
    for idx, partition in enumerate(_PARTITIONS.values()):
        print("{} PARTITION #{}:".format(__title__.upper(), idx + 1))
        print("\tdomain = {}".format(partition.domain))
        print("\tio-dir = {}".format(partition.io.root_dir))

