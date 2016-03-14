
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from typeset_for_designing_package import *
from typeset_for_shared_package import *
from typeset_for_activity_package import *
from typeset_for_software_package import *
from typeset_for_science_package import *
from typeset_for_data_package import *
from typeset_for_drs_package import *
from typeset_for_platform_package import *


import typeset_for_designing_package as designing
import typeset_for_shared_package as shared
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_data_package as data
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform



# Module exports.
__all__ = [
    # Packages
    designing,
    shared,
    activity,
    software,
    science,
    data,
    drs,
    platform,
    # Classes
    Performance,
    ParentSimulation,
    Ensemble,
    Dataset,
    Variable,
    ScientificDomain,
    ConservationProperties,
    MultiEnsemble,
    RegularTimeset,
    Simulation,
    EnsembleRequirement,
    SubProcess,
    ForcingConstraint,
    VariableCollection,
    TemporalConstraint,
    OnlineResource,
    Pid,
    DrsPublicationDataset,
    Downscaling,
    QualityReview,
    Machine,
    Partition,
    NumberArray,
    Party,
    Resolution,
    ComponentPerformance,
    ComponentBase,
    DrsGeographicalIndicator,
    Composition,
    StorageVolume,
    SimulationPlan,
    NumericalExperiment,
    Project,
    Extent,
    Reference,
    UberEnsemble,
    KeyFloat,
    EnsembleMember,
    Responsibility,
    ComputePool,
    Calendar,
    EntryPoint,
    Model,
    TimePeriod,
    OutputTemporalRequirement,
    KeyProperties,
    Tuning,
    ExternalDocument,
    Gridspec,
    DomainProperties,
    AxisMember,
    Conformance,
    StoragePool,
    ScienceContext,
    DevelopmentPath,
    DocReference,
    MultiTimeEnsemble,
    DatetimeSet,
    Process,
    Algorithm,
    Activity,
    TimesliceList,
    Grid,
    NumericalRequirement,
    DrsTemporalIdentifier,
    Detail,
    IrregularDateset,
    DocMetaInfo,
    DrsEnsembleIdentifier,
    SoftwareComponent,
    DrsAtomicDataset,
    DateTime,
    Cimtext,
    EnsembleAxis,
    # Enums
    ForcingTypes,
    SelectionCardinality,
    StorageSystems,
    DrsTimeSuffixes,
    PeriodDateTypes,
    EnsembleTypes,
    DrsGeographicalOperators,
    DrsRealms,
    TimeUnits,
    ModelTypes,
    EnsembleTypes,
    ForcingTypes,
    NilReason,
    RoleCode,
    TextCode,
    SlicetimeUnits,
    ExperimentalRelationships,
    DrsFrequencyTypes,
    CalendarTypes,
    DataAssociationTypes,
    QualityStatus,
    VolumeUnits,
    DocumentTypes,
    ProgrammingLanguage,
    CouplingFramework,
]

# Set type keys.
# TODO deprecate
software.ComponentBase.type_key = u"cim.2.software.ComponentBase"
software.SoftwareComponent.type_key = u"cim.2.software.SoftwareComponent"
software.Composition.type_key = u"cim.2.software.Composition"
software.Variable.type_key = u"cim.2.software.Variable"
software.DevelopmentPath.type_key = u"cim.2.software.DevelopmentPath"
software.EntryPoint.type_key = u"cim.2.software.EntryPoint"
software.Gridspec.type_key = u"cim.2.software.Gridspec"
drs.DrsTemporalIdentifier.type_key = u"cim.2.drs.DrsTemporalIdentifier"
drs.DrsGeographicalIndicator.type_key = u"cim.2.drs.DrsGeographicalIndicator"
drs.DrsAtomicDataset.type_key = u"cim.2.drs.DrsAtomicDataset"
drs.DrsPublicationDataset.type_key = u"cim.2.drs.DrsPublicationDataset"
drs.DrsEnsembleIdentifier.type_key = u"cim.2.drs.DrsEnsembleIdentifier"
platform.Performance.type_key = u"cim.2.platform.Performance"
platform.ComponentPerformance.type_key = u"cim.2.platform.ComponentPerformance"
platform.StoragePool.type_key = u"cim.2.platform.StoragePool"
platform.ComputePool.type_key = u"cim.2.platform.ComputePool"
platform.Machine.type_key = u"cim.2.platform.Machine"
platform.StorageVolume.type_key = u"cim.2.platform.StorageVolume"
platform.Partition.type_key = u"cim.2.platform.Partition"
activity.Ensemble.type_key = u"cim.2.activity.Ensemble"
activity.EnsembleAxis.type_key = u"cim.2.activity.EnsembleAxis"
activity.Activity.type_key = u"cim.2.activity.Activity"
activity.ParentSimulation.type_key = u"cim.2.activity.ParentSimulation"
activity.EnsembleMember.type_key = u"cim.2.activity.EnsembleMember"
activity.AxisMember.type_key = u"cim.2.activity.AxisMember"
activity.UberEnsemble.type_key = u"cim.2.activity.UberEnsemble"
activity.Conformance.type_key = u"cim.2.activity.Conformance"
science.ScienceContext.type_key = u"cim.2.science.ScienceContext"
science.KeyProperties.type_key = u"cim.2.science.KeyProperties"
science.ConservationProperties.type_key = u"cim.2.science.ConservationProperties"
science.ScientificDomain.type_key = u"cim.2.science.ScientificDomain"
science.Model.type_key = u"cim.2.science.Model"
science.Detail.type_key = u"cim.2.science.Detail"
science.Process.type_key = u"cim.2.science.Process"
science.Extent.type_key = u"cim.2.science.Extent"
science.Algorithm.type_key = u"cim.2.science.Algorithm"
science.SubProcess.type_key = u"cim.2.science.SubProcess"
science.Resolution.type_key = u"cim.2.science.Resolution"
science.Grid.type_key = u"cim.2.science.Grid"
science.Tuning.type_key = u"cim.2.science.Tuning"
data.VariableCollection.type_key = u"cim.2.data.VariableCollection"
data.Downscaling.type_key = u"cim.2.data.Downscaling"
data.Dataset.type_key = u"cim.2.data.Dataset"
data.Simulation.type_key = u"cim.2.data.Simulation"
shared.DocMetaInfo.type_key = u"cim.2.shared.DocMetaInfo"
shared.Cimtext.type_key = u"cim.2.shared.Cimtext"
shared.RegularTimeset.type_key = u"cim.2.shared.RegularTimeset"
shared.Party.type_key = u"cim.2.shared.Party"
shared.DocReference.type_key = u"cim.2.shared.DocReference"
shared.Pid.type_key = u"cim.2.shared.Pid"
shared.ExternalDocument.type_key = u"cim.2.shared.ExternalDocument"
shared.TimePeriod.type_key = u"cim.2.shared.TimePeriod"
shared.QualityReview.type_key = u"cim.2.shared.QualityReview"
shared.Calendar.type_key = u"cim.2.shared.Calendar"
shared.KeyFloat.type_key = u"cim.2.shared.KeyFloat"
shared.TimesliceList.type_key = u"cim.2.shared.TimesliceList"
shared.Reference.type_key = u"cim.2.shared.Reference"
shared.DateTime.type_key = u"cim.2.shared.DateTime"
shared.Responsibility.type_key = u"cim.2.shared.Responsibility"
shared.NumberArray.type_key = u"cim.2.shared.NumberArray"
shared.DatetimeSet.type_key = u"cim.2.shared.DatetimeSet"
shared.IrregularDateset.type_key = u"cim.2.shared.IrregularDateset"
shared.OnlineResource.type_key = u"cim.2.shared.OnlineResource"
designing.Project.type_key = u"cim.2.designing.Project"
designing.MultiTimeEnsemble.type_key = u"cim.2.designing.MultiTimeEnsemble"
designing.SimulationPlan.type_key = u"cim.2.designing.SimulationPlan"
designing.NumericalExperiment.type_key = u"cim.2.designing.NumericalExperiment"
designing.ForcingConstraint.type_key = u"cim.2.designing.ForcingConstraint"
designing.DomainProperties.type_key = u"cim.2.designing.DomainProperties"
designing.TemporalConstraint.type_key = u"cim.2.designing.TemporalConstraint"
designing.NumericalRequirement.type_key = u"cim.2.designing.NumericalRequirement"
designing.EnsembleRequirement.type_key = u"cim.2.designing.EnsembleRequirement"
designing.OutputTemporalRequirement.type_key = u"cim.2.designing.OutputTemporalRequirement"
designing.MultiEnsemble.type_key = u"cim.2.designing.MultiEnsemble"
software.ProgrammingLanguage.type_key = u"cim.2.software.ProgrammingLanguage"
software.CouplingFramework.type_key = u"cim.2.software.CouplingFramework"
drs.DrsRealms.type_key = u"cim.2.drs.DrsRealms"
drs.DrsFrequencyTypes.type_key = u"cim.2.drs.DrsFrequencyTypes"
drs.DrsTimeSuffixes.type_key = u"cim.2.drs.DrsTimeSuffixes"
drs.DrsGeographicalOperators.type_key = u"cim.2.drs.DrsGeographicalOperators"
platform.VolumeUnits.type_key = u"cim.2.platform.VolumeUnits"
platform.StorageSystems.type_key = u"cim.2.platform.StorageSystems"
activity.EnsembleTypes.type_key = u"cim.2.activity.EnsembleTypes"
activity.ForcingTypes.type_key = u"cim.2.activity.ForcingTypes"
science.ModelTypes.type_key = u"cim.2.science.ModelTypes"
science.SelectionCardinality.type_key = u"cim.2.science.SelectionCardinality"
data.DataAssociationTypes.type_key = u"cim.2.data.DataAssociationTypes"
shared.SlicetimeUnits.type_key = u"cim.2.shared.SlicetimeUnits"
shared.DocumentTypes.type_key = u"cim.2.shared.DocumentTypes"
shared.TimeUnits.type_key = u"cim.2.shared.TimeUnits"
shared.CalendarTypes.type_key = u"cim.2.shared.CalendarTypes"
shared.NilReason.type_key = u"cim.2.shared.NilReason"
shared.QualityStatus.type_key = u"cim.2.shared.QualityStatus"
shared.RoleCode.type_key = u"cim.2.shared.RoleCode"
shared.TextCode.type_key = u"cim.2.shared.TextCode"
shared.PeriodDateTypes.type_key = u"cim.2.shared.PeriodDateTypes"
designing.ExperimentalRelationships.type_key = u"cim.2.designing.ExperimentalRelationships"
designing.ForcingTypes.type_key = u"cim.2.designing.ForcingTypes"
designing.EnsembleTypes.type_key = u"cim.2.designing.EnsembleTypes"

