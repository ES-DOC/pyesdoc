# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_drs_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.drs package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_drs_package as drs



class DrsEnsembleIdentifier(object):
    """A concrete class within the cim v2 type system.

    Identifies an ensemble realisation.

    """
    def __init__(self):
        """Constructor.

        """
        super(DrsEnsembleIdentifier, self).__init__()

        self.initialisation_method_number = None          # int
        self.perturbation_number = None                   # int
        self.realisation_number = None                    # int


class DrsPublicationDataset(object):
    """A concrete class within the cim v2 type system.

    A collection of atomic datasets which share a single combination of DRS component values

    """
    def __init__(self):
        """Constructor.

        """
        super(DrsPublicationDataset, self).__init__()

        self.activity = None                              # str
        self.experiment = None                            # str
        self.frequency = None                             # drs.DrsFrequencyTypes
        self.institute = None                             # str
        self.model = None                                 # str
        self.product = None                               # str
        self.realm = None                                 # drs.DrsRealms
        self.version_number = None                        # int


class DrsTemporalIdentifier(object):
    """A concrete class within the cim v2 type system.

    Provides information about temporal subsetting and/or averaging.
    If only N1 is present, it a temporal instant,
    If N1-N2 are present with no suffix, it is a temporal subset,
    If N1-N2 with a suffix are present, then some sort of temporal averaging has been applied across
    the period.

    """
    def __init__(self):
        """Constructor.

        """
        super(DrsTemporalIdentifier, self).__init__()

        self.end = None                                   # str
        self.start = None                                 # str
        self.suffix = None                                # drs.DrsTimeSuffixes


class DrsGeographicalIndicator(object):
    """A concrete class within the cim v2 type system.

    Specifies geographical subsets described by bounding boxes or by named regions.
     One of spatial domain or bounding box must appear.

    """
    def __init__(self):
        """Constructor.

        """
        super(DrsGeographicalIndicator, self).__init__()

        self.bounding_box = None                          # str
        self.operator = None                              # drs.DrsGeographicalOperators
        self.spatial_domain = None                        # str


class DrsAtomicDataset(DrsPublicationDataset):
    """A concrete class within the cim v2 type system.

    An entity in a DRS file system

    """
    def __init__(self):
        """Constructor.

        """
        super(DrsAtomicDataset, self).__init__()

        self.ensemble_member = None                       # drs.DrsEnsembleIdentifier
        self.geographical_constraint = None               # drs.DrsGeographicalIndicator
        self.mip_table = None                             # str
        self.temporal_constraint = None                   # drs.DrsTemporalIdentifier
        self.variable_name = None                         # str


class DrsFrequencyTypes(object):
    """An enumeration within the cim v2 type system.

    Set of allowed DRS frequency types
    """

    pass


class DrsGeographicalOperators(object):
    """An enumeration within the cim v2 type system.

    Set of permitted spatial averaging operator suffixes for drs spatial indicators (yyyy-zzzz)
    """

    pass


class DrsRealms(object):
    """An enumeration within the cim v2 type system.

    Set of allowed DRS modelling realms
    """

    pass


class DrsTimeSuffixes(object):
    """An enumeration within the cim v2 type system.

    Set of permitted time averaging suffixes for drs temporal identifiers.
    """

    pass


