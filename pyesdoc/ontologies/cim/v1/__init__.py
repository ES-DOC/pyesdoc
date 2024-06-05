
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

# Ontology packag set.
from . import typeset_for_activity_package as activity
from . import typeset_for_data_package as data
from . import typeset_for_grids_package as grids
from . import typeset_for_misc_package as misc
from . import typeset_for_quality_package as quality
from . import typeset_for_shared_package as shared
from . import typeset_for_software_package as software

# Ontology class set.
from .typeset_for_activity_package import Activity
from .typeset_for_activity_package import BoundaryCondition
from .typeset_for_activity_package import Conformance
from .typeset_for_activity_package import DownscalingSimulation
from .typeset_for_activity_package import Ensemble
from .typeset_for_activity_package import EnsembleMember
from .typeset_for_activity_package import Experiment
from .typeset_for_activity_package import ExperimentRelationship
from .typeset_for_activity_package import ExperimentRelationshipTarget
from .typeset_for_activity_package import InitialCondition
from .typeset_for_activity_package import LateralBoundaryCondition
from .typeset_for_activity_package import MeasurementCampaign
from .typeset_for_activity_package import NumericalActivity
from .typeset_for_activity_package import NumericalExperiment
from .typeset_for_activity_package import NumericalRequirement
from .typeset_for_activity_package import NumericalRequirementOption
from .typeset_for_activity_package import OutputRequirement
from .typeset_for_activity_package import PhysicalModification
from .typeset_for_activity_package import Simulation
from .typeset_for_activity_package import SimulationComposite
from .typeset_for_activity_package import SimulationRelationship
from .typeset_for_activity_package import SimulationRelationshipTarget
from .typeset_for_activity_package import SimulationRun
from .typeset_for_activity_package import SpatioTemporalConstraint
from .typeset_for_data_package import DataContent
from .typeset_for_data_package import DataDistribution
from .typeset_for_data_package import DataExtent
from .typeset_for_data_package import DataExtentGeographical
from .typeset_for_data_package import DataExtentTemporal
from .typeset_for_data_package import DataExtentTimeInterval
from .typeset_for_data_package import DataHierarchyLevel
from .typeset_for_data_package import DataObject
from .typeset_for_data_package import DataProperty
from .typeset_for_data_package import DataRestriction
from .typeset_for_data_package import DataStorage
from .typeset_for_data_package import DataStorageDb
from .typeset_for_data_package import DataStorageFile
from .typeset_for_data_package import DataStorageIp
from .typeset_for_data_package import DataTopic
from .typeset_for_grids_package import CoordinateList
from .typeset_for_grids_package import GridExtent
from .typeset_for_grids_package import GridMosaic
from .typeset_for_grids_package import GridProperty
from .typeset_for_grids_package import GridSpec
from .typeset_for_grids_package import GridTile
from .typeset_for_grids_package import GridTileResolutionType
from .typeset_for_grids_package import SimpleGridGeometry
from .typeset_for_grids_package import VerticalCoordinateList
from .typeset_for_misc_package import DocumentSet
from .typeset_for_quality_package import CimQuality
from .typeset_for_quality_package import Evaluation
from .typeset_for_quality_package import Measure
from .typeset_for_quality_package import Report
from .typeset_for_shared_package import Calendar
from .typeset_for_shared_package import Change
from .typeset_for_shared_package import ChangeProperty
from .typeset_for_shared_package import Citation
from .typeset_for_shared_package import ClosedDateRange
from .typeset_for_shared_package import Compiler
from .typeset_for_shared_package import Daily360
from .typeset_for_shared_package import DataSource
from .typeset_for_shared_package import DateRange
from .typeset_for_shared_package import DocMetaInfo
from .typeset_for_shared_package import DocReference
from .typeset_for_shared_package import License
from .typeset_for_shared_package import Machine
from .typeset_for_shared_package import MachineCompilerUnit
from .typeset_for_shared_package import OpenDateRange
from .typeset_for_shared_package import PerpetualPeriod
from .typeset_for_shared_package import Platform
from .typeset_for_shared_package import Property
from .typeset_for_shared_package import RealCalendar
from .typeset_for_shared_package import Relationship
from .typeset_for_shared_package import ResponsibleParty
from .typeset_for_shared_package import Standard
from .typeset_for_shared_package import StandardName
from .typeset_for_software_package import Component
from .typeset_for_software_package import ComponentLanguage
from .typeset_for_software_package import ComponentLanguageProperty
from .typeset_for_software_package import ComponentProperty
from .typeset_for_software_package import Composition
from .typeset_for_software_package import Connection
from .typeset_for_software_package import ConnectionEndpoint
from .typeset_for_software_package import ConnectionProperty
from .typeset_for_software_package import Coupling
from .typeset_for_software_package import CouplingEndpoint
from .typeset_for_software_package import CouplingProperty
from .typeset_for_software_package import Deployment
from .typeset_for_software_package import EntryPoint
from .typeset_for_software_package import ModelComponent
from .typeset_for_software_package import Parallelisation
from .typeset_for_software_package import ProcessorComponent
from .typeset_for_software_package import Rank
from .typeset_for_software_package import SpatialRegridding
from .typeset_for_software_package import SpatialRegriddingProperty
from .typeset_for_software_package import SpatialRegriddingUserMethod
from .typeset_for_software_package import StatisticalModelComponent
from .typeset_for_software_package import TimeLag
from .typeset_for_software_package import TimeTransformation
from .typeset_for_software_package import Timing

# Ontology enum set.
from .typeset_for_activity_package import ConformanceType
from .typeset_for_activity_package import DownscalingType
from .typeset_for_activity_package import EnsembleType
from .typeset_for_activity_package import ExperimentRelationshipType
from .typeset_for_activity_package import FrequencyType
from .typeset_for_activity_package import ProjectType
from .typeset_for_activity_package import ResolutionType
from .typeset_for_activity_package import SimulationRelationshipType
from .typeset_for_activity_package import SimulationType
from .typeset_for_data_package import DataHierarchyType
from .typeset_for_data_package import DataStatusType
from .typeset_for_grids_package import ArcTypeEnum
from .typeset_for_grids_package import DiscretizationEnum
from .typeset_for_grids_package import FeatureTypeEnum
from .typeset_for_grids_package import GeometryTypeEnum
from .typeset_for_grids_package import GridNodePositionEnum
from .typeset_for_grids_package import GridTypeEnum
from .typeset_for_grids_package import HorizontalCsEnum
from .typeset_for_grids_package import RefinementTypeEnum
from .typeset_for_grids_package import VerticalCsEnum
from .typeset_for_quality_package import CimFeatureType
from .typeset_for_quality_package import CimResultType
from .typeset_for_quality_package import CimScopeCodeType
from .typeset_for_quality_package import QualityIssueType
from .typeset_for_quality_package import QualitySeverityType
from .typeset_for_quality_package import QualityStatusType
from .typeset_for_shared_package import ChangePropertyType
from .typeset_for_shared_package import CompilerType
from .typeset_for_shared_package import DataPurpose
from .typeset_for_shared_package import InterconnectType
from .typeset_for_shared_package import MachineType
from .typeset_for_shared_package import MachineVendorType
from .typeset_for_shared_package import OperatingSystemType
from .typeset_for_shared_package import ProcessorType
from .typeset_for_shared_package import UnitType
from .typeset_for_software_package import ComponentPropertyIntentType
from .typeset_for_software_package import ConnectionType
from .typeset_for_software_package import CouplingFrameworkType
from .typeset_for_software_package import ModelComponentType
from .typeset_for_software_package import SpatialRegriddingDimensionType
from .typeset_for_software_package import SpatialRegriddingStandardMethodType
from .typeset_for_software_package import StatisticalModelComponentType
from .typeset_for_software_package import TimeMappingType
from .typeset_for_software_package import TimingUnits

from . import type_info
from . import typeset
try:
	from . import decoder
except ImportError:
	pass
