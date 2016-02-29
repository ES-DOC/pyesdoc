# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_drs_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.drs package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import abc
import datetime
import uuid




class DrsEnsembleIdentifier(object):
    """A concrete class within the cim v2 type system.

    Identifies an ensemble realisation.

    """
    def __init__(self):
        """Constructor.

        """
        super(DrsEnsembleIdentifier, self).__init__()

        self.initialisation_method_number = None          # int (1.1)
        self.perturbation_number = None                   # int (1.1)
        self.realisation_number = None                    # int (1.1)


class DrsGeographicalIndicator(object):
    """A concrete class within the cim v2 type system.

    Specifies geographical subsets described by bounding boxes or by named regions.
     One of spatial domain or bounding box must appear.

    """
    def __init__(self):
        """Constructor.

        """
        super(DrsGeographicalIndicator, self).__init__()

        self.bounding_box = None                          # unicode (0.1)
        self.operator = None                              # drs.DrsGeographicalOperators (0.1)
        self.spatial_domain = None                        # unicode (0.1)


class DrsPublicationDataset(object):
    """A concrete class within the cim v2 type system.

    A collection of atomic datasets which share a single combination of DRS component values.

    """
    def __init__(self):
        """Constructor.

        """
        super(DrsPublicationDataset, self).__init__()

        self.activity = None                              # unicode (1.1)
        self.experiment = None                            # unicode (1.1)
        self.frequency = None                             # drs.DrsFrequencyTypes (0.1)
        self.institute = None                             # unicode (1.1)
        self.model = None                                 # unicode (1.1)
        self.product = None                               # unicode (1.1)
        self.realm = None                                 # drs.DrsRealms (0.1)
        self.version_number = None                        # int (0.1)


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

        self.end = None                                   # unicode (0.1)
        self.start = None                                 # unicode (1.1)
        self.suffix = None                                # drs.DrsTimeSuffixes (0.1)


class DrsAtomicDataset(DrsPublicationDataset):
    """A concrete class within the cim v2 type system.

    An entity in a DRS file system.

    """
    def __init__(self):
        """Constructor.

        """
        super(DrsAtomicDataset, self).__init__()

        self.ensemble_member = None                       # drs.DrsEnsembleIdentifier (1.1)
        self.geographical_constraint = None               # drs.DrsGeographicalIndicator (0.1)
        self.mip_table = None                             # unicode (1.1)
        self.temporal_constraint = None                   # drs.DrsTemporalIdentifier (0.1)
        self.variable_name = None                         # unicode (1.1)


class DrsFrequencyTypes(object):
    """An enumeration within the cim v2 type system.

    Set of allowed DRS frequency types.
    """
    is_open = False
    members = [
        "3hr",
        "6hr",
        "day",
        "fx",
        "mon",
        "monClim",
        "subhr",
        "yr"
        ]


class DrsGeographicalOperators(object):
    """An enumeration within the cim v2 type system.

    Set of permitted spatial averaging operator suffixes for drs spatial indicators (yyyy-zzzz).
    """
    is_open = False
    members = [
        "areaavg",
        "lnd-areaavg",
        "lnd-zonalavg",
        "ocn-areaavg",
        "ocn-zonalavg",
        "zonalavg"
        ]


class DrsRealms(object):
    """An enumeration within the cim v2 type system.

    Set of allowed DRS modelling realms.
    """
    is_open = False
    members = [
        "aerosol",
        "atmos",
        "atmosChem",
        "land",
        "landIce",
        "ocean",
        "ocnBgchem",
        "seaIce"
        ]


class DrsTimeSuffixes(object):
    """An enumeration within the cim v2 type system.

    Set of permitted time averaging suffixes for drs temporal identifiers.
    """
    is_open = False
    members = [
        "avg",
        "clim"
        ]


