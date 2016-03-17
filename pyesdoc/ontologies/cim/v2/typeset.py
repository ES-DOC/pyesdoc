
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from typeset_for_activity_package import *
from typeset_for_data_package import *
from typeset_for_designing_package import *
from typeset_for_drs_package import *
from typeset_for_platform_package import *
from typeset_for_science_package import *
from typeset_for_shared_package import *
from typeset_for_software_package import *


import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_designing_package as designing
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform
import typeset_for_science_package as science
import typeset_for_shared_package as shared
import typeset_for_software_package as software



# Module exports.
__all__ = [
    # Packages
    activity,
    data,
    designing,
    drs,
    platform,
    science,
    shared,
    software,
    # Classes
    Activity,
    AxisMember,
    Conformance,
    Ensemble,
    EnsembleAxis,
    EnsembleMember,
    ParentSimulation,
    UberEnsemble,
    Dataset,
    Downscaling,
    Simulation,
    VariableCollection,
    AxisMember,
    DomainProperties,
    EnsembleRequirement,
    ForcingConstraint,
    MultiEnsemble,
    NumericalExperiment,
    NumericalRequirement,
    OutputTemporalRequirement,
    Project,
    SimulationPlan,
    StartDateEnsemble,
    TemporalConstraint,
    DrsAtomicDataset,
    DrsEnsembleIdentifier,
    DrsExperiment,
    DrsGeographicalIndicator,
    DrsPublicationDataset,
    DrsSimulationIdentifier,
    DrsTemporalIdentifier,
    ComponentPerformance,
    ComputePool,
    Machine,
    Partition,
    Performance,
    StoragePool,
    StorageVolume,
    ConservationProperties,
    Detail,
    Discretisation,
    Extent,
    Grid,
    KeyProperties,
    Model,
    Process,
    Resolution,
    ScienceContext,
    ScientificDomain,
    SubProcess,
    Tuning,
    Calendar,
    Cimtext,
    CitationTarget,
    DateTime,
    DatetimeSet,
    DocMetaInfo,
    DocReference,
    IrregularDateset,
    KeyFloat,
    NumberArray,
    OnlineResource,
    Party,
    Pid,
    QualityReview,
    Reference,
    RegularTimeset,
    Responsibility,
    TimePeriod,
    TimesliceList,
    ComponentBase,
    Composition,
    DevelopmentPath,
    EntryPoint,
    Gridspec,
    SoftwareComponent,
    Variable,
    # Enums
    DataAssociationTypes,
    EnsembleTypes,
    ExperimentalRelationships,
    ForcingTypes,
    DrsFrequencyTypes,
    DrsGeographicalOperators,
    DrsRealms,
    DrsTimeSuffixes,
    StorageSystems,
    VolumeUnits,
    ModelTypes,
    SelectionCardinality,
    CalendarTypes,
    DocumentTypes,
    NilReason,
    PeriodDateTypes,
    QualityStatus,
    RoleCode,
    SlicetimeUnits,
    TextCode,
    TimeUnits,
    CouplingFramework,
    ProgrammingLanguage,
]

