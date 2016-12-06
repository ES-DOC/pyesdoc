# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_science_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.science package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared
import typeset_for_software_package as software



class Grid(object):
    """A concrete class within the cim v2 type system.

    This describes the numerical grid used for the calculations.  It
    is not necessarily the grid upon which the data is output.  It is
    NOT the resolution, which is a property of a specific domain.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Grid, self).__init__()

        self.citations = []                               # shared.Citation (0.N)
        self.description = None                           # unicode (1.1)
        self.details = []                                 # science.Detail (0.N)
        self.discretisation = None                        # science.Discretisation (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (1.1)


class Model(software.ComponentBase):
    """A concrete class within the cim v2 type system.

    A model component: can be executed standalone, and has as
    scientific description available via a link to a science.domain
    document. (A configured model can be understood in terms of a
    simulation, a model, and a configuration.).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Model, self).__init__()

        self.category = None                              # science.ModelTypes (1.1)
        self.coupled_components = []                      # science.Model (0.N)
        self.coupler = None                               # software.CouplingFramework (0.1)
        self.internal_software_components = []            # software.SoftwareComponent (0.N)
        self.key_properties = None                        # science.KeyProperties (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.realms = []                                  # science.ScientificRealm (0.N)
        self.specialization_id = None                     # unicode (0.1)


class ScienceContext(object):
    """An abstract class within the cim v2 type system.

    This is the base class for the science mixins, that is the classes
    which we expect to be specialised and extended by project specific
    vocabularies.  It is expected that values of these will be
    provided within vocabulary definitions.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(ScienceContext, self).__init__()

        self.description = None                           # unicode (1.1)
        self.short_name = None                            # unicode (1.1)
        self.specialization_id = None                     # unicode (1.1)


class ScientificRealm(object):
    """A concrete class within the cim v2 type system.

    Scientific area of a numerical model - usually a sub-model or component.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ScientificRealm, self).__init__()

        self.citations = []                               # shared.Citation (0.N)
        self.grid = None                                  # science.Grid (0.1)
        self.key_properties = None                        # science.KeyProperties (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (1.1)
        self.overview = None                              # unicode (0.1)
        self.processes = []                               # science.Process (1.N)
        self.realm = None                                 # unicode (0.1)
        self.specialization_id = None                     # unicode (0.1)


class Detail(ScienceContext):
    """A concrete class within the cim v2 type system.

    Provides details of specific properties of a process, sub-process,
    key properties, etc., there are two possible specialisations
    expected: (1) A detail_vocabulary is identified, and a cardinality
    is assigned to that for possible responses, or (2) Detail is used
    to provide a collection for a set of properties which are defined
    in the sub-class. However, those properties must have a type which
    is selected from the classmap (that is, standard 'non-es-doc'
    types).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Detail, self).__init__()



class Process(ScienceContext):
    """A concrete class within the cim v2 type system.

    Provides structure for description of a process simulated within a
    particular area (or domain/realm/component) of a model. This will
    often be subclassed within a specific implementation so that
    constraints can be used to ensure that the process details
    requested are consistent with project requirements for
    information.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Process, self).__init__()

        self.citations = []                               # shared.Citation (0.N)
        self.details = []                                 # science.Detail (0.N)
        self.implementation_overview = None               # unicode (1.1)
        self.keywords = None                              # unicode (0.1)
        self.sub_processes = []                           # science.SubProcess (0.N)


class SubProcess(ScienceContext):
    """A concrete class within the cim v2 type system.

    Provides structure for description of part of process simulated
    within a particular area (or domain/realm/component) of a
    model. Typically this will be a part of process which shares
    common properties. It will normally be sub classed within a
    specific implementation so that constraints can be used to ensure
    that the process details requested are consistent with projects
    requirements for information.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SubProcess, self).__init__()

        self.citations = []                               # shared.Citation (0.N)
        self.details = []                                 # science.Detail (0.N)
        self.implementation_overview = None               # unicode (1.1)


class Tuning(SubProcess):
    """A concrete class within the cim v2 type system.

    Method used to optimise equation parameters in model component
    (aka 'tuning').

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Tuning, self).__init__()

        self.description = None                           # unicode (1.1)
        self.global_mean_metrics_used = None              # data.VariableCollection (0.1)
        self.regional_metrics_used = None                 # data.VariableCollection (0.1)
        self.trend_metrics_used = None                    # data.VariableCollection (0.1)


class ConservationProperties(SubProcess):
    """A concrete class within the cim v2 type system.

    Describes how prognostic variables are conserved.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ConservationProperties, self).__init__()

        self.corrected_conserved_prognostic_variables = None# data.VariableCollection (0.1)
        self.description = None                           # unicode (1.1)
        self.was_flux_correction_used = None              # bool (0.1)


class Discretisation(SubProcess):
    """A concrete class within the cim v2 type system.

    Collection of properties related to method of process discretisation.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Discretisation, self).__init__()



class Extent(SubProcess):
    """A concrete class within the cim v2 type system.

    Key scientific characteristics of the grid use to simulate a
    specific domain.  Note that the extent does not itself describe a
    grid, so, for example, a polar stereographic grid may have an
    extent of northern boundary 90N, southern boundary 45N, but the
    fact that it is PS comes from the grid_type.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Extent, self).__init__()

        self.is_global = None                             # bool (1.1)
        self.region_known_as = []                         # unicode (0.N)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.region_known_as)


class IsoExtent(Extent):
    """A concrete class within the cim v2 type system.

    Extent on a latitude-longitudinal grid - to aid traditional cartesian discovery.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(IsoExtent, self).__init__()

        self.eastern_boundary = None                      # float (0.1)
        self.northern_boundary = None                     # float (0.1)
        self.southern_boundary = None                     # float (0.1)
        self.western_boundary = None                      # float (0.1)


class KeyProperties(Process):
    """A concrete class within the cim v2 type system.

    High level list of key properties. It can be specialised in
    extension packages using the detail extensions.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(KeyProperties, self).__init__()

        self.extent = None                                # science.Extent (0.1)
        self.extra_conservation_properties = None         # science.ConservationProperties (0.1)
        self.resolution = None                            # science.Resolution (0.1)
        self.time_step = None                             # float (0.1)
        self.tuning_applied = None                        # science.Tuning (0.1)


class Resolution(SubProcess):
    """A concrete class within the cim v2 type system.

    Describes the computational spatial resolution of a component or
    process.  Not intended to replace or replicate the output grid
    description.  When it appears as part of a process description,
    provide only properties that differ from parent domain.  Note that
    this is supposed to capture gross features of the grid, we expect
    many grids will have different variable layouts, those should be
    described in the grid description, and the exact resolution is not
    required. Note that many properties are not appropriate for
    adaptive grids.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Resolution, self).__init__()

        self.canonical_horizontal_resolution = None       # unicode (0.1)
        self.is_adaptive_grid = None                      # bool (0.1)
        self.name = None                                  # unicode (1.1)
        self.number_of_horizontal_gridpoints = None       # int (0.1)
        self.number_of_vertical_levels = None             # int (0.1)


class ModelTypes(object):
    """An enumeration within the cim v2 type system.

    Defines a set of gross model classes.
    """
    is_open = False
    members = [
        "Atm Only",
        "Ocean Only",
        "Regional",
        "ESM",
        "GCM",
        "IGCM",
        "GCM-MLO",
        "Mesoscale",
        "Process",
        "Planetary"
        ]
    descriptions = [
        "Atmosphere Only",
        "Ocean Only",
        "Regional Model",
        "Earth System Model (Atmosphere, Ocean, Land, Sea-ice and cycles)",
        "Global Climate Model (Atmosphere, Ocean, no carbon cycle)",
        "Intermediate Complexity GCM",
        "GCM with mixed layer ocean",
        "Mesoscale Model",
        "Limited Area process model",
        "Non-Earth model"
        ]


class SelectionCardinality(object):
    """An enumeration within the cim v2 type system.

    Provides the possible cardinalities for selecting from a controlled
    vocabulary.
    """
    is_open = False
    members = [
        "0.1",
        "0.N",
        "1.1",
        "1.N"
        ]
    descriptions = [
        "Zero or one selections are permitted",
        "Zero or many selections are permitted",
        "One and only one selection is required",
        "At least one, and possibly many, selections are required"
        ]


