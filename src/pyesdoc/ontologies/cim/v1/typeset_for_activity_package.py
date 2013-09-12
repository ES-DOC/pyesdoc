"""
.. module:: cim.v1.typeset_for_activity_package.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.activity package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-09-12 17:03:09.141765.

"""
# Module imports.
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
        """Constructor.

        """
        super(Activity, self).__init__()

        self.funding_sources = []                         # str
        self.projects = []                                # activity.ProjectType
        self.rationales = []                              # str
        self.responsible_parties = []                     # shared.ResponsibleParty


class Conformance(object):
    """A concrete class within the cim v1 type system.

    A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.
    """
    def __init__(self):
        """Constructor.

        """
        super(Conformance, self).__init__()

        self.description = str()                          # str
        self.frequency = ''                               # activity.FrequencyType
        self.is_conformant = bool()                       # bool
        self.requirements = []                            # activity.NumericalRequirement
        self.requirements_references = []                 # shared.DocReference
        self.sources = []                                 # shared.DataSource
        self.sources_references = []                      # shared.DocReference
        self.type = ''                                    # activity.ConformanceType


class ExperimentRelationship(shared.Relationship):
    """A concrete class within the cim v1 type system.

    Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.
    """
    def __init__(self):
        """Constructor.

        """
        super(ExperimentRelationship, self).__init__()

        self.target = ExperimentRelationshipTarget()      # activity.ExperimentRelationshipTarget
        self.type = ''                                    # activity.ExperimentRelationshipType


class ExperimentRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(ExperimentRelationshipTarget, self).__init__()

        self.numerical_experiment = None                  # activity.NumericalExperiment
        self.reference = None                             # shared.DocReference


class NumericalRequirement(object):
    """An abstract class within the cim v1 type system.

    A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(NumericalRequirement, self).__init__()

        self.description = str()                          # str
        self.id = str()                                   # str
        self.name = str()                                 # str
        self.options = []                                 # activity.NumericalRequirementOption
        self.requirement_type = str()                     # str
        self.source = None                                # shared.DataSource
        self.source_reference = None                      # shared.DocReference


class NumericalRequirementOption(object):
    """A concrete class within the cim v1 type system.

    A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that "parent" requirement would have three "child" RequirmentOptions (each of one with the XOR optionRelationship).
    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalRequirementOption, self).__init__()

        self.relationship = str()                         # str
        self.requirement = None                           # activity.NumericalRequirement


class SimulationRelationship(shared.Relationship):
    """A concrete class within the cim v1 type system.

    Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.
    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationRelationship, self).__init__()

        self.target = SimulationRelationshipTarget()      # activity.SimulationRelationshipTarget
        self.type = ''                                    # activity.SimulationRelationshipType


class SimulationRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationRelationshipTarget, self).__init__()

        self.reference = None                             # shared.DocReference
        self.target = ''                                  # activity.SimulationType


class BoundaryCondition(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).
    """
    def __init__(self):
        """Constructor.

        """
        super(BoundaryCondition, self).__init__()

        self.requirement_type = str("boundaryCondition")


class Experiment(Activity):
    """An abstract class within the cim v1 type system.

    An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Experiment, self).__init__()

        self.generates = []                               # str
        self.measurement_campaigns = []                   # activity.MeasurementCampaign
        self.requires = []                                # activity.NumericalActivity
        self.requires_references = []                     # shared.DocReference
        self.supports = []                                # str
        self.supports_references = []                     # shared.DocReference


class InitialCondition(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    An initial condition is a numerical requirement on a model prognostic variable value at time zero.
    """
    def __init__(self):
        """Constructor.

        """
        super(InitialCondition, self).__init__()

        self.requirement_type = str("initialCondition")


class LateralBoundaryCondition(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).
    """
    def __init__(self):
        """Constructor.

        """
        super(LateralBoundaryCondition, self).__init__()

        self.requirement_type = str("lateralBoundaryCondition")


class MeasurementCampaign(Activity):
    """A concrete class within the cim v1 type system.

    
    """
    def __init__(self):
        """Constructor.

        """
        super(MeasurementCampaign, self).__init__()

        self.duration = int()                             # int


class NumericalActivity(Activity):
    """An abstract class within the cim v1 type system.

    
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(NumericalActivity, self).__init__()

        self.description = str()                          # str
        self.long_name = str()                            # str
        self.short_name = str()                           # str
        self.supports = []                                # activity.Experiment
        self.supports_references = []                     # shared.DocReference


class NumericalExperiment(Experiment):
    """A concrete class within the cim v1 type system.

    A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.
    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalExperiment, self).__init__()

        self.description = str()                          # str
        self.doc_info = shared.DocInfo()                  # shared.DocInfo
        self.experiment_id = str()                        # str
        self.long_name = str()                            # str
        self.requirements = []                            # activity.NumericalRequirement
        self.short_name = str()                           # str


class OutputRequirement(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.
    """
    def __init__(self):
        """Constructor.

        """
        super(OutputRequirement, self).__init__()

        self.requirement_type = str("outputRequirement")


class PhysicalModification(Conformance):
    """A concrete class within the cim v1 type system.

    Physical modification is the implementation of a boundary condition numerical requirement that is achieved within the model code rather than from some external source file. It  might include, for example,  a specific rate constant within a chemical reaction, or coefficient value(s) in a parameterisation.  For example, one might require a numerical experiment where specific chemical reactions were turned off - e.g. no heterogeneous chemistry.
    """
    def __init__(self):
        """Constructor.

        """
        super(PhysicalModification, self).__init__()



class Simulation(NumericalActivity):
    """An abstract class within the cim v1 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Simulation, self).__init__()

        self.authors = str()                              # str
        self.calendar = shared.Calendar()                 # shared.Calendar
        self.conformances = []                            # activity.Conformance
        self.control_simulation = None                    # activity.Simulation
        self.control_simulation_reference = None          # shared.DocReference
        self.deployments = []                             # software.Deployment
        self.inputs = []                                  # software.Coupling
        self.output_references = []                       # shared.DocReference
        self.outputs = []                                 # data.DataObject
        self.restart_references = []                      # shared.DocReference
        self.restarts = []                                # data.DataObject
        self.simulation_id = str()                        # str
        self.spinup_date_range = None                     # shared.ClosedDateRange
        self.spinup_simulation = None                     # activity.Simulation
        self.spinup_simulation_reference = None           # shared.DocReference


class SimulationComposite(Simulation):
    """A concrete class within the cim v1 type system.

    A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.
    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationComposite, self).__init__()

        self.child = []                                   # activity.Simulation
        self.date_range = shared.DateRange()              # shared.DateRange
        self.doc_info = shared.DocInfo()                  # shared.DocInfo
        self.rank = int()                                 # int


class SimulationRun(Simulation):
    """A concrete class within the cim v1 type system.

    A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.
    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationRun, self).__init__()

        self.date_range = shared.DateRange()              # shared.DateRange
        self.doc_info = shared.DocInfo()                  # shared.DocInfo
        self.model = None                                 # software.ModelComponent
        self.model_reference = None                       # shared.DocReference


class SpatioTemporalConstraint(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.
    """
    def __init__(self):
        """Constructor.

        """
        super(SpatioTemporalConstraint, self).__init__()

        self.date_range = None                            # shared.DateRange
        self.spatial_resolution = ''                      # activity.ResolutionType
        self.requirement_type = str("spatioTemporalConstraint")


class DownscalingSimulation(NumericalActivity):
    """An abstract class within the cim v1 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DownscalingSimulation, self).__init__()

        self.calendar = shared.Calendar()                 # shared.Calendar
        self.doc_info = shared.DocInfo()                  # shared.DocInfo
        self.downscaled_from = shared.DataSource()        # shared.DataSource
        self.downscaled_from_reference = shared.DocReference()# shared.DocReference
        self.downscaling_id = str()                       # str
        self.downscaling_type = ''                        # activity.DownscalingType
        self.inputs = []                                  # software.Coupling
        self.output_references = []                       # shared.DocReference
        self.outputs = []                                 # data.DataObject


class Ensemble(NumericalActivity):
    """A concrete class within the cim v1 type system.

    An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.
    """
    def __init__(self):
        """Constructor.

        """
        super(Ensemble, self).__init__()

        self.doc_info = shared.DocInfo()                  # shared.DocInfo
        self.members = []                                 # activity.EnsembleMember
        self.outputs = []                                 # shared.DataSource
        self.outputs_references = []                      # shared.DocReference
        self.types = []                                   # activity.EnsembleType


class EnsembleMember(NumericalActivity):
    """A concrete class within the cim v1 type system.

    A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.
    """
    def __init__(self):
        """Constructor.

        """
        super(EnsembleMember, self).__init__()

        self.ensemble = None                              # activity.Ensemble
        self.ensemble_ids = []                            # shared.StandardName
        self.ensemble_reference = None                    # shared.DocReference
        self.simulation = None                            # activity.Simulation
        self.simulation_reference = None                  # shared.DocReference


class ConformanceType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class DownscalingType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class EnsembleType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class ExperimentRelationshipType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class FrequencyType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class ProjectType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class ResolutionType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class SimulationRelationshipType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


class SimulationType(object):
    """An enumeration within the cim v1 type system.

    
    """

    pass


