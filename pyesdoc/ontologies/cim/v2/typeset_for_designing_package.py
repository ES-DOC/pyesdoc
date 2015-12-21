# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_designing_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.designing package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_activity_package as activity



class NumericalExperiment(activity.Activity):
    """A concrete class within the cim v2 type system.

    Defines a numerical experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalExperiment, self).__init__()

        self.link_to_related_experiments = []             # shared.DocReference
        self.link_to_requirements = []                    # shared.DocReference
        self.related_experiments = []                     # designing.NumericalExperiment
        self.requirements = []                            # designing.NumericalRequirement


class NumericalRequirement(activity.Activity):
    """A concrete class within the cim v2 type system.

    A numerical requirement associated with a numerical experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalRequirement, self).__init__()

        self.additional_requirements = []                 # designing.NumericalRequirement
        self.conformance_is_requested = None              # bool
        self.link_to_additional_requirements = []         # shared.DocReference


class Project(activity.Activity):
    """A concrete class within the cim v2 type system.

    Describes a scientific project.

    """
    def __init__(self):
        """Constructor.

        """
        super(Project, self).__init__()

        self.link_to_previous_projects = []               # shared.DocReference
        self.link_to_requires_experiments = []            # shared.DocReference
        self.link_to_sub_projects = []                    # shared.DocReference
        self.previous_projects = []                       # designing.Project
        self.requires_experiments = []                    # designing.NumericalExperiment
        self.sub_projects = []                            # designing.Project


class SimulationPlan(activity.Activity):
    """A concrete class within the cim v2 type system.

    Describes a simulation that needs to be run.

    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationPlan, self).__init__()

        self.expected_model = None                        # science.Model
        self.expected_performance_sypd = None             # float
        self.expected_platform = None                     # platform.Machine
        self.link_to_expected_model = None                # shared.DocReference
        self.link_to_expected_platform = None             # shared.DocReference
        self.link_to_will_support_experiments = []        # shared.DocReference
        self.will_support_experiments = []                # designing.NumericalExperiment


class DomainProperties(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Properties of the domain which needs to be simulated, extend and/or resolution.

    """
    def __init__(self):
        """Constructor.

        """
        super(DomainProperties, self).__init__()

        self.required_extent = None                       # science.Extent
        self.required_resolution = None                   # science.Resolution


class EnsembleRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines an experiment ensemble.

    """
    def __init__(self):
        """Constructor.

        """
        super(EnsembleRequirement, self).__init__()

        self.ensemble_member = []                         # designing.NumericalRequirement
        self.ensemble_type = None                         # designing.EnsembleTypes
        self.link_to_ensemble_member = []                 # shared.DocReference
        self.minimum_size = None                          # int


class ForcingConstraint(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Identifies a model forcing constraint.

    """
    def __init__(self):
        """Constructor.

        """
        super(ForcingConstraint, self).__init__()

        self.additional_constraint = None                 # unicode
        self.category = None                              # shared.VocabMember
        self.code = None                                  # shared.VocabMember
        self.data_link = None                             # shared.OnlineResource
        self.forcing_type = None                          # designing.ForcingTypes
        self.group = None                                 # shared.VocabMember
        self.origin = None                                # shared.Citation


class MultiEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    In the case of multiple ensemble axes, defines how they
    are set up and ordered.

    """
    def __init__(self):
        """Constructor.

        """
        super(MultiEnsemble, self).__init__()

        self.ensemble_axis = []                           # designing.EnsembleRequirement
        self.link_to_ensemble_axis = []                   # shared.DocReference


class MultiTimeEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines an experiment ensemble with multiple start dates.

    """
    def __init__(self):
        """Constructor.

        """
        super(MultiTimeEnsemble, self).__init__()

        self.ensemble_members = None                      # shared.DatetimeSet


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
        self.sliced_subset = None                         # shared.TimesliceList
        self.throughout = None                            # bool


class TemporalConstraint(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    A temporal constraint on a numerical experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(TemporalConstraint, self).__init__()

        self.required_calendar = None                     # shared.Calendar
        self.required_duration = None                     # shared.TimePeriod
        self.start_date = None                            # shared.DateTime
        self.start_flexibility = None                     # shared.TimePeriod


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


