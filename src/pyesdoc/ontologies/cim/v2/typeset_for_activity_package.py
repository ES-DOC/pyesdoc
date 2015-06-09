# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_activity_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.activity package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 14:48:44.252820.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class AxisMember(object):
    """A concrete class within the cim v2 type system.

    Describes an individual ensemble member.

    """
    def __init__(self):
        """Constructor.

        """
        super(AxisMember, self).__init__()

        self.start_date = None                            # time.DateTime
        self.value = None                                 # float
        self.description = None                           # str
        self.index = None                                 # int


class Activity(object):
    """An abstract class within the cim v2 type system.

    Base class for activities.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Activity, self).__init__()

        self.references = []                              # shared.Citation
        self.meta = shared.Meta()                         # shared.Meta
        self.responsible_parties = []                     # shared.Responsibility
        self.description = None                           # shared.CimText
        self.long_name = None                             # str
        self.name = None                                  # str
        self.keywords = []                                # str
        self.canonical_name = None                        # activity.VocabMember
        self.duration = None                              # time.TimePeriod


class MemberDescription(object):
    """A concrete class within the cim v2 type system.

    Defines the r/i/p axes of an ensemble.

    """
    def __init__(self):
        """Constructor.

        """
        super(MemberDescription, self).__init__()

        self.member = []                                  # activity.AxisMember
        self.axis = None                                  # activity.EnsembleTypes
        self.description = None                           # shared.CimText


class NumericalRequirement(Activity):
    """A concrete class within the cim v2 type system.

    Numerical requirement base class.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalRequirement, self).__init__()

        self.additional_requirements = []                 # linked_to(activity.NumericalRequirement)
        self.was_conformance_requested = None             # bool


class Conformance(Activity):
    """A concrete class within the cim v2 type system.

    Conformance information for a particular numerical requirement.

    """
    def __init__(self):
        """Constructor.

        """
        super(Conformance, self).__init__()

        self.conformance_detail = None                    # shared.CimText
        self.target_requirement = None                    # str
        self.target_name = None                           # str


class MultiTimeEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines an experiment ensemble with multiple start dates.

    """
    def __init__(self):
        """Constructor.

        """
        super(MultiTimeEnsemble, self).__init__()

        self.ensemble_members = None                      # time.DatetimeSet


class Configuration(Activity):
    """A concrete class within the cim v2 type system.

    Aggregation of conformance information for a particular configuration of a model for a particular experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(Configuration, self).__init__()

        self.conformances = []                            # linked_to(activity.Conformance)
        self.description = None                           # str


class Simulation(Activity):
    """A concrete class within the cim v2 type system.

    Provides the integrating link about what models were run and why.

    """
    def __init__(self):
        """Constructor.

        """
        super(Simulation, self).__init__()

        self.supported = []                               # linked_to(activity.NumericalExperiment)
        self.used = None                                  # linked_to(software.ConfiguredModel)
        self.ran_on = None                                # linked_to(platform.Machine)
        self.conformed_via = None                         # linked_to(activity.Configuration)
        self.had_performance = None                       # linked_to(platform.Performance)


class Project(Activity):
    """A concrete class within the cim v2 type system.

    Describes a scientific project.

    """
    def __init__(self):
        """Constructor.

        """
        super(Project, self).__init__()

        self.sub_projects = []                            # linked_to(activity.Project)
        self.previous_projects = []                       # linked_to(activity.Project)
        self.required_experiments = []                    # linked_to(activity.NumericalExperiment)


class Ensemble(Activity):
    """A concrete class within the cim v2 type system.

    Provides the ensemble r/i/p definitions.

    """
    def __init__(self):
        """Constructor.

        """
        super(Ensemble, self).__init__()

        self.s_defined_by = None                          # activity.MemberDescription
        self.simulations_include = []                     # linked_to(activity.Simulation)
        self.r_defined_by = None                          # activity.MemberDescription
        self.i_defined_by = None                          # activity.MemberDescription
        self.supported = []                               # linked_to(activity.NumericalExperiment)
        self.p_defined_by = None                          # activity.MemberDescription


class MultiEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    In the case of multiple ensemble axes, defines how they are set up and ordered.

    """
    def __init__(self):
        """Constructor.

        """
        super(MultiEnsemble, self).__init__()

        self.ensemble_axis = []                           # linked_to(activity.EnsembleRequirement)


class EnsembleRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines details of experiment ensemble.

    """
    def __init__(self):
        """Constructor.

        """
        super(EnsembleRequirement, self).__init__()

        self.ensemble_member = []                         # linked_to(activity.NumericalRequirement)
        self.minimum_size = None                          # int
        self.ensemble_type = None                         # activity.EnsembleTypes


class EnsembleRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines details of an experiment ensemble requirement.

    """
    def __init__(self):
        """Constructor.

        """
        super(EnsembleRequirement, self).__init__()

        self.minimum_size = None                          # int
        self.ensemble_member = []                         # linked_to(activity.NumericalRequirement)
        self.ensemble_type = None                         # activity.EnsembleTypes


class NumericalExperiment(Activity):
    """A concrete class within the cim v2 type system.

    Defines a numerical experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalExperiment, self).__init__()

        self.experiment_id = None                         # str
        self.requirements = []                            # linked_to(activity.NumericalRequirement)
        self.related_experiments = []                     # linked_to(activity.NumericalExperiment)


class TemporalConstraint(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    A temporal constraint on a numerical experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(TemporalConstraint, self).__init__()

        self.required_calendar = None                     # time.Calendar
        self.start_flexibility = None                     # time.TimePeriod
        self.required_duration = None                     # time.TimePeriod
        self.start_date = None                            # time.DateTime


class SimulationPlan(Activity):
    """A concrete class within the cim v2 type system.

    Describes a simulation that needs to be run.

    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationPlan, self).__init__()

        self.machine = None                               # linked_to(platform.Machine)
        self.model = None                                 # linked_to(software.ConfiguredModel)
        self.expected_performance = None                  # linked_to(platform.Performance)
        self.experiments = []                             # linked_to(activity.NumericalExperiment)


class OutputTemporalRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines gross details of output temporal requirements. Typically output
    will be required in one of three modes: (1) continuous,
    (2) continuos for a set of subset periods, or (3) sliced
    for a set of months in year or days a month.

    """
    def __init__(self):
        """Constructor.

        """
        super(OutputTemporalRequirement, self).__init__()

        self.continuous_subset = []                       # time.TimePeriod
        self.throughout = None                            # bool
        self.sliced_subset = None                         # time.TimesliceList


class ForcingConstraint(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Identifies a model forcing constraint.

    """
    def __init__(self):
        """Constructor.

        """
        super(ForcingConstraint, self).__init__()

        self.category = None                              # activity.VocabMember
        self.origin = None                                # shared.Citation
        self.group = None                                 # activity.VocabMember
        self.data_link = None                             # shared.OnlineResource
        self.forcing_Type = None                          # activity.ForcingTypes
        self.code = None                                  # activity.VocabMember
        self.additional_constraint = None                 # shared.CimText


class ModelTypes(object):
    """An enumeration within the cim v2 type system.

    Defines a set of gross model classes.
    """

    pass


class EnsembleTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the various axes along which one can set up an ensemble.
    """

    pass


class ForcingTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the possible set of forcing types for a forcing constraint.
    """

    pass


