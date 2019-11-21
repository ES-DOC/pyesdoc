"""
.. module:: cim.v2.typeset_for_activity_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.activity package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

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
        """Instance constructor.

        """
        super(Activity, self).__init__()

        self.alternative_names = []                       # unicode (0.N)
        self.canonical_name = None                        # unicode (0.1)
        self.citations = []                               # shared.Citation (0.N)
        self.description = None                           # unicode (0.1)
        self.duration = None                              # time.TimePeriod (0.1)
        self.internal_name = None                         # unicode (0.1)
        self.keywords = None                              # unicode (0.1)
        self.long_name = None                             # unicode (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (1.1)
        self.previously_known_as = []                     # unicode (0.N)
        self.rationale = None                             # unicode (0.1)
        self.responsible_parties = []                     # shared.Responsibility (0.N)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.canonical_name)


class AxisMember(object):
    """A concrete class within the cim v2 type system.

    Description of a given ensemble member. It will normally be related to a specific
    ensemble requirement. Note that start dates can be extracted directly from the simulations
    and do not need to be recorded with an axis member description.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(AxisMember, self).__init__()

        self.description = None                           # unicode (0.1)
        self.extra_detail = None                          # unicode (0.1)
        self.index = None                                 # int (1.1)
        self.target_requirement = None                    # designing.NumericalRequirement (0.1)
        self.value = None                                 # float (0.1)


class EnsembleAxis(object):
    """A concrete class within the cim v2 type system.

    Defines the meaning of r/i/p indices in an ensemble.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(EnsembleAxis, self).__init__()

        self.extra_detail = None                          # unicode (0.1)
        self.member = []                                  # activity.AxisMember (1.N)
        self.short_identifier = None                      # unicode (1.1)
        self.target_requirement = None                    # designing.NumericalRequirement (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.axis)


class EnsembleMember(object):
    """A concrete class within the cim v2 type system.

    An ensemble may be a complicated interplay of axes, for example, r/i/p, not all of which
    are populated, so we need a list of the actual simulations and how they map onto the ensemble
    axes.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(EnsembleMember, self).__init__()

        self.errata = None                                # shared.OnlineResource (0.1)
        self.had_performance = None                       # platform.Performance (0.1)
        self.ran_on = None                                # platform.Machine (0.1)
        self.simulation = None                            # data.Simulation (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.simulation)


class ParentSimulation(object):
    """A concrete class within the cim v2 type system.

    Defines the relationship between a simulation and its parent.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ParentSimulation, self).__init__()

        self.branch_method = None                         # unicode (0.1)
        self.branch_time_in_child = None                  # time.DateTime (0.1)
        self.branch_time_in_parent = None                 # time.DateTime (0.1)
        self.parent = None                                # data.Simulation (1.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.parent)


class Conformance(Activity):
    """A concrete class within the cim v2 type system.

    A specific conformance. Describes how a particular numerical requirement has been implemented.
    Will normally be linked from an ensemble descriptor.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Conformance, self).__init__()

        self.conformance_achieved = None                  # activity.ConformanceType (1.1)
        self.datasets = []                                # data.InputDataset (0.N)
        self.models = []                                  # science.Model (1.N)
        self.target_requirement = None                    # designing.NumericalRequirement (1.1)


class Ensemble(Activity):
    """A concrete class within the cim v2 type system.

    Generic ensemble definition.
    Holds the definition of how the various ensemble members have been configured.
    If ensemble axes are not present, then this is either a single member ensemble,
    or part of an uber ensemble.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Ensemble, self).__init__()

        self.common_conformances = []                     # activity.Conformance (0.N)
        self.documentation = []                           # shared.OnlineResource (0.N)
        self.ensemble_axes = []                           # activity.EnsembleAxis (0.N)
        self.experiments = []                             # designing.NumericalExperiment (1.N)
        self.members = []                                 # activity.EnsembleMember (1.N)
        self.representative_performance = None            # platform.Performance (0.1)
        self.uber_ensembles = []                          # activity.UberEnsemble (0.N)


class UberEnsemble(Ensemble):
    """A concrete class within the cim v2 type system.

    An ensemble made up of other ensembles. Often used where parts of an ensemble were run by
    different institutes. Could also be used when a new experiment is designed which can use
    ensemble members from previous experiments and/or projects.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(UberEnsemble, self).__init__()

        self.child_ensembles = []                         # activity.Ensemble (1.N)


class ConformanceType(object):
    """An enumeration within the cim v2 type system.

    Standardised set of conformance responses.
    """
    is_open = True
    members = [
        "Conformed",
        "Partially Conformed",
        "Not Conformed",
        "Not Applicable"
        ]
    descriptions = [
        "Simulation (or ensemble) conformed to requirement",
        "Simulation (or ensemble) partially conformed to requirement - details in description",
        "Simulation (or ensemble) was unable to conform to requirement",
        "Requirement is not relevant"
        ]


