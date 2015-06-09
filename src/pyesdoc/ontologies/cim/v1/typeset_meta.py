# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_meta.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encpasulates meta-information pertaining to the cim.v1 typeset.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 15:44:25.797070.

"""
import datetime
import uuid

import typeset_for_misc_package as misc
import typeset_for_data_package as data
import typeset_for_grids_package as grids
import typeset_for_software_package as software
import typeset_for_quality_package as quality
import typeset_for_activity_package as activity
import typeset_for_shared_package as shared




# Set type keys.
shared.Citation.type_key = 'cim.1.shared.Citation'
activity.BoundaryCondition.type_key = 'cim.1.activity.BoundaryCondition'
shared.Compiler.type_key = 'cim.1.shared.Compiler'
software.ComponentLanguage.type_key = 'cim.1.software.ComponentLanguage'
quality.Evaluation.type_key = 'cim.1.quality.Evaluation'
data.DataStorageDb.type_key = 'cim.1.data.DataStorageDb'
data.DataExtentGeographical.type_key = 'cim.1.data.DataExtentGeographical'
shared.Standard.type_key = 'cim.1.shared.Standard'
software.CouplingProperty.type_key = 'cim.1.software.CouplingProperty'
activity.MeasurementCampaign.type_key = 'cim.1.activity.MeasurementCampaign'
software.SpatialRegridding.type_key = 'cim.1.software.SpatialRegridding'
shared.Platform.type_key = 'cim.1.shared.Platform'
grids.GridExtent.type_key = 'cim.1.grids.GridExtent'
shared.Change.type_key = 'cim.1.shared.Change'
activity.InitialCondition.type_key = 'cim.1.activity.InitialCondition'
activity.ExperimentRelationshipTarget.type_key = 'cim.1.activity.ExperimentRelationshipTarget'
shared.License.type_key = 'cim.1.shared.License'
software.Component.type_key = 'cim.1.software.Component'
grids.VerticalCoordinateList.type_key = 'cim.1.grids.VerticalCoordinateList'
quality.Measure.type_key = 'cim.1.quality.Measure'
software.SpatialRegriddingProperty.type_key = 'cim.1.software.SpatialRegriddingProperty'
shared.DocMetaInfo.type_key = 'cim.1.shared.DocMetaInfo'
activity.DownscalingSimulation.type_key = 'cim.1.activity.DownscalingSimulation'
activity.SimulationRelationshipTarget.type_key = 'cim.1.activity.SimulationRelationshipTarget'
data.DataExtentTemporal.type_key = 'cim.1.data.DataExtentTemporal'
activity.SimulationRun.type_key = 'cim.1.activity.SimulationRun'
software.Composition.type_key = 'cim.1.software.Composition'
shared.DocReference.type_key = 'cim.1.shared.DocReference'
software.Rank.type_key = 'cim.1.software.Rank'
data.DataContent.type_key = 'cim.1.data.DataContent'
activity.ExperimentRelationship.type_key = 'cim.1.activity.ExperimentRelationship'
software.Deployment.type_key = 'cim.1.software.Deployment'
activity.Ensemble.type_key = 'cim.1.activity.Ensemble'
software.EntryPoint.type_key = 'cim.1.software.EntryPoint'
activity.NumericalRequirement.type_key = 'cim.1.activity.NumericalRequirement'
grids.GridTileResolutionType.type_key = 'cim.1.grids.GridTileResolutionType'
shared.Daily360.type_key = 'cim.1.shared.Daily360'
software.ProcessorComponent.type_key = 'cim.1.software.ProcessorComponent'
activity.Conformance.type_key = 'cim.1.activity.Conformance'
shared.DataSource.type_key = 'cim.1.shared.DataSource'
data.DataStorageFile.type_key = 'cim.1.data.DataStorageFile'
shared.StandardName.type_key = 'cim.1.shared.StandardName'
data.DataRestriction.type_key = 'cim.1.data.DataRestriction'
software.TimeTransformation.type_key = 'cim.1.software.TimeTransformation'
shared.DocRelationship.type_key = 'cim.1.shared.DocRelationship'
grids.GridProperty.type_key = 'cim.1.grids.GridProperty'
data.DataStorageIp.type_key = 'cim.1.data.DataStorageIp'
activity.Simulation.type_key = 'cim.1.activity.Simulation'
activity.Experiment.type_key = 'cim.1.activity.Experiment'
quality.Report.type_key = 'cim.1.quality.Report'
data.DataExtentTimeInterval.type_key = 'cim.1.data.DataExtentTimeInterval'
shared.DocGenealogy.type_key = 'cim.1.shared.DocGenealogy'
shared.ResponsibleParty.type_key = 'cim.1.shared.ResponsibleParty'
software.CouplingEndpoint.type_key = 'cim.1.software.CouplingEndpoint'
software.ComponentLanguageProperty.type_key = 'cim.1.software.ComponentLanguageProperty'
software.Parallelisation.type_key = 'cim.1.software.Parallelisation'
shared.MachineCompilerUnit.type_key = 'cim.1.shared.MachineCompilerUnit'
shared.RealCalendar.type_key = 'cim.1.shared.RealCalendar'
activity.LateralBoundaryCondition.type_key = 'cim.1.activity.LateralBoundaryCondition'
software.StatisticalModelComponent.type_key = 'cim.1.software.StatisticalModelComponent'
software.ConnectionEndpoint.type_key = 'cim.1.software.ConnectionEndpoint'
activity.Activity.type_key = 'cim.1.activity.Activity'
software.Connection.type_key = 'cim.1.software.Connection'
shared.ChangeProperty.type_key = 'cim.1.shared.ChangeProperty'
grids.GridSpec.type_key = 'cim.1.grids.GridSpec'
software.SpatialRegriddingUserMethod.type_key = 'cim.1.software.SpatialRegriddingUserMethod'
data.DataExtent.type_key = 'cim.1.data.DataExtent'
shared.Relationship.type_key = 'cim.1.shared.Relationship'
software.ComponentProperty.type_key = 'cim.1.software.ComponentProperty'
shared.DocRelationshipTarget.type_key = 'cim.1.shared.DocRelationshipTarget'
grids.CoordinateList.type_key = 'cim.1.grids.CoordinateList'
activity.SimulationRelationship.type_key = 'cim.1.activity.SimulationRelationship'
data.DataStorage.type_key = 'cim.1.data.DataStorage'
data.DataDistribution.type_key = 'cim.1.data.DataDistribution'
shared.Calendar.type_key = 'cim.1.shared.Calendar'
software.Coupling.type_key = 'cim.1.software.Coupling'
activity.SpatioTemporalConstraint.type_key = 'cim.1.activity.SpatioTemporalConstraint'
activity.SimulationComposite.type_key = 'cim.1.activity.SimulationComposite'
data.DataObject.type_key = 'cim.1.data.DataObject'
activity.EnsembleMember.type_key = 'cim.1.activity.EnsembleMember'
shared.DateRange.type_key = 'cim.1.shared.DateRange'
software.ConnectionProperty.type_key = 'cim.1.software.ConnectionProperty'
shared.ClosedDateRange.type_key = 'cim.1.shared.ClosedDateRange'
quality.CimQuality.type_key = 'cim.1.quality.CimQuality'
software.Timing.type_key = 'cim.1.software.Timing'
software.ModelComponent.type_key = 'cim.1.software.ModelComponent'
grids.GridMosaic.type_key = 'cim.1.grids.GridMosaic'
data.DataTopic.type_key = 'cim.1.data.DataTopic'
activity.PhysicalModification.type_key = 'cim.1.activity.PhysicalModification'
activity.NumericalExperiment.type_key = 'cim.1.activity.NumericalExperiment'
grids.SimpleGridGeometry.type_key = 'cim.1.grids.SimpleGridGeometry'
shared.OpenDateRange.type_key = 'cim.1.shared.OpenDateRange'
shared.Property.type_key = 'cim.1.shared.Property'
grids.GridTile.type_key = 'cim.1.grids.GridTile'
misc.DocumentSet.type_key = 'cim.1.misc.DocumentSet'
shared.Machine.type_key = 'cim.1.shared.Machine'
activity.OutputRequirement.type_key = 'cim.1.activity.OutputRequirement'
activity.NumericalActivity.type_key = 'cim.1.activity.NumericalActivity'
software.TimeLag.type_key = 'cim.1.software.TimeLag'
data.DataProperty.type_key = 'cim.1.data.DataProperty'
data.DataHierarchyLevel.type_key = 'cim.1.data.DataHierarchyLevel'
activity.NumericalRequirementOption.type_key = 'cim.1.activity.NumericalRequirementOption'
shared.PerpetualPeriod.type_key = 'cim.1.shared.PerpetualPeriod'


# Set type info (name, type, is_required, is_iterative).
shared.Citation.type_info = (
    ('date', datetime.datetime, False, False),
    ('collective_title', str, False, False),
    ('alternative_title', str, False, False),
    ('role', str, False, False),
    ('organisation', str, False, False),
    ('date_type', str, False, False),
    ('location', str, False, False),
    ('type', str, False, False),
    ('reference', shared.DocReference, False, False),
    ('title', str, False, False),
)

activity.BoundaryCondition.type_info = (
)

shared.Compiler.type_info = (
    ('name', str, True, False),
    ('options', str, False, False),
    ('environment_variables', str, False, False),
    ('type', str, False, False),
    ('language', str, False, False),
    ('version', str, True, False),
)

software.ComponentLanguage.type_info = (
    ('name', str, True, False),
    ('properties', software.ComponentLanguageProperty, False, True),
)

quality.Evaluation.type_info = (
    ('specification_hyperlink', str, False, False),
    ('description', str, False, False),
    ('title', str, False, False),
    ('did_pass', bool, False, False),
    ('type', str, False, False),
    ('explanation', str, False, False),
    ('specification', str, False, False),
    ('type_hyperlink', str, False, False),
    ('date', datetime.datetime, False, False),
)

data.DataStorageDb.type_info = (
    ('access_string', str, False, False),
    ('owner', str, False, False),
    ('table', str, False, False),
    ('name', str, False, False),
)

data.DataExtentGeographical.type_info = (
    ('west', float, False, False),
    ('south', float, False, False),
    ('east', float, False, False),
    ('north', float, False, False),
)

shared.Standard.type_info = (
    ('version', str, False, False),
    ('description', str, False, False),
    ('name', str, True, False),
)

software.CouplingProperty.type_info = (
)

activity.MeasurementCampaign.type_info = (
    ('duration', int, True, False),
)

software.SpatialRegridding.type_info = (
    ('standard_method', str, False, False),
    ('user_method', software.SpatialRegriddingUserMethod, False, False),
    ('dimension', str, False, False),
    ('properties', software.SpatialRegriddingProperty, False, True),
)

shared.Platform.type_info = (
    ('contacts', shared.ResponsibleParty, False, True),
    ('units', shared.MachineCompilerUnit, True, True),
    ('description', str, False, False),
    ('long_name', str, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('short_name', str, True, False),
)

grids.GridExtent.type_info = (
    ('minimum_longitude', str, True, False),
    ('maximum_latitude', str, True, False),
    ('minimum_latitude', str, True, False),
    ('units', str, False, False),
    ('maximum_longitude', str, True, False),
)

shared.Change.type_info = (
    ('details', shared.ChangeProperty, True, True),
    ('date', datetime.datetime, False, False),
    ('author', shared.ResponsibleParty, False, False),
    ('type', str, False, False),
    ('name', str, False, False),
    ('description', str, False, False),
)

activity.InitialCondition.type_info = (
)

activity.ExperimentRelationshipTarget.type_info = (
    ('numerical_experiment', activity.NumericalExperiment, False, False),
    ('reference', shared.DocReference, False, False),
)

shared.License.type_info = (
    ('name', str, False, False),
    ('is_unrestricted', str, False, False),
    ('contact', str, False, False),
    ('description', str, False, False),
)

software.Component.type_info = (
    ('is_embedded', bool, False, False),
    ('language', software.ComponentLanguage, False, False),
    ('license', shared.License, False, False),
    ('dependencies', software.EntryPoint, False, True),
    ('long_name', str, False, False),
    ('online_resource', str, False, False),
    ('parent', software.Component, False, False),
    ('sub_components', software.Component, False, True),
    ('previous_version', str, False, False),
    ('citations', shared.Citation, False, True),
    ('properties', software.ComponentProperty, False, True),
    ('code_access', str, False, False),
    ('release_date', datetime.datetime, False, False),
    ('composition', software.Composition, False, False),
    ('responsible_parties', shared.ResponsibleParty, False, True),
    ('coupling_framework', str, False, False),
    ('short_name', str, True, False),
    ('version', str, False, False),
    ('deployments', software.Deployment, False, True),
    ('description', str, False, False),
    ('funding_sources', str, False, True),
    ('grid', grids.GridSpec, False, False),
)

grids.VerticalCoordinateList.type_info = (
    ('form', str, False, False),
    ('type', str, False, False),
    ('properties', grids.GridProperty, False, True),
)

quality.Measure.type_info = (
    ('description', str, False, False),
    ('name', str, False, False),
    ('identification', str, False, False),
)

software.SpatialRegriddingProperty.type_info = (
)

shared.DocMetaInfo.type_info = (
    ('type_display_name', str, False, False),
    ('id', uuid.UUID, True, False),
    ('metadata_version', str, False, False),
    ('drs_keys', str, False, True),
    ('source', str, True, False),
    ('status', str, False, False),
    ('source_key', str, False, False),
    ('metadata_id', str, False, False),
    ('encodings', str, False, True),
    ('author', shared.ResponsibleParty, False, False),
    ('genealogy', shared.DocGenealogy, False, False),
    ('institute', str, False, False),
    ('project', str, True, False),
    ('external_ids', shared.StandardName, False, True),
    ('sort_key', str, False, False),
    ('type_sort_key', str, False, False),
    ('type', str, True, False),
    ('language', str, True, False),
    ('version', int, True, False),
    ('drs_path', str, False, False),
    ('create_date', datetime.datetime, True, False),
)

activity.DownscalingSimulation.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('downscaling_id', str, False, False),
    ('output_references', shared.DocReference, False, True),
    ('inputs', software.Coupling, False, True),
    ('downscaled_from', shared.DataSource, True, False),
    ('downscaled_from_reference', shared.DocReference, True, False),
    ('outputs', data.DataObject, False, True),
    ('downscaling_type', str, False, False),
    ('calendar', shared.Calendar, True, False),
)

activity.SimulationRelationshipTarget.type_info = (
    ('reference', shared.DocReference, False, False),
    ('target', str, False, False),
)

data.DataExtentTemporal.type_info = (
    ('begin', datetime.date, False, False),
    ('time_interval', data.DataExtentTimeInterval, False, False),
    ('end', datetime.date, False, False),
)

activity.SimulationRun.type_info = (
    ('date_range', shared.DateRange, True, False),
    ('model_reference', shared.DocReference, False, False),
    ('model', software.ModelComponent, False, False),
    ('meta', shared.DocMetaInfo, True, False),
)

software.Composition.type_info = (
    ('couplings', str, False, True),
    ('description', str, False, False),
)

shared.DocReference.type_info = (
    ('name', str, False, False),
    ('version', int, False, False),
    ('type', str, False, False),
    ('description', str, False, False),
    ('external_id', str, False, False),
    ('id', uuid.UUID, False, False),
    ('changes', shared.Change, False, True),
)

software.Rank.type_info = (
    ('min', int, False, False),
    ('increment', int, False, False),
    ('value', int, False, False),
    ('max', int, False, False),
)

data.DataContent.type_info = (
    ('aggregation', str, False, False),
    ('topic', data.DataTopic, True, False),
    ('frequency', str, False, False),
)

activity.ExperimentRelationship.type_info = (
    ('target', activity.ExperimentRelationshipTarget, True, False),
    ('type', str, True, False),
)

software.Deployment.type_info = (
    ('executable_arguments', str, False, True),
    ('platform_reference', shared.DocReference, False, False),
    ('platform', shared.Platform, False, False),
    ('description', str, False, False),
    ('deployment_date', datetime.datetime, False, False),
    ('executable_name', str, False, False),
    ('parallelisation', software.Parallelisation, False, False),
)

activity.Ensemble.type_info = (
    ('members', activity.EnsembleMember, True, True),
    ('outputs_references', shared.DocReference, False, True),
    ('types', str, True, True),
    ('outputs', shared.DataSource, False, True),
    ('meta', shared.DocMetaInfo, True, False),
)

software.EntryPoint.type_info = (
    ('name', str, False, False),
)

activity.NumericalRequirement.type_info = (
    ('source', shared.DataSource, False, False),
    ('name', str, True, False),
    ('description', str, False, False),
    ('options', activity.NumericalRequirementOption, False, True),
    ('source_reference', shared.DocReference, False, False),
    ('requirement_type', str, True, False),
    ('id', str, False, False),
)

grids.GridTileResolutionType.type_info = (
    ('description', str, False, False),
    ('properties', grids.GridProperty, False, True),
)

shared.Daily360.type_info = (
)

software.ProcessorComponent.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
)

activity.Conformance.type_info = (
    ('requirements', activity.NumericalRequirement, False, True),
    ('type', str, False, False),
    ('description', str, False, False),
    ('requirements_references', shared.DocReference, False, True),
    ('frequency', str, False, False),
    ('sources', shared.DataSource, False, True),
    ('is_conformant', bool, True, False),
    ('sources_references', shared.DocReference, False, True),
)

shared.DataSource.type_info = (
    ('purpose', str, False, False),
)

data.DataStorageFile.type_info = (
    ('file_name', str, False, False),
    ('path', str, False, False),
    ('file_system', str, False, False),
)

shared.StandardName.type_info = (
    ('is_open', bool, True, False),
    ('value', str, True, False),
    ('standards', shared.Standard, False, True),
)

data.DataRestriction.type_info = (
    ('scope', str, False, False),
    ('license', shared.License, False, False),
    ('restriction', str, False, False),
)

software.TimeTransformation.type_info = (
    ('description', str, False, False),
    ('mapping_type', str, True, False),
)

shared.DocRelationship.type_info = (
    ('target', shared.DocRelationshipTarget, True, False),
    ('type', str, True, False),
)

grids.GridProperty.type_info = (
)

data.DataStorageIp.type_info = (
    ('host', str, False, False),
    ('protocol', str, False, False),
    ('file_name', str, False, False),
    ('path', str, False, False),
)

activity.Simulation.type_info = (
    ('spinup_simulation_reference', shared.DocReference, False, False),
    ('inputs', software.Coupling, False, True),
    ('output_references', shared.DocReference, False, True),
    ('control_simulation_reference', shared.DocReference, False, False),
    ('simulation_id', str, False, False),
    ('restarts', data.DataObject, False, True),
    ('conformances', activity.Conformance, False, True),
    ('authors', str, False, False),
    ('spinup_date_range', shared.ClosedDateRange, False, False),
    ('outputs', data.DataObject, False, True),
    ('deployments', software.Deployment, False, True),
    ('spinup_simulation', activity.Simulation, False, False),
    ('restart_references', shared.DocReference, False, True),
    ('control_simulation', activity.Simulation, False, False),
    ('calendar', shared.Calendar, True, False),
)

activity.Experiment.type_info = (
    ('supports', str, False, True),
    ('supports_references', shared.DocReference, False, True),
    ('requires_references', shared.DocReference, False, True),
    ('requires', activity.NumericalActivity, False, True),
    ('generates', str, False, True),
    ('measurement_campaigns', activity.MeasurementCampaign, False, True),
)

quality.Report.type_info = (
    ('date', datetime.datetime, False, False),
    ('measure', quality.Measure, True, False),
    ('evaluator', shared.ResponsibleParty, False, False),
    ('evaluation', quality.Evaluation, True, False),
)

data.DataExtentTimeInterval.type_info = (
    ('unit', str, False, False),
    ('factor', int, False, False),
    ('radix', int, False, False),
)

shared.DocGenealogy.type_info = (
    ('relationships', shared.DocRelationship, False, True),
)

shared.ResponsibleParty.type_info = (
    ('individual_name', str, False, False),
    ('address', str, False, False),
    ('abbreviation', str, False, False),
    ('role', str, False, False),
    ('organisation_name', str, False, False),
    ('email', str, False, False),
    ('url', str, False, False),
)

software.CouplingEndpoint.type_info = (
    ('properties', software.CouplingProperty, False, True),
    ('instance_id', str, False, False),
    ('data_source', shared.DataSource, False, False),
    ('data_source_reference', shared.DocReference, False, False),
)

software.ComponentLanguageProperty.type_info = (
)

software.Parallelisation.type_info = (
    ('processes', int, True, False),
    ('ranks', software.Rank, False, True),
)

shared.MachineCompilerUnit.type_info = (
    ('compilers', shared.Compiler, False, True),
    ('machine', shared.Machine, True, False),
)

shared.RealCalendar.type_info = (
)

activity.LateralBoundaryCondition.type_info = (
)

software.StatisticalModelComponent.type_info = (
    ('type', str, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('types', str, True, True),
    ('timing', software.Timing, False, False),
)

software.ConnectionEndpoint.type_info = (
    ('properties', software.ConnectionProperty, False, True),
    ('instance_id', str, False, False),
    ('data_source', shared.DataSource, False, False),
    ('data_source_reference', shared.DocReference, False, False),
)

activity.Activity.type_info = (
    ('responsible_parties', shared.ResponsibleParty, False, True),
    ('rationales', str, False, True),
    ('funding_sources', str, False, True),
    ('projects', str, False, True),
)

software.Connection.type_info = (
    ('properties', software.ConnectionProperty, False, True),
    ('transformers_references', shared.DocReference, False, True),
    ('type', str, False, False),
    ('target', software.ConnectionEndpoint, False, False),
    ('priming', shared.DataSource, False, False),
    ('priming_reference', shared.DocReference, False, False),
    ('time_profile', software.Timing, False, False),
    ('spatial_regridding', software.SpatialRegridding, False, True),
    ('transformers', software.ProcessorComponent, False, True),
    ('sources', software.ConnectionEndpoint, False, True),
    ('description', str, False, False),
    ('time_lag', str, False, False),
    ('time_transformation', software.TimeTransformation, False, False),
)

shared.ChangeProperty.type_info = (
    ('description', str, False, False),
    ('id', str, False, False),
)

grids.GridSpec.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('esm_exchange_grids', grids.GridMosaic, False, True),
    ('esm_model_grids', grids.GridMosaic, False, True),
)

software.SpatialRegriddingUserMethod.type_info = (
    ('name', str, True, False),
    ('file', data.DataObject, False, False),
    ('file_reference', shared.DocReference, False, False),
)

data.DataExtent.type_info = (
    ('geographical', data.DataExtentGeographical, True, False),
    ('temporal', data.DataExtentTemporal, True, False),
)

shared.Relationship.type_info = (
    ('description', str, False, False),
    ('direction', str, True, False),
)

software.ComponentProperty.type_info = (
    ('values', str, False, True),
    ('grid', str, False, False),
    ('short_name', str, True, False),
    ('intent', str, False, False),
    ('description', str, False, False),
    ('units', str, False, False),
    ('citations', shared.Citation, False, True),
    ('sub_properties', software.ComponentProperty, False, True),
    ('standard_names', str, False, True),
    ('long_name', str, False, False),
    ('is_represented', bool, True, False),
)

shared.DocRelationshipTarget.type_info = (
    ('document', str, False, False),
    ('reference', shared.DocReference, False, False),
)

grids.CoordinateList.type_info = (
    ('has_constant_offset', bool, False, False),
    ('uom', str, False, False),
    ('length', int, False, False),
)

activity.SimulationRelationship.type_info = (
    ('target', activity.SimulationRelationshipTarget, True, False),
    ('type', str, True, False),
)

data.DataStorage.type_info = (
    ('format', str, False, False),
    ('size', int, False, False),
    ('modification_date', datetime.datetime, False, False),
    ('location', str, False, False),
)

data.DataDistribution.type_info = (
    ('access', str, False, False),
    ('format', str, False, False),
    ('responsible_party', shared.ResponsibleParty, False, False),
    ('fee', str, False, False),
)

shared.Calendar.type_info = (
    ('range', shared.DateRange, False, False),
    ('description', str, False, False),
    ('length', int, False, False),
)

software.Coupling.type_info = (
    ('transformers', software.ProcessorComponent, False, True),
    ('target', software.CouplingEndpoint, True, False),
    ('priming', shared.DataSource, False, False),
    ('is_fully_specified', bool, True, False),
    ('connections', software.Connection, False, True),
    ('priming_reference', shared.DocReference, False, False),
    ('type', str, False, False),
    ('time_transformation', software.TimeTransformation, False, False),
    ('transformers_references', shared.DocReference, False, True),
    ('properties', software.CouplingProperty, False, True),
    ('sources', software.CouplingEndpoint, True, True),
    ('spatial_regriddings', software.SpatialRegridding, False, True),
    ('description', str, False, False),
    ('purpose', str, True, False),
    ('time_profile', software.Timing, False, False),
    ('time_lag', software.TimeLag, False, False),
)

activity.SpatioTemporalConstraint.type_info = (
    ('date_range', shared.DateRange, False, False),
    ('spatial_resolution', str, False, False),
)

activity.SimulationComposite.type_info = (
    ('rank', int, True, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('child', activity.Simulation, False, True),
    ('date_range', shared.DateRange, True, False),
)

data.DataObject.type_info = (
    ('hierarchy_level', data.DataHierarchyLevel, False, False),
    ('keyword', str, False, False),
    ('child_object', data.DataObject, False, True),
    ('properties', data.DataProperty, False, True),
    ('storage', data.DataStorage, False, True),
    ('description', str, False, False),
    ('purpose', str, False, False),
    ('citations', shared.Citation, False, True),
    ('source_simulation', str, False, False),
    ('acronym', str, False, False),
    ('distribution', data.DataDistribution, False, False),
    ('restriction', data.DataRestriction, False, True),
    ('content', data.DataContent, False, True),
    ('parent_object_reference', shared.DocReference, False, False),
    ('parent_object', data.DataObject, False, False),
    ('extent', data.DataExtent, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('data_status', str, False, False),
    ('geometry_model', str, False, False),
)

activity.EnsembleMember.type_info = (
    ('simulation_reference', shared.DocReference, False, False),
    ('ensemble', activity.Ensemble, False, False),
    ('ensemble_reference', shared.DocReference, False, False),
    ('simulation', activity.Simulation, False, False),
    ('ensemble_ids', shared.StandardName, False, True),
)

shared.DateRange.type_info = (
    ('duration', str, False, False),
)

software.ConnectionProperty.type_info = (
)

shared.ClosedDateRange.type_info = (
    ('end', datetime.datetime, False, False),
    ('start', datetime.datetime, True, False),
)

quality.CimQuality.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('reports', quality.Report, False, True),
)

software.Timing.type_info = (
    ('end', datetime.datetime, False, False),
    ('start', datetime.datetime, False, False),
    ('rate', int, False, False),
    ('units', str, False, False),
    ('is_variable_rate', bool, False, False),
)

software.ModelComponent.type_info = (
    ('types', str, True, True),
    ('type', str, False, False),
    ('timing', software.Timing, False, False),
    ('activity', activity.Activity, False, False),
    ('meta', shared.DocMetaInfo, True, False),
)

grids.GridMosaic.type_info = (
    ('mosaic_count', int, False, False),
    ('is_leaf', bool, True, False),
    ('tiles', grids.GridTile, False, True),
    ('mnemonic', str, False, False),
    ('mosaics', grids.GridMosaic, False, True),
    ('type', str, True, False),
    ('extent', grids.GridExtent, False, False),
    ('citations', shared.Citation, False, True),
    ('has_congruent_tiles', bool, False, False),
    ('tile_count', int, False, False),
    ('long_name', str, False, False),
    ('short_name', str, True, False),
    ('id', str, True, False),
    ('description', str, False, False),
)

data.DataTopic.type_info = (
    ('unit', str, False, False),
    ('description', str, False, False),
    ('name', str, False, False),
)

activity.PhysicalModification.type_info = (
)

activity.NumericalExperiment.type_info = (
    ('meta', shared.DocMetaInfo, True, False),
    ('requirements', activity.NumericalRequirement, False, True),
    ('experiment_id', str, False, False),
    ('description', str, False, False),
    ('short_name', str, True, False),
    ('long_name', str, False, False),
)

grids.SimpleGridGeometry.type_info = (
    ('xcoords', grids.CoordinateList, True, False),
    ('is_mesh', bool, False, False),
    ('dim_order', str, False, False),
    ('zcoords', grids.CoordinateList, False, False),
    ('ycoords', grids.CoordinateList, True, False),
    ('num_dims', int, True, False),
)

shared.OpenDateRange.type_info = (
    ('end', datetime.datetime, False, False),
    ('start', datetime.datetime, False, False),
)

shared.Property.type_info = (
    ('name', str, False, False),
    ('value', str, False, False),
)

grids.GridTile.type_info = (
    ('mnemonic', str, False, False),
    ('nx', int, False, False),
    ('short_name', str, False, False),
    ('ny', int, False, False),
    ('nz', int, False, False),
    ('vertical_crs', str, False, False),
    ('refinement_scheme', str, False, False),
    ('description', str, False, False),
    ('discretization_type', str, False, False),
    ('extent', grids.GridExtent, False, False),
    ('grid_north_pole', str, False, False),
    ('geometry_type', str, False, False),
    ('vertical_resolution', grids.GridTileResolutionType, False, False),
    ('zcoords', grids.VerticalCoordinateList, False, False),
    ('horizontal_resolution', grids.GridTileResolutionType, False, False),
    ('id', str, False, False),
    ('area', str, False, False),
    ('is_conformal', bool, False, False),
    ('cell_array', str, False, False),
    ('is_regular', bool, False, False),
    ('cell_ref_array', str, False, False),
    ('simple_grid_geom', grids.SimpleGridGeometry, False, False),
    ('is_terrain_following', bool, False, False),
    ('coord_file', str, False, False),
    ('is_uniform', bool, False, False),
    ('coordinate_pole', str, False, False),
    ('long_name', str, False, False),
    ('horizontal_crs', str, False, False),
)

misc.DocumentSet.type_info = (
    ('simulation', activity.SimulationRun, False, False),
    ('simulation_reference', shared.DocReference, False, False),
    ('experiment_reference', shared.DocReference, False, False),
    ('model', software.ModelComponent, False, False),
    ('ensembles', activity.Ensemble, False, True),
    ('grids', grids.GridSpec, False, True),
    ('model_reference', shared.DocReference, False, False),
    ('meta', shared.DocMetaInfo, True, False),
    ('ensembles_references', shared.DocReference, False, True),
    ('data', data.DataObject, False, True),
    ('platform_reference', shared.DocReference, False, False),
    ('experiment', activity.NumericalExperiment, False, False),
    ('data_references', shared.DocReference, False, True),
    ('platform', shared.Platform, False, False),
    ('grids_references', shared.DocReference, False, True),
)

shared.Machine.type_info = (
    ('type', str, False, False),
    ('maximum_processors', int, False, False),
    ('processor_type', str, False, False),
    ('vendor', str, False, False),
    ('name', str, True, False),
    ('operating_system', str, False, False),
    ('cores_per_processor', int, False, False),
    ('libraries', str, False, True),
    ('system', str, False, False),
    ('description', str, False, False),
    ('location', str, False, False),
    ('interconnect', str, False, False),
)

activity.OutputRequirement.type_info = (
)

activity.NumericalActivity.type_info = (
    ('description', str, False, False),
    ('supports', activity.Experiment, False, True),
    ('long_name', str, False, False),
    ('supports_references', shared.DocReference, False, True),
    ('short_name', str, True, False),
)

software.TimeLag.type_info = (
    ('units', str, False, False),
    ('value', int, False, False),
)

data.DataProperty.type_info = (
    ('description', str, False, False),
)

data.DataHierarchyLevel.type_info = (
    ('is_open', bool, False, False),
    ('value', str, False, False),
    ('name', str, False, False),
)

activity.NumericalRequirementOption.type_info = (
    ('relationship', str, False, False),
    ('sub_options', activity.NumericalRequirementOption, False, True),
    ('name', str, True, False),
    ('description', str, False, False),
    ('id', str, False, False),
)

shared.PerpetualPeriod.type_info = (
)

