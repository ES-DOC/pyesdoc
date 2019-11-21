"""
.. module:: cim.v1.typeset_for_activity_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.activity package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class Activity(object):
    """An abstract class within the cim v1 type system.

    An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(Activity, self).__init__()

        self.funding_sources = []                         # unicode (0.N)
        self.projects = []                                # activity.ProjectType (0.N)
        self.rationales = []                              # unicode (0.N)
        self.responsible_parties = []                     # shared.ResponsibleParty (0.N)


class Conformance(object):
    """A concrete class within the cim v1 type system.

    A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Conformance, self).__init__()

        self.description = None                           # unicode (0.1)
        self.frequency = None                             # activity.FrequencyType (0.1)
        self.is_conformant = None                         # bool (1.1)
        self.requirements = []                            # activity.NumericalRequirement (1.N)
        self.sources = []                                 # shared.DataSource (0.N)
        self.type = None                                  # activity.ConformanceType (0.1)


class ExperimentRelationship(shared.Relationship):
    """A concrete class within the cim v1 type system.

    Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ExperimentRelationship, self).__init__()

        self.target = None                                # activity.ExperimentRelationshipTarget (1.1)
        self.type = None                                  # activity.ExperimentRelationshipType (1.1)


class ExperimentRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of experiment_relationship_target class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(ExperimentRelationshipTarget, self).__init__()

        self.numerical_experiment = None                  # activity.NumericalExperiment (0.1)


class NumericalRequirement(object):
    """An abstract class within the cim v1 type system.

    A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(NumericalRequirement, self).__init__()

        self.description = None                           # unicode (0.1)
        self.id = None                                    # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.options = []                                 # activity.NumericalRequirementOption (0.N)
        self.requirement_type = None                      # unicode (1.1)
        self.source = None                                # shared.DataSource (0.1)


class NumericalRequirementOption(object):
    """A concrete class within the cim v1 type system.

    A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that "parent" requirement would have three "child" RequirmentOptions (each of one with the XOR optionRelationship).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(NumericalRequirementOption, self).__init__()

        self.description = None                           # unicode (0.1)
        self.id = None                                    # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.relationship = None                          # unicode (0.1)
        self.sub_options = []                             # activity.NumericalRequirementOption (0.N)


class SimulationRelationship(shared.Relationship):
    """A concrete class within the cim v1 type system.

    Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SimulationRelationship, self).__init__()

        self.target = None                                # activity.SimulationRelationshipTarget (1.1)
        self.type = None                                  # activity.SimulationRelationshipType (1.1)


class SimulationRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of simulation_relationship_target class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SimulationRelationshipTarget, self).__init__()

        self.simulation = None                            # shared.DocReference (0.1)
        self.target = None                                # activity.SimulationType (0.1)


class BoundaryCondition(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(BoundaryCondition, self).__init__()

        self.requirement_type = unicode("boundaryCondition")


class Experiment(Activity):
    """An abstract class within the cim v1 type system.

    An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(Experiment, self).__init__()

        self.generates = []                               # unicode (0.N)
        self.measurement_campaigns = []                   # activity.MeasurementCampaign (0.N)
        self.requires = []                                # activity.NumericalActivity (0.N)
        self.supports = []                                # unicode (0.N)


class InitialCondition(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    An initial condition is a numerical requirement on a model prognostic variable value at time zero.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(InitialCondition, self).__init__()

        self.requirement_type = unicode("initialCondition")


class LateralBoundaryCondition(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(LateralBoundaryCondition, self).__init__()

        self.requirement_type = unicode("lateralBoundaryCondition")


class MeasurementCampaign(Activity):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of measurement_campaign class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(MeasurementCampaign, self).__init__()

        self.duration = None                              # int (1.1)


class NumericalActivity(Activity):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of numerical_activity class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(NumericalActivity, self).__init__()

        self.description = None                           # unicode (0.1)
        self.long_name = None                             # unicode (0.1)
        self.short_name = None                            # unicode (1.1)
        self.supports = []                                # activity.Experiment (0.N)


class NumericalExperiment(Experiment):
    """A concrete class within the cim v1 type system.

    A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(NumericalExperiment, self).__init__()

        self.description = None                           # unicode (0.1)
        self.experiment_id = None                         # unicode (0.1)
        self.long_name = None                             # unicode (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.requirements = []                            # activity.NumericalRequirement (0.N)
        self.short_name = None                            # unicode (1.1)


class OutputRequirement(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(OutputRequirement, self).__init__()

        self.requirement_type = unicode("outputRequirement")


class PhysicalModification(Conformance):
    """A concrete class within the cim v1 type system.

    Physical modification is the implementation of a boundary condition numerical requirement that is achieved within the model code rather than from some external source file. It  might include, for example,  a specific rate constant within a chemical reaction, or coefficient value(s) in a parameterisation.  For example, one might require a numerical experiment where specific chemical reactions were turned off - e.g. no heterogeneous chemistry.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(PhysicalModification, self).__init__()



class Simulation(NumericalActivity):
    """An abstract class within the cim v1 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(Simulation, self).__init__()

        self.authors = None                               # unicode (0.1)
        self.calendar = None                              # shared.Calendar (1.1)
        self.conformances = []                            # activity.Conformance (0.N)
        self.control_simulation = None                    # activity.Simulation (0.1)
        self.deployments = []                             # software.Deployment (0.N)
        self.inputs = []                                  # software.Coupling (0.N)
        self.outputs = []                                 # data.DataObject (0.N)
        self.restarts = []                                # data.DataObject (0.N)
        self.simulation_id = None                         # unicode (0.1)
        self.spinup_date_range = None                     # shared.ClosedDateRange (0.1)
        self.spinup_simulation = None                     # activity.Simulation (0.1)


class SimulationComposite(Simulation):
    """A concrete class within the cim v1 type system.

    A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SimulationComposite, self).__init__()

        self.child = []                                   # activity.Simulation (0.N)
        self.date_range = None                            # shared.DateRange (1.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.rank = None                                  # int (1.1)


class SimulationRun(Simulation):
    """A concrete class within the cim v1 type system.

    A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SimulationRun, self).__init__()

        self.date_range = None                            # shared.DateRange (1.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.model = None                                 # software.ModelComponent (0.1)


class SpatioTemporalConstraint(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SpatioTemporalConstraint, self).__init__()

        self.date_range = None                            # shared.DateRange (0.1)
        self.spatial_resolution = None                    # activity.ResolutionType (0.1)
        self.requirement_type = unicode("spatioTemporalConstraint")


class DownscalingSimulation(NumericalActivity):
    """An abstract class within the cim v1 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(DownscalingSimulation, self).__init__()

        self.calendar = None                              # shared.Calendar (1.1)
        self.downscaled_from = None                       # shared.DataSource (1.1)
        self.downscaling_id = None                        # unicode (0.1)
        self.downscaling_type = None                      # activity.DownscalingType (0.1)
        self.inputs = []                                  # software.Coupling (0.N)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.outputs = []                                 # data.DataObject (0.N)


class Ensemble(NumericalActivity):
    """A concrete class within the cim v1 type system.

    An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Ensemble, self).__init__()

        self.members = []                                 # activity.EnsembleMember (1.N)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.outputs = []                                 # shared.DataSource (0.N)
        self.types = []                                   # activity.EnsembleType (1.N)


class EnsembleMember(NumericalActivity):
    """A concrete class within the cim v1 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(EnsembleMember, self).__init__()

        self.ensemble = None                              # activity.Ensemble (0.1)
        self.ensemble_ids = []                            # shared.StandardName (0.N)
        self.simulation = None                            # activity.Simulation (0.1)


class ConformanceType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of conformance_type enum.
    """
    is_open = False
    members = [
        "not-xxx",
        "not conformant",
        "standard config",
        "via inputs",
        "via model mods",
        "combination"
        ]
    descriptions = [
        "None",
        "Describes a simulation that is purpefully non-conformant to an experimental requirement.",
        "Describes a simulation that is naturally conformant to an experimental requirement.",
        "Describes a simulation that conforms to an experimental requirement by using particular inputs.",
        "Describes a simulation that conforms to an experimental requirement by changing the configuration of the software model implementing that simulation.",
        "Describes a simulation that conforms to an experimental requirement by using more than one method."
        ]


class DownscalingType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of downscaling_type enum.
    """
    is_open = False
    members = [
        "statistical",
        "dynamic"
        ]
    descriptions = [
        "None",
        "None"
        ]


class EnsembleType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of ensemble_type enum.
    """
    is_open = True
    members = []
    descriptions = []


class ExperimentRelationshipType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of experiment_relationship_type enum.
    """
    is_open = False
    members = [
        "previousRealisation",
        "continuationOf",
        "controlExperiment",
        "higherResolutionVersionOf",
        "lowerResolutionVersionOf",
        "increaseEnsembleOf",
        "modifiedInputMethodOf",
        "shorterVersionOf",
        "extensionOf"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None"
        ]


class FrequencyType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of frequency_type enum.
    """
    is_open = True
    members = []
    descriptions = []


class ProjectType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of project_type enum.
    """
    is_open = True
    members = []
    descriptions = []


class ResolutionType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of resolution_type enum.
    """
    is_open = True
    members = []
    descriptions = []


class SimulationRelationshipType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of simulation_relationship_type enum.
    """
    is_open = False
    members = [
        "extensionOf",
        "responseTo",
        "continuationOf",
        "previousSimulation",
        "higherResolutionVersionOf",
        "lowerResolutionVersionOf",
        "fixedVersionOf",
        "followingSimulation"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None"
        ]


class SimulationType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of simulation_type enum.
    """
    is_open = False
    members = [
        "simulationRun",
        "assimilation",
        "simulationComposite"
        ]
    descriptions = [
        "None",
        "None",
        "None"
        ]


