# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_meta.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v1 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:33:18.136604.

"""
import datetime
import uuid

import typeset_for_quality_package as quality
import typeset_for_grids_package as grids
import typeset_for_activity_package as activity
import typeset_for_shared_package as shared
import typeset_for_data_package as data
import typeset_for_software_package as software
import typeset_for_misc_package as misc




# Set type keys.
shared.Change.type_key = 'cim.1.shared.Change'
data.DataExtent.type_key = 'cim.1.data.DataExtent'
activity.NumericalExperiment.type_key = 'cim.1.activity.NumericalExperiment'
software.Component.type_key = 'cim.1.software.Component'
software.Parallelisation.type_key = 'cim.1.software.Parallelisation'
activity.NumericalRequirement.type_key = 'cim.1.activity.NumericalRequirement'
software.Composition.type_key = 'cim.1.software.Composition'
shared.Standard.type_key = 'cim.1.shared.Standard'
data.DataRestriction.type_key = 'cim.1.data.DataRestriction'
software.ComponentProperty.type_key = 'cim.1.software.ComponentProperty'
activity.SimulationRun.type_key = 'cim.1.activity.SimulationRun'
software.ComponentLanguageProperty.type_key = 'cim.1.software.ComponentLanguageProperty'
grids.CoordinateList.type_key = 'cim.1.grids.CoordinateList'
software.TimeLag.type_key = 'cim.1.software.TimeLag'
grids.GridTileResolutionType.type_key = 'cim.1.grids.GridTileResolutionType'
shared.Platform.type_key = 'cim.1.shared.Platform'
software.Connection.type_key = 'cim.1.software.Connection'
software.StatisticalModelComponent.type_key = 'cim.1.software.StatisticalModelComponent'
data.DataExtentTimeInterval.type_key = 'cim.1.data.DataExtentTimeInterval'
shared.ClosedDateRange.type_key = 'cim.1.shared.ClosedDateRange'
data.DataStorageDb.type_key = 'cim.1.data.DataStorageDb'
shared.DataSource.type_key = 'cim.1.shared.DataSource'
activity.ExperimentRelationshipTarget.type_key = 'cim.1.activity.ExperimentRelationshipTarget'
data.DataDistribution.type_key = 'cim.1.data.DataDistribution'
software.CouplingEndpoint.type_key = 'cim.1.software.CouplingEndpoint'
activity.SimulationRelationshipTarget.type_key = 'cim.1.activity.SimulationRelationshipTarget'
shared.OpenDateRange.type_key = 'cim.1.shared.OpenDateRange'
software.Deployment.type_key = 'cim.1.software.Deployment'
quality.Measure.type_key = 'cim.1.quality.Measure'
software.CouplingProperty.type_key = 'cim.1.software.CouplingProperty'
shared.ChangeProperty.type_key = 'cim.1.shared.ChangeProperty'
grids.VerticalCoordinateList.type_key = 'cim.1.grids.VerticalCoordinateList'
shared.DocGenealogy.type_key = 'cim.1.shared.DocGenealogy'
data.DataObject.type_key = 'cim.1.data.DataObject'
activity.ExperimentRelationship.type_key = 'cim.1.activity.ExperimentRelationship'
software.SpatialRegriddingUserMethod.type_key = 'cim.1.software.SpatialRegriddingUserMethod'
activity.EnsembleMember.type_key = 'cim.1.activity.EnsembleMember'
shared.Compiler.type_key = 'cim.1.shared.Compiler'
shared.StandardName.type_key = 'cim.1.shared.StandardName'
software.Rank.type_key = 'cim.1.software.Rank'
shared.MachineCompilerUnit.type_key = 'cim.1.shared.MachineCompilerUnit'
shared.Property.type_key = 'cim.1.shared.Property'
shared.DateRange.type_key = 'cim.1.shared.DateRange'
software.Coupling.type_key = 'cim.1.software.Coupling'
grids.GridSpec.type_key = 'cim.1.grids.GridSpec'
activity.Experiment.type_key = 'cim.1.activity.Experiment'
activity.SimulationRelationship.type_key = 'cim.1.activity.SimulationRelationship'
activity.SpatioTemporalConstraint.type_key = 'cim.1.activity.SpatioTemporalConstraint'
activity.SimulationComposite.type_key = 'cim.1.activity.SimulationComposite'
shared.License.type_key = 'cim.1.shared.License'
activity.InitialCondition.type_key = 'cim.1.activity.InitialCondition'
data.DataProperty.type_key = 'cim.1.data.DataProperty'
activity.NumericalActivity.type_key = 'cim.1.activity.NumericalActivity'
data.DataStorageFile.type_key = 'cim.1.data.DataStorageFile'
data.DataTopic.type_key = 'cim.1.data.DataTopic'
grids.GridTile.type_key = 'cim.1.grids.GridTile'
data.DataExtentTemporal.type_key = 'cim.1.data.DataExtentTemporal'
misc.DocumentSet.type_key = 'cim.1.misc.DocumentSet'
shared.Relationship.type_key = 'cim.1.shared.Relationship'
shared.DocRelationshipTarget.type_key = 'cim.1.shared.DocRelationshipTarget'
grids.SimpleGridGeometry.type_key = 'cim.1.grids.SimpleGridGeometry'
data.DataContent.type_key = 'cim.1.data.DataContent'
software.EntryPoint.type_key = 'cim.1.software.EntryPoint'
data.DataExtentGeographical.type_key = 'cim.1.data.DataExtentGeographical'
software.Timing.type_key = 'cim.1.software.Timing'
software.ProcessorComponent.type_key = 'cim.1.software.ProcessorComponent'
shared.Calendar.type_key = 'cim.1.shared.Calendar'
activity.Activity.type_key = 'cim.1.activity.Activity'
software.SpatialRegriddingProperty.type_key = 'cim.1.software.SpatialRegriddingProperty'
software.ConnectionProperty.type_key = 'cim.1.software.ConnectionProperty'
shared.Citation.type_key = 'cim.1.shared.Citation'
software.ConnectionEndpoint.type_key = 'cim.1.software.ConnectionEndpoint'
software.TimeTransformation.type_key = 'cim.1.software.TimeTransformation'
activity.PhysicalModification.type_key = 'cim.1.activity.PhysicalModification'
shared.PerpetualPeriod.type_key = 'cim.1.shared.PerpetualPeriod'
activity.LateralBoundaryCondition.type_key = 'cim.1.activity.LateralBoundaryCondition'
shared.DocReference.type_key = 'cim.1.shared.DocReference'
activity.OutputRequirement.type_key = 'cim.1.activity.OutputRequirement'
quality.CimQuality.type_key = 'cim.1.quality.CimQuality'
activity.Ensemble.type_key = 'cim.1.activity.Ensemble'
activity.Simulation.type_key = 'cim.1.activity.Simulation'
activity.Conformance.type_key = 'cim.1.activity.Conformance'
software.SpatialRegridding.type_key = 'cim.1.software.SpatialRegridding'
shared.DocMetaInfo.type_key = 'cim.1.shared.DocMetaInfo'
shared.Machine.type_key = 'cim.1.shared.Machine'
software.ModelComponent.type_key = 'cim.1.software.ModelComponent'
grids.GridProperty.type_key = 'cim.1.grids.GridProperty'
grids.GridMosaic.type_key = 'cim.1.grids.GridMosaic'
data.DataHierarchyLevel.type_key = 'cim.1.data.DataHierarchyLevel'
quality.Evaluation.type_key = 'cim.1.quality.Evaluation'
software.ComponentLanguage.type_key = 'cim.1.software.ComponentLanguage'
shared.DocRelationship.type_key = 'cim.1.shared.DocRelationship'
activity.NumericalRequirementOption.type_key = 'cim.1.activity.NumericalRequirementOption'
data.DataStorageIp.type_key = 'cim.1.data.DataStorageIp'
activity.DownscalingSimulation.type_key = 'cim.1.activity.DownscalingSimulation'
shared.ResponsibleParty.type_key = 'cim.1.shared.ResponsibleParty'
grids.GridExtent.type_key = 'cim.1.grids.GridExtent'
activity.MeasurementCampaign.type_key = 'cim.1.activity.MeasurementCampaign'
shared.RealCalendar.type_key = 'cim.1.shared.RealCalendar'
quality.Report.type_key = 'cim.1.quality.Report'
data.DataStorage.type_key = 'cim.1.data.DataStorage'
shared.Daily360.type_key = 'cim.1.shared.Daily360'
activity.BoundaryCondition.type_key = 'cim.1.activity.BoundaryCondition'


# Set type info (name, type, is_required, is_iterative).
shared.Change.type_info = (
    ('name', str, False, False),
    ('type', str, False, False),
    ('date', datetime.datetime, False, False),
    ('description', str, False, False),
    ('details', shared.ChangeProperty, True, True),
    ('author', shared.ResponsibleParty, False, False),
)

data.DataExtent.type_info = (
    ('geographical', data.DataExtentGeographical, True, False),
    ('temporal', data.DataExtentTemporal, True, False),
)

activity.NumericalExperiment.type_info = (
    ('experiment_id', str, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('long_name', str, False, False),
    ('requirements', activity.NumericalRequirement, False, True),
    ('description', str, False, False),
    ('short_name', str, True, False),
)

software.Component.type_info = (
    ('properties', software.ComponentProperty, False, True),
    ('is_embedded', bool, False, False),
    ('language', software.ComponentLanguage, False, False),
    ('license', shared.License, False, False),
    ('long_name', str, False, False),
    ('sub_components', software.Component, False, True),
    ('online_resource', str, False, False),
    ('parent', software.Component, False, False),
    ('release_date', datetime.datetime, False, False),
    ('citations', shared.Citation, False, True),
    ('code_access', str, False, False),
    ('composition', software.Composition, False, False),
    ('coupling_framework', str, False, False),
    ('previous_version', str, False, False),
    ('short_name', str, True, False),
    ('dependencies', software.EntryPoint, False, True),
    ('version', str, False, False),
    ('deployments', software.Deployment, False, True),
    ('responsible_parties', shared.ResponsibleParty, False, True),
    ('description', str, False, False),
    ('funding_sources', str, False, True),
    ('grid', grids.GridSpec, False, False),
)

software.Parallelisation.type_info = (
    ('processes', int, True, False),
    ('ranks', software.Rank, False, True),
)

activity.NumericalRequirement.type_info = (
    ('source', shared.DataSource, False, False),
    ('id', str, False, False),
    ('name', str, True, False),
    ('options', activity.NumericalRequirementOption, False, True),
    ('source_reference', shared.DocReference, False, False),
    ('requirement_type', str, True, False),
    ('description', str, False, False),
)

software.Composition.type_info = (
    ('couplings', str, False, True),
    ('description', str, False, False),
)

shared.Standard.type_info = (
    ('version', str, False, False),
    ('description', str, False, False),
    ('name', str, True, False),
)

data.DataRestriction.type_info = (
    ('license', shared.License, False, False),
    ('scope', str, False, False),
    ('restriction', str, False, False),
)

software.ComponentProperty.type_info = (
    ('grid', str, False, False),
    ('is_represented', bool, True, False),
    ('sub_properties', software.ComponentProperty, False, True),
    ('intent', str, False, False),
    ('standard_names', str, False, True),
    ('units', str, False, False),
    ('citations', shared.Citation, False, True),
    ('description', str, False, False),
    ('long_name', str, False, False),
    ('short_name', str, True, False),
    ('values', str, False, True),
)

activity.SimulationRun.type_info = (
    ('model', software.ModelComponent, False, False),
    ('model_reference', shared.DocReference, False, False),
    ('date_range', shared.DateRange, True, False),
    ('meta', shared.DocMetaInfo, True, False),
)

software.ComponentLanguageProperty.type_info = (
)

grids.CoordinateList.type_info = (
    ('uom', str, False, False),
    ('has_constant_offset', bool, False, False),
    ('length', int, False, False),
)

software.TimeLag.type_info = (
    ('units', str, False, False),
    ('value', int, False, False),
)

grids.GridTileResolutionType.type_info = (
    ('description', str, False, False),
    ('properties', grids.GridProperty, False, True),
)

shared.Platform.type_info = (
    ('description', str, False, False),
    ('long_name', str, False, False),
    ('contacts', shared.ResponsibleParty, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('units', shared.MachineCompilerUnit, True, True),
    ('short_name', str, True, False),
)

software.Connection.type_info = (
    ('transformers', software.ProcessorComponent, False, True),
    ('priming_reference', shared.DocReference, False, False),
    ('sources', software.ConnectionEndpoint, False, True),
    ('spatial_regridding', software.SpatialRegridding, False, True),
    ('type', str, False, False),
    ('time_lag', str, False, False),
    ('time_transformation', software.TimeTransformation, False, False),
    ('description', str, False, False),
    ('priming', shared.DataSource, False, False),
    ('transformers_references', shared.DocReference, False, True),
    ('properties', software.ConnectionProperty, False, True),
    ('target', software.ConnectionEndpoint, False, False),
    ('time_profile', software.Timing, False, False),
)

software.StatisticalModelComponent.type_info = (
    ('type', str, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('types', str, True, True),
    ('timing', software.Timing, False, False),
)

data.DataExtentTimeInterval.type_info = (
    ('unit', str, False, False),
    ('factor', int, False, False),
    ('radix', int, False, False),
)

shared.ClosedDateRange.type_info = (
    ('end', datetime.datetime, False, False),
    ('start', datetime.datetime, True, False),
)

data.DataStorageDb.type_info = (
    ('access_string', str, False, False),
    ('table', str, False, False),
    ('owner', str, False, False),
    ('name', str, False, False),
)

shared.DataSource.type_info = (
    ('purpose', str, False, False),
)

activity.ExperimentRelationshipTarget.type_info = (
    ('numerical_experiment', activity.NumericalExperiment, False, False),
    ('reference', shared.DocReference, False, False),
)

data.DataDistribution.type_info = (
    ('format', str, False, False),
    ('access', str, False, False),
    ('responsible_party', shared.ResponsibleParty, False, False),
    ('fee', str, False, False),
)

software.CouplingEndpoint.type_info = (
    ('instance_id', str, False, False),
    ('data_source', shared.DataSource, False, False),
    ('properties', software.CouplingProperty, False, True),
    ('data_source_reference', shared.DocReference, False, False),
)

activity.SimulationRelationshipTarget.type_info = (
    ('reference', shared.DocReference, False, False),
    ('target', str, False, False),
)

shared.OpenDateRange.type_info = (
    ('end', datetime.datetime, False, False),
    ('start', datetime.datetime, False, False),
)

software.Deployment.type_info = (
    ('platform', shared.Platform, False, False),
    ('description', str, False, False),
    ('deployment_date', datetime.datetime, False, False),
    ('platform_reference', shared.DocReference, False, False),
    ('executable_name', str, False, False),
    ('executable_arguments', str, False, True),
    ('parallelisation', software.Parallelisation, False, False),
)

quality.Measure.type_info = (
    ('description', str, False, False),
    ('name', str, False, False),
    ('identification', str, False, False),
)

software.CouplingProperty.type_info = (
)

shared.ChangeProperty.type_info = (
    ('description', str, False, False),
    ('id', str, False, False),
)

grids.VerticalCoordinateList.type_info = (
    ('type', str, False, False),
    ('form', str, False, False),
    ('properties', grids.GridProperty, False, True),
)

shared.DocGenealogy.type_info = (
    ('relationships', shared.DocRelationship, False, True),
)

data.DataObject.type_info = (
    ('extent', data.DataExtent, False, False),
    ('content', data.DataContent, False, True),
    ('geometry_model', str, False, False),
    ('storage', data.DataStorage, False, True),
    ('parent_object', data.DataObject, False, False),
    ('parent_object_reference', shared.DocReference, False, False),
    ('purpose', str, False, False),
    ('data_status', str, False, False),
    ('acronym', str, False, False),
    ('distribution', data.DataDistribution, False, False),
    ('hierarchy_level', data.DataHierarchyLevel, False, False),
    ('description', str, False, False),
    ('properties', data.DataProperty, False, True),
    ('source_simulation', str, False, False),
    ('keyword', str, False, False),
    ('restriction', data.DataRestriction, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('citations', shared.Citation, False, True),
    ('child_object', data.DataObject, False, True),
)

activity.ExperimentRelationship.type_info = (
    ('target', activity.ExperimentRelationshipTarget, True, False),
    ('type', str, True, False),
)

software.SpatialRegriddingUserMethod.type_info = (
    ('name', str, True, False),
    ('file', data.DataObject, False, False),
    ('file_reference', shared.DocReference, False, False),
)

activity.EnsembleMember.type_info = (
    ('ensemble_reference', shared.DocReference, False, False),
    ('simulation', activity.Simulation, False, False),
    ('simulation_reference', shared.DocReference, False, False),
    ('ensemble', activity.Ensemble, False, False),
    ('ensemble_ids', shared.StandardName, False, True),
)

shared.Compiler.type_info = (
    ('name', str, True, False),
    ('type', str, False, False),
    ('options', str, False, False),
    ('environment_variables', str, False, False),
    ('language', str, False, False),
    ('version', str, True, False),
)

shared.StandardName.type_info = (
    ('is_open', bool, True, False),
    ('value', str, True, False),
    ('standards', shared.Standard, False, True),
)

software.Rank.type_info = (
    ('value', int, False, False),
    ('increment', int, False, False),
    ('min', int, False, False),
    ('max', int, False, False),
)

shared.MachineCompilerUnit.type_info = (
    ('compilers', shared.Compiler, False, True),
    ('machine', shared.Machine, True, False),
)

shared.Property.type_info = (
    ('name', str, False, False),
    ('value', str, False, False),
)

shared.DateRange.type_info = (
    ('duration', str, False, False),
)

software.Coupling.type_info = (
    ('purpose', str, True, False),
    ('type', str, False, False),
    ('target', software.CouplingEndpoint, True, False),
    ('time_lag', software.TimeLag, False, False),
    ('description', str, False, False),
    ('transformers', software.ProcessorComponent, False, True),
    ('priming', shared.DataSource, False, False),
    ('connections', software.Connection, False, True),
    ('priming_reference', shared.DocReference, False, False),
    ('transformers_references', shared.DocReference, False, True),
    ('properties', software.CouplingProperty, False, True),
    ('time_profile', software.Timing, False, False),
    ('spatial_regriddings', software.SpatialRegridding, False, True),
    ('time_transformation', software.TimeTransformation, False, False),
    ('is_fully_specified', bool, True, False),
    ('sources', software.CouplingEndpoint, True, True),
)

grids.GridSpec.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('esm_exchange_grids', grids.GridMosaic, False, True),
    ('esm_model_grids', grids.GridMosaic, False, True),
)

activity.Experiment.type_info = (
    ('supports', str, False, True),
    ('supports_references', shared.DocReference, False, True),
    ('requires_references', shared.DocReference, False, True),
    ('requires', activity.NumericalActivity, False, True),
    ('generates', str, False, True),
    ('measurement_campaigns', activity.MeasurementCampaign, False, True),
)

activity.SimulationRelationship.type_info = (
    ('target', activity.SimulationRelationshipTarget, True, False),
    ('type', str, True, False),
)

activity.SpatioTemporalConstraint.type_info = (
    ('date_range', shared.DateRange, False, False),
    ('spatial_resolution', str, False, False),
)

activity.SimulationComposite.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('rank', int, True, False),
    ('child', activity.Simulation, False, True),
    ('date_range', shared.DateRange, True, False),
)

shared.License.type_info = (
    ('name', str, False, False),
    ('contact', str, False, False),
    ('is_unrestricted', str, False, False),
    ('description', str, False, False),
)

activity.InitialCondition.type_info = (
)

data.DataProperty.type_info = (
    ('description', str, False, False),
)

activity.NumericalActivity.type_info = (
    ('supports', activity.Experiment, False, True),
    ('description', str, False, False),
    ('short_name', str, True, False),
    ('supports_references', shared.DocReference, False, True),
    ('long_name', str, False, False),
)

data.DataStorageFile.type_info = (
    ('file_name', str, False, False),
    ('path', str, False, False),
    ('file_system', str, False, False),
)

data.DataTopic.type_info = (
    ('unit', str, False, False),
    ('description', str, False, False),
    ('name', str, False, False),
)

grids.GridTile.type_info = (
    ('zcoords', grids.VerticalCoordinateList, False, False),
    ('horizontal_resolution', grids.GridTileResolutionType, False, False),
    ('id', str, False, False),
    ('area', str, False, False),
    ('is_conformal', bool, False, False),
    ('cell_array', str, False, False),
    ('is_regular', bool, False, False),
    ('cell_ref_array', str, False, False),
    ('is_terrain_following', bool, False, False),
    ('vertical_crs', str, False, False),
    ('coord_file', str, False, False),
    ('is_uniform', bool, False, False),
    ('coordinate_pole', str, False, False),
    ('long_name', str, False, False),
    ('horizontal_crs', str, False, False),
    ('mnemonic', str, False, False),
    ('grid_north_pole', str, False, False),
    ('nx', int, False, False),
    ('simple_grid_geom', grids.SimpleGridGeometry, False, False),
    ('ny', int, False, False),
    ('nz', int, False, False),
    ('refinement_scheme', str, False, False),
    ('description', str, False, False),
    ('discretization_type', str, False, False),
    ('short_name', str, False, False),
    ('extent', grids.GridExtent, False, False),
    ('vertical_resolution', grids.GridTileResolutionType, False, False),
    ('geometry_type', str, False, False),
)

data.DataExtentTemporal.type_info = (
    ('time_interval', data.DataExtentTimeInterval, False, False),
    ('begin', datetime.date, False, False),
    ('end', datetime.date, False, False),
)

misc.DocumentSet.type_info = (
    ('grids_references', shared.DocReference, False, True),
    ('simulation_reference', shared.DocReference, False, False),
    ('experiment', activity.NumericalExperiment, False, False),
    ('model_reference', shared.DocReference, False, False),
    ('model', software.ModelComponent, False, False),
    ('simulation', activity.SimulationRun, False, False),
    ('data_references', shared.DocReference, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('experiment_reference', shared.DocReference, False, False),
    ('ensembles', activity.Ensemble, False, True),
    ('platform', shared.Platform, False, False),
    ('grids', grids.GridSpec, False, True),
    ('platform_reference', shared.DocReference, False, False),
    ('ensembles_references', shared.DocReference, False, True),
    ('data', data.DataObject, False, True),
)

shared.Relationship.type_info = (
    ('description', str, False, False),
    ('direction', str, True, False),
)

shared.DocRelationshipTarget.type_info = (
    ('document', str, False, False),
    ('reference', shared.DocReference, False, False),
)

grids.SimpleGridGeometry.type_info = (
    ('xcoords', grids.CoordinateList, True, False),
    ('is_mesh', bool, False, False),
    ('dim_order', str, False, False),
    ('zcoords', grids.CoordinateList, False, False),
    ('ycoords', grids.CoordinateList, True, False),
    ('num_dims', int, True, False),
)

data.DataContent.type_info = (
    ('aggregation', str, False, False),
    ('topic', data.DataTopic, True, False),
    ('frequency', str, False, False),
)

software.EntryPoint.type_info = (
    ('name', str, False, False),
)

data.DataExtentGeographical.type_info = (
    ('west', float, False, False),
    ('east', float, False, False),
    ('south', float, False, False),
    ('north', float, False, False),
)

software.Timing.type_info = (
    ('rate', int, False, False),
    ('units', str, False, False),
    ('start', datetime.datetime, False, False),
    ('end', datetime.datetime, False, False),
    ('is_variable_rate', bool, False, False),
)

software.ProcessorComponent.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
)

shared.Calendar.type_info = (
    ('range', shared.DateRange, False, False),
    ('description', str, False, False),
    ('length', int, False, False),
)

activity.Activity.type_info = (
    ('funding_sources', str, False, True),
    ('responsible_parties', shared.ResponsibleParty, False, True),
    ('projects', str, False, True),
    ('rationales', str, False, True),
)

software.SpatialRegriddingProperty.type_info = (
)

software.ConnectionProperty.type_info = (
)

shared.Citation.type_info = (
    ('location', str, False, False),
    ('type', str, False, False),
    ('date_type', str, False, False),
    ('date', datetime.datetime, False, False),
    ('role', str, False, False),
    ('alternative_title', str, False, False),
    ('title', str, False, False),
    ('collective_title', str, False, False),
    ('organisation', str, False, False),
    ('reference', shared.DocReference, False, False),
)

software.ConnectionEndpoint.type_info = (
    ('data_source', shared.DataSource, False, False),
    ('properties', software.ConnectionProperty, False, True),
    ('instance_id', str, False, False),
    ('data_source_reference', shared.DocReference, False, False),
)

software.TimeTransformation.type_info = (
    ('description', str, False, False),
    ('mapping_type', str, True, False),
)

activity.PhysicalModification.type_info = (
)

shared.PerpetualPeriod.type_info = (
)

activity.LateralBoundaryCondition.type_info = (
)

shared.DocReference.type_info = (
    ('type', str, False, False),
    ('description', str, False, False),
    ('external_id', str, False, False),
    ('version', int, False, False),
    ('id', uuid.UUID, False, False),
    ('name', str, False, False),
    ('changes', shared.Change, False, True),
)

activity.OutputRequirement.type_info = (
)

quality.CimQuality.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('reports', quality.Report, False, True),
)

activity.Ensemble.type_info = (
    ('members', activity.EnsembleMember, True, True),
    ('outputs', shared.DataSource, False, True),
    ('outputs_references', shared.DocReference, False, True),
    ('types', str, True, True),
    ('meta', shared.DocMetaInfo, True, False),
)

activity.Simulation.type_info = (
    ('control_simulation', activity.Simulation, False, False),
    ('spinup_simulation', activity.Simulation, False, False),
    ('inputs', software.Coupling, False, True),
    ('conformances', activity.Conformance, False, True),
    ('control_simulation_reference', shared.DocReference, False, False),
    ('outputs', data.DataObject, False, True),
    ('simulation_id', str, False, False),
    ('authors', str, False, False),
    ('spinup_date_range', shared.ClosedDateRange, False, False),
    ('output_references', shared.DocReference, False, True),
    ('calendar', shared.Calendar, True, False),
    ('deployments', software.Deployment, False, True),
    ('restarts', data.DataObject, False, True),
    ('spinup_simulation_reference', shared.DocReference, False, False),
    ('restart_references', shared.DocReference, False, True),
)

activity.Conformance.type_info = (
    ('type', str, False, False),
    ('description', str, False, False),
    ('requirements_references', shared.DocReference, False, True),
    ('frequency', str, False, False),
    ('sources', shared.DataSource, False, True),
    ('is_conformant', bool, True, False),
    ('sources_references', shared.DocReference, False, True),
    ('requirements', activity.NumericalRequirement, False, True),
)

software.SpatialRegridding.type_info = (
    ('standard_method', str, False, False),
    ('user_method', software.SpatialRegriddingUserMethod, False, False),
    ('dimension', str, False, False),
    ('properties', software.SpatialRegriddingProperty, False, True),
)

shared.DocMetaInfo.type_info = (
    ('language', str, True, False),
    ('type_sort_key', str, False, False),
    ('type_display_name', str, False, False),
    ('drs_path', str, False, False),
    ('sort_key', str, False, False),
    ('metadata_version', str, False, False),
    ('genealogy', shared.DocGenealogy, False, False),
    ('status', str, False, False),
    ('drs_keys', str, False, True),
    ('create_date', datetime.datetime, True, False),
    ('id', uuid.UUID, True, False),
    ('version', int, True, False),
    ('type', str, True, False),
    ('encodings', str, False, True),
    ('source', str, True, False),
    ('metadata_id', str, False, False),
    ('institute', str, False, False),
    ('project', str, True, False),
    ('source_key', str, False, False),
    ('external_ids', shared.StandardName, False, True),
    ('author', shared.ResponsibleParty, False, False),
)

shared.Machine.type_info = (
    ('description', str, False, False),
    ('location', str, False, False),
    ('processor_type', str, False, False),
    ('system', str, False, False),
    ('interconnect', str, False, False),
    ('maximum_processors', int, False, False),
    ('type', str, False, False),
    ('name', str, True, False),
    ('operating_system', str, False, False),
    ('vendor', str, False, False),
    ('libraries', str, False, True),
    ('cores_per_processor', int, False, False),
)

software.ModelComponent.type_info = (
    ('activity', activity.Activity, False, False),
    ('type', str, False, False),
    ('types', str, True, True),
    ('timing', software.Timing, False, False),
    ('meta', shared.DocMetaInfo, True, False),
)

grids.GridProperty.type_info = (
)

grids.GridMosaic.type_info = (
    ('long_name', str, False, False),
    ('mosaics', grids.GridMosaic, False, True),
    ('tile_count', int, False, False),
    ('mosaic_count', int, False, False),
    ('has_congruent_tiles', bool, False, False),
    ('type', str, True, False),
    ('citations', shared.Citation, False, True),
    ('id', str, True, False),
    ('description', str, False, False),
    ('short_name', str, True, False),
    ('mnemonic', str, False, False),
    ('is_leaf', bool, True, False),
    ('tiles', grids.GridTile, False, True),
    ('extent', grids.GridExtent, False, False),
)

data.DataHierarchyLevel.type_info = (
    ('is_open', bool, False, False),
    ('value', str, False, False),
    ('name', str, False, False),
)

quality.Evaluation.type_info = (
    ('type_hyperlink', str, False, False),
    ('date', datetime.datetime, False, False),
    ('specification', str, False, False),
    ('description', str, False, False),
    ('specification_hyperlink', str, False, False),
    ('did_pass', bool, False, False),
    ('title', str, False, False),
    ('type', str, False, False),
    ('explanation', str, False, False),
)

software.ComponentLanguage.type_info = (
    ('name', str, True, False),
    ('properties', software.ComponentLanguageProperty, False, True),
)

shared.DocRelationship.type_info = (
    ('type', str, True, False),
    ('target', shared.DocRelationshipTarget, True, False),
)

activity.NumericalRequirementOption.type_info = (
    ('sub_options', activity.NumericalRequirementOption, False, True),
    ('name', str, True, False),
    ('relationship', str, False, False),
    ('description', str, False, False),
    ('id', str, False, False),
)

data.DataStorageIp.type_info = (
    ('host', str, False, False),
    ('protocol', str, False, False),
    ('file_name', str, False, False),
    ('path', str, False, False),
)

activity.DownscalingSimulation.type_info = (
    ('downscaling_type', str, False, False),
    ('downscaled_from', shared.DataSource, True, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('calendar', shared.Calendar, True, False),
    ('output_references', shared.DocReference, False, True),
    ('inputs', software.Coupling, False, True),
    ('downscaling_id', str, False, False),
    ('outputs', data.DataObject, False, True),
    ('downscaled_from_reference', shared.DocReference, True, False),
)

shared.ResponsibleParty.type_info = (
    ('role', str, False, False),
    ('email', str, False, False),
    ('individual_name', str, False, False),
    ('abbreviation', str, False, False),
    ('url', str, False, False),
    ('organisation_name', str, False, False),
    ('address', str, False, False),
)

grids.GridExtent.type_info = (
    ('minimum_longitude', str, True, False),
    ('maximum_latitude', str, True, False),
    ('minimum_latitude', str, True, False),
    ('units', str, False, False),
    ('maximum_longitude', str, True, False),
)

activity.MeasurementCampaign.type_info = (
    ('duration', int, True, False),
)

shared.RealCalendar.type_info = (
)

quality.Report.type_info = (
    ('evaluator', shared.ResponsibleParty, False, False),
    ('date', datetime.datetime, False, False),
    ('measure', quality.Measure, True, False),
    ('evaluation', quality.Evaluation, True, False),
)

data.DataStorage.type_info = (
    ('size', int, False, False),
    ('modification_date', datetime.datetime, False, False),
    ('format', str, False, False),
    ('location', str, False, False),
)

shared.Daily360.type_info = (
)

activity.BoundaryCondition.type_info = (
)

