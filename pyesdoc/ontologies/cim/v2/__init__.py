
"""
.. module:: cim.v2.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim v2 package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
# Ontology name.
NAME = 'cim'

# Ontology Version.
VERSION = '2'

# Ontology full name.
FULL_NAME = '{}.{}'.format(NAME, VERSION)

# Ontology packag set.
from . import typeset_for_activity_package as activity
from . import typeset_for_cmip_package as cmip
from . import typeset_for_data_package as data
from . import typeset_for_designing_package as designing
from . import typeset_for_drs_package as drs
from . import typeset_for_iso_package as iso
from . import typeset_for_platform_package as platform
from . import typeset_for_science_package as science
from . import typeset_for_shared_package as shared
from . import typeset_for_software_package as software
from . import typeset_for_time_package as time

# Ontology class set.
from .typeset_for_activity_package import Activity
from .typeset_for_activity_package import AxisMember
from .typeset_for_activity_package import ChildSimulation
from .typeset_for_activity_package import Conformance
from .typeset_for_activity_package import Ensemble
from .typeset_for_activity_package import EnsembleAxis
from .typeset_for_activity_package import Simulation
from .typeset_for_activity_package import UberEnsemble
from .typeset_for_cmip_package import CmipDataset
from .typeset_for_cmip_package import CmipSimulation
from .typeset_for_data_package import Dataset
from .typeset_for_data_package import VariableCollection
from .typeset_for_designing_package import DomainRequirements
from .typeset_for_designing_package import EnsembleRequirement
from .typeset_for_designing_package import ForcingConstraint
from .typeset_for_designing_package import InitialisationRequirement
from .typeset_for_designing_package import MultiEnsemble
from .typeset_for_designing_package import NumericalExperiment
from .typeset_for_designing_package import NumericalRequirement
from .typeset_for_designing_package import Objective
from .typeset_for_designing_package import OutputRequirement
from .typeset_for_designing_package import Project
from .typeset_for_designing_package import SimulationPlan
from .typeset_for_designing_package import StartDateEnsemble
from .typeset_for_designing_package import TemporalConstraint
from .typeset_for_drs_package import DrsAtomicDataset
from .typeset_for_drs_package import DrsEnsembleIdentifier
from .typeset_for_drs_package import DrsExperiment
from .typeset_for_drs_package import DrsGeographicalIndicator
from .typeset_for_drs_package import DrsPublicationDataset
from .typeset_for_drs_package import DrsSimulationIdentifier
from .typeset_for_drs_package import DrsTemporalIdentifier
from .typeset_for_iso_package import Algorithm
from .typeset_for_iso_package import Lineage
from .typeset_for_iso_package import ProcessStep
from .typeset_for_iso_package import ProcessStepReport
from .typeset_for_iso_package import Processing
from .typeset_for_iso_package import QualityEvaluationOutput
from .typeset_for_iso_package import QualityEvaluationResult
from .typeset_for_iso_package import QualityIssue
from .typeset_for_iso_package import QualityReport
from .typeset_for_platform_package import ComputePool
from .typeset_for_platform_package import Interconnect
from .typeset_for_platform_package import Machine
from .typeset_for_platform_package import Nic
from .typeset_for_platform_package import Partition
from .typeset_for_platform_package import Performance
from .typeset_for_platform_package import PerformanceDetail
from .typeset_for_platform_package import ProjectCost
from .typeset_for_platform_package import StoragePool
from .typeset_for_science_package import Model
from .typeset_for_science_package import Realm
from .typeset_for_science_package import RealmCoupling
from .typeset_for_science_package import Topic
from .typeset_for_science_package import TopicProperty
from .typeset_for_science_package import TopicPropertySet
from .typeset_for_shared_package import Citation
from .typeset_for_shared_package import DocMetaInfo
from .typeset_for_shared_package import DocReference
from .typeset_for_shared_package import ExtraAttribute
from .typeset_for_shared_package import FormalAssociation
from .typeset_for_shared_package import Numeric
from .typeset_for_shared_package import OnlineResource
from .typeset_for_shared_package import Party
from .typeset_for_shared_package import QualityReview
from .typeset_for_shared_package import Responsibility
from .typeset_for_shared_package import TextBlob
from .typeset_for_software_package import ComponentBase
from .typeset_for_software_package import Composition
from .typeset_for_software_package import DevelopmentPath
from .typeset_for_software_package import EntryPoint
from .typeset_for_software_package import Gridspec
from .typeset_for_software_package import Implementation
from .typeset_for_software_package import SoftwareComponent
from .typeset_for_software_package import Variable
from .typeset_for_time_package import Calendar
from .typeset_for_time_package import DateTime
from .typeset_for_time_package import DatetimeSet
from .typeset_for_time_package import IrregularDateset
from .typeset_for_time_package import RegularTimeset
from .typeset_for_time_package import TimePeriod

# Ontology enum set.
from .typeset_for_activity_package import ConformanceType
from .typeset_for_data_package import DatasetType
from .typeset_for_designing_package import EnsembleTypes
from .typeset_for_designing_package import ExperimentalRelationships
from .typeset_for_designing_package import ForcingTypes
from .typeset_for_designing_package import NumericalRequirementScope
from .typeset_for_drs_package import DrsFrequencyTypes
from .typeset_for_drs_package import DrsGeographicalOperators
from .typeset_for_drs_package import DrsRealms
from .typeset_for_drs_package import DrsTimeSuffixes
from .typeset_for_iso_package import DqEvaluationResultType
from .typeset_for_iso_package import DsInitiativeTypecode
from .typeset_for_iso_package import MdCellgeometryCode
from .typeset_for_iso_package import MdProgressCode
from .typeset_for_platform_package import StorageSystems
from .typeset_for_science_package import ModelTypes
from .typeset_for_shared_package import NilReason
from .typeset_for_shared_package import QualityStatus
from .typeset_for_shared_package import RoleCode
from .typeset_for_shared_package import TextBlobEncoding
from .typeset_for_software_package import CouplingFramework
from .typeset_for_software_package import ProgrammingLanguage
from .typeset_for_time_package import CalendarTypes
from .typeset_for_time_package import PeriodDateTypes
from .typeset_for_time_package import TimeUnits

from . import type_info
from . import typeset
try:
	import decoder
except ImportError:
	pass
