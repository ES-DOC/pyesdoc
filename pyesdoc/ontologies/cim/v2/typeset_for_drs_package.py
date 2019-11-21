"""
.. module:: cim.v2.typeset_for_drs_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.drs package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid




class DrsAtomicDataset(object):
    """A concrete class within the cim v2 type system.

    An entity in a DRS file system.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DrsAtomicDataset, self).__init__()

        self.frequency = None                             # drs.DrsFrequencyTypes (1.1)
        self.geographical_constraint = None               # drs.DrsGeographicalIndicator (0.1)
        self.mip_table = None                             # unicode (1.1)
        self.realm = None                                 # drs.DrsRealms (0.1)
        self.temporal_constraint = None                   # drs.DrsTemporalIdentifier (0.1)
        self.variable_name = None                         # unicode (1.1)
        self.version_number = None                        # int (0.1)


class DrsEnsembleIdentifier(object):
    """A concrete class within the cim v2 type system.

    Identifies a 'response ensemble' realisation using the semantic content ofa 'run_variant_id'.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DrsEnsembleIdentifier, self).__init__()

        self.forcing_number = None                        # int (0.1)
        self.initialisation_method_number = None          # int (1.1)
        self.perturbation_number = None                   # int (1.1)
        self.realisation_number = None                    # int (1.1)


class DrsExperiment(object):
    """A concrete class within the cim v2 type system.

    An encoding of a drs experiment_id.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DrsExperiment, self).__init__()

        self.axis_identifer = None                        # designing.AxisMember (0.1)
        self.axis_type = None                             # designing.EnsembleTypes (0.1)
        self.family = None                                # unicode (1.1)


class DrsGeographicalIndicator(object):
    """A concrete class within the cim v2 type system.

    Specifies geographical subsets described by bounding boxes or by named regions.
     One of spatial domain or bounding box must appear.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DrsGeographicalIndicator, self).__init__()

        self.bounding_box = None                          # unicode (0.1)
        self.operator = None                              # drs.DrsGeographicalOperators (0.1)
        self.spatial_domain = None                        # unicode (0.1)


class DrsPublicationDataset(object):
    """A concrete class within the cim v2 type system.

    PLACEHOLDER for the real drs_publication_dataset.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DrsPublicationDataset, self).__init__()



class DrsSimulationIdentifier(object):
    """A concrete class within the cim v2 type system.

    That part of the DRS which identifies the response to the experiment: the simulation.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DrsSimulationIdentifier, self).__init__()

        self.institute = None                             # unicode (1.1)
        self.model = None                                 # unicode (1.1)
        self.run_variant_id = None                        # drs.DrsEnsembleIdentifier (1.1)


class DrsTemporalIdentifier(object):
    """A concrete class within the cim v2 type system.

    Provides information about temporal subsetting and/or averaging.
    If only N1 is present, it a temporal instant,
    If N1-N2 are present with no suffix, it is a temporal subset,
    If N1-N2 with a suffix are present, then some sort of temporal averaging has been applied across
    the period.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DrsTemporalIdentifier, self).__init__()

        self.end = None                                   # unicode (0.1)
        self.start = None                                 # unicode (1.1)
        self.suffix = None                                # drs.DrsTimeSuffixes (0.1)


class DrsFrequencyTypes(object):
    """An enumeration within the cim v2 type system.

    Set of allowed DRS frequency types.
    """
    is_open = False
    members = [
        "yr",
        "mon",
        "day",
        "6hr",
        "3hr",
        "subhr",
        "monClim",
        "fx"
        ]
    descriptions = [
        "Yearly",
        "Monthly",
        "Daily",
        "Every six hours",
        "Every three hours",
        "Sampling frequency less than an hour",
        "Climatological Monthly Mean",
        "Fixed Time independent"
        ]


class DrsGeographicalOperators(object):
    """An enumeration within the cim v2 type system.

    Set of permitted spatial averaging operator suffixes for drs spatial indicators (yyyy-zzzz).
    """
    is_open = False
    members = [
        "zonalavg",
        "lnd-zonalavg",
        "ocn-zonalavg",
        "areaavg",
        "lnd-areaavg",
        "ocn-areaavg"
        ]
    descriptions = [
        "Data is zonally averaged",
        "Data is zonally averaged over land in region",
        "Data is zonally averaged over oceans in region",
        "Data is averaged over the area of the region",
        "Data is averaged over the land area of the region",
        "Data is averaged over the ocean area of the region"
        ]


class DrsRealms(object):
    """An enumeration within the cim v2 type system.

    Set of allowed DRS modelling realms.
    """
    is_open = False
    members = [
        "atmos",
        "ocean",
        "land",
        "landIce",
        "seaIce",
        "aerosol",
        "atmosChem",
        "ocnBgchem"
        ]
    descriptions = [
        "Atmosphere",
        "Ocean",
        "Land",
        "Land Ice",
        "Sea Ice",
        "Aerosol",
        "Atmospheric Chemistry",
        "Ocean Biogeochemistry"
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
    descriptions = [
        "Indicates data is a single average of DRS frequency data across temporal period N1-N2",
        "Indicates data is climatological average data at the DRS frequency from the period N1-N2"
        ]


