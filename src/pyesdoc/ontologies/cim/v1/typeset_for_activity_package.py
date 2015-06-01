# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_activity_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.activity package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-01 16:50:10.355813.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class Activity(object):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of numerical_experiment class.

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

    Creates and returns instance of conformance class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Conformance, self).__init__()

        self.description = None                           # str
        self.frequency = None                             # activity.FrequencyType
        self.is_conformant = None                         # bool
        self.requirements = []                            # activity.NumericalRequirement
        self.requirements_references = []                 # shared.DocReference
        self.sources = []                                 # shared.DataSource
        self.sources_references = []                      # shared.DocReference
        self.type = None                                  # activity.ConformanceType


class ExperimentRelationship(shared.Relationship):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of experiment_relationship class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ExperimentRelationship, self).__init__()

        self.target = None                                # activity.ExperimentRelationshipTarget
        self.type = None                                  # activity.ExperimentRelationshipType


class ExperimentRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of experiment_relationship_target class.

    """
    def __init__(self):
        """Constructor.

        """
        super(ExperimentRelationshipTarget, self).__init__()

        self.numerical_experiment = None                  # activity.NumericalExperiment
        self.reference = None                             # shared.DocReference


class NumericalRequirement(object):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of numerical_requirement class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(NumericalRequirement, self).__init__()

        self.description = None                           # str
        self.id = None                                    # str
        self.name = None                                  # str
        self.options = []                                 # activity.NumericalRequirementOption
        self.requirement_type = None                      # str
        self.source = None                                # shared.DataSource
        self.source_reference = None                      # shared.DocReference


class NumericalRequirementOption(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of numerical_requirement_option class.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalRequirementOption, self).__init__()

        self.description = None                           # str
        self.id = None                                    # str
        self.name = None                                  # str
        self.relationship = None                          # str
        self.sub_options = []                             # activity.NumericalRequirementOption


class SimulationRelationship(shared.Relationship):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of simulation_relationship class.

    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationRelationship, self).__init__()

        self.target = None                                # activity.SimulationRelationshipTarget
        self.type = None                                  # activity.SimulationRelationshipType


class SimulationRelationshipTarget(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of simulation_relationship_target class.

    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationRelationshipTarget, self).__init__()

        self.reference = None                             # shared.DocReference
        self.target = None                                # activity.SimulationType


class BoundaryCondition(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of boundary_condition class.

    """
    def __init__(self):
        """Constructor.

        """
        super(BoundaryCondition, self).__init__()

        self.requirement_type = str("boundaryCondition")


class Experiment(Activity):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of experiment class.

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

    Creates and returns instance of initial_condition class.

    """
    def __init__(self):
        """Constructor.

        """
        super(InitialCondition, self).__init__()

        self.requirement_type = str("initialCondition")


class LateralBoundaryCondition(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of lateral_boundary_condition class.

    """
    def __init__(self):
        """Constructor.

        """
        super(LateralBoundaryCondition, self).__init__()

        self.requirement_type = str("lateralBoundaryCondition")


class MeasurementCampaign(Activity):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of measurement_campaign class.

    """
    def __init__(self):
        """Constructor.

        """
        super(MeasurementCampaign, self).__init__()

        self.duration = None                              # int


class NumericalActivity(Activity):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of numerical_activity class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(NumericalActivity, self).__init__()

        self.description = None                           # str
        self.long_name = None                             # str
        self.short_name = None                            # str
        self.supports = []                                # activity.Experiment
        self.supports_references = []                     # shared.DocReference


class NumericalExperiment(Experiment):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of numerical_experiment class.

    """
    def __init__(self):
        """Constructor.

        """
        super(NumericalExperiment, self).__init__()

        self.description = None                           # str
        self.experiment_id = None                         # str
        self.long_name = None                             # str
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.requirements = []                            # activity.NumericalRequirement
        self.short_name = None                            # str


class OutputRequirement(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of output_requirement class.

    """
    def __init__(self):
        """Constructor.

        """
        super(OutputRequirement, self).__init__()

        self.requirement_type = str("outputRequirement")


class PhysicalModification(Conformance):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of physical_modification class.

    """
    def __init__(self):
        """Constructor.

        """
        super(PhysicalModification, self).__init__()



class Simulation(NumericalActivity):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of simulation class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(Simulation, self).__init__()

        self.authors = None                               # str
        self.calendar = None                              # shared.Calendar
        self.conformances = []                            # activity.Conformance
        self.control_simulation = None                    # activity.Simulation
        self.control_simulation_reference = None          # shared.DocReference
        self.deployments = []                             # software.Deployment
        self.inputs = []                                  # software.Coupling
        self.output_references = []                       # shared.DocReference
        self.outputs = []                                 # data.DataObject
        self.restart_references = []                      # shared.DocReference
        self.restarts = []                                # data.DataObject
        self.simulation_id = None                         # str
        self.spinup_date_range = None                     # shared.ClosedDateRange
        self.spinup_simulation = None                     # activity.Simulation
        self.spinup_simulation_reference = None           # shared.DocReference


class SimulationComposite(Simulation):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of simulation_composite class.

    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationComposite, self).__init__()

        self.child = []                                   # activity.Simulation
        self.date_range = None                            # shared.DateRange
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.rank = None                                  # int


class SimulationRun(Simulation):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of simulation_run class.

    """
    def __init__(self):
        """Constructor.

        """
        super(SimulationRun, self).__init__()

        self.date_range = None                            # shared.DateRange
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.model = None                                 # software.ModelComponent
        self.model_reference = None                       # shared.DocReference


class SpatioTemporalConstraint(NumericalRequirement):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of spatio_temporal_constraint class.

    """
    def __init__(self):
        """Constructor.

        """
        super(SpatioTemporalConstraint, self).__init__()

        self.date_range = None                            # shared.DateRange
        self.spatial_resolution = None                    # activity.ResolutionType
        self.requirement_type = str("spatioTemporalConstraint")


class DownscalingSimulation(NumericalActivity):
    """An abstract class within the cim v1 type system.

    Creates and returns instance of downscaling simulation class.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor.

        """
        super(DownscalingSimulation, self).__init__()

        self.calendar = None                              # shared.Calendar
        self.downscaled_from = None                       # shared.DataSource
        self.downscaled_from_reference = None             # shared.DocReference
        self.downscaling_id = None                        # str
        self.downscaling_type = None                      # activity.DownscalingType
        self.inputs = []                                  # software.Coupling
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.output_references = []                       # shared.DocReference
        self.outputs = []                                 # data.DataObject


class Ensemble(NumericalActivity):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of ensemble class.

    """
    def __init__(self):
        """Constructor.

        """
        super(Ensemble, self).__init__()

        self.members = []                                 # activity.EnsembleMember
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.outputs = []                                 # shared.DataSource
        self.outputs_references = []                      # shared.DocReference
        self.types = []                                   # activity.EnsembleType


class EnsembleMember(NumericalActivity):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of ensemble_member class.

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

    Creates and returns instance of conformance_type enum.
    """

    pass


class DownscalingType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of downscaling_type enum.
    """

    pass


class EnsembleType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of ensemble_type enum.
    """

    pass


class ExperimentRelationshipType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of experiment_relationship_type enum.
    """

    pass


class FrequencyType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of frequency_type enum.
    """

    pass


class ProjectType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of project_type enum.
    """

    pass


class ResolutionType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of resolution_type enum.
    """

    pass


class SimulationRelationshipType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of simulation_relationship_type enum.
    """

    pass


class SimulationType(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of simulation_type enum.
    """

    pass


