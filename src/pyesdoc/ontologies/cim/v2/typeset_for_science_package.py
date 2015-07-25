# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_science_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.science package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_science_package as science
import typeset_for_shared_package as shared



class ProcessDetail(object):
    """A concrete class within the cim v2 type system.

    Three possible implementations of process_detail:
        1) A generic description of some aspect of detail,
        2) Several specific descriptions selected from a vocabulary, or
        3) One specfic property selected from a vocabulary

    """
    def __init__(self):
        """Constructor.

        """
        super(ProcessDetail, self).__init__()

        self.content = None                               # shared.Cimtext
        self.heading = None                               # str
        self.properties = []                              # shared.KeyFloat
        self.selection = []                               # str
        self.vocabulary = None                            # str


class GridSummary(object):
    """A concrete class within the cim v2 type system.

    Key scientific characteristics of the grid use to simulate a specific domain

    """
    def __init__(self):
        """Constructor.

        """
        super(GridSummary, self).__init__()

        self.grid_extent = None                           # science.Extent
        self.grid_layout = None                           # science.GridLayouts
        self.grid_type = None                             # science.GridTypes


class Resolution(object):
    """A concrete class within the cim v2 type system.

    Describes the computational spatial resolution of a component or process. Not intended
        to replace or replicate the output grid description.  When it appears as part of a process
        description, provide only properties that differ from parent domain. Note that where
        different variables have different grids, differences in resolution can be captured by
        repeating the number_of_ properties.

    """
    def __init__(self):
        """Constructor.

        """
        super(Resolution, self).__init__()

        self.equivalent_horizontal_resolution = None      # float
        self.is_adaptive_grid = None                      # bool
        self.name = None                                  # str
        self.number_of_levels = []                        # int
        self.number_of_xy_gridpoints = []                 # int


class Extent(object):
    """A concrete class within the cim v2 type system.

    Key scientific characteristics of the grid use to simulate a specific domain.
    Note that the extent does not itself describe a grid, so, for example, a polar
    stereographic grid may have an extent of northern boundary 90N, southern boundary
    45N, but the fact that it is PS comes from the grid_type.

    """
    def __init__(self):
        """Constructor.

        """
        super(Extent, self).__init__()

        self.eastern_boundary = None                      # float
        self.is_global = None                             # bool
        self.maximum_vertical_level = None                # float
        self.minimum_vertical_level = None                # float
        self.northern_boundary = None                     # float
        self.region_known_as = []                         # str
        self.southern_boundary = None                     # float
        self.western_boundary = None                      # float
        self.z_units = None                               # str


class ScientificDomain(object):
    """A concrete class within the cim v2 type system.

    Scientific area of a numerical model - usually a sub-model or component.
    Can also be known as a realm

    """
    def __init__(self):
        """Constructor.

        """
        super(ScientificDomain, self).__init__()

        self.extra_conservation_properties = None         # science.ConservationProperties
        self.grid = None                                  # science.GridSummary
        self.meta = shared.Meta()                         # shared.Meta
        self.name = None                                  # str
        self.overview = None                              # shared.Cimtext
        self.realm = None                                 # str
        self.references = []                              # shared.Reference
        self.resolution = None                            # science.Resolution
        self.simulates = []                               # science.Process
        self.time_step = None                             # float


class Algorithm(object):
    """A concrete class within the cim v2 type system.

    Used to hold information associated with a process algorithm and it's properties.
    Expected to be used to describe aspects of how a process is implemented.

    """
    def __init__(self):
        """Constructor.

        """
        super(Algorithm, self).__init__()

        self.diagnostic_variables = []                    # data.VariableCollection
        self.heading = None                               # str
        self.implementation_overview = None               # shared.Cimtext
        self.prognostic_variables = []                    # data.VariableCollection
        self.references = []                              # shared.Citation


class Process(object):
    """A concrete class within the cim v2 type system.

    Provides structure for description of a process simulated within a particular
    area (or domain/realm/component) of a model. This will often be subclassed
    within a specific implementation so that constraints can be used to ensure
    that the vocabulary used is consistent with project requirements.

    """
    def __init__(self):
        """Constructor.

        """
        super(Process, self).__init__()

        self.algorithm_properties = []                    # science.Algorithm
        self.description = None                           # str
        self.detailed_properties = []                     # science.ProcessDetail
        self.implementation_overview = None               # shared.Cimtext
        self.keywords = None                              # str
        self.name = None                                  # str
        self.references = []                              # shared.Reference
        self.time_step_in_process = None                  # float


class Tuning(object):
    """A concrete class within the cim v2 type system.

    Method used to optimise equation parameters in model component (aka "tuning")

    """
    def __init__(self):
        """Constructor.

        """
        super(Tuning, self).__init__()

        self.description = None                           # shared.Cimtext
        self.global_mean_metrics_used = None              # data.VariableCollection
        self.regional_metrics_used = None                 # data.VariableCollection
        self.trend_metrics_used = None                    # data.VariableCollection


class ConservationProperties(object):
    """A concrete class within the cim v2 type system.

    Describes how prognostic variables are conserved

    """
    def __init__(self):
        """Constructor.

        """
        super(ConservationProperties, self).__init__()

        self.corrected_conserved_prognostic_variables = None# data.VariableCollection
        self.correction_methodology = None                # shared.Cimtext
        self.flux_correction_was_used = None              # bool


class GridLayouts(object):
    """An enumeration within the cim v2 type system.

    Defines the set of grid layouts (e.g. Arakawa C-Grid) which are understood
    """

    pass


class GridTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the set of grid types (e.g Cubed Sphere) which are understood
    """

    pass


class ModelTypes(object):
    """An enumeration within the cim v2 type system.

    Defines a set of gross model classes
    """

    pass


