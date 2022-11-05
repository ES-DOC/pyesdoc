
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

# Ontology package set.
import pyesdoc.ontologies.cim.v2.typeset_for_activity_package as activity
import pyesdoc.ontologies.cim.v2.typeset_for_cmip_package as cmip
import pyesdoc.ontologies.cim.v2.typeset_for_data_package as data
import pyesdoc.ontologies.cim.v2.typeset_for_designing_package as designing
import pyesdoc.ontologies.cim.v2.typeset_for_drs_package as drs
import pyesdoc.ontologies.cim.v2.typeset_for_iso_package as iso
import pyesdoc.ontologies.cim.v2.typeset_for_platform_package as platform
import pyesdoc.ontologies.cim.v2.typeset_for_science_package as science
import pyesdoc.ontologies.cim.v2.typeset_for_shared_package as shared
import pyesdoc.ontologies.cim.v2.typeset_for_software_package as software
import pyesdoc.ontologies.cim.v2.typeset_for_time_package as time

# Ontology class set.
from pyesdoc.ontologies.cim.v2.typeset_for_activity_package import Activity
from pyesdoc.ontologies.cim.v2.typeset_for_activity_package import AxisMember
from pyesdoc.ontologies.cim.v2.typeset_for_activity_package import ChildSimulation
from pyesdoc.ontologies.cim.v2.typeset_for_activity_package import Conformance
from pyesdoc.ontologies.cim.v2.typeset_for_activity_package import Ensemble
from pyesdoc.ontologies.cim.v2.typeset_for_activity_package import EnsembleAxis
from pyesdoc.ontologies.cim.v2.typeset_for_activity_package import Simulation
from pyesdoc.ontologies.cim.v2.typeset_for_activity_package import UberEnsemble
from pyesdoc.ontologies.cim.v2.typeset_for_cmip_package import CmipDataset
from pyesdoc.ontologies.cim.v2.typeset_for_cmip_package import CmipSimulation
from pyesdoc.ontologies.cim.v2.typeset_for_data_package import Dataset
from pyesdoc.ontologies.cim.v2.typeset_for_data_package import VariableCollection
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import DomainRequirements
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import EnsembleRequirement
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import ForcingConstraint
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import InitialisationRequirement
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import MultiEnsemble
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import NumericalExperiment
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import NumericalRequirement
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import Objective
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import OutputRequirement
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import Project
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import SimulationPlan
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import StartDateEnsemble
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import TemporalConstraint
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsAtomicDataset
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsEnsembleIdentifier
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsExperiment
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsGeographicalIndicator
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsPublicationDataset
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsSimulationIdentifier
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsTemporalIdentifier
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import Algorithm
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import Lineage
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import ProcessStep
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import ProcessStepReport
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import Processing
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import QualityEvaluationOutput
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import QualityEvaluationResult
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import QualityIssue
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import QualityReport
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import ComputePool
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import Interconnect
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import Machine
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import Nic
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import Partition
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import Performance
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import PerformanceDetail
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import ProjectCost
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import StoragePool
from pyesdoc.ontologies.cim.v2.typeset_for_science_package import Model
from pyesdoc.ontologies.cim.v2.typeset_for_science_package import Realm
from pyesdoc.ontologies.cim.v2.typeset_for_science_package import RealmCoupling
from pyesdoc.ontologies.cim.v2.typeset_for_science_package import Topic
from pyesdoc.ontologies.cim.v2.typeset_for_science_package import TopicProperty
from pyesdoc.ontologies.cim.v2.typeset_for_science_package import TopicPropertySet
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import Citation
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import DocMetaInfo
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import DocReference
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import ExtraAttribute
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import FormalAssociation
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import Numeric
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import OnlineResource
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import Party
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import QualityReview
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import Responsibility
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import TextBlob
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import ComponentBase
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import Composition
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import DevelopmentPath
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import EntryPoint
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import Gridspec
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import Implementation
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import SoftwareComponent
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import Variable
from pyesdoc.ontologies.cim.v2.typeset_for_time_package import Calendar
from pyesdoc.ontologies.cim.v2.typeset_for_time_package import DateTime
from pyesdoc.ontologies.cim.v2.typeset_for_time_package import DatetimeSet
from pyesdoc.ontologies.cim.v2.typeset_for_time_package import IrregularDateset
from pyesdoc.ontologies.cim.v2.typeset_for_time_package import RegularTimeset
from pyesdoc.ontologies.cim.v2.typeset_for_time_package import TimePeriod

# Ontology enum set.
from pyesdoc.ontologies.cim.v2.typeset_for_activity_package import ConformanceType
from pyesdoc.ontologies.cim.v2.typeset_for_data_package import DatasetType
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import EnsembleTypes
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import ExperimentalRelationships
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import ForcingTypes
from pyesdoc.ontologies.cim.v2.typeset_for_designing_package import NumericalRequirementScope
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsFrequencyTypes
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsGeographicalOperators
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsRealms
from pyesdoc.ontologies.cim.v2.typeset_for_drs_package import DrsTimeSuffixes
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import DqEvaluationResultType
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import DsInitiativeTypecode
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import MdCellgeometryCode
from pyesdoc.ontologies.cim.v2.typeset_for_iso_package import MdProgressCode
from pyesdoc.ontologies.cim.v2.typeset_for_platform_package import StorageSystems
from pyesdoc.ontologies.cim.v2.typeset_for_science_package import ModelTypes
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import NilReason
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import QualityStatus
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import RoleCode
from pyesdoc.ontologies.cim.v2.typeset_for_shared_package import TextBlobEncoding
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import CouplingFramework
from pyesdoc.ontologies.cim.v2.typeset_for_software_package import ProgrammingLanguage
from pyesdoc.ontologies.cim.v2.typeset_for_time_package import CalendarTypes
from pyesdoc.ontologies.cim.v2.typeset_for_time_package import PeriodDateTypes
from pyesdoc.ontologies.cim.v2.typeset_for_time_package import TimeUnits

from pyesdoc.ontologies.cim.v2 import type_info
from pyesdoc.ontologies.cim.v2 import typeset
try:
	from pyesdoc.ontologies.cim.v2 import decoder
except ImportError:
	pass
