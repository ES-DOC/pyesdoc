# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_meta.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v1 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-05-08 17:03:15.630507.

"""
# Module imports.
import datetime
import uuid

import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_grids_package as grids
import typeset_for_misc_package as misc
import typeset_for_quality_package as quality
import typeset_for_shared_package as shared
import typeset_for_software_package as software




# Set type keys.
activity.Activity.type_key = 'cim.1.activity.Activity'
activity.BoundaryCondition.type_key = 'cim.1.activity.BoundaryCondition'
activity.Conformance.type_key = 'cim.1.activity.Conformance'
activity.DownscalingSimulation.type_key = 'cim.1.activity.DownscalingSimulation'
activity.Ensemble.type_key = 'cim.1.activity.Ensemble'
activity.EnsembleMember.type_key = 'cim.1.activity.EnsembleMember'
activity.Experiment.type_key = 'cim.1.activity.Experiment'
activity.ExperimentRelationship.type_key = 'cim.1.activity.ExperimentRelationship'
activity.ExperimentRelationshipTarget.type_key = 'cim.1.activity.ExperimentRelationshipTarget'
activity.InitialCondition.type_key = 'cim.1.activity.InitialCondition'
activity.LateralBoundaryCondition.type_key = 'cim.1.activity.LateralBoundaryCondition'
activity.MeasurementCampaign.type_key = 'cim.1.activity.MeasurementCampaign'
activity.NumericalActivity.type_key = 'cim.1.activity.NumericalActivity'
activity.NumericalExperiment.type_key = 'cim.1.activity.NumericalExperiment'
activity.NumericalRequirement.type_key = 'cim.1.activity.NumericalRequirement'
activity.NumericalRequirementOption.type_key = 'cim.1.activity.NumericalRequirementOption'
activity.OutputRequirement.type_key = 'cim.1.activity.OutputRequirement'
activity.PhysicalModification.type_key = 'cim.1.activity.PhysicalModification'
activity.Simulation.type_key = 'cim.1.activity.Simulation'
activity.SimulationComposite.type_key = 'cim.1.activity.SimulationComposite'
activity.SimulationRelationship.type_key = 'cim.1.activity.SimulationRelationship'
activity.SimulationRelationshipTarget.type_key = 'cim.1.activity.SimulationRelationshipTarget'
activity.SimulationRun.type_key = 'cim.1.activity.SimulationRun'
activity.SpatioTemporalConstraint.type_key = 'cim.1.activity.SpatioTemporalConstraint'
data.DataContent.type_key = 'cim.1.data.DataContent'
data.DataDistribution.type_key = 'cim.1.data.DataDistribution'
data.DataExtent.type_key = 'cim.1.data.DataExtent'
data.DataExtentGeographical.type_key = 'cim.1.data.DataExtentGeographical'
data.DataExtentTemporal.type_key = 'cim.1.data.DataExtentTemporal'
data.DataExtentTimeInterval.type_key = 'cim.1.data.DataExtentTimeInterval'
data.DataHierarchyLevel.type_key = 'cim.1.data.DataHierarchyLevel'
data.DataObject.type_key = 'cim.1.data.DataObject'
data.DataProperty.type_key = 'cim.1.data.DataProperty'
data.DataRestriction.type_key = 'cim.1.data.DataRestriction'
data.DataStorage.type_key = 'cim.1.data.DataStorage'
data.DataStorageDb.type_key = 'cim.1.data.DataStorageDb'
data.DataStorageFile.type_key = 'cim.1.data.DataStorageFile'
data.DataStorageIp.type_key = 'cim.1.data.DataStorageIp'
data.DataTopic.type_key = 'cim.1.data.DataTopic'
grids.CoordinateList.type_key = 'cim.1.grids.CoordinateList'
grids.GridExtent.type_key = 'cim.1.grids.GridExtent'
grids.GridMosaic.type_key = 'cim.1.grids.GridMosaic'
grids.GridProperty.type_key = 'cim.1.grids.GridProperty'
grids.GridSpec.type_key = 'cim.1.grids.GridSpec'
grids.GridTile.type_key = 'cim.1.grids.GridTile'
grids.GridTileResolutionType.type_key = 'cim.1.grids.GridTileResolutionType'
grids.VerticalCoordinateList.type_key = 'cim.1.grids.VerticalCoordinateList'
quality.CimQuality.type_key = 'cim.1.quality.CimQuality'
quality.Evaluation.type_key = 'cim.1.quality.Evaluation'
quality.Measure.type_key = 'cim.1.quality.Measure'
quality.Report.type_key = 'cim.1.quality.Report'
shared.Calendar.type_key = 'cim.1.shared.Calendar'
shared.Change.type_key = 'cim.1.shared.Change'
shared.ChangeProperty.type_key = 'cim.1.shared.ChangeProperty'
shared.Citation.type_key = 'cim.1.shared.Citation'
shared.ClosedDateRange.type_key = 'cim.1.shared.ClosedDateRange'
shared.Compiler.type_key = 'cim.1.shared.Compiler'
shared.Daily360.type_key = 'cim.1.shared.Daily360'
shared.DataSource.type_key = 'cim.1.shared.DataSource'
shared.DateRange.type_key = 'cim.1.shared.DateRange'
shared.DocGenealogy.type_key = 'cim.1.shared.DocGenealogy'
shared.DocMetaInfo.type_key = 'cim.1.shared.DocMetaInfo'
shared.DocReference.type_key = 'cim.1.shared.DocReference'
shared.DocRelationship.type_key = 'cim.1.shared.DocRelationship'
shared.DocRelationshipTarget.type_key = 'cim.1.shared.DocRelationshipTarget'
shared.License.type_key = 'cim.1.shared.License'
shared.Machine.type_key = 'cim.1.shared.Machine'
shared.MachineCompilerUnit.type_key = 'cim.1.shared.MachineCompilerUnit'
shared.OpenDateRange.type_key = 'cim.1.shared.OpenDateRange'
shared.PerpetualPeriod.type_key = 'cim.1.shared.PerpetualPeriod'
shared.Platform.type_key = 'cim.1.shared.Platform'
shared.Property.type_key = 'cim.1.shared.Property'
shared.RealCalendar.type_key = 'cim.1.shared.RealCalendar'
shared.Relationship.type_key = 'cim.1.shared.Relationship'
shared.ResponsibleParty.type_key = 'cim.1.shared.ResponsibleParty'
shared.ResponsiblePartyContactInfo.type_key = 'cim.1.shared.ResponsiblePartyContactInfo'
shared.Standard.type_key = 'cim.1.shared.Standard'
shared.StandardName.type_key = 'cim.1.shared.StandardName'
software.Component.type_key = 'cim.1.software.Component'
software.ComponentLanguage.type_key = 'cim.1.software.ComponentLanguage'
software.ComponentLanguageProperty.type_key = 'cim.1.software.ComponentLanguageProperty'
software.ComponentProperty.type_key = 'cim.1.software.ComponentProperty'
software.Composition.type_key = 'cim.1.software.Composition'
software.Connection.type_key = 'cim.1.software.Connection'
software.ConnectionEndpoint.type_key = 'cim.1.software.ConnectionEndpoint'
software.ConnectionProperty.type_key = 'cim.1.software.ConnectionProperty'
software.Coupling.type_key = 'cim.1.software.Coupling'
software.CouplingEndpoint.type_key = 'cim.1.software.CouplingEndpoint'
software.CouplingProperty.type_key = 'cim.1.software.CouplingProperty'
software.Deployment.type_key = 'cim.1.software.Deployment'
software.EntryPoint.type_key = 'cim.1.software.EntryPoint'
software.ModelComponent.type_key = 'cim.1.software.ModelComponent'
software.Parallelisation.type_key = 'cim.1.software.Parallelisation'
software.ProcessorComponent.type_key = 'cim.1.software.ProcessorComponent'
software.Rank.type_key = 'cim.1.software.Rank'
software.SpatialRegridding.type_key = 'cim.1.software.SpatialRegridding'
software.SpatialRegriddingProperty.type_key = 'cim.1.software.SpatialRegriddingProperty'
software.SpatialRegriddingUserMethod.type_key = 'cim.1.software.SpatialRegriddingUserMethod'
software.StatisticalModelComponent.type_key = 'cim.1.software.StatisticalModelComponent'
software.TimeLag.type_key = 'cim.1.software.TimeLag'
software.TimeTransformation.type_key = 'cim.1.software.TimeTransformation'
software.Timing.type_key = 'cim.1.software.Timing'
misc.DocumentSet.type_key = 'cim.1.misc.DocumentSet'


# Set type info (name, type, is_required, is_iterative).
activity.Activity.type_info = (
    ('funding_sources', str, False, True),
    ('projects', str, False, True),
    ('rationales', str, False, True),
    ('responsible_parties', shared.ResponsibleParty, False, True),
)

activity.BoundaryCondition.type_info = (
)

activity.Conformance.type_info = (
    ('description', str, False, False),
    ('frequency', str, False, False),
    ('is_conformant', bool, True, False),
    ('requirements', activity.NumericalRequirement, False, True),
    ('requirements_references', shared.DocReference, False, True),
    ('sources', shared.DataSource, False, True),
    ('sources_references', shared.DocReference, False, True),
    ('type', str, False, False),
)

activity.DownscalingSimulation.type_info = (
    ('calendar', shared.Calendar, True, False),
    ('downscaled_from', shared.DataSource, True, False),
    ('downscaled_from_reference', shared.DocReference, True, False),
    ('downscaling_id', str, False, False),
    ('downscaling_type', str, False, False),
    ('inputs', software.Coupling, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('output_references', shared.DocReference, False, True),
    ('outputs', data.DataObject, False, True),
)

activity.Ensemble.type_info = (
    ('members', activity.EnsembleMember, True, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('outputs', shared.DataSource, False, True),
    ('outputs_references', shared.DocReference, False, True),
    ('types', str, True, True),
)

activity.EnsembleMember.type_info = (
    ('ensemble', activity.Ensemble, False, False),
    ('ensemble_ids', shared.StandardName, False, True),
    ('ensemble_reference', shared.DocReference, False, False),
    ('simulation', activity.Simulation, False, False),
    ('simulation_reference', shared.DocReference, False, False),
)

activity.Experiment.type_info = (
    ('generates', str, False, True),
    ('measurement_campaigns', activity.MeasurementCampaign, False, True),
    ('requires', activity.NumericalActivity, False, True),
    ('requires_references', shared.DocReference, False, True),
    ('supports', str, False, True),
    ('supports_references', shared.DocReference, False, True),
)

activity.ExperimentRelationship.type_info = (
    ('target', activity.ExperimentRelationshipTarget, True, False),
    ('type', str, True, False),
)

activity.ExperimentRelationshipTarget.type_info = (
    ('numerical_experiment', activity.NumericalExperiment, False, False),
    ('reference', shared.DocReference, False, False),
)

activity.InitialCondition.type_info = (
)

activity.LateralBoundaryCondition.type_info = (
)

activity.MeasurementCampaign.type_info = (
    ('duration', int, True, False),
)

activity.NumericalActivity.type_info = (
    ('description', str, False, False),
    ('long_name', str, False, False),
    ('short_name', str, True, False),
    ('supports', activity.Experiment, False, True),
    ('supports_references', shared.DocReference, False, True),
)

activity.NumericalExperiment.type_info = (
    ('description', str, False, False),
    ('experiment_id', str, False, False),
    ('long_name', str, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('requirements', activity.NumericalRequirement, False, True),
    ('short_name', str, True, False),
)

activity.NumericalRequirement.type_info = (
    ('description', str, False, False),
    ('id', str, False, False),
    ('name', str, True, False),
    ('options', activity.NumericalRequirementOption, False, True),
    ('requirement_type', str, True, False),
    ('source', shared.DataSource, False, False),
    ('source_reference', shared.DocReference, False, False),
)

activity.NumericalRequirementOption.type_info = (
    ('relationship', str, False, False),
    ('requirement', activity.NumericalRequirement, False, False),
)

activity.OutputRequirement.type_info = (
)

activity.PhysicalModification.type_info = (
)

activity.Simulation.type_info = (
    ('authors', str, False, False),
    ('calendar', shared.Calendar, True, False),
    ('conformances', activity.Conformance, False, True),
    ('control_simulation', activity.Simulation, False, False),
    ('control_simulation_reference', shared.DocReference, False, False),
    ('deployments', software.Deployment, False, True),
    ('inputs', software.Coupling, False, True),
    ('output_references', shared.DocReference, False, True),
    ('outputs', data.DataObject, False, True),
    ('restart_references', shared.DocReference, False, True),
    ('restarts', data.DataObject, False, True),
    ('simulation_id', str, False, False),
    ('spinup_date_range', shared.ClosedDateRange, False, False),
    ('spinup_simulation', activity.Simulation, False, False),
    ('spinup_simulation_reference', shared.DocReference, False, False),
)

activity.SimulationComposite.type_info = (
    ('child', activity.Simulation, False, True),
    ('date_range', shared.DateRange, True, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('rank', int, True, False),
)

activity.SimulationRelationship.type_info = (
    ('target', activity.SimulationRelationshipTarget, True, False),
    ('type', str, True, False),
)

activity.SimulationRelationshipTarget.type_info = (
    ('reference', shared.DocReference, False, False),
    ('target', str, False, False),
)

activity.SimulationRun.type_info = (
    ('date_range', shared.DateRange, True, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('model', software.ModelComponent, False, False),
    ('model_reference', shared.DocReference, False, False),
)

activity.SpatioTemporalConstraint.type_info = (
    ('date_range', shared.DateRange, False, False),
    ('spatial_resolution', str, False, False),
)

data.DataContent.type_info = (
    ('aggregation', str, False, False),
    ('frequency', str, False, False),
    ('topic', data.DataTopic, True, False),
)

data.DataDistribution.type_info = (
    ('access', str, False, False),
    ('fee', str, False, False),
    ('format', str, False, False),
    ('responsible_party', shared.ResponsibleParty, False, False),
)

data.DataExtent.type_info = (
    ('geographical', data.DataExtentGeographical, True, False),
    ('temporal', data.DataExtentTemporal, True, False),
)

data.DataExtentGeographical.type_info = (
    ('east', float, False, False),
    ('north', float, False, False),
    ('south', float, False, False),
    ('west', float, False, False),
)

data.DataExtentTemporal.type_info = (
    ('begin', datetime.date, False, False),
    ('end', datetime.date, False, False),
    ('time_interval', data.DataExtentTimeInterval, False, False),
)

data.DataExtentTimeInterval.type_info = (
    ('factor', int, False, False),
    ('radix', int, False, False),
    ('unit', str, False, False),
)

data.DataHierarchyLevel.type_info = (
    ('is_open', bool, False, False),
    ('name', str, False, False),
    ('value', str, False, False),
)

data.DataObject.type_info = (
    ('acronym', str, False, False),
    ('child_object', data.DataObject, False, True),
    ('citations', shared.Citation, False, True),
    ('content', data.DataContent, False, True),
    ('data_status', str, False, False),
    ('description', str, False, False),
    ('distribution', data.DataDistribution, False, False),
    ('extent', data.DataExtent, False, False),
    ('geometry_model', str, False, False),
    ('hierarchy_level', data.DataHierarchyLevel, False, False),
    ('keyword', str, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('parent_object', data.DataObject, False, False),
    ('parent_object_reference', shared.DocReference, False, False),
    ('properties', data.DataProperty, False, True),
    ('purpose', str, False, False),
    ('restriction', data.DataRestriction, False, True),
    ('source_simulation', str, False, False),
    ('storage', data.DataStorage, False, True),
)

data.DataProperty.type_info = (
    ('description', str, False, False),
)

data.DataRestriction.type_info = (
    ('license', shared.License, False, False),
    ('restriction', str, False, False),
    ('scope', str, False, False),
)

data.DataStorage.type_info = (
    ('format', str, False, False),
    ('location', str, False, False),
    ('modification_date', datetime.datetime, False, False),
    ('size', int, False, False),
)

data.DataStorageDb.type_info = (
    ('access_string', str, False, False),
    ('name', str, False, False),
    ('owner', str, False, False),
    ('table', str, False, False),
)

data.DataStorageFile.type_info = (
    ('file_name', str, False, False),
    ('file_system', str, False, False),
    ('path', str, False, False),
)

data.DataStorageIp.type_info = (
    ('fileName', str, False, False),
    ('host', str, False, False),
    ('path', str, False, False),
    ('protocol', str, False, False),
)

data.DataTopic.type_info = (
    ('description', str, False, False),
    ('name', str, False, False),
    ('unit', str, False, False),
)

grids.CoordinateList.type_info = (
    ('has_constant_offset', bool, False, False),
    ('length', int, False, False),
    ('uom', str, False, False),
)

grids.GridExtent.type_info = (
    ('maximum_latitude', str, True, False),
    ('maximum_longitude', str, True, False),
    ('minimum_latitude', str, True, False),
    ('minimum_longitude', str, True, False),
    ('units', str, False, False),
)

grids.GridMosaic.type_info = (
    ('citations', shared.Citation, False, True),
    ('description', str, False, False),
    ('extent', grids.GridExtent, False, False),
    ('has_congruent_tiles', bool, False, False),
    ('id', str, True, False),
    ('is_leaf', bool, True, False),
    ('long_name', str, False, False),
    ('mnemonic', str, False, False),
    ('mosaic_count', int, False, False),
    ('mosaics', grids.GridMosaic, False, True),
    ('short_name', str, True, False),
    ('tile_count', int, False, False),
    ('tiles', grids.GridTile, False, True),
    ('type', str, True, False),
)

grids.GridProperty.type_info = (
)

grids.GridSpec.type_info = (
    ('esm_exchange_grids', grids.GridMosaic, False, True),
    ('esm_model_grids', grids.GridMosaic, False, True),
    ('meta', shared.DocMetaInfo, True, False),
)

grids.GridTile.type_info = (
    ('area', str, False, False),
    ('cell_array', str, False, False),
    ('cell_ref_array', str, False, False),
    ('coord_file', str, False, False),
    ('coordinate_pole', str, False, False),
    ('description', str, False, False),
    ('discretization_type', str, False, False),
    ('extent', grids.GridExtent, False, False),
    ('geometry_type', str, False, False),
    ('grid_north_pole', str, False, False),
    ('horizontal_crs', str, False, False),
    ('horizontal_resolution', grids.GridTileResolutionType, False, False),
    ('id', str, False, False),
    ('is_conformal', bool, False, False),
    ('is_regular', bool, False, False),
    ('is_terrain_following', bool, False, False),
    ('is_uniform', bool, False, False),
    ('long_name', str, False, False),
    ('mnemonic', str, False, False),
    ('nx', int, False, False),
    ('ny', int, False, False),
    ('nz', int, False, False),
    ('refinement_scheme', str, False, False),
    ('short_name', str, False, False),
    ('simple_grid_geom', str, False, False),
    ('vertical_crs', str, False, False),
    ('vertical_resolution', grids.GridTileResolutionType, False, False),
    ('zcoords', grids.VerticalCoordinateList, False, False),
)

grids.GridTileResolutionType.type_info = (
    ('description', str, False, False),
    ('properties', grids.GridProperty, False, True),
)

grids.VerticalCoordinateList.type_info = (
    ('form', str, False, False),
    ('properties', grids.GridProperty, False, True),
    ('type', str, False, False),
)

quality.CimQuality.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('reports', quality.Report, False, True),
)

quality.Evaluation.type_info = (
    ('date', datetime.datetime, False, False),
    ('description', str, False, False),
    ('did_pass', bool, False, False),
    ('explanation', str, False, False),
    ('specification', str, False, False),
    ('specification_hyperlink', str, False, False),
    ('title', str, False, False),
    ('type', str, False, False),
    ('type_hyperlink', str, False, False),
)

quality.Measure.type_info = (
    ('description', str, False, False),
    ('identification', str, False, False),
    ('name', str, False, False),
)

quality.Report.type_info = (
    ('date', datetime.datetime, False, False),
    ('evaluation', quality.Evaluation, True, False),
    ('evaluator', shared.ResponsibleParty, False, False),
    ('measure', quality.Measure, True, False),
)

shared.Calendar.type_info = (
    ('description', str, False, False),
    ('length', int, False, False),
    ('range', shared.DateRange, False, False),
)

shared.Change.type_info = (
    ('author', shared.ResponsibleParty, False, False),
    ('date', datetime.datetime, False, False),
    ('description', str, False, False),
    ('details', shared.ChangeProperty, True, True),
    ('name', str, False, False),
    ('type', str, False, False),
)

shared.ChangeProperty.type_info = (
    ('description', str, False, False),
    ('id', str, False, False),
)

shared.Citation.type_info = (
    ('alternative_title', str, False, False),
    ('collective_title', str, False, False),
    ('date', datetime.datetime, False, False),
    ('date_type', str, False, False),
    ('location', str, False, False),
    ('organisation', str, False, False),
    ('reference', shared.DocReference, False, False),
    ('role', str, False, False),
    ('title', str, False, False),
    ('type', str, False, False),
)

shared.ClosedDateRange.type_info = (
    ('end', datetime.datetime, False, False),
    ('start', datetime.datetime, True, False),
)

shared.Compiler.type_info = (
    ('environment_variables', str, False, False),
    ('language', str, False, False),
    ('name', str, True, False),
    ('options', str, False, False),
    ('type', str, False, False),
    ('version', str, True, False),
)

shared.Daily360.type_info = (
)

shared.DataSource.type_info = (
    ('purpose', str, False, False),
)

shared.DateRange.type_info = (
    ('duration', str, False, False),
)

shared.DocGenealogy.type_info = (
    ('relationships', shared.DocRelationship, False, True),
)

shared.DocMetaInfo.type_info = (
    ('author', shared.ResponsibleParty, False, False),
    ('create_date', datetime.datetime, True, False),
    ('encodings', str, False, True),
    ('external_ids', shared.StandardName, False, True),
    ('genealogy', shared.DocGenealogy, False, False),
    ('id', uuid.UUID, True, False),
    ('institute', str, False, False),
    ('language', str, True, False),
    ('metadata_id', str, False, False),
    ('metadata_version', str, False, False),
    ('project', str, True, False),
    ('source', str, True, False),
    ('status', str, False, False),
    ('type', str, True, False),
    ('type_display_name', str, False, False),
    ('version', int, True, False),
)

shared.DocReference.type_info = (
    ('changes', shared.Change, False, True),
    ('description', str, False, False),
    ('external_id', str, False, False),
    ('id', uuid.UUID, False, False),
    ('name', str, False, False),
    ('type', str, False, False),
    ('version', str, False, False),
)

shared.DocRelationship.type_info = (
    ('target', shared.DocRelationshipTarget, True, False),
    ('type', str, True, False),
)

shared.DocRelationshipTarget.type_info = (
    ('document', str, False, False),
    ('reference', shared.DocReference, False, False),
)

shared.License.type_info = (
    ('contact', str, False, False),
    ('description', str, False, False),
    ('is_unrestricted', str, False, False),
    ('name', str, False, False),
)

shared.Machine.type_info = (
    ('cores_per_processor', int, False, False),
    ('description', str, False, False),
    ('interconnect', str, False, False),
    ('libraries', str, False, True),
    ('location', str, False, False),
    ('maximum_processors', int, False, False),
    ('name', str, True, False),
    ('operating_system', str, False, False),
    ('processor_type', str, False, False),
    ('system', str, False, False),
    ('type', str, False, False),
    ('vendor', str, False, False),
)

shared.MachineCompilerUnit.type_info = (
    ('compilers', shared.Compiler, False, True),
    ('machine', shared.Machine, True, False),
)

shared.OpenDateRange.type_info = (
    ('end', datetime.datetime, False, False),
    ('start', datetime.datetime, False, False),
)

shared.PerpetualPeriod.type_info = (
)

shared.Platform.type_info = (
    ('contacts', shared.ResponsibleParty, False, True),
    ('description', str, False, False),
    ('long_name', str, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('short_name', str, True, False),
    ('units', shared.MachineCompilerUnit, True, True),
)

shared.Property.type_info = (
    ('name', str, False, False),
    ('value', str, False, False),
)

shared.RealCalendar.type_info = (
)

shared.Relationship.type_info = (
    ('description', str, False, False),
    ('direction', str, True, False),
)

shared.ResponsibleParty.type_info = (
    ('abbreviation', str, False, False),
    ('contact_info', shared.ResponsiblePartyContactInfo, False, False),
    ('individual_name', str, False, False),
    ('organisation_name', str, False, False),
    ('role', str, False, False),
)

shared.ResponsiblePartyContactInfo.type_info = (
    ('address', str, False, False),
    ('email', str, False, False),
    ('url', str, False, False),
)

shared.Standard.type_info = (
    ('description', str, False, False),
    ('name', str, True, False),
    ('version', str, False, False),
)

shared.StandardName.type_info = (
    ('is_open', bool, True, False),
    ('standards', shared.Standard, False, True),
    ('value', str, True, False),
)

software.Component.type_info = (
    ('citations', shared.Citation, False, True),
    ('composition', software.Composition, False, False),
    ('coupling_framework', str, False, False),
    ('dependencies', software.EntryPoint, False, True),
    ('deployments', software.Deployment, False, True),
    ('description', str, False, False),
    ('funding_sources', str, False, True),
    ('grid', grids.GridSpec, False, False),
    ('is_embedded', bool, False, False),
    ('language', software.ComponentLanguage, False, False),
    ('license', shared.License, False, False),
    ('long_name', str, False, False),
    ('online_resource', str, False, False),
    ('parent', software.Component, False, False),
    ('previous_version', str, False, False),
    ('properties', software.ComponentProperty, False, True),
    ('release_date', datetime.datetime, False, False),
    ('responsible_parties', shared.ResponsibleParty, False, True),
    ('short_name', str, True, False),
    ('sub_components', software.Component, False, True),
)

software.ComponentLanguage.type_info = (
    ('name', str, True, False),
    ('properties', software.ComponentLanguageProperty, False, True),
)

software.ComponentLanguageProperty.type_info = (
)

software.ComponentProperty.type_info = (
    ('citations', shared.Citation, False, True),
    ('description', str, False, False),
    ('grid', str, False, False),
    ('intent', str, False, False),
    ('is_represented', bool, True, False),
    ('long_name', str, False, False),
    ('short_name', str, True, False),
    ('standard_names', str, False, True),
    ('sub_properties', software.ComponentProperty, False, True),
    ('units', str, False, False),
    ('values', str, False, True),
)

software.Composition.type_info = (
    ('couplings', str, False, True),
    ('description', str, False, False),
)

software.Connection.type_info = (
    ('description', str, False, False),
    ('priming', shared.DataSource, False, False),
    ('priming_reference', shared.DocReference, False, False),
    ('properties', software.ConnectionProperty, False, True),
    ('sources', software.ConnectionEndpoint, False, True),
    ('spatial_regridding', software.SpatialRegridding, False, True),
    ('target', software.ConnectionEndpoint, False, False),
    ('time_lag', str, False, False),
    ('time_profile', software.Timing, False, False),
    ('time_transformation', software.TimeTransformation, False, False),
    ('transformers', software.ProcessorComponent, False, True),
    ('transformers_references', shared.DocReference, False, True),
    ('type', str, False, False),
)

software.ConnectionEndpoint.type_info = (
    ('data_source', shared.DataSource, False, False),
    ('data_source_reference', shared.DocReference, False, False),
    ('instance_id', str, False, False),
    ('properties', software.ConnectionProperty, False, True),
)

software.ConnectionProperty.type_info = (
)

software.Coupling.type_info = (
    ('connections', software.Connection, False, True),
    ('description', str, False, False),
    ('is_fully_specified', bool, True, False),
    ('priming', shared.DataSource, False, False),
    ('priming_reference', shared.DocReference, False, False),
    ('properties', software.CouplingProperty, False, True),
    ('purpose', str, True, False),
    ('sources', software.CouplingEndpoint, True, True),
    ('spatial_regriddings', software.SpatialRegridding, False, True),
    ('target', software.CouplingEndpoint, True, False),
    ('time_lag', software.TimeLag, False, False),
    ('time_profile', software.Timing, False, False),
    ('time_transformation', software.TimeTransformation, False, False),
    ('transformers', software.ProcessorComponent, False, True),
    ('transformers_references', shared.DocReference, False, True),
    ('type', str, False, False),
)

software.CouplingEndpoint.type_info = (
    ('data_source', shared.DataSource, False, False),
    ('data_source_reference', shared.DocReference, False, False),
    ('instance_id', str, False, False),
    ('properties', software.CouplingProperty, False, True),
)

software.CouplingProperty.type_info = (
)

software.Deployment.type_info = (
    ('deployment_date', datetime.datetime, False, False),
    ('description', str, False, False),
    ('executable_arguments', str, False, True),
    ('executable_name', str, False, False),
    ('parallelisation', software.Parallelisation, False, False),
    ('platform', shared.Platform, False, False),
    ('platform_reference', shared.DocReference, False, False),
)

software.EntryPoint.type_info = (
    ('name', str, False, False),
)

software.ModelComponent.type_info = (
    ('activity', activity.Activity, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('timing', software.Timing, False, False),
    ('type', str, False, False),
    ('types', str, True, True),
)

software.Parallelisation.type_info = (
    ('processes', int, True, False),
    ('ranks', software.Rank, False, True),
)

software.ProcessorComponent.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
)

software.Rank.type_info = (
    ('increment', int, False, False),
    ('max', int, False, False),
    ('min', int, False, False),
    ('value', int, False, False),
)

software.SpatialRegridding.type_info = (
    ('dimension', str, False, False),
    ('properties', software.SpatialRegriddingProperty, False, True),
    ('standard_method', str, False, False),
    ('user_method', software.SpatialRegriddingUserMethod, False, False),
)

software.SpatialRegriddingProperty.type_info = (
)

software.SpatialRegriddingUserMethod.type_info = (
    ('file', data.DataObject, False, False),
    ('file_reference', shared.DocReference, False, False),
    ('name', str, True, False),
)

software.StatisticalModelComponent.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('timing', software.Timing, False, False),
    ('type', str, False, False),
    ('types', str, True, True),
)

software.TimeLag.type_info = (
    ('units', str, False, False),
    ('value', int, False, False),
)

software.TimeTransformation.type_info = (
    ('description', str, False, False),
    ('mapping_type', str, True, False),
)

software.Timing.type_info = (
    ('end', datetime.datetime, False, False),
    ('is_variable_rate', bool, False, False),
    ('rate', int, False, False),
    ('start', datetime.datetime, False, False),
    ('units', str, False, False),
)

misc.DocumentSet.type_info = (
    ('data', str, False, True),
    ('ensembles', activity.Ensemble, False, True),
    ('experiment', activity.NumericalExperiment, False, False),
    ('grids', grids.GridSpec, False, True),
    ('meta', shared.DocMetaInfo, True, False),
    ('model', software.ModelComponent, False, False),
    ('platform', shared.Platform, False, False),
    ('simulation', activity.SimulationRun, False, False),
)

