# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_activity_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.activity package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class Activity(object):
    """An abstract class within the cim v2 type system.

    Base class for activities.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Activity, self).__init__()

        self.canonical_name = None                        # unicode
        self.description = None                           # unicode
        self.duration = None                              # shared.TimePeriod
        self.keywords = []                                # unicode
        self.long_name = None                             # unicode
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.name = None                                  # unicode
        self.rationale = None                             # unicode
        self.references = []                              # shared.Citation
        self.responsible_parties = []                     # shared.Responsibility


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

        self.description = None                           # unicode
        self.index = None                                 # int
        self.value = None                                 # float


class EnsembleAxis(object):
    """A concrete class within the cim v2 type system.

    Defines the meaning of r/i/p indices in an ensemble.

    """
    def __init__(self):
        """Constructor.

        """
        super(EnsembleAxis, self).__init__()

        self.extra_detail = None                          # unicode
        self.member = []                                  # activity.AxisMember
        self.short_identifier = None                      # unicode
        self.target_requirement = None                    # designing.NumericalRequirement
        self.target_requirement_reference = None          # shared.DocReference


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
        self.had_performance_reference = None             # shared.DocReference
        self.ran_on = None                                # platform.Machine
        self.ran_on_reference = None                      # shared.DocReference
        self.simulation = None                            # data.Simulation
        self.simulation_reference = None                  # shared.DocReference


class ParentSimulation(object):
    """A concrete class within the cim v2 type system.

    Defines the relationship between a simulation and its parent.

    """
    def __init__(self):
        """Constructor.

        """
        super(ParentSimulation, self).__init__()

        self.branch_time_in_child = None                  # shared.DateTime
        self.branch_time_in_parent = None                 # shared.DateTime
        self.parent = None                                # data.Simulation
        self.parent_reference = None                      # shared.DocReference


class Conformance(Activity):
    """A concrete class within the cim v2 type system.

    A specific conformance. Describes how a particular numerical requirement has been implemented.
    Will normally be linked from an ensemble descriptor.

    """
    def __init__(self):
        """Constructor.

        """
        super(Conformance, self).__init__()

        self.target_requirement = None                    # designing.NumericalRequirement
        self.target_requirement_reference = None          # shared.DocReference


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

        self.common_conformances = []                     # activity.Conformance
        self.common_conformances_references = []          # shared.DocReference
        self.has_ensemble_axes = []                       # activity.EnsembleAxis
        self.members = []                                 # activity.EnsembleMember
        self.part_of = []                                 # activity.UberEnsemble
        self.supported = []                               # designing.NumericalExperiment
        self.supported_references = []                    # shared.DocReference


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
        self.child_ensembles_references = []              # shared.DocReference


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


