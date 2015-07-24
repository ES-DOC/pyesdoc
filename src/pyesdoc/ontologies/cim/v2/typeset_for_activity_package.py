# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_activity_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.activity package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:58:29.543824.

"""
import abc
import datetime
import uuid

import typeset_for_software_package as software
import typeset_for_platform_package as platform
import typeset_for_activity_package as activity
import typeset_for_shared_package as shared



class EnsembleAxis(object):
    """A concrete class within the cim v2 type system.

    Defines the meaning of r/i/p indices in an ensemble

    """
    def __init__(self):
        """Constructor.

        """
        super(EnsembleAxis, self).__init__()

        self.short_identifier = None                      # str
        self.target_requirement = None                    # activity.NumericalRequirement
        self.extra_detail = None                          # shared.Cimtext
        self.member = []                                  # activity.AxisMember


class ParentSimulation(object):
    """A concrete class within the cim v2 type system.

    Defines the relationship between a simulation and its parent

    """
    def __init__(self):
        """Constructor.

        """
        super(ParentSimulation, self).__init__()

        self.parent = None                                # activity.Simulation
        self.branch_time_in_child = None                  # shared.DateTime
        self.branch_time_in_parent = None                 # shared.DateTime


class EnsembleMember(object):
    """A concrete class within the cim v2 type system.

    An ensemble may be a complicated interplay of axes, for example, r/i/p, not all of which
    are populated, so we need a list of the actual simulations and how they map onto the ensemble
    axes.

    """
    def __init__(self):
        """Constructor.

        """
        super(EnsembleMember, self).__init__()

        self.had_performance = None                       # platform.Performance
        self.simulation = None                            # activity.Simulation
        self.ran_on = None                                # platform.Machine


class Activity(object):
    """An abstract class within the cim v2 type system.

    Base class for activities

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Activity, self).__init__()

        self.long_name = None                             # str
        self.duration = None                              # shared.TimePeriod
        self.canonical_name = None                        # str
        self.rationale = None                             # shared.Cimtext
        self.responsible_parties = []                     # shared.Responsibility
        self.references = []                              # shared.Citation
        self.keywords = []                                # str
        self.name = None                                  # str
        self.meta = shared.Meta()                         # shared.Meta
        self.description = None                           # shared.Cimtext


class AxisMember(object):
    """A concrete class within the cim v2 type system.

    Description of a given ensemble member. It will normally be related to a specific
    ensemble requirement. Note that start dates can be extracted directly from the simulations
    and do not need to be recorded with an axis member description.

    """
    def __init__(self):
        """Constructor.

        """
        super(AxisMember, self).__init__()

        self.value = None                                 # float
        self.description = None                           # str
        self.index = None                                 # int


class NumericalRequirement(Activity):
    """A concrete class within the cim v2 type system.

    A numerical requirement associated with a numerical experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalRequirement, self).__init__()

        self.additional_requirements = []                 # activity.NumericalRequirement
        self.conformance_is_requested = None              # bool


class Simulation(Activity):
    """A concrete class within the cim v2 type system.

    Simulation class provides the integrating link about what models were run and wny.
    In many cases this should be auto-generated from output file headers.

    """
    def __init__(self):
        """Constructor.

        """
        super(Simulation, self).__init__()

        self.ensemble_identifier = None                   # str
        self.run_for_experiments = []                     # activity.NumericalExperiment
        self.parent_simulation = None                     # activity.ParentSimulation
        self.used = None                                  # software.Model
        self.primary_ensemble = None                      # activity.Ensemble
        self.part_of_project = []                         # activity.Project


class OutputTemporalRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Provides details of when output is required from an experiment.
    Typically output will be required in one of three modes:
    (1) continuous,
    (2) continuous for a set of subset periods, or
    (3) sliced for a set of months in a year or days in a month.

    """
    def __init__(self):
        """Constructor.

        """
        super(OutputTemporalRequirement, self).__init__()

        self.continuous_subset = []                       # shared.TimePeriod
        self.throughout = None                            # bool
        self.sliced_subset = None                         # shared.TimesliceList


class Conformance(Activity):
    """A concrete class within the cim v2 type system.

    A specific conformance. Describes how a particular numerical requirement has been implemented.
    Will normally be linked from an ensemble descriptor.

    """
    def __init__(self):
        """Constructor.

        """
        super(Conformance, self).__init__()

        self.target_requirement = None                    # activity.NumericalRequirement


class MultiEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    In the case of multiple ensemble axes, defines how they
    are set up and ordered

    """
    def __init__(self):
        """Constructor.

        """
        super(MultiEnsemble, self).__init__()

        self.ensemble_axis = []                           # activity.EnsembleRequirement


class Ensemble(Activity):
    """A concrete class within the cim v2 type system.

    Generic ensemble definition.
    Holds the definition of how the various ensemble members have been configured.
    If ensemble axes are not present, then this is either a single member ensemble,
    or part of an uber ensemble.

    """
    def __init__(self):
        """Constructor.

        """
        super(Ensemble, self).__init__()

        self.part_of = []                                 # activity.UberEnsemble
        self.members = []                                 # activity.EnsembleMember
        self.supported = []                               # activity.NumericalExperiment
        self.common_conformances = []                     # activity.Conformance
        self.has_ensemble_axes = []                       # activity.EnsembleAxis


class NumericalExperiment(Activity):
    """A concrete class within the cim v2 type system.

    Defines a numerical experiment

    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalExperiment, self).__init__()

        self.requirements = []                            # activity.NumericalRequirement
        self.related_experiments = []                     # activity.NumericalExperiment


class MultiTimeEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines an experiment ensemble with multiple start dates

    """
    def __init__(self):
        """Constructor.

        """
        super(MultiTimeEnsemble, self).__init__()

        self.ensemble_members = None                      # shared.DatetimeSet


class ForcingConstraint(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Identifies a model forcing constraint

    """
    def __init__(self):
        """Constructor.

        """
        super(ForcingConstraint, self).__init__()

        self.category = None                              # shared.VocabMember
        self.origin = None                                # shared.Citation
        self.group = None                                 # shared.VocabMember
        self.data_link = None                             # shared.OnlineResource
        self.forcing_type = None                          # activity.ForcingTypes
        self.code = None                                  # shared.VocabMember
        self.additional_constraint = None                 # shared.Cimtext


class Project(Activity):
    """A concrete class within the cim v2 type system.

    Describes a scientific project.

    """
    def __init__(self):
        """Constructor.

        """
        super(Project, self).__init__()

        self.previous_projects = []                       # activity.Project
        self.sub_projects = []                            # activity.Project
        self.requires_experiments = []                    # activity.NumericalExperiment


class UberEnsemble(Ensemble):
    """A concrete class within the cim v2 type system.

    An ensemble made up of other ensembles. Often used where parts of an ensemble were run by
    different institutes. Could also be used when a new experiment is designed which can use
    ensemble members from previous experiments and/or projects.

    """
    def __init__(self):
        """Constructor.

        """
        super(UberEnsemble, self).__init__()

        self.child_ensembles = []                         # activity.Ensemble


class Downscaling(Simulation):
    """A concrete class within the cim v2 type system.

    Defines a downscaling activity

    """
    def __init__(self):
        """Constructor.

        """
        super(Downscaling, self).__init__()

        self.downscaled_from = None                       # activity.Simulation


class DomainProperties(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Properties of the domain which needs to be simulated, extend and/or resolution

    """
    def __init__(self):
        """Constructor.

        """
        super(DomainProperties, self).__init__()

        self.required_extent = None                       # science.Extent
        self.required_resolution = None                   # science.Resolution


class EnsembleRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines an experiment ensemble

    """
    def __init__(self):
        """Constructor.

        """
        super(EnsembleRequirement, self).__init__()

        self.ensemble_member = []                         # activity.NumericalRequirement
        self.minimum_size = None                          # int
        self.ensemble_type = None                         # activity.EnsembleTypes


class SimulationPlan(Activity):
    """A concrete class within the cim v2 type system.

    Describes a simulation that needs to be run

    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationPlan, self).__init__()

        self.expected_platform = None                     # platform.Machine
        self.will_support_experiments = []                # activity.NumericalExperiment
        self.expected_model = None                        # software.Model
        self.expected_performance_sypd = None             # float


class TemporalConstraint(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    A temporal constraint on a numerical experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(TemporalConstraint, self).__init__()

        self.required_calendar = None                     # shared.Calendar
        self.start_flexibility = None                     # shared.TimePeriod
        self.start_date = None                            # shared.DateTime
        self.required_duration = None                     # shared.TimePeriod


class ForcingTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the possible set of forcing types for a forcing constraint
    """

    pass


class EnsembleTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the various axes along which one can set up an ensemble
    """

    pass


