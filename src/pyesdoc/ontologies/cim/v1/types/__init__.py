"""
.. module:: cim.v1.types.__init__.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 types.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.013856.

"""

# Module imports.
from pyesdoc.ontologies.cim.v1.types.activity.activity import Activity
from pyesdoc.ontologies.cim.v1.types.activity.boundary_condition import BoundaryCondition
from pyesdoc.ontologies.cim.v1.types.activity.conformance import Conformance
from pyesdoc.ontologies.cim.v1.types.activity.downscaling_simulation import DownscalingSimulation
from pyesdoc.ontologies.cim.v1.types.activity.ensemble import Ensemble
from pyesdoc.ontologies.cim.v1.types.activity.ensemble_member import EnsembleMember
from pyesdoc.ontologies.cim.v1.types.activity.experiment import Experiment
from pyesdoc.ontologies.cim.v1.types.activity.experiment_relationship import ExperimentRelationship
from pyesdoc.ontologies.cim.v1.types.activity.experiment_relationship_target import ExperimentRelationshipTarget
from pyesdoc.ontologies.cim.v1.types.activity.initial_condition import InitialCondition
from pyesdoc.ontologies.cim.v1.types.activity.lateral_boundary_condition import LateralBoundaryCondition
from pyesdoc.ontologies.cim.v1.types.activity.measurement_campaign import MeasurementCampaign
from pyesdoc.ontologies.cim.v1.types.activity.numerical_activity import NumericalActivity
from pyesdoc.ontologies.cim.v1.types.activity.numerical_experiment import NumericalExperiment
from pyesdoc.ontologies.cim.v1.types.activity.numerical_requirement import NumericalRequirement
from pyesdoc.ontologies.cim.v1.types.activity.numerical_requirement_option import NumericalRequirementOption
from pyesdoc.ontologies.cim.v1.types.activity.output_requirement import OutputRequirement
from pyesdoc.ontologies.cim.v1.types.activity.physical_modification import PhysicalModification
from pyesdoc.ontologies.cim.v1.types.activity.simulation import Simulation
from pyesdoc.ontologies.cim.v1.types.activity.simulation_composite import SimulationComposite
from pyesdoc.ontologies.cim.v1.types.activity.simulation_relationship import SimulationRelationship
from pyesdoc.ontologies.cim.v1.types.activity.simulation_relationship_target import SimulationRelationshipTarget
from pyesdoc.ontologies.cim.v1.types.activity.simulation_run import SimulationRun
from pyesdoc.ontologies.cim.v1.types.activity.spatio_temporal_constraint import SpatioTemporalConstraint
from pyesdoc.ontologies.cim.v1.types.data.data_content import DataContent
from pyesdoc.ontologies.cim.v1.types.data.data_distribution import DataDistribution
from pyesdoc.ontologies.cim.v1.types.data.data_extent import DataExtent
from pyesdoc.ontologies.cim.v1.types.data.data_extent_geographical import DataExtentGeographical
from pyesdoc.ontologies.cim.v1.types.data.data_extent_temporal import DataExtentTemporal
from pyesdoc.ontologies.cim.v1.types.data.data_extent_time_interval import DataExtentTimeInterval
from pyesdoc.ontologies.cim.v1.types.data.data_hierarchy_level import DataHierarchyLevel
from pyesdoc.ontologies.cim.v1.types.data.data_object import DataObject
from pyesdoc.ontologies.cim.v1.types.data.data_property import DataProperty
from pyesdoc.ontologies.cim.v1.types.data.data_restriction import DataRestriction
from pyesdoc.ontologies.cim.v1.types.data.data_storage import DataStorage
from pyesdoc.ontologies.cim.v1.types.data.data_storage_db import DataStorageDb
from pyesdoc.ontologies.cim.v1.types.data.data_storage_file import DataStorageFile
from pyesdoc.ontologies.cim.v1.types.data.data_storage_ip import DataStorageIp
from pyesdoc.ontologies.cim.v1.types.data.data_topic import DataTopic
from pyesdoc.ontologies.cim.v1.types.grids.coordinate_list import CoordinateList
from pyesdoc.ontologies.cim.v1.types.grids.grid_extent import GridExtent
from pyesdoc.ontologies.cim.v1.types.grids.grid_mosaic import GridMosaic
from pyesdoc.ontologies.cim.v1.types.grids.grid_property import GridProperty
from pyesdoc.ontologies.cim.v1.types.grids.grid_spec import GridSpec
from pyesdoc.ontologies.cim.v1.types.grids.grid_tile import GridTile
from pyesdoc.ontologies.cim.v1.types.grids.grid_tile_resolution_type import GridTileResolutionType
from pyesdoc.ontologies.cim.v1.types.grids.vertical_coordinate_list import VerticalCoordinateList
from pyesdoc.ontologies.cim.v1.types.quality.cim_quality import CimQuality
from pyesdoc.ontologies.cim.v1.types.quality.evaluation import Evaluation
from pyesdoc.ontologies.cim.v1.types.quality.measure import Measure
from pyesdoc.ontologies.cim.v1.types.quality.report import Report
from pyesdoc.ontologies.cim.v1.types.shared.calendar import Calendar
from pyesdoc.ontologies.cim.v1.types.shared.change import Change
from pyesdoc.ontologies.cim.v1.types.shared.change_property import ChangeProperty
from pyesdoc.ontologies.cim.v1.types.shared.cim_document_relationship import CimDocumentRelationship
from pyesdoc.ontologies.cim.v1.types.shared.cim_document_relationship_target import CimDocumentRelationshipTarget
from pyesdoc.ontologies.cim.v1.types.shared.cim_genealogy import CimGenealogy
from pyesdoc.ontologies.cim.v1.types.shared.cim_info import CimInfo
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.shared.cim_relationship import CimRelationship
from pyesdoc.ontologies.cim.v1.types.shared.cim_type_info import CimTypeInfo
from pyesdoc.ontologies.cim.v1.types.shared.citation import Citation
from pyesdoc.ontologies.cim.v1.types.shared.closed_date_range import ClosedDateRange
from pyesdoc.ontologies.cim.v1.types.shared.compiler import Compiler
from pyesdoc.ontologies.cim.v1.types.shared.daily_360 import Daily360
from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.date_range import DateRange
from pyesdoc.ontologies.cim.v1.types.shared.license import License
from pyesdoc.ontologies.cim.v1.types.shared.machine import Machine
from pyesdoc.ontologies.cim.v1.types.shared.machine_compiler_unit import MachineCompilerUnit
from pyesdoc.ontologies.cim.v1.types.shared.open_date_range import OpenDateRange
from pyesdoc.ontologies.cim.v1.types.shared.perpetual_period import PerpetualPeriod
from pyesdoc.ontologies.cim.v1.types.shared.platform import Platform
from pyesdoc.ontologies.cim.v1.types.shared.property import Property
from pyesdoc.ontologies.cim.v1.types.shared.real_calendar import RealCalendar
from pyesdoc.ontologies.cim.v1.types.shared.responsible_party import ResponsibleParty
from pyesdoc.ontologies.cim.v1.types.shared.responsible_party_contact_info import ResponsiblePartyContactInfo
from pyesdoc.ontologies.cim.v1.types.shared.standard import Standard
from pyesdoc.ontologies.cim.v1.types.shared.standard_name import StandardName
from pyesdoc.ontologies.cim.v1.types.software.component import Component
from pyesdoc.ontologies.cim.v1.types.software.component_language import ComponentLanguage
from pyesdoc.ontologies.cim.v1.types.software.component_language_property import ComponentLanguageProperty
from pyesdoc.ontologies.cim.v1.types.software.component_property import ComponentProperty
from pyesdoc.ontologies.cim.v1.types.software.composition import Composition
from pyesdoc.ontologies.cim.v1.types.software.connection import Connection
from pyesdoc.ontologies.cim.v1.types.software.connection_endpoint import ConnectionEndpoint
from pyesdoc.ontologies.cim.v1.types.software.connection_property import ConnectionProperty
from pyesdoc.ontologies.cim.v1.types.software.coupling import Coupling
from pyesdoc.ontologies.cim.v1.types.software.coupling_endpoint import CouplingEndpoint
from pyesdoc.ontologies.cim.v1.types.software.coupling_property import CouplingProperty
from pyesdoc.ontologies.cim.v1.types.software.deployment import Deployment
from pyesdoc.ontologies.cim.v1.types.software.entry_point import EntryPoint
from pyesdoc.ontologies.cim.v1.types.software.model_component import ModelComponent
from pyesdoc.ontologies.cim.v1.types.software.parallelisation import Parallelisation
from pyesdoc.ontologies.cim.v1.types.software.processor_component import ProcessorComponent
from pyesdoc.ontologies.cim.v1.types.software.rank import Rank
from pyesdoc.ontologies.cim.v1.types.software.spatial_regridding import SpatialRegridding
from pyesdoc.ontologies.cim.v1.types.software.spatial_regridding_property import SpatialRegriddingProperty
from pyesdoc.ontologies.cim.v1.types.software.spatial_regridding_user_method import SpatialRegriddingUserMethod
from pyesdoc.ontologies.cim.v1.types.software.statistical_model_component import StatisticalModelComponent
from pyesdoc.ontologies.cim.v1.types.software.time_lag import TimeLag
from pyesdoc.ontologies.cim.v1.types.software.time_transformation import TimeTransformation
from pyesdoc.ontologies.cim.v1.types.software.timing import Timing


