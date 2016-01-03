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

        self.related_experiments = []                     # designing.NumericalExperiment (0.N)
        self.requirements = []                            # designing.NumericalRequirement (0.N)


class NumericalRequirement(activity.Activity):
    """A concrete class within the cim v2 type system.

    A numerical requirement associated with a numerical experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalRequirement, self).__init__()

        self.additional_requirements = []                 # designing.NumericalRequirement (0.N)
        self.conformance_is_requested = None              # bool (1.1)


class Project(activity.Activity):
    """A concrete class within the cim v2 type system.

    Describes a scientific project.

    """
    def __init__(self):
        """Constructor.

        """
        super(Project, self).__init__()

        self.previous_projects = []                       # designing.Project (0.N)
        self.requires_experiments = []                    # designing.NumericalExperiment (0.N)
        self.sub_projects = []                            # designing.Project (0.N)


class SimulationPlan(activity.Activity):
    """A concrete class within the cim v2 type system.

    Describes a simulation that needs to be run.

    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationPlan, self).__init__()

        self.expected_model = None                        # science.Model (1.1)
        self.expected_performance_sypd = None             # float (0.1)
        self.expected_platform = None                     # platform.Machine (0.1)
        self.will_support_experiments = []                # designing.NumericalExperiment (1.N)


class DomainProperties(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Properties of the domain which needs to be simulated, extend and/or resolution.

    """
    def __init__(self):
        """Constructor.

        """
        super(DomainProperties, self).__init__()

        self.required_extent = None                       # science.Extent (0.1)
        self.required_resolution = None                   # science.Resolution (0.1)


class EnsembleRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines an experiment ensemble.

    """
    def __init__(self):
        """Constructor.

        """
        super(EnsembleRequirement, self).__init__()

        self.ensemble_member = []                         # designing.NumericalRequirement (0.N)
        self.ensemble_type = None                         # designing.EnsembleTypes (1.1)
        self.minimum_size = None                          # int (1.1)


class ForcingConstraint(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Identifies a model forcing constraint.

    """
    def __init__(self):
        """Constructor.

        """
        super(ForcingConstraint, self).__init__()

        self.additional_constraint = None                 # unicode (0.1)
        self.category = None                              # shared.VocabMember (1.1)
        self.code = None                                  # shared.VocabMember (1.1)
        self.data_link = None                             # shared.OnlineResource (0.1)
        self.forcing_type = None                          # designing.ForcingTypes (1.1)
        self.group = None                                 # shared.VocabMember (0.1)
        self.origin = None                                # shared.Citation (0.1)


class MultiEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    In the case of multiple ensemble axes, defines how they
    are set up and ordered.

    """
    def __init__(self):
        """Constructor.

        """
        super(MultiEnsemble, self).__init__()

        self.ensemble_axis = []                           # designing.EnsembleRequirement (1.N)


class MultiTimeEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines an experiment ensemble with multiple start dates.

    """
    def __init__(self):
        """Constructor.

        """
        super(MultiTimeEnsemble, self).__init__()

        self.ensemble_members = None                      # shared.DatetimeSet (1.1)


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

        self.continuous_subset = []                       # shared.TimePeriod (0.N)
        self.sliced_subset = None                         # shared.TimesliceList (0.1)
        self.throughout = None                            # bool (1.1)


class TemporalConstraint(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    A temporal constraint on a numerical experiment.

    """
    def __init__(self):
        """Constructor.

        """
        super(TemporalConstraint, self).__init__()

        self.required_calendar = None                     # shared.Calendar (0.1)
        self.required_duration = None                     # shared.TimePeriod (0.1)
        self.start_date = None                            # shared.DateTime (0.1)
        self.start_flexibility = None                     # shared.TimePeriod (0.1)


class EnsembleTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the various axes along which one can set up an ensemble.
    """
    is_open = False
    members = [
        "Forced",
        "Initialisation Method",
        "Initialisation",
        "Perturbed Physics",
        "Resolution",
        "Staggered Start"
        ]


class ForcingTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the possible set of forcing types for a forcing constraint.
    """
    is_open = False
    members = [
        "another simulation",
        "historical",
        "idealised",
        "scenario"
        ]


