
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import datetime
import uuid

from typeset_for_shared_package import *
from typeset_for_platform_package import *
from typeset_for_data_package import *
from typeset_for_activity_package import *
from typeset_for_drs_package import *
from typeset_for_software_package import *
from typeset_for_science_package import *
from typeset_for_designing_package import *


import typeset_for_shared_package as shared
import typeset_for_platform_package as platform
import typeset_for_data_package as data
import typeset_for_activity_package as activity
import typeset_for_drs_package as drs
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_designing_package as designing



# Module exports.
__all__ = [
    'PACKAGES',
    'DOCUMENT_TYPES',
    'CLASSES',
    'ENUMS',

    # Packages
    shared,
    platform,
    data,
    activity,
    drs,
    software,
    science,
    designing,

    # Classes
    ConservationProperties,
    Detail,
    DrsAtomicDataset,
    Extent,
    Simulation,
    EnsembleAxis,
    OutputTemporalRequirement,
    ScienceContext,
    DomainProperties,
    MultiEnsemble,
    SubProcess,
    KeyProperties,
    IrregularDateset,
    EntryPoint,
    UberEnsemble,
    KeyFloat,
    ComputePool,
    Resolution,
    ComponentBase,
    TimesliceList,
    ScientificDomain,
    ParentSimulation,
    OnlineResource,
    QualityReview,
    Process,
    EnsembleRequirement,
    Dataset,
    DocMetaInfo,
    Reference,
    DrsGeographicalIndicator,
    DevelopmentPath,
    Responsibility,
    StoragePool,
    Partition,
    SoftwareComponent,
    EnsembleMember,
    Algorithm,
    Machine,
    Cimtext,
    RegularTimeset,
    Model,
    DocReference,
    NumericalRequirement,
    ForcingConstraint,
    ExternalDocument,
    NumericalExperiment,
    TimePeriod,
    VariableCollection,
    DateTime,
    Gridspec,
    MultiTimeEnsemble,
    Grid,
    Performance,
    DatetimeSet,
    TemporalConstraint,
    Tuning,
    Activity,
    DrsEnsembleIdentifier,
    SimulationPlan,
    Conformance,
    Project,
    DrsPublicationDataset,
    AxisMember,
    Party,
    DrsTemporalIdentifier,
    Ensemble,
    StorageVolume,
    ComponentPerformance,
    Pid,
    Calendar,
    NumberArray,
    Composition,
    Downscaling,
    Variable,

    # Enums
    DrsTimeSuffixes,
    StorageSystems,
    PeriodDateTypes,
    DocumentTypes,
    DrsGeographicalOperators,
    TimeUnits,
    EnsembleTypes,
    SlicetimeUnits,
    SelectionCardinality,
    TextCode,
    VolumeUnits,
    ProgrammingLanguage,
    ForcingTypes,
    ModelTypes,
    NilReason,
    DrsRealms,
    ForcingTypes,
    ExperimentalRelationships,
    DrsFrequencyTypes,
    CouplingFramework,
    CalendarTypes,
    DataAssociationTypes,
    RoleCode,
    QualityStatus,
    EnsembleTypes,
    ]



# Supported packages.
PACKAGES = (
    shared,
    platform,
    data,
    activity,
    drs,
    software,
    science,
    designing,
	)

# Supported classes.
CLASSES = (
    science.ConservationProperties,
    science.Detail,
    drs.DrsAtomicDataset,
    science.Extent,
    data.Simulation,
    activity.EnsembleAxis,
    designing.OutputTemporalRequirement,
    science.ScienceContext,
    designing.DomainProperties,
    designing.MultiEnsemble,
    science.SubProcess,
    science.KeyProperties,
    shared.IrregularDateset,
    software.EntryPoint,
    activity.UberEnsemble,
    shared.KeyFloat,
    platform.ComputePool,
    science.Resolution,
    software.ComponentBase,
    shared.TimesliceList,
    science.ScientificDomain,
    activity.ParentSimulation,
    shared.OnlineResource,
    shared.QualityReview,
    science.Process,
    designing.EnsembleRequirement,
    data.Dataset,
    shared.DocMetaInfo,
    shared.Reference,
    drs.DrsGeographicalIndicator,
    software.DevelopmentPath,
    shared.Responsibility,
    platform.StoragePool,
    platform.Partition,
    software.SoftwareComponent,
    activity.EnsembleMember,
    science.Algorithm,
    platform.Machine,
    shared.Cimtext,
    shared.RegularTimeset,
    science.Model,
    shared.DocReference,
    designing.NumericalRequirement,
    designing.ForcingConstraint,
    shared.ExternalDocument,
    designing.NumericalExperiment,
    shared.TimePeriod,
    data.VariableCollection,
    shared.DateTime,
    software.Gridspec,
    designing.MultiTimeEnsemble,
    science.Grid,
    platform.Performance,
    shared.DatetimeSet,
    designing.TemporalConstraint,
    science.Tuning,
    activity.Activity,
    drs.DrsEnsembleIdentifier,
    designing.SimulationPlan,
    activity.Conformance,
    designing.Project,
    drs.DrsPublicationDataset,
    activity.AxisMember,
    shared.Party,
    drs.DrsTemporalIdentifier,
    activity.Ensemble,
    platform.StorageVolume,
    platform.ComponentPerformance,
    shared.Pid,
    shared.Calendar,
    shared.NumberArray,
    software.Composition,
    data.Downscaling,
    software.Variable,
	)

# Supported enums.
ENUMS = (
    drs.DrsTimeSuffixes,
    platform.StorageSystems,
    shared.PeriodDateTypes,
    shared.DocumentTypes,
    drs.DrsGeographicalOperators,
    shared.TimeUnits,
    designing.EnsembleTypes,
    shared.SlicetimeUnits,
    science.SelectionCardinality,
    shared.TextCode,
    platform.VolumeUnits,
    software.ProgrammingLanguage,
    designing.ForcingTypes,
    science.ModelTypes,
    shared.NilReason,
    drs.DrsRealms,
    activity.ForcingTypes,
    designing.ExperimentalRelationships,
    drs.DrsFrequencyTypes,
    software.CouplingFramework,
    shared.CalendarTypes,
    data.DataAssociationTypes,
    shared.RoleCode,
    shared.QualityStatus,
    activity.EnsembleTypes,
	)

# Supported document types.
DOCUMENT_TYPES = (
    shared.ExternalDocument,
    shared.Party,
    platform.Performance,
    platform.Machine,
    data.Dataset,
    data.Simulation,
    data.Downscaling,
    activity.UberEnsemble,
    activity.Conformance,
    activity.Ensemble,
    activity.Activity,
    science.Grid,
    science.ScientificDomain,
    science.Model,
    designing.OutputTemporalRequirement,
    designing.MultiEnsemble,
    designing.Project,
    designing.MultiTimeEnsemble,
    designing.SimulationPlan,
    designing.NumericalExperiment,
    designing.ForcingConstraint,
    designing.DomainProperties,
    designing.TemporalConstraint,
    designing.NumericalRequirement,
    designing.EnsembleRequirement,
	)

# Set type keys.
# TODO deprecate
shared.Reference.type_key = u"cim.2.shared.Reference"
shared.ExternalDocument.type_key = u"cim.2.shared.ExternalDocument"
shared.Calendar.type_key = u"cim.2.shared.Calendar"
shared.NumberArray.type_key = u"cim.2.shared.NumberArray"
shared.TimesliceList.type_key = u"cim.2.shared.TimesliceList"
shared.DateTime.type_key = u"cim.2.shared.DateTime"
shared.Responsibility.type_key = u"cim.2.shared.Responsibility"
shared.DatetimeSet.type_key = u"cim.2.shared.DatetimeSet"
shared.OnlineResource.type_key = u"cim.2.shared.OnlineResource"
shared.IrregularDateset.type_key = u"cim.2.shared.IrregularDateset"
shared.Cimtext.type_key = u"cim.2.shared.Cimtext"
shared.Party.type_key = u"cim.2.shared.Party"
shared.DocReference.type_key = u"cim.2.shared.DocReference"
shared.DocMetaInfo.type_key = u"cim.2.shared.DocMetaInfo"
shared.Pid.type_key = u"cim.2.shared.Pid"
shared.RegularTimeset.type_key = u"cim.2.shared.RegularTimeset"
shared.KeyFloat.type_key = u"cim.2.shared.KeyFloat"
shared.TimePeriod.type_key = u"cim.2.shared.TimePeriod"
shared.QualityReview.type_key = u"cim.2.shared.QualityReview"
designing.OutputTemporalRequirement.type_key = u"cim.2.designing.OutputTemporalRequirement"
designing.MultiEnsemble.type_key = u"cim.2.designing.MultiEnsemble"
designing.Project.type_key = u"cim.2.designing.Project"
designing.MultiTimeEnsemble.type_key = u"cim.2.designing.MultiTimeEnsemble"
designing.SimulationPlan.type_key = u"cim.2.designing.SimulationPlan"
designing.NumericalExperiment.type_key = u"cim.2.designing.NumericalExperiment"
designing.ForcingConstraint.type_key = u"cim.2.designing.ForcingConstraint"
designing.DomainProperties.type_key = u"cim.2.designing.DomainProperties"
designing.TemporalConstraint.type_key = u"cim.2.designing.TemporalConstraint"
designing.NumericalRequirement.type_key = u"cim.2.designing.NumericalRequirement"
designing.EnsembleRequirement.type_key = u"cim.2.designing.EnsembleRequirement"
software.EntryPoint.type_key = u"cim.2.software.EntryPoint"
software.Gridspec.type_key = u"cim.2.software.Gridspec"
software.ComponentBase.type_key = u"cim.2.software.ComponentBase"
software.SoftwareComponent.type_key = u"cim.2.software.SoftwareComponent"
software.Composition.type_key = u"cim.2.software.Composition"
software.Variable.type_key = u"cim.2.software.Variable"
software.DevelopmentPath.type_key = u"cim.2.software.DevelopmentPath"
drs.DrsPublicationDataset.type_key = u"cim.2.drs.DrsPublicationDataset"
drs.DrsEnsembleIdentifier.type_key = u"cim.2.drs.DrsEnsembleIdentifier"
drs.DrsTemporalIdentifier.type_key = u"cim.2.drs.DrsTemporalIdentifier"
drs.DrsGeographicalIndicator.type_key = u"cim.2.drs.DrsGeographicalIndicator"
drs.DrsAtomicDataset.type_key = u"cim.2.drs.DrsAtomicDataset"
activity.AxisMember.type_key = u"cim.2.activity.AxisMember"
activity.UberEnsemble.type_key = u"cim.2.activity.UberEnsemble"
activity.Conformance.type_key = u"cim.2.activity.Conformance"
activity.Ensemble.type_key = u"cim.2.activity.Ensemble"
activity.ParentSimulation.type_key = u"cim.2.activity.ParentSimulation"
activity.EnsembleAxis.type_key = u"cim.2.activity.EnsembleAxis"
activity.Activity.type_key = u"cim.2.activity.Activity"
activity.EnsembleMember.type_key = u"cim.2.activity.EnsembleMember"
platform.StorageVolume.type_key = u"cim.2.platform.StorageVolume"
platform.Partition.type_key = u"cim.2.platform.Partition"
platform.Performance.type_key = u"cim.2.platform.Performance"
platform.ComponentPerformance.type_key = u"cim.2.platform.ComponentPerformance"
platform.StoragePool.type_key = u"cim.2.platform.StoragePool"
platform.ComputePool.type_key = u"cim.2.platform.ComputePool"
platform.Machine.type_key = u"cim.2.platform.Machine"
data.Dataset.type_key = u"cim.2.data.Dataset"
data.Simulation.type_key = u"cim.2.data.Simulation"
data.Downscaling.type_key = u"cim.2.data.Downscaling"
data.VariableCollection.type_key = u"cim.2.data.VariableCollection"
science.SubProcess.type_key = u"cim.2.science.SubProcess"
science.Resolution.type_key = u"cim.2.science.Resolution"
science.Grid.type_key = u"cim.2.science.Grid"
science.ConservationProperties.type_key = u"cim.2.science.ConservationProperties"
science.Tuning.type_key = u"cim.2.science.Tuning"
science.ScienceContext.type_key = u"cim.2.science.ScienceContext"
science.KeyProperties.type_key = u"cim.2.science.KeyProperties"
science.Detail.type_key = u"cim.2.science.Detail"
science.ScientificDomain.type_key = u"cim.2.science.ScientificDomain"
science.Model.type_key = u"cim.2.science.Model"
science.Extent.type_key = u"cim.2.science.Extent"
science.Process.type_key = u"cim.2.science.Process"
science.Algorithm.type_key = u"cim.2.science.Algorithm"
shared.TimeUnits.type_key = u"cim.2.shared.TimeUnits"
shared.QualityStatus.type_key = u"cim.2.shared.QualityStatus"
shared.CalendarTypes.type_key = u"cim.2.shared.CalendarTypes"
shared.NilReason.type_key = u"cim.2.shared.NilReason"
shared.RoleCode.type_key = u"cim.2.shared.RoleCode"
shared.TextCode.type_key = u"cim.2.shared.TextCode"
shared.PeriodDateTypes.type_key = u"cim.2.shared.PeriodDateTypes"
shared.SlicetimeUnits.type_key = u"cim.2.shared.SlicetimeUnits"
shared.DocumentTypes.type_key = u"cim.2.shared.DocumentTypes"
designing.EnsembleTypes.type_key = u"cim.2.designing.EnsembleTypes"
designing.ExperimentalRelationships.type_key = u"cim.2.designing.ExperimentalRelationships"
designing.ForcingTypes.type_key = u"cim.2.designing.ForcingTypes"
software.ProgrammingLanguage.type_key = u"cim.2.software.ProgrammingLanguage"
software.CouplingFramework.type_key = u"cim.2.software.CouplingFramework"
drs.DrsRealms.type_key = u"cim.2.drs.DrsRealms"
drs.DrsFrequencyTypes.type_key = u"cim.2.drs.DrsFrequencyTypes"
drs.DrsTimeSuffixes.type_key = u"cim.2.drs.DrsTimeSuffixes"
drs.DrsGeographicalOperators.type_key = u"cim.2.drs.DrsGeographicalOperators"
activity.EnsembleTypes.type_key = u"cim.2.activity.EnsembleTypes"
activity.ForcingTypes.type_key = u"cim.2.activity.ForcingTypes"
platform.VolumeUnits.type_key = u"cim.2.platform.VolumeUnits"
platform.StorageSystems.type_key = u"cim.2.platform.StorageSystems"
data.DataAssociationTypes.type_key = u"cim.2.data.DataAssociationTypes"
science.ModelTypes.type_key = u"cim.2.science.ModelTypes"
science.SelectionCardinality.type_key = u"cim.2.science.SelectionCardinality"

