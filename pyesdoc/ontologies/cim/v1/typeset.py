
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from typeset_for_shared_package import *
from typeset_for_software_package import *
from typeset_for_grids_package import *
from typeset_for_quality_package import *
from typeset_for_data_package import *
from typeset_for_activity_package import *
from typeset_for_misc_package import *


import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_grids_package as grids
import typeset_for_quality_package as quality
import typeset_for_data_package as data
import typeset_for_activity_package as activity
import typeset_for_misc_package as misc



# Module exports.
__all__ = [
    # Packages
    shared,
    software,
    grids,
    quality,
    data,
    activity,
    misc,
    # Classes
    Calendar,
    ExperimentRelationship,
    DataStorage,
    CouplingProperty,
    SimulationRun,
    BoundaryCondition,
    EntryPoint,
    SpatialRegriddingUserMethod,
    SimulationRelationshipTarget,
    ComponentLanguage,
    Deployment,
    GridTileResolutionType,
    Daily360,
    Component,
    DateRange,
    DataHierarchyLevel,
    DataTopic,
    NumericalActivity,
    EnsembleMember,
    Machine,
    ExperimentRelationshipTarget,
    NumericalRequirementOption,
    SpatioTemporalConstraint,
    DataStorageIp,
    SpatialRegriddingProperty,
    Platform,
    NumericalExperiment,
    Parallelisation,
    MeasurementCampaign,
    GridSpec,
    ResponsibleParty,
    Experiment,
    Citation,
    DataExtent,
    TimeLag,
    PerpetualPeriod,
    DocGenealogy,
    Conformance,
    Timing,
    DocumentSet,
    RealCalendar,
    Ensemble,
    DataProperty,
    ConnectionProperty,
    DataExtentGeographical,
    StatisticalModelComponent,
    GridMosaic,
    CoordinateList,
    ProcessorComponent,
    SimulationRelationship,
    DataRestriction,
    DataStorageDb,
    DataContent,
    ChangeProperty,
    DocRelationshipTarget,
    DataExtentTimeInterval,
    Standard,
    Composition,
    VerticalCoordinateList,
    DataExtentTemporal,
    Property,
    Change,
    GridTile,
    Evaluation,
    ComponentLanguageProperty,
    DataObject,
    Rank,
    ConnectionEndpoint,
    DataSource,
    SimulationComposite,
    DataDistribution,
    GridProperty,
    MachineCompilerUnit,
    Simulation,
    DocReference,
    CimQuality,
    DownscalingSimulation,
    Compiler,
    License,
    DataStorageFile,
    CouplingEndpoint,
    DocMetaInfo,
    Relationship,
    Activity,
    ModelComponent,
    ComponentProperty,
    OutputRequirement,
    GridExtent,
    Connection,
    TimeTransformation,
    Report,
    DocRelationship,
    StandardName,
    SimpleGridGeometry,
    NumericalRequirement,
    PhysicalModification,
    InitialCondition,
    ClosedDateRange,
    OpenDateRange,
    Measure,
    LateralBoundaryCondition,
    Coupling,
    SpatialRegridding,
    # Enums
    DocRelationshipDirectionType,
    CompilerType,
    DocStatusType,
    CouplingFrameworkType,
    ConnectionType,
    FeatureTypeEnum,
    CimScopeCodeType,
    InterconnectType,
    VerticalCsEnum,
    ModelComponentType,
    SpatialRegriddingDimensionType,
    FrequencyType,
    ChangePropertyType,
    MachineVendorType,
    ResolutionType,
    SimulationType,
    CimFeatureType,
    SpatialRegriddingStandardMethodType,
    DataHierarchyType,
    DiscretizationEnum,
    DataPurpose,
    ProcessorType,
    DocRelationshipType,
    CimResultType,
    GeometryTypeEnum,
    DataStatusType,
    ArcTypeEnum,
    HorizontalCsEnum,
    ProjectType,
    SimulationRelationshipType,
    QualitySeverityType,
    StatisticalModelComponentType,
    ComponentPropertyIntentType,
    TimeMappingType,
    TimingUnits,
    EnsembleType,
    GridNodePositionEnum,
    ConformanceType,
    UnitType,
    GridTypeEnum,
    OperatingSystemType,
    DownscalingType,
    DocType,
    QualityStatusType,
    QualityIssueType,
    MachineType,
    ExperimentRelationshipType,
    RefinementTypeEnum,
]

