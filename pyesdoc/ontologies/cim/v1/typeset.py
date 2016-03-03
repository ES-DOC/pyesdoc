
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import datetime
import uuid

from typeset_for_activity_package import *
from typeset_for_data_package import *
from typeset_for_shared_package import *
from typeset_for_software_package import *
from typeset_for_grids_package import *
from typeset_for_misc_package import *
from typeset_for_quality_package import *


import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_grids_package as grids
import typeset_for_misc_package as misc
import typeset_for_quality_package as quality



# Module exports.
__all__ = [
    'PACKAGES',
    'DOCUMENT_TYPES',
    'CLASSES',
    'ENUMS',

    # Packages
    activity,
    data,
    shared,
    software,
    grids,
    misc,
    quality,

    # Classes
    DataHierarchyLevel,
    RealCalendar,
    Report,
    Activity,
    Machine,
    License,
    ExperimentRelationshipTarget,
    StatisticalModelComponent,
    DocReference,
    PerpetualPeriod,
    Evaluation,
    Calendar,
    NumericalRequirementOption,
    OutputRequirement,
    GridSpec,
    GridExtent,
    ComponentLanguageProperty,
    Daily360,
    SimpleGridGeometry,
    DataStorage,
    SpatialRegridding,
    SpatialRegriddingProperty,
    Experiment,
    DataDistribution,
    Citation,
    SpatioTemporalConstraint,
    ClosedDateRange,
    Composition,
    DataContent,
    Deployment,
    ProcessorComponent,
    DataExtentTimeInterval,
    DataSource,
    DataExtentGeographical,
    TimeLag,
    DataTopic,
    ChangeProperty,
    GridProperty,
    ConnectionProperty,
    MachineCompilerUnit,
    MeasurementCampaign,
    NumericalActivity,
    DataStorageDb,
    GridTileResolutionType,
    DataStorageFile,
    DataStorageIp,
    Connection,
    SpatialRegriddingUserMethod,
    Rank,
    Ensemble,
    ResponsibleParty,
    VerticalCoordinateList,
    DocRelationship,
    DataExtent,
    CouplingEndpoint,
    DataRestriction,
    Relationship,
    Change,
    GridMosaic,
    PhysicalModification,
    Parallelisation,
    Platform,
    ConnectionEndpoint,
    Component,
    Simulation,
    ExperimentRelationship,
    DownscalingSimulation,
    NumericalExperiment,
    CimQuality,
    TimeTransformation,
    DocRelationshipTarget,
    Standard,
    SimulationRelationshipTarget,
    Property,
    DataProperty,
    DataExtentTemporal,
    ComponentProperty,
    CoordinateList,
    DocGenealogy,
    NumericalRequirement,
    DataObject,
    Conformance,
    BoundaryCondition,
    Coupling,
    DateRange,
    SimulationRun,
    OpenDateRange,
    Compiler,
    EntryPoint,
    GridTile,
    CouplingProperty,
    ModelComponent,
    EnsembleMember,
    Timing,
    StandardName,
    DocMetaInfo,
    InitialCondition,
    SimulationRelationship,
    ComponentLanguage,
    Measure,
    LateralBoundaryCondition,
    DocumentSet,
    SimulationComposite,

    # Enums
    ArcTypeEnum,
    FeatureTypeEnum,
    MachineVendorType,
    QualityStatusType,
    FrequencyType,
    CimScopeCodeType,
    DocRelationshipDirectionType,
    VerticalCsEnum,
    ChangePropertyType,
    CimResultType,
    OperatingSystemType,
    ComponentPropertyIntentType,
    DataHierarchyType,
    ProjectType,
    MachineType,
    ResolutionType,
    GeometryTypeEnum,
    SimulationRelationshipType,
    DocRelationshipType,
    ConnectionType,
    CouplingFrameworkType,
    ProcessorType,
    DocStatusType,
    ModelComponentType,
    GridTypeEnum,
    SpatialRegriddingDimensionType,
    DiscretizationEnum,
    UnitType,
    ConformanceType,
    SpatialRegriddingStandardMethodType,
    TimeMappingType,
    DocType,
    DataStatusType,
    RefinementTypeEnum,
    CompilerType,
    DataPurpose,
    QualityIssueType,
    ExperimentRelationshipType,
    QualitySeverityType,
    HorizontalCsEnum,
    TimingUnits,
    GridNodePositionEnum,
    StatisticalModelComponentType,
    EnsembleType,
    CimFeatureType,
    SimulationType,
    DownscalingType,
    InterconnectType,
    ]



# Supported packages.
PACKAGES = (
    activity,
    data,
    shared,
    software,
    grids,
    misc,
    quality,
	)

# Supported classes.
CLASSES = (
    data.DataHierarchyLevel,
    shared.RealCalendar,
    quality.Report,
    activity.Activity,
    shared.Machine,
    shared.License,
    activity.ExperimentRelationshipTarget,
    software.StatisticalModelComponent,
    shared.DocReference,
    shared.PerpetualPeriod,
    quality.Evaluation,
    shared.Calendar,
    activity.NumericalRequirementOption,
    activity.OutputRequirement,
    grids.GridSpec,
    grids.GridExtent,
    software.ComponentLanguageProperty,
    shared.Daily360,
    grids.SimpleGridGeometry,
    data.DataStorage,
    software.SpatialRegridding,
    software.SpatialRegriddingProperty,
    activity.Experiment,
    data.DataDistribution,
    shared.Citation,
    activity.SpatioTemporalConstraint,
    shared.ClosedDateRange,
    software.Composition,
    data.DataContent,
    software.Deployment,
    software.ProcessorComponent,
    data.DataExtentTimeInterval,
    shared.DataSource,
    data.DataExtentGeographical,
    software.TimeLag,
    data.DataTopic,
    shared.ChangeProperty,
    grids.GridProperty,
    software.ConnectionProperty,
    shared.MachineCompilerUnit,
    activity.MeasurementCampaign,
    activity.NumericalActivity,
    data.DataStorageDb,
    grids.GridTileResolutionType,
    data.DataStorageFile,
    data.DataStorageIp,
    software.Connection,
    software.SpatialRegriddingUserMethod,
    software.Rank,
    activity.Ensemble,
    shared.ResponsibleParty,
    grids.VerticalCoordinateList,
    shared.DocRelationship,
    data.DataExtent,
    software.CouplingEndpoint,
    data.DataRestriction,
    shared.Relationship,
    shared.Change,
    grids.GridMosaic,
    activity.PhysicalModification,
    software.Parallelisation,
    shared.Platform,
    software.ConnectionEndpoint,
    software.Component,
    activity.Simulation,
    activity.ExperimentRelationship,
    activity.DownscalingSimulation,
    activity.NumericalExperiment,
    quality.CimQuality,
    software.TimeTransformation,
    shared.DocRelationshipTarget,
    shared.Standard,
    activity.SimulationRelationshipTarget,
    shared.Property,
    data.DataProperty,
    data.DataExtentTemporal,
    software.ComponentProperty,
    grids.CoordinateList,
    shared.DocGenealogy,
    activity.NumericalRequirement,
    data.DataObject,
    activity.Conformance,
    activity.BoundaryCondition,
    software.Coupling,
    shared.DateRange,
    activity.SimulationRun,
    shared.OpenDateRange,
    shared.Compiler,
    software.EntryPoint,
    grids.GridTile,
    software.CouplingProperty,
    software.ModelComponent,
    activity.EnsembleMember,
    software.Timing,
    shared.StandardName,
    shared.DocMetaInfo,
    activity.InitialCondition,
    activity.SimulationRelationship,
    software.ComponentLanguage,
    quality.Measure,
    activity.LateralBoundaryCondition,
    misc.DocumentSet,
    activity.SimulationComposite,
	)

# Supported enums.
ENUMS = (
    grids.ArcTypeEnum,
    grids.FeatureTypeEnum,
    shared.MachineVendorType,
    quality.QualityStatusType,
    activity.FrequencyType,
    quality.CimScopeCodeType,
    shared.DocRelationshipDirectionType,
    grids.VerticalCsEnum,
    shared.ChangePropertyType,
    quality.CimResultType,
    shared.OperatingSystemType,
    software.ComponentPropertyIntentType,
    data.DataHierarchyType,
    activity.ProjectType,
    shared.MachineType,
    activity.ResolutionType,
    grids.GeometryTypeEnum,
    activity.SimulationRelationshipType,
    shared.DocRelationshipType,
    software.ConnectionType,
    software.CouplingFrameworkType,
    shared.ProcessorType,
    shared.DocStatusType,
    software.ModelComponentType,
    grids.GridTypeEnum,
    software.SpatialRegriddingDimensionType,
    grids.DiscretizationEnum,
    shared.UnitType,
    activity.ConformanceType,
    software.SpatialRegriddingStandardMethodType,
    software.TimeMappingType,
    shared.DocType,
    data.DataStatusType,
    grids.RefinementTypeEnum,
    shared.CompilerType,
    shared.DataPurpose,
    quality.QualityIssueType,
    activity.ExperimentRelationshipType,
    quality.QualitySeverityType,
    grids.HorizontalCsEnum,
    software.TimingUnits,
    grids.GridNodePositionEnum,
    software.StatisticalModelComponentType,
    activity.EnsembleType,
    quality.CimFeatureType,
    activity.SimulationType,
    activity.DownscalingType,
    shared.InterconnectType,
	)

# Supported document types.
DOCUMENT_TYPES = (
    activity.SimulationComposite,
    activity.SimulationRun,
    activity.Ensemble,
    activity.DownscalingSimulation,
    activity.NumericalExperiment,
    data.DataObject,
    shared.Platform,
    software.StatisticalModelComponent,
    software.ModelComponent,
    software.ProcessorComponent,
    grids.GridSpec,
    misc.DocumentSet,
    quality.CimQuality,
	)

# Set type keys.
# TODO deprecate
software.Rank.type_key = u"cim.1.software.Rank"
software.CouplingProperty.type_key = u"cim.1.software.CouplingProperty"
software.SpatialRegridding.type_key = u"cim.1.software.SpatialRegridding"
software.SpatialRegriddingUserMethod.type_key = u"cim.1.software.SpatialRegriddingUserMethod"
software.SpatialRegriddingProperty.type_key = u"cim.1.software.SpatialRegriddingProperty"
software.Composition.type_key = u"cim.1.software.Composition"
software.TimeLag.type_key = u"cim.1.software.TimeLag"
software.Connection.type_key = u"cim.1.software.Connection"
software.StatisticalModelComponent.type_key = u"cim.1.software.StatisticalModelComponent"
software.ConnectionEndpoint.type_key = u"cim.1.software.ConnectionEndpoint"
software.Parallelisation.type_key = u"cim.1.software.Parallelisation"
software.TimeTransformation.type_key = u"cim.1.software.TimeTransformation"
software.ConnectionProperty.type_key = u"cim.1.software.ConnectionProperty"
software.Coupling.type_key = u"cim.1.software.Coupling"
software.Component.type_key = u"cim.1.software.Component"
software.CouplingEndpoint.type_key = u"cim.1.software.CouplingEndpoint"
software.ComponentProperty.type_key = u"cim.1.software.ComponentProperty"
software.Deployment.type_key = u"cim.1.software.Deployment"
software.Timing.type_key = u"cim.1.software.Timing"
software.EntryPoint.type_key = u"cim.1.software.EntryPoint"
software.ModelComponent.type_key = u"cim.1.software.ModelComponent"
software.ComponentLanguageProperty.type_key = u"cim.1.software.ComponentLanguageProperty"
software.ComponentLanguage.type_key = u"cim.1.software.ComponentLanguage"
software.ProcessorComponent.type_key = u"cim.1.software.ProcessorComponent"
quality.Report.type_key = u"cim.1.quality.Report"
quality.Evaluation.type_key = u"cim.1.quality.Evaluation"
quality.Measure.type_key = u"cim.1.quality.Measure"
quality.CimQuality.type_key = u"cim.1.quality.CimQuality"
grids.VerticalCoordinateList.type_key = u"cim.1.grids.VerticalCoordinateList"
grids.GridSpec.type_key = u"cim.1.grids.GridSpec"
grids.CoordinateList.type_key = u"cim.1.grids.CoordinateList"
grids.GridTile.type_key = u"cim.1.grids.GridTile"
grids.GridExtent.type_key = u"cim.1.grids.GridExtent"
grids.GridTileResolutionType.type_key = u"cim.1.grids.GridTileResolutionType"
grids.GridMosaic.type_key = u"cim.1.grids.GridMosaic"
grids.SimpleGridGeometry.type_key = u"cim.1.grids.SimpleGridGeometry"
grids.GridProperty.type_key = u"cim.1.grids.GridProperty"
activity.EnsembleMember.type_key = u"cim.1.activity.EnsembleMember"
activity.SimulationComposite.type_key = u"cim.1.activity.SimulationComposite"
activity.NumericalRequirement.type_key = u"cim.1.activity.NumericalRequirement"
activity.SimulationRelationship.type_key = u"cim.1.activity.SimulationRelationship"
activity.ExperimentRelationshipTarget.type_key = u"cim.1.activity.ExperimentRelationshipTarget"
activity.NumericalRequirementOption.type_key = u"cim.1.activity.NumericalRequirementOption"
activity.ExperimentRelationship.type_key = u"cim.1.activity.ExperimentRelationship"
activity.SimulationRelationshipTarget.type_key = u"cim.1.activity.SimulationRelationshipTarget"
activity.BoundaryCondition.type_key = u"cim.1.activity.BoundaryCondition"
activity.SimulationRun.type_key = u"cim.1.activity.SimulationRun"
activity.InitialCondition.type_key = u"cim.1.activity.InitialCondition"
activity.LateralBoundaryCondition.type_key = u"cim.1.activity.LateralBoundaryCondition"
activity.Activity.type_key = u"cim.1.activity.Activity"
activity.SpatioTemporalConstraint.type_key = u"cim.1.activity.SpatioTemporalConstraint"
activity.MeasurementCampaign.type_key = u"cim.1.activity.MeasurementCampaign"
activity.Ensemble.type_key = u"cim.1.activity.Ensemble"
activity.Conformance.type_key = u"cim.1.activity.Conformance"
activity.Experiment.type_key = u"cim.1.activity.Experiment"
activity.NumericalActivity.type_key = u"cim.1.activity.NumericalActivity"
activity.DownscalingSimulation.type_key = u"cim.1.activity.DownscalingSimulation"
activity.PhysicalModification.type_key = u"cim.1.activity.PhysicalModification"
activity.NumericalExperiment.type_key = u"cim.1.activity.NumericalExperiment"
activity.Simulation.type_key = u"cim.1.activity.Simulation"
activity.OutputRequirement.type_key = u"cim.1.activity.OutputRequirement"
shared.Compiler.type_key = u"cim.1.shared.Compiler"
shared.Standard.type_key = u"cim.1.shared.Standard"
shared.DocRelationshipTarget.type_key = u"cim.1.shared.DocRelationshipTarget"
shared.ChangeProperty.type_key = u"cim.1.shared.ChangeProperty"
shared.DocRelationship.type_key = u"cim.1.shared.DocRelationship"
shared.DocGenealogy.type_key = u"cim.1.shared.DocGenealogy"
shared.DocReference.type_key = u"cim.1.shared.DocReference"
shared.Change.type_key = u"cim.1.shared.Change"
shared.DataSource.type_key = u"cim.1.shared.DataSource"
shared.ResponsibleParty.type_key = u"cim.1.shared.ResponsibleParty"
shared.Relationship.type_key = u"cim.1.shared.Relationship"
shared.StandardName.type_key = u"cim.1.shared.StandardName"
shared.ClosedDateRange.type_key = u"cim.1.shared.ClosedDateRange"
shared.Daily360.type_key = u"cim.1.shared.Daily360"
shared.License.type_key = u"cim.1.shared.License"
shared.MachineCompilerUnit.type_key = u"cim.1.shared.MachineCompilerUnit"
shared.DateRange.type_key = u"cim.1.shared.DateRange"
shared.Platform.type_key = u"cim.1.shared.Platform"
shared.OpenDateRange.type_key = u"cim.1.shared.OpenDateRange"
shared.Property.type_key = u"cim.1.shared.Property"
shared.PerpetualPeriod.type_key = u"cim.1.shared.PerpetualPeriod"
shared.DocMetaInfo.type_key = u"cim.1.shared.DocMetaInfo"
shared.RealCalendar.type_key = u"cim.1.shared.RealCalendar"
shared.Calendar.type_key = u"cim.1.shared.Calendar"
shared.Citation.type_key = u"cim.1.shared.Citation"
shared.Machine.type_key = u"cim.1.shared.Machine"
misc.DocumentSet.type_key = u"cim.1.misc.DocumentSet"
data.DataStorageDb.type_key = u"cim.1.data.DataStorageDb"
data.DataExtentGeographical.type_key = u"cim.1.data.DataExtentGeographical"
data.DataStorageFile.type_key = u"cim.1.data.DataStorageFile"
data.DataExtentTemporal.type_key = u"cim.1.data.DataExtentTemporal"
data.DataStorageIp.type_key = u"cim.1.data.DataStorageIp"
data.DataExtentTimeInterval.type_key = u"cim.1.data.DataExtentTimeInterval"
data.DataTopic.type_key = u"cim.1.data.DataTopic"
data.DataHierarchyLevel.type_key = u"cim.1.data.DataHierarchyLevel"
data.DataObject.type_key = u"cim.1.data.DataObject"
data.DataContent.type_key = u"cim.1.data.DataContent"
data.DataProperty.type_key = u"cim.1.data.DataProperty"
data.DataDistribution.type_key = u"cim.1.data.DataDistribution"
data.DataRestriction.type_key = u"cim.1.data.DataRestriction"
data.DataExtent.type_key = u"cim.1.data.DataExtent"
data.DataStorage.type_key = u"cim.1.data.DataStorage"
software.SpatialRegriddingStandardMethodType.type_key = u"cim.1.software.SpatialRegriddingStandardMethodType"
software.StatisticalModelComponentType.type_key = u"cim.1.software.StatisticalModelComponentType"
software.TimeMappingType.type_key = u"cim.1.software.TimeMappingType"
software.TimingUnits.type_key = u"cim.1.software.TimingUnits"
software.ComponentPropertyIntentType.type_key = u"cim.1.software.ComponentPropertyIntentType"
software.ConnectionType.type_key = u"cim.1.software.ConnectionType"
software.CouplingFrameworkType.type_key = u"cim.1.software.CouplingFrameworkType"
software.ModelComponentType.type_key = u"cim.1.software.ModelComponentType"
software.SpatialRegriddingDimensionType.type_key = u"cim.1.software.SpatialRegriddingDimensionType"
quality.QualityIssueType.type_key = u"cim.1.quality.QualityIssueType"
quality.QualitySeverityType.type_key = u"cim.1.quality.QualitySeverityType"
quality.CimFeatureType.type_key = u"cim.1.quality.CimFeatureType"
quality.QualityStatusType.type_key = u"cim.1.quality.QualityStatusType"
quality.CimResultType.type_key = u"cim.1.quality.CimResultType"
quality.CimScopeCodeType.type_key = u"cim.1.quality.CimScopeCodeType"
grids.RefinementTypeEnum.type_key = u"cim.1.grids.RefinementTypeEnum"
grids.GridNodePositionEnum.type_key = u"cim.1.grids.GridNodePositionEnum"
grids.ArcTypeEnum.type_key = u"cim.1.grids.ArcTypeEnum"
grids.VerticalCsEnum.type_key = u"cim.1.grids.VerticalCsEnum"
grids.GridTypeEnum.type_key = u"cim.1.grids.GridTypeEnum"
grids.DiscretizationEnum.type_key = u"cim.1.grids.DiscretizationEnum"
grids.HorizontalCsEnum.type_key = u"cim.1.grids.HorizontalCsEnum"
grids.FeatureTypeEnum.type_key = u"cim.1.grids.FeatureTypeEnum"
grids.GeometryTypeEnum.type_key = u"cim.1.grids.GeometryTypeEnum"
activity.ProjectType.type_key = u"cim.1.activity.ProjectType"
activity.ResolutionType.type_key = u"cim.1.activity.ResolutionType"
activity.SimulationRelationshipType.type_key = u"cim.1.activity.SimulationRelationshipType"
activity.ConformanceType.type_key = u"cim.1.activity.ConformanceType"
activity.SimulationType.type_key = u"cim.1.activity.SimulationType"
activity.DownscalingType.type_key = u"cim.1.activity.DownscalingType"
activity.EnsembleType.type_key = u"cim.1.activity.EnsembleType"
activity.FrequencyType.type_key = u"cim.1.activity.FrequencyType"
activity.ExperimentRelationshipType.type_key = u"cim.1.activity.ExperimentRelationshipType"
shared.CompilerType.type_key = u"cim.1.shared.CompilerType"
shared.DocType.type_key = u"cim.1.shared.DocType"
shared.DataPurpose.type_key = u"cim.1.shared.DataPurpose"
shared.InterconnectType.type_key = u"cim.1.shared.InterconnectType"
shared.MachineType.type_key = u"cim.1.shared.MachineType"
shared.MachineVendorType.type_key = u"cim.1.shared.MachineVendorType"
shared.OperatingSystemType.type_key = u"cim.1.shared.OperatingSystemType"
shared.ProcessorType.type_key = u"cim.1.shared.ProcessorType"
shared.UnitType.type_key = u"cim.1.shared.UnitType"
shared.DocRelationshipDirectionType.type_key = u"cim.1.shared.DocRelationshipDirectionType"
shared.DocRelationshipType.type_key = u"cim.1.shared.DocRelationshipType"
shared.DocStatusType.type_key = u"cim.1.shared.DocStatusType"
shared.ChangePropertyType.type_key = u"cim.1.shared.ChangePropertyType"
data.DataHierarchyType.type_key = u"cim.1.data.DataHierarchyType"
data.DataStatusType.type_key = u"cim.1.data.DataStatusType"

