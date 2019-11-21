"""
.. module:: cim.v2.typeset_for_designing_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.designing package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_activity_package as activity



class AxisMember(object):
    """A concrete class within the cim v2 type system.

    PLACEHOLDER for the real axis_member.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(AxisMember, self).__init__()



class NumericalExperiment(activity.Activity):
    """A concrete class within the cim v2 type system.

    Defines a numerical experiment.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(NumericalExperiment, self).__init__()

        self.governing_mips = []                          # designing.Project (0.N)
        self.related_experiments = []                     # designing.NumericalExperiment (0.N)
        self.related_mips = []                            # designing.Project (0.N)
        self.required_period = None                       # designing.TemporalConstraint (1.1)
        self.requirements = []                            # designing.NumericalRequirement (0.N)
        self.tier = None                                  # int (0.1)


class NumericalRequirement(activity.Activity):
    """A concrete class within the cim v2 type system.

    A numerical requirement associated with a numerical experiment.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(NumericalRequirement, self).__init__()

        self.additional_requirements = []                 # designing.NumericalRequirement (0.N)
        self.is_conformance_info_required = None          # bool (1.1)
        self.is_conformance_requested = None              # bool (1.1)
        self.scope = None                                 # designing.NumericalRequirementScope (0.1)


class Project(activity.Activity):
    """A concrete class within the cim v2 type system.

    Describes a scientific project.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Project, self).__init__()

        self.governed_experiments = []                    # designing.NumericalExperiment (0.N)
        self.homepage = None                              # unicode (0.1)
        self.objectives = []                              # unicode (0.N)
        self.previous_projects = []                       # designing.Project (0.N)
        self.required_experiments = []                    # designing.NumericalExperiment (0.N)
        self.sub_projects = []                            # designing.Project (0.N)


class SimulationPlan(activity.Activity):
    """A concrete class within the cim v2 type system.

    Describes a simulation that needs to be run.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SimulationPlan, self).__init__()

        self.expected_model = None                        # science.Model (1.1)
        self.expected_performance_sypd = None             # float (0.1)
        self.expected_platform = None                     # platform.Machine (0.1)
        self.will_support_experiments = []                # designing.NumericalExperiment (1.N)


class DomainRequirements(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Properties of the domain which needs to be simulated, extent and/or resolution.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DomainRequirements, self).__init__()

        self.required_extent = None                       # science.Topic (0.1)
        self.required_resolution = None                   # science.Topic (0.1)


class EnsembleRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines an experiment ensemble.

    """
    def __init__(self):
        """Instance constructor.

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
        """Instance constructor.

        """
        super(ForcingConstraint, self).__init__()

        self.additional_constraint = None                 # unicode (0.1)
        self.category = None                              # unicode (0.1)
        self.code = None                                  # unicode (0.1)
        self.data_link = None                             # data.Dataset (0.1)
        self.forcing_type = None                          # designing.ForcingTypes (1.1)
        self.group = None                                 # unicode (0.1)
        self.origin = None                                # shared.Citation (0.1)


class InitialisationRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    A requirement on how a particular simulation should be initialised.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(InitialisationRequirement, self).__init__()

        self.branch_time_in_initialisation_source = None  # time.DateTime (0.1)
        self.initialise_from_data = None                  # data.Dataset (0.1)
        self.initialise_from_experiment = None            # designing.NumericalExperiment (0.1)


class MultiEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    In the case of multiple ensemble axes, defines how they
    are set up and ordered.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(MultiEnsemble, self).__init__()

        self.ensemble_axis = []                           # designing.EnsembleRequirement (1.N)


class OutputRequirement(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Provides details of what output is required and when from an experiment.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(OutputRequirement, self).__init__()

        self.formal_data_request = None                   # shared.OnlineResource (0.1)


class StartDateEnsemble(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    Defines an experiment ensemble with multiple start dates.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(StartDateEnsemble, self).__init__()

        self.ensemble_members = None                      # time.DatetimeSet (1.1)


class TemporalConstraint(NumericalRequirement):
    """A concrete class within the cim v2 type system.

    A spatio-temporal constraint on a numerical experiment.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(TemporalConstraint, self).__init__()

        self.required_calendar = None                     # time.Calendar (0.1)
        self.required_duration = None                     # time.TimePeriod (0.1)
        self.start_date = None                            # time.DateTime (0.1)
        self.start_flexibility = None                     # time.TimePeriod (0.1)


class EnsembleTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the various axes along which one can set up an ensemble, whether
     as an experiment designer, or in designing a 'response' ensemble around an
     experiment.
    """
    is_open = False
    members = [
        "Perturbed Physics",
        "Initialisation Method",
        "Realization",
        "Start Date",
        "Forced",
        "Resolution",
        "Driven"
        ]
    descriptions = [
        "Members differ in some aspects of their physics.",
        "Members differ in how they are initialised.",
        "Members initialised to sample possible initial conditions.",
        "Members initialised at different starting dates.",
        "Members have differing forcing data.",
        "Members are/should-be run at different resolutions.",
        "Members are/should-be driven by different models."
        ]


class ExperimentalRelationships(object):
    """An enumeration within the cim v2 type system.

    Defines the canonical set of experimental relationships.
    """
    is_open = True
    members = [
        "is_constrained_by",
        "is_constrainer_of",
        "is_perturbation_from",
        "is_control_for",
        "is_initialized_by",
        "is_initializer_of",
        "is_sibling_of"
        ]
    descriptions = [
        "The experiment that provides constraint(s) for the target experiment (e.g SST forcing).",
        "The set of experiments constrained by the experiment.",
        "The experiment that provides a control for the target experiment.",
        "The set of experiments that use the experiment as a control.",
        "The experiment providing initialization for the experiment.",
        "The set of experiments initialized by the experiment.",
        "Part of a family (e.g. experiments where solar forcing is either increased or reduced)."
        ]


class ForcingTypes(object):
    """An enumeration within the cim v2 type system.

    Defines the possible set of forcing types for a forcing constraint.
    """
    is_open = False
    members = [
        "historical",
        "idealised",
        "scenario",
        "driven"
        ]
    descriptions = [
        "Best estimates of actual state (included synthesized)",
        "Simplified and/or exemplar, e.g. 1%C02",
        "Intended to represent a possible future, e.g. RCP4.5",
        "Driven from another simulation"
        ]


class NumericalRequirementScope(object):
    """An enumeration within the cim v2 type system.

    The scope to which a numerical requirement may or may not apply.
    """
    is_open = False
    members = [
        "mip-era",
        "mip-group",
        "mip",
        "experiment"
        ]
    descriptions = [
        "MIP era wide e.g. 'concentration of pre-industrial CO2' & 'Impose AMIP SSTs'",
        "Shared across a group of MIPs e.g. aerosol forcing in GeoMIP and AerChemMIP.",
        "Shared within a single MIP e.g. spin-up protocol for land surface experiments in LUMIP.",
        "Applies to a single experiment e.g. CFMIP 'zonally uniform SST plus 4K'"
        ]


