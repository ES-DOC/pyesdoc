# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_science_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.science package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared
import typeset_for_software_package as software



class Algorithm(object):
    """A concrete class within the cim v2 type system.

    Used to hold information associated with an algorithm which implements some key
    part of a process. In most cases this is quite a high level concept and isn't intended
    to describe the gory detail of how the code implements the algorithm rather the key
    scientific aspects of the algorithm. In particular, it provides a method
    of grouping variables which take part in an algorithm within a process.

    """
    def __init__(self):
        """Constructor.

        """
        super(Algorithm, self).__init__()

        self.diagnostic_variables = []                    # data.VariableCollection
        self.heading = None                               # unicode
        self.implementation_overview = None               # unicode
        self.prognostic_variables = []                    # data.VariableCollection
        self.references = []                              # shared.Citation


class ConservationProperties(object):
    """A concrete class within the cim v2 type system.

    Describes how prognostic variables are conserved.

    """
    def __init__(self):
        """Constructor.

        """
        super(ConservationProperties, self).__init__()

        self.corrected_conserved_prognostic_variables = None# data.VariableCollection
        self.correction_methodology = None                # unicode
        self.flux_correction_was_used = None              # bool


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
        self.region_known_as = []                         # unicode
        self.southern_boundary = None                     # float
        self.western_boundary = None                      # float
        self.z_units = None                               # unicode


class GridSummary(object):
    """A concrete class within the cim v2 type system.

    Key scientific characteristics of the grid use to simulate a specific domain.

    """
    def __init__(self):
        """Constructor.

        """
        super(GridSummary, self).__init__()

        self.grid_extent = None                           # science.Extent
        self.grid_layout = None                           # science.GridLayouts
        self.grid_type = None                             # science.GridTypes


class Model(software.ComponentBase):
    """A concrete class within the cim v2 type system.

    A model component: can be executed standalone, and has as scientific
    description available via a link to a science.domain document. (A configured model can
     be understood in terms of a simulation, a model, and a configuration.).

    """
    def __init__(self):
        """Constructor.

        """
        super(Model, self).__init__()

        self.category = None                              # science.ModelTypes
        self.coupled_software_components = []             # science.Model
        self.coupled_software_components_references = []  # shared.DocReference
        self.coupler = None                               # software.CouplingFramework
        self.extra_conservation_properties = None         # science.ConservationProperties
        self.internal_software_components = []            # software.SoftwareComponent
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.scientific_domain = []                       # science.ScientificDomain
        self.scientific_domain_references = []            # shared.DocReference


class Process(object):
    """A concrete class within the cim v2 type system.

    Provides structure for description of a process simulated within a particular
    area (or domain/realm/component) of a model. This will often be subclassed
    within a specific implementation so that constraints can be used to ensure
    that the process details requested are consistent with project requirements
    for information.

    """
    def __init__(self):
        """Constructor.

        """
        super(Process, self).__init__()

        self.algorithms = []                              # science.Algorithm
        self.description = None                           # unicode
        self.implementation_overview = None               # unicode
        self.keywords = None                              # unicode
        self.name = None                                  # unicode
        self.properties = []                              # science.ProcessDetail
        self.references = []                              # shared.Reference
        self.sub_processes = []                           # science.SubProcess
        self.time_step_in_process = None                  # float


class ProcessDetail(object):
    """A concrete class within the cim v2 type system.

    Provides detail of specific properties of a process, there are two possible specialisations
    expected: (1) A detail_vocabulary is identified, and a cardinality is assigned to that
    for possible responses, or (2) Process_Detail is used to provide a collection for a set of
    properties which are defined in the sub-class. However, those properties must have a type
    which is selected from the classmap (that is, standard 'non-es-doc' types).

    """
    def __init__(self):
        """Constructor.

        """
        super(ProcessDetail, self).__init__()

        self.cardinality_of_selection = None              # science.SelectionCardinality
        self.content = None                               # unicode
        self.detail_selection = []                        # unicode
        self.detail_vocabulary = None                     # unicode
        self.heading = None                               # unicode


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
        self.name = None                                  # unicode
        self.number_of_levels = []                        # int
        self.number_of_xy_gridpoints = []                 # int


class ScientificDomain(object):
    """A concrete class within the cim v2 type system.

    Scientific area of a numerical model - usually a sub-model or component.
    Can also be known as a realm.

    """
    def __init__(self):
        """Constructor.

        """
        super(ScientificDomain, self).__init__()

        self.extra_conservation_properties = None         # science.ConservationProperties
        self.grid = None                                  # science.GridSummary
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.name = None                                  # unicode
        self.overview = None                              # unicode
        self.realm = None                                 # unicode
        self.references = []                              # shared.Reference
        self.resolution = None                            # science.Resolution
        self.simulates = []                               # science.Process
        self.time_step = None                             # float
        self.tuning_applied = None                        # science.Tuning


class SubProcess(object):
    """A concrete class within the cim v2 type system.

    Provides structure for description of part of process simulated within a particular
    area (or domain/realm/component) of a model. Typically this will be a part of process
    which shares common properties. It will normally be sub classed within a specific
    implementation so that constraints can be used to ensure that the process details requested are
    consistent with projects requirements for information.

    """
    def __init__(self):
        """Constructor.

        """
        super(SubProcess, self).__init__()

        self.description = None                           # unicode
        self.implementation_overview = None               # unicode
        self.keywords = None                              # unicode
        self.name = None                                  # unicode
        self.properties = []                              # science.ProcessDetail
        self.references = []                              # shared.Reference


class Tuning(object):
    """A concrete class within the cim v2 type system.

    Method used to optimise equation parameters in model component (aka 'tuning').

    """
    def __init__(self):
        """Constructor.

        """
        super(Tuning, self).__init__()

        self.description = None                           # unicode
        self.global_mean_metrics_used = None              # data.VariableCollection
        self.regional_metrics_used = None                 # data.VariableCollection
        self.trend_metrics_used = None                    # data.VariableCollection


class GridLayouts(object):
    """An enumeration within the cim v2 type system.

    Defines the set of grid layouts (e.g. Arakawa C-Grid) which are understood.
    """

    pass


class GridTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the set of grid types (e.g Cubed Sphere) which are understood.
    """

    pass


class ModelTypes(object):
    """An enumeration within the cim v2 type system.

    Defines a set of gross model classes.
    """

    pass


class SelectionCardinality(object):
    """An enumeration within the cim v2 type system.

    Provides the possible cardinalities for selecting from a controlled vocabulary.
    """

    pass


