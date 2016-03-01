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
from typeset_for_grids_package import *
from typeset_for_misc_package import *
from typeset_for_quality_package import *
from typeset_for_shared_package import *
from typeset_for_software_package import *

import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_grids_package as grids
import typeset_for_misc_package as misc
import typeset_for_quality_package as quality
import typeset_for_shared_package as shared
import typeset_for_software_package as software




# Module exports.
__all__ = [
    'TYPES',
    # Packages
    'activity',
    'data',
    'grids',
    'misc',
    'quality',
    'shared',
    'software',
	# Types
    'Activity',
    'BoundaryCondition',
    'Calendar',
    'Change',
    'ChangeProperty',
    'CimQuality',
    'Citation',
    'ClosedDateRange',
    'Compiler',
    'Component',
    'ComponentLanguage',
    'ComponentLanguageProperty',
    'ComponentProperty',
    'Composition',
    'Conformance',
    'Connection',
    'ConnectionEndpoint',
    'ConnectionProperty',
    'CoordinateList',
    'Coupling',
    'CouplingEndpoint',
    'CouplingProperty',
    'Daily360',
    'DataContent',
    'DataDistribution',
    'DataExtent',
    'DataExtentGeographical',
    'DataExtentTemporal',
    'DataExtentTimeInterval',
    'DataHierarchyLevel',
    'DataObject',
    'DataProperty',
    'DataRestriction',
    'DataSource',
    'DataStorage',
    'DataStorageDb',
    'DataStorageFile',
    'DataStorageIp',
    'DataTopic',
    'DateRange',
    'Deployment',
    'DocGenealogy',
    'DocMetaInfo',
    'DocReference',
    'DocRelationship',
    'DocRelationshipTarget',
    'DocumentSet',
    'DownscalingSimulation',
    'Ensemble',
    'EnsembleMember',
    'EntryPoint',
    'Evaluation',
    'Experiment',
    'ExperimentRelationship',
    'ExperimentRelationshipTarget',
    'GridExtent',
    'GridMosaic',
    'GridProperty',
    'GridSpec',
    'GridTile',
    'GridTileResolutionType',
    'InitialCondition',
    'LateralBoundaryCondition',
    'License',
    'Machine',
    'MachineCompilerUnit',
    'Measure',
    'MeasurementCampaign',
    'ModelComponent',
    'NumericalActivity',
    'NumericalExperiment',
    'NumericalRequirement',
    'NumericalRequirementOption',
    'OpenDateRange',
    'OutputRequirement',
    'Parallelisation',
    'PerpetualPeriod',
    'PhysicalModification',
    'Platform',
    'ProcessorComponent',
    'Property',
    'Rank',
    'RealCalendar',
    'Relationship',
    'Report',
    'ResponsibleParty',
    'SimpleGridGeometry',
    'Simulation',
    'SimulationComposite',
    'SimulationRelationship',
    'SimulationRelationshipTarget',
    'SimulationRun',
    'SpatialRegridding',
    'SpatialRegriddingProperty',
    'SpatialRegriddingUserMethod',
    'SpatioTemporalConstraint',
    'Standard',
    'StandardName',
    'StatisticalModelComponent',
    'TimeLag',
    'TimeTransformation',
    'Timing',
    'VerticalCoordinateList',
]


# Supported packages.
PACKAGES = (
    activity,
    data,
    grids,
    misc,
    quality,
    shared,
    software,
)


# Supported types.
TYPES = (
    activity.Activity,
    activity.BoundaryCondition,
    activity.Conformance,
    activity.DownscalingSimulation,
    activity.Ensemble,
    activity.EnsembleMember,
    activity.Experiment,
    activity.ExperimentRelationship,
    activity.ExperimentRelationshipTarget,
    activity.InitialCondition,
    activity.LateralBoundaryCondition,
    activity.MeasurementCampaign,
    activity.NumericalActivity,
    activity.NumericalExperiment,
    activity.NumericalRequirement,
    activity.NumericalRequirementOption,
    activity.OutputRequirement,
    activity.PhysicalModification,
    activity.Simulation,
    activity.SimulationComposite,
    activity.SimulationRelationship,
    activity.SimulationRelationshipTarget,
    activity.SimulationRun,
    activity.SpatioTemporalConstraint,
    data.DataContent,
    data.DataDistribution,
    data.DataExtent,
    data.DataExtentGeographical,
    data.DataExtentTemporal,
    data.DataExtentTimeInterval,
    data.DataHierarchyLevel,
    data.DataObject,
    data.DataProperty,
    data.DataRestriction,
    data.DataStorage,
    data.DataStorageDb,
    data.DataStorageFile,
    data.DataStorageIp,
    data.DataTopic,
    grids.CoordinateList,
    grids.GridExtent,
    grids.GridMosaic,
    grids.GridProperty,
    grids.GridSpec,
    grids.GridTile,
    grids.GridTileResolutionType,
    grids.SimpleGridGeometry,
    grids.VerticalCoordinateList,
    misc.DocumentSet,
    quality.CimQuality,
    quality.Evaluation,
    quality.Measure,
    quality.Report,
    shared.Calendar,
    shared.Change,
    shared.ChangeProperty,
    shared.Citation,
    shared.ClosedDateRange,
    shared.Compiler,
    shared.Daily360,
    shared.DataSource,
    shared.DateRange,
    shared.DocGenealogy,
    shared.DocMetaInfo,
    shared.DocReference,
    shared.DocRelationship,
    shared.DocRelationshipTarget,
    shared.License,
    shared.Machine,
    shared.MachineCompilerUnit,
    shared.OpenDateRange,
    shared.PerpetualPeriod,
    shared.Platform,
    shared.Property,
    shared.RealCalendar,
    shared.Relationship,
    shared.ResponsibleParty,
    shared.Standard,
    shared.StandardName,
    software.Component,
    software.ComponentLanguage,
    software.ComponentLanguageProperty,
    software.ComponentProperty,
    software.Composition,
    software.Connection,
    software.ConnectionEndpoint,
    software.ConnectionProperty,
    software.Coupling,
    software.CouplingEndpoint,
    software.CouplingProperty,
    software.Deployment,
    software.EntryPoint,
    software.ModelComponent,
    software.Parallelisation,
    software.ProcessorComponent,
    software.Rank,
    software.SpatialRegridding,
    software.SpatialRegriddingProperty,
    software.SpatialRegriddingUserMethod,
    software.StatisticalModelComponent,
    software.TimeLag,
    software.TimeTransformation,
    software.Timing,
)

# Set type keys.
activity.Activity.type_key = u'cim.1.activity.Activity'
activity.BoundaryCondition.type_key = u'cim.1.activity.BoundaryCondition'
activity.Conformance.type_key = u'cim.1.activity.Conformance'
activity.DownscalingSimulation.type_key = u'cim.1.activity.DownscalingSimulation'
activity.Ensemble.type_key = u'cim.1.activity.Ensemble'
activity.EnsembleMember.type_key = u'cim.1.activity.EnsembleMember'
activity.Experiment.type_key = u'cim.1.activity.Experiment'
activity.ExperimentRelationship.type_key = u'cim.1.activity.ExperimentRelationship'
activity.ExperimentRelationshipTarget.type_key = u'cim.1.activity.ExperimentRelationshipTarget'
activity.InitialCondition.type_key = u'cim.1.activity.InitialCondition'
activity.LateralBoundaryCondition.type_key = u'cim.1.activity.LateralBoundaryCondition'
activity.MeasurementCampaign.type_key = u'cim.1.activity.MeasurementCampaign'
activity.NumericalActivity.type_key = u'cim.1.activity.NumericalActivity'
activity.NumericalExperiment.type_key = u'cim.1.activity.NumericalExperiment'
activity.NumericalRequirement.type_key = u'cim.1.activity.NumericalRequirement'
activity.NumericalRequirementOption.type_key = u'cim.1.activity.NumericalRequirementOption'
activity.OutputRequirement.type_key = u'cim.1.activity.OutputRequirement'
activity.PhysicalModification.type_key = u'cim.1.activity.PhysicalModification'
activity.Simulation.type_key = u'cim.1.activity.Simulation'
activity.SimulationComposite.type_key = u'cim.1.activity.SimulationComposite'
activity.SimulationRelationship.type_key = u'cim.1.activity.SimulationRelationship'
activity.SimulationRelationshipTarget.type_key = u'cim.1.activity.SimulationRelationshipTarget'
activity.SimulationRun.type_key = u'cim.1.activity.SimulationRun'
activity.SpatioTemporalConstraint.type_key = u'cim.1.activity.SpatioTemporalConstraint'
data.DataContent.type_key = u'cim.1.data.DataContent'
data.DataDistribution.type_key = u'cim.1.data.DataDistribution'
data.DataExtent.type_key = u'cim.1.data.DataExtent'
data.DataExtentGeographical.type_key = u'cim.1.data.DataExtentGeographical'
data.DataExtentTemporal.type_key = u'cim.1.data.DataExtentTemporal'
data.DataExtentTimeInterval.type_key = u'cim.1.data.DataExtentTimeInterval'
data.DataHierarchyLevel.type_key = u'cim.1.data.DataHierarchyLevel'
data.DataObject.type_key = u'cim.1.data.DataObject'
data.DataProperty.type_key = u'cim.1.data.DataProperty'
data.DataRestriction.type_key = u'cim.1.data.DataRestriction'
data.DataStorage.type_key = u'cim.1.data.DataStorage'
data.DataStorageDb.type_key = u'cim.1.data.DataStorageDb'
data.DataStorageFile.type_key = u'cim.1.data.DataStorageFile'
data.DataStorageIp.type_key = u'cim.1.data.DataStorageIp'
data.DataTopic.type_key = u'cim.1.data.DataTopic'
grids.CoordinateList.type_key = u'cim.1.grids.CoordinateList'
grids.GridExtent.type_key = u'cim.1.grids.GridExtent'
grids.GridMosaic.type_key = u'cim.1.grids.GridMosaic'
grids.GridProperty.type_key = u'cim.1.grids.GridProperty'
grids.GridSpec.type_key = u'cim.1.grids.GridSpec'
grids.GridTile.type_key = u'cim.1.grids.GridTile'
grids.GridTileResolutionType.type_key = u'cim.1.grids.GridTileResolutionType'
grids.SimpleGridGeometry.type_key = u'cim.1.grids.SimpleGridGeometry'
grids.VerticalCoordinateList.type_key = u'cim.1.grids.VerticalCoordinateList'
misc.DocumentSet.type_key = u'cim.1.misc.DocumentSet'
quality.CimQuality.type_key = u'cim.1.quality.CimQuality'
quality.Evaluation.type_key = u'cim.1.quality.Evaluation'
quality.Measure.type_key = u'cim.1.quality.Measure'
quality.Report.type_key = u'cim.1.quality.Report'
shared.Calendar.type_key = u'cim.1.shared.Calendar'
shared.Change.type_key = u'cim.1.shared.Change'
shared.ChangeProperty.type_key = u'cim.1.shared.ChangeProperty'
shared.Citation.type_key = u'cim.1.shared.Citation'
shared.ClosedDateRange.type_key = u'cim.1.shared.ClosedDateRange'
shared.Compiler.type_key = u'cim.1.shared.Compiler'
shared.Daily360.type_key = u'cim.1.shared.Daily360'
shared.DataSource.type_key = u'cim.1.shared.DataSource'
shared.DateRange.type_key = u'cim.1.shared.DateRange'
shared.DocGenealogy.type_key = u'cim.1.shared.DocGenealogy'
shared.DocMetaInfo.type_key = u'cim.1.shared.DocMetaInfo'
shared.DocReference.type_key = u'cim.1.shared.DocReference'
shared.DocRelationship.type_key = u'cim.1.shared.DocRelationship'
shared.DocRelationshipTarget.type_key = u'cim.1.shared.DocRelationshipTarget'
shared.License.type_key = u'cim.1.shared.License'
shared.Machine.type_key = u'cim.1.shared.Machine'
shared.MachineCompilerUnit.type_key = u'cim.1.shared.MachineCompilerUnit'
shared.OpenDateRange.type_key = u'cim.1.shared.OpenDateRange'
shared.PerpetualPeriod.type_key = u'cim.1.shared.PerpetualPeriod'
shared.Platform.type_key = u'cim.1.shared.Platform'
shared.Property.type_key = u'cim.1.shared.Property'
shared.RealCalendar.type_key = u'cim.1.shared.RealCalendar'
shared.Relationship.type_key = u'cim.1.shared.Relationship'
shared.ResponsibleParty.type_key = u'cim.1.shared.ResponsibleParty'
shared.Standard.type_key = u'cim.1.shared.Standard'
shared.StandardName.type_key = u'cim.1.shared.StandardName'
software.Component.type_key = u'cim.1.software.Component'
software.ComponentLanguage.type_key = u'cim.1.software.ComponentLanguage'
software.ComponentLanguageProperty.type_key = u'cim.1.software.ComponentLanguageProperty'
software.ComponentProperty.type_key = u'cim.1.software.ComponentProperty'
software.Composition.type_key = u'cim.1.software.Composition'
software.Connection.type_key = u'cim.1.software.Connection'
software.ConnectionEndpoint.type_key = u'cim.1.software.ConnectionEndpoint'
software.ConnectionProperty.type_key = u'cim.1.software.ConnectionProperty'
software.Coupling.type_key = u'cim.1.software.Coupling'
software.CouplingEndpoint.type_key = u'cim.1.software.CouplingEndpoint'
software.CouplingProperty.type_key = u'cim.1.software.CouplingProperty'
software.Deployment.type_key = u'cim.1.software.Deployment'
software.EntryPoint.type_key = u'cim.1.software.EntryPoint'
software.ModelComponent.type_key = u'cim.1.software.ModelComponent'
software.Parallelisation.type_key = u'cim.1.software.Parallelisation'
software.ProcessorComponent.type_key = u'cim.1.software.ProcessorComponent'
software.Rank.type_key = u'cim.1.software.Rank'
software.SpatialRegridding.type_key = u'cim.1.software.SpatialRegridding'
software.SpatialRegriddingProperty.type_key = u'cim.1.software.SpatialRegriddingProperty'
software.SpatialRegriddingUserMethod.type_key = u'cim.1.software.SpatialRegriddingUserMethod'
software.StatisticalModelComponent.type_key = u'cim.1.software.StatisticalModelComponent'
software.TimeLag.type_key = u'cim.1.software.TimeLag'
software.TimeTransformation.type_key = u'cim.1.software.TimeTransformation'
software.Timing.type_key = u'cim.1.software.Timing'


# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.Activity.type_info = (
    ('funding_sources', unicode, False, True),
    ('projects', unicode, False, True),
    ('rationales', unicode, False, True),
    ('responsible_parties', shared.ResponsibleParty, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.BoundaryCondition.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.Conformance.type_info = (
    ('description', unicode, False, False),
    ('frequency', unicode, False, False),
    ('is_conformant', bool, True, False),
    ('requirements', activity.NumericalRequirement, False, True),
    ('sources', shared.DataSource, False, True),
    ('type', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.DownscalingSimulation.type_info = (
    ('calendar', shared.Calendar, True, False),
    ('downscaled_from', shared.DataSource, True, False),
    ('downscaling_id', unicode, False, False),
    ('downscaling_type', unicode, False, False),
    ('inputs', software.Coupling, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('outputs', data.DataObject, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.Ensemble.type_info = (
    ('members', activity.EnsembleMember, True, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('outputs', shared.DataSource, False, True),
    ('types', unicode, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.EnsembleMember.type_info = (
    ('ensemble', activity.Ensemble, False, False),
    ('ensemble_ids', shared.StandardName, False, True),
    ('simulation', activity.Simulation, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.Experiment.type_info = (
    ('generates', unicode, False, True),
    ('measurement_campaigns', activity.MeasurementCampaign, False, True),
    ('requires', activity.NumericalActivity, False, True),
    ('supports', unicode, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.ExperimentRelationship.type_info = (
    ('target', activity.ExperimentRelationshipTarget, True, False),
    ('type', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.ExperimentRelationshipTarget.type_info = (
    ('numerical_experiment', activity.NumericalExperiment, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.InitialCondition.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.LateralBoundaryCondition.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.MeasurementCampaign.type_info = (
    ('duration', int, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.NumericalActivity.type_info = (
    ('description', unicode, False, False),
    ('long_name', unicode, False, False),
    ('short_name', unicode, True, False),
    ('supports', activity.Experiment, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.NumericalExperiment.type_info = (
    ('description', unicode, False, False),
    ('experiment_id', unicode, False, False),
    ('long_name', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('requirements', activity.NumericalRequirement, False, True),
    ('short_name', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.NumericalRequirement.type_info = (
    ('description', unicode, False, False),
    ('id', unicode, False, False),
    ('name', unicode, True, False),
    ('options', activity.NumericalRequirementOption, False, True),
    ('requirement_type', unicode, True, False),
    ('source', shared.DataSource, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.NumericalRequirementOption.type_info = (
    ('description', unicode, False, False),
    ('id', unicode, False, False),
    ('name', unicode, True, False),
    ('relationship', unicode, False, False),
    ('sub_options', activity.NumericalRequirementOption, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.OutputRequirement.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.PhysicalModification.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.Simulation.type_info = (
    ('authors', unicode, False, False),
    ('calendar', shared.Calendar, True, False),
    ('conformances', activity.Conformance, False, True),
    ('control_simulation', activity.Simulation, False, False),
    ('deployments', software.Deployment, False, True),
    ('inputs', software.Coupling, False, True),
    ('outputs', data.DataObject, False, True),
    ('restarts', data.DataObject, False, True),
    ('simulation_id', unicode, False, False),
    ('spinup_date_range', shared.ClosedDateRange, False, False),
    ('spinup_simulation', activity.Simulation, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.SimulationComposite.type_info = (
    ('child', activity.Simulation, False, True),
    ('date_range', shared.DateRange, True, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('rank', int, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.SimulationRelationship.type_info = (
    ('target', activity.SimulationRelationshipTarget, True, False),
    ('type', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.SimulationRelationshipTarget.type_info = (
    ('simulation', shared.DocReference, False, False),
    ('target', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.SimulationRun.type_info = (
    ('date_range', shared.DateRange, True, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('model', software.ModelComponent, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
activity.SpatioTemporalConstraint.type_info = (
    ('date_range', shared.DateRange, False, False),
    ('spatial_resolution', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataContent.type_info = (
    ('aggregation', unicode, False, False),
    ('frequency', unicode, False, False),
    ('topic', data.DataTopic, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataDistribution.type_info = (
    ('access', unicode, False, False),
    ('fee', unicode, False, False),
    ('format', unicode, False, False),
    ('responsible_party', shared.ResponsibleParty, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataExtent.type_info = (
    ('geographical', data.DataExtentGeographical, True, False),
    ('temporal', data.DataExtentTemporal, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataExtentGeographical.type_info = (
    ('east', float, False, False),
    ('north', float, False, False),
    ('south', float, False, False),
    ('west', float, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataExtentTemporal.type_info = (
    ('begin', datetime.date, False, False),
    ('end', datetime.date, False, False),
    ('time_interval', data.DataExtentTimeInterval, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataExtentTimeInterval.type_info = (
    ('factor', int, False, False),
    ('radix', int, False, False),
    ('unit', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataHierarchyLevel.type_info = (
    ('is_open', bool, False, False),
    ('name', unicode, False, False),
    ('value', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataObject.type_info = (
    ('acronym', unicode, False, False),
    ('child_object', data.DataObject, False, True),
    ('citations', shared.Citation, False, True),
    ('content', data.DataContent, False, True),
    ('data_status', unicode, False, False),
    ('description', unicode, False, False),
    ('distribution', data.DataDistribution, False, False),
    ('extent', data.DataExtent, False, False),
    ('geometry_model', unicode, False, False),
    ('hierarchy_level', data.DataHierarchyLevel, False, False),
    ('keyword', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('parent_object', data.DataObject, False, False),
    ('properties', data.DataProperty, False, True),
    ('purpose', unicode, False, False),
    ('restriction', data.DataRestriction, False, True),
    ('source_simulation', unicode, False, False),
    ('storage', data.DataStorage, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataProperty.type_info = (
    ('description', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataRestriction.type_info = (
    ('license', shared.License, False, False),
    ('restriction', unicode, False, False),
    ('scope', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataStorage.type_info = (
    ('format', unicode, False, False),
    ('location', unicode, False, False),
    ('modification_date', datetime.datetime, False, False),
    ('size', int, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataStorageDb.type_info = (
    ('access_string', unicode, False, False),
    ('name', unicode, False, False),
    ('owner', unicode, False, False),
    ('table', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataStorageFile.type_info = (
    ('file_name', unicode, False, False),
    ('file_system', unicode, False, False),
    ('path', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataStorageIp.type_info = (
    ('file_name', unicode, False, False),
    ('host', unicode, False, False),
    ('path', unicode, False, False),
    ('protocol', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
data.DataTopic.type_info = (
    ('description', unicode, False, False),
    ('name', unicode, False, False),
    ('unit', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
grids.CoordinateList.type_info = (
    ('has_constant_offset', bool, False, False),
    ('length', int, False, False),
    ('uom', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
grids.GridExtent.type_info = (
    ('maximum_latitude', unicode, True, False),
    ('maximum_longitude', unicode, True, False),
    ('minimum_latitude', unicode, True, False),
    ('minimum_longitude', unicode, True, False),
    ('units', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
grids.GridMosaic.type_info = (
    ('citations', shared.Citation, False, True),
    ('description', unicode, False, False),
    ('extent', grids.GridExtent, False, False),
    ('has_congruent_tiles', bool, False, False),
    ('id', unicode, True, False),
    ('is_leaf', bool, True, False),
    ('long_name', unicode, False, False),
    ('mnemonic', unicode, False, False),
    ('mosaic_count', int, False, False),
    ('mosaics', grids.GridMosaic, False, True),
    ('short_name', unicode, True, False),
    ('tile_count', int, False, False),
    ('tiles', grids.GridTile, False, True),
    ('type', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
grids.GridProperty.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
grids.GridSpec.type_info = (
    ('esm_exchange_grids', grids.GridMosaic, False, True),
    ('esm_model_grids', grids.GridMosaic, False, True),
    ('meta', shared.DocMetaInfo, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
grids.GridTile.type_info = (
    ('area', unicode, False, False),
    ('cell_array', unicode, False, False),
    ('cell_ref_array', unicode, False, False),
    ('coord_file', unicode, False, False),
    ('coordinate_pole', unicode, False, False),
    ('description', unicode, False, False),
    ('discretization_type', unicode, False, False),
    ('extent', grids.GridExtent, False, False),
    ('geometry_type', unicode, False, False),
    ('grid_north_pole', unicode, False, False),
    ('horizontal_crs', unicode, False, False),
    ('horizontal_resolution', grids.GridTileResolutionType, False, False),
    ('id', unicode, False, False),
    ('is_conformal', bool, False, False),
    ('is_regular', bool, False, False),
    ('is_terrain_following', bool, False, False),
    ('is_uniform', bool, False, False),
    ('long_name', unicode, False, False),
    ('mnemonic', unicode, False, False),
    ('nx', int, False, False),
    ('ny', int, False, False),
    ('nz', int, False, False),
    ('refinement_scheme', unicode, False, False),
    ('short_name', unicode, False, False),
    ('simple_grid_geom', grids.SimpleGridGeometry, False, False),
    ('vertical_crs', unicode, False, False),
    ('vertical_resolution', grids.GridTileResolutionType, False, False),
    ('zcoords', grids.VerticalCoordinateList, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
grids.GridTileResolutionType.type_info = (
    ('description', unicode, False, False),
    ('properties', grids.GridProperty, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
grids.SimpleGridGeometry.type_info = (
    ('dim_order', unicode, False, False),
    ('is_mesh', bool, False, False),
    ('num_dims', int, True, False),
    ('xcoords', grids.CoordinateList, True, False),
    ('ycoords', grids.CoordinateList, True, False),
    ('zcoords', grids.CoordinateList, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
grids.VerticalCoordinateList.type_info = (
    ('form', unicode, False, False),
    ('properties', grids.GridProperty, False, True),
    ('type', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
misc.DocumentSet.type_info = (
    ('data', data.DataObject, False, True),
    ('ensembles', activity.Ensemble, False, True),
    ('experiment', activity.NumericalExperiment, False, False),
    ('grids', grids.GridSpec, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('model', software.ModelComponent, False, False),
    ('platform', shared.Platform, False, False),
    ('simulation', activity.SimulationRun, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
quality.CimQuality.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('reports', quality.Report, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
quality.Evaluation.type_info = (
    ('date', datetime.datetime, False, False),
    ('description', unicode, False, False),
    ('did_pass', bool, False, False),
    ('explanation', unicode, False, False),
    ('specification', unicode, False, False),
    ('specification_hyperlink', unicode, False, False),
    ('title', unicode, False, False),
    ('type', unicode, False, False),
    ('type_hyperlink', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
quality.Measure.type_info = (
    ('description', unicode, False, False),
    ('identification', unicode, False, False),
    ('name', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
quality.Report.type_info = (
    ('date', datetime.datetime, False, False),
    ('evaluation', quality.Evaluation, True, False),
    ('evaluator', shared.ResponsibleParty, False, False),
    ('measure', quality.Measure, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Calendar.type_info = (
    ('description', unicode, False, False),
    ('length', int, False, False),
    ('range', shared.DateRange, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Change.type_info = (
    ('author', shared.ResponsibleParty, False, False),
    ('date', datetime.datetime, False, False),
    ('description', unicode, False, False),
    ('details', shared.ChangeProperty, True, True),
    ('name', unicode, False, False),
    ('type', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.ChangeProperty.type_info = (
    ('description', unicode, False, False),
    ('id', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Citation.type_info = (
    ('alternative_title', unicode, False, False),
    ('collective_title', unicode, False, False),
    ('date', datetime.datetime, False, False),
    ('date_type', unicode, False, False),
    ('location', unicode, False, False),
    ('organisation', unicode, False, False),
    ('role', unicode, False, False),
    ('title', unicode, False, False),
    ('type', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.ClosedDateRange.type_info = (
    ('end', datetime.datetime, False, False),
    ('start', datetime.datetime, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Compiler.type_info = (
    ('environment_variables', unicode, False, False),
    ('language', unicode, False, False),
    ('name', unicode, True, False),
    ('options', unicode, False, False),
    ('type', unicode, False, False),
    ('version', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Daily360.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DataSource.type_info = (
    ('purpose', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DateRange.type_info = (
    ('duration', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DocGenealogy.type_info = (
    ('relationships', shared.DocRelationship, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DocMetaInfo.type_info = (
    ('author', shared.ResponsibleParty, False, False),
    ('create_date', datetime.datetime, True, False),
    ('drs_keys', unicode, False, True),
    ('drs_path', unicode, False, False),
    ('external_ids', shared.StandardName, False, True),
    ('genealogy', shared.DocGenealogy, False, False),
    ('id', uuid.UUID, True, False),
    ('institute', unicode, False, False),
    ('language', unicode, True, False),
    ('project', unicode, True, False),
    ('sort_key', unicode, False, False),
    ('source', unicode, True, False),
    ('source_key', unicode, False, False),
    ('status', unicode, False, False),
    ('type', unicode, True, False),
    ('type_display_name', unicode, False, False),
    ('type_sort_key', unicode, False, False),
    ('update_date', datetime.datetime, True, False),
    ('version', int, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DocReference.type_info = (
    ('changes', shared.Change, False, True),
    ('description', unicode, False, False),
    ('external_id', unicode, False, False),
    ('id', uuid.UUID, False, False),
    ('name', unicode, False, False),
    ('type', unicode, False, False),
    ('url', unicode, False, False),
    ('version', int, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DocRelationship.type_info = (
    ('target', shared.DocRelationshipTarget, True, False),
    ('type', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.DocRelationshipTarget.type_info = (
    ('reference', shared.DocReference, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.License.type_info = (
    ('contact', unicode, False, False),
    ('description', unicode, False, False),
    ('is_unrestricted', bool, False, False),
    ('name', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Machine.type_info = (
    ('cores_per_processor', int, False, False),
    ('description', unicode, False, False),
    ('interconnect', unicode, False, False),
    ('libraries', unicode, False, True),
    ('location', unicode, False, False),
    ('maximum_processors', int, False, False),
    ('name', unicode, True, False),
    ('operating_system', unicode, False, False),
    ('processor_type', unicode, False, False),
    ('system', unicode, False, False),
    ('type', unicode, False, False),
    ('vendor', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.MachineCompilerUnit.type_info = (
    ('compilers', shared.Compiler, False, True),
    ('machine', shared.Machine, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.OpenDateRange.type_info = (
    ('end', datetime.datetime, False, False),
    ('start', datetime.datetime, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.PerpetualPeriod.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Platform.type_info = (
    ('contacts', shared.ResponsibleParty, False, True),
    ('description', unicode, False, False),
    ('long_name', unicode, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('short_name', unicode, True, False),
    ('units', shared.MachineCompilerUnit, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Property.type_info = (
    ('name', unicode, False, False),
    ('value', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.RealCalendar.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Relationship.type_info = (
    ('description', unicode, False, False),
    ('direction', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.ResponsibleParty.type_info = (
    ('abbreviation', unicode, False, False),
    ('address', unicode, False, False),
    ('email', unicode, False, False),
    ('individual_name', unicode, False, False),
    ('organisation_name', unicode, False, False),
    ('role', unicode, False, False),
    ('url', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.Standard.type_info = (
    ('description', unicode, False, False),
    ('name', unicode, True, False),
    ('version', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
shared.StandardName.type_info = (
    ('is_open', bool, True, False),
    ('standards', shared.Standard, False, True),
    ('value', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Component.type_info = (
    ('citations', shared.Citation, False, True),
    ('code_access', unicode, False, False),
    ('composition', software.Composition, False, False),
    ('coupling_framework', unicode, False, False),
    ('dependencies', software.EntryPoint, False, True),
    ('deployments', software.Deployment, False, True),
    ('description', unicode, False, False),
    ('funding_sources', unicode, False, True),
    ('grid', grids.GridSpec, False, False),
    ('is_embedded', bool, False, False),
    ('language', software.ComponentLanguage, False, False),
    ('license', shared.License, False, False),
    ('long_name', unicode, False, False),
    ('online_resource', unicode, False, False),
    ('parent', software.Component, False, False),
    ('previous_version', unicode, False, False),
    ('properties', software.ComponentProperty, False, True),
    ('release_date', datetime.datetime, False, False),
    ('responsible_parties', shared.ResponsibleParty, False, True),
    ('short_name', unicode, True, False),
    ('sub_components', software.Component, False, True),
    ('version', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.ComponentLanguage.type_info = (
    ('name', unicode, True, False),
    ('properties', software.ComponentLanguageProperty, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.ComponentLanguageProperty.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.ComponentProperty.type_info = (
    ('citations', shared.Citation, False, True),
    ('description', unicode, False, False),
    ('grid', unicode, False, False),
    ('intent', unicode, False, False),
    ('is_represented', bool, True, False),
    ('long_name', unicode, False, False),
    ('short_name', unicode, True, False),
    ('standard_names', unicode, False, True),
    ('sub_properties', software.ComponentProperty, False, True),
    ('units', unicode, False, False),
    ('values', unicode, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Composition.type_info = (
    ('couplings', unicode, False, True),
    ('description', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Connection.type_info = (
    ('description', unicode, False, False),
    ('priming', shared.DataSource, False, False),
    ('properties', software.ConnectionProperty, False, True),
    ('sources', software.ConnectionEndpoint, False, True),
    ('spatial_regridding', software.SpatialRegridding, False, True),
    ('target', software.ConnectionEndpoint, False, False),
    ('time_lag', unicode, False, False),
    ('time_profile', software.Timing, False, False),
    ('time_transformation', software.TimeTransformation, False, False),
    ('transformers', software.ProcessorComponent, False, True),
    ('type', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.ConnectionEndpoint.type_info = (
    ('data_source', shared.DataSource, False, False),
    ('instance_id', unicode, False, False),
    ('properties', software.ConnectionProperty, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.ConnectionProperty.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Coupling.type_info = (
    ('connections', software.Connection, False, True),
    ('description', unicode, False, False),
    ('is_fully_specified', bool, True, False),
    ('priming', shared.DataSource, False, False),
    ('properties', software.CouplingProperty, False, True),
    ('purpose', unicode, True, False),
    ('sources', software.CouplingEndpoint, True, True),
    ('spatial_regriddings', software.SpatialRegridding, False, True),
    ('target', software.CouplingEndpoint, True, False),
    ('time_lag', software.TimeLag, False, False),
    ('time_profile', software.Timing, False, False),
    ('time_transformation', software.TimeTransformation, False, False),
    ('transformers', software.ProcessorComponent, False, True),
    ('type', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.CouplingEndpoint.type_info = (
    ('data_source', shared.DataSource, False, False),
    ('instance_id', unicode, False, False),
    ('properties', software.CouplingProperty, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.CouplingProperty.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Deployment.type_info = (
    ('deployment_date', datetime.datetime, False, False),
    ('description', unicode, False, False),
    ('executable_arguments', unicode, False, True),
    ('executable_name', unicode, False, False),
    ('parallelisation', software.Parallelisation, False, False),
    ('platform', shared.Platform, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.EntryPoint.type_info = (
    ('name', unicode, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.ModelComponent.type_info = (
    ('activity', activity.Activity, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('timing', software.Timing, False, False),
    ('type', unicode, False, False),
    ('types', unicode, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Parallelisation.type_info = (
    ('processes', int, True, False),
    ('ranks', software.Rank, False, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.ProcessorComponent.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Rank.type_info = (
    ('increment', int, False, False),
    ('max', int, False, False),
    ('min', int, False, False),
    ('value', int, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.SpatialRegridding.type_info = (
    ('dimension', unicode, False, False),
    ('properties', software.SpatialRegriddingProperty, False, True),
    ('standard_method', unicode, False, False),
    ('user_method', software.SpatialRegriddingUserMethod, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.SpatialRegriddingProperty.type_info = (
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.SpatialRegriddingUserMethod.type_info = (
    ('file', data.DataObject, False, False),
    ('name', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.StatisticalModelComponent.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('timing', software.Timing, False, False),
    ('type', unicode, False, False),
    ('types', unicode, True, True),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.TimeLag.type_info = (
    ('units', unicode, False, False),
    ('value', int, False, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.TimeTransformation.type_info = (
    ('description', unicode, False, False),
    ('mapping_type', unicode, True, False),
)

# Set class type info (property-name, property-type, property-is-required, property-is-iterable).
software.Timing.type_info = (
    ('end', datetime.datetime, False, False),
    ('is_variable_rate', bool, False, False),
    ('rate', int, False, False),
    ('start', datetime.datetime, False, False),
    ('units', unicode, False, False),
)


