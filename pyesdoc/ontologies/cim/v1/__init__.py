
"""
.. module:: cim.v1.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v1 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
# Ontology name.
NAME = 'cim'

# Ontology Version.
VERSION = '1'

# Ontology full name.
FULL_NAME = '{}.{}'.format(NAME, VERSION)

# Ontology package set.
from pyesdoc.ontologies.cim.v1 import typeset_for_activity_package as activity
from pyesdoc.ontologies.cim.v1 import typeset_for_data_package as data
from pyesdoc.ontologies.cim.v1 import typeset_for_grids_package as grids
from pyesdoc.ontologies.cim.v1 import typeset_for_misc_package as misc
from pyesdoc.ontologies.cim.v1 import typeset_for_quality_package as quality
from pyesdoc.ontologies.cim.v1 import typeset_for_shared_package as shared
from pyesdoc.ontologies.cim.v1 import typeset_for_software_package as software

# Ontology class set.
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import Activity
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import BoundaryCondition
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import Conformance
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import DownscalingSimulation
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import Ensemble
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import EnsembleMember
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import Experiment
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import ExperimentRelationship
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import ExperimentRelationshipTarget
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import InitialCondition
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import LateralBoundaryCondition
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import MeasurementCampaign
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import NumericalActivity
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import NumericalExperiment
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import NumericalRequirement
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import NumericalRequirementOption
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import OutputRequirement
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import PhysicalModification
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import Simulation
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import SimulationComposite
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import SimulationRelationship
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import SimulationRelationshipTarget
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import SimulationRun
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import SpatioTemporalConstraint
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataContent
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataDistribution
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataExtent
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataExtentGeographical
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataExtentTemporal
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataExtentTimeInterval
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataHierarchyLevel
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataObject
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataProperty
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataRestriction
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataStorage
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataStorageDb
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataStorageFile
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataStorageIp
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataTopic
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import CoordinateList
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import GridExtent
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import GridMosaic
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import GridProperty
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import GridSpec
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import GridTile
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import GridTileResolutionType
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import SimpleGridGeometry
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import VerticalCoordinateList
from pyesdoc.ontologies.cim.v1.typeset_for_misc_package import DocumentSet
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import CimQuality
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import Evaluation
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import Measure
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import Report
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Calendar
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Change
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import ChangeProperty
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Citation
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import ClosedDateRange
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Compiler
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Daily360
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import DataSource
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import DateRange
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import DocMetaInfo
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import DocReference
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import License
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Machine
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import MachineCompilerUnit
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import OpenDateRange
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import PerpetualPeriod
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Platform
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Property
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import RealCalendar
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Relationship
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import ResponsibleParty
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import Standard
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import StandardName
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import Component
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ComponentLanguage
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ComponentLanguageProperty
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ComponentProperty
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import Composition
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import Connection
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ConnectionEndpoint
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ConnectionProperty
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import Coupling
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import CouplingEndpoint
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import CouplingProperty
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import Deployment
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import EntryPoint
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ModelComponent
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import Parallelisation
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ProcessorComponent
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import Rank
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import SpatialRegridding
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import SpatialRegriddingProperty
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import SpatialRegriddingUserMethod
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import StatisticalModelComponent
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import TimeLag
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import TimeTransformation
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import Timing

# Ontology enum set.
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import ConformanceType
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import DownscalingType
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import EnsembleType
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import ExperimentRelationshipType
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import FrequencyType
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import ProjectType
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import ResolutionType
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import SimulationRelationshipType
from pyesdoc.ontologies.cim.v1.typeset_for_activity_package import SimulationType
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataHierarchyType
from pyesdoc.ontologies.cim.v1.typeset_for_data_package import DataStatusType
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import ArcTypeEnum
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import DiscretizationEnum
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import FeatureTypeEnum
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import GeometryTypeEnum
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import GridNodePositionEnum
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import GridTypeEnum
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import HorizontalCsEnum
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import RefinementTypeEnum
from pyesdoc.ontologies.cim.v1.typeset_for_grids_package import VerticalCsEnum
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import CimFeatureType
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import CimResultType
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import CimScopeCodeType
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import QualityIssueType
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import QualitySeverityType
from pyesdoc.ontologies.cim.v1.typeset_for_quality_package import QualityStatusType
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import ChangePropertyType
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import CompilerType
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import DataPurpose
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import InterconnectType
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import MachineType
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import MachineVendorType
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import OperatingSystemType
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import ProcessorType
from pyesdoc.ontologies.cim.v1.typeset_for_shared_package import UnitType
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ComponentPropertyIntentType
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ConnectionType
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import CouplingFrameworkType
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import ModelComponentType
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import SpatialRegriddingDimensionType
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import SpatialRegriddingStandardMethodType
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import StatisticalModelComponentType
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import TimeMappingType
from pyesdoc.ontologies.cim.v1.typeset_for_software_package import TimingUnits

from pyesdoc.ontologies.cim.v1 import decoder
from pyesdoc.ontologies.cim.v1 import type_info
from pyesdoc.ontologies.cim.v1 import typeset
