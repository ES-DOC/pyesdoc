
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.keys.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The ontology map of types to keys.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import typeset_for_designing_package as designing
import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_drs_package as drs
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_shared_package as shared




# Map of ontology types to type keys.
KEYS = {
    # ------------------------------------------------
    # Packages.
    # ------------------------------------------------

    designing: "cim.2.designing",

    data: "cim.2.data",

    platform: "cim.2.platform",

    drs: "cim.2.drs",

    activity: "cim.2.activity",

    software: "cim.2.software",

    science: "cim.2.science",

    shared: "cim.2.shared",

    # ------------------------------------------------
    # Classes.
    # ------------------------------------------------


    designing.MultiTimeEnsemble: "cim.2.designing.MultiTimeEnsemble",

    designing.MultiEnsemble: "cim.2.designing.MultiEnsemble",

    designing.TemporalConstraint: "cim.2.designing.TemporalConstraint",

    designing.ForcingConstraint: "cim.2.designing.ForcingConstraint",

    designing.EnsembleRequirement: "cim.2.designing.EnsembleRequirement",

    designing.NumericalRequirement: "cim.2.designing.NumericalRequirement",

    designing.SimulationPlan: "cim.2.designing.SimulationPlan",

    designing.DomainProperties: "cim.2.designing.DomainProperties",

    designing.Project: "cim.2.designing.Project",

    designing.NumericalExperiment: "cim.2.designing.NumericalExperiment",

    designing.OutputTemporalRequirement: "cim.2.designing.OutputTemporalRequirement",



    data.VariableCollection: "cim.2.data.VariableCollection",

    data.Dataset: "cim.2.data.Dataset",

    data.Downscaling: "cim.2.data.Downscaling",

    data.Simulation: "cim.2.data.Simulation",



    platform.Machine: "cim.2.platform.Machine",

    platform.ComputePool: "cim.2.platform.ComputePool",

    platform.ComponentPerformance: "cim.2.platform.ComponentPerformance",

    platform.Performance: "cim.2.platform.Performance",

    platform.StoragePool: "cim.2.platform.StoragePool",

    platform.Partition: "cim.2.platform.Partition",

    platform.StorageVolume: "cim.2.platform.StorageVolume",



    drs.DrsAtomicDataset: "cim.2.drs.DrsAtomicDataset",

    drs.DrsPublicationDataset: "cim.2.drs.DrsPublicationDataset",

    drs.DrsTemporalIdentifier: "cim.2.drs.DrsTemporalIdentifier",

    drs.DrsGeographicalIndicator: "cim.2.drs.DrsGeographicalIndicator",

    drs.DrsEnsembleIdentifier: "cim.2.drs.DrsEnsembleIdentifier",



    activity.ParentSimulation: "cim.2.activity.ParentSimulation",

    activity.AxisMember: "cim.2.activity.AxisMember",

    activity.Activity: "cim.2.activity.Activity",

    activity.Conformance: "cim.2.activity.Conformance",

    activity.EnsembleAxis: "cim.2.activity.EnsembleAxis",

    activity.Ensemble: "cim.2.activity.Ensemble",

    activity.UberEnsemble: "cim.2.activity.UberEnsemble",

    activity.EnsembleMember: "cim.2.activity.EnsembleMember",



    software.Gridspec: "cim.2.software.Gridspec",

    software.Variable: "cim.2.software.Variable",

    software.DevelopmentPath: "cim.2.software.DevelopmentPath",

    software.ComponentBase: "cim.2.software.ComponentBase",

    software.SoftwareComponent: "cim.2.software.SoftwareComponent",

    software.EntryPoint: "cim.2.software.EntryPoint",

    software.Composition: "cim.2.software.Composition",



    science.ScienceContext: "cim.2.science.ScienceContext",

    science.SubProcess: "cim.2.science.SubProcess",

    science.Resolution: "cim.2.science.Resolution",

    science.ScientificDomain: "cim.2.science.ScientificDomain",

    science.Extent: "cim.2.science.Extent",

    science.Model: "cim.2.science.Model",

    science.Tuning: "cim.2.science.Tuning",

    science.Process: "cim.2.science.Process",

    science.Detail: "cim.2.science.Detail",

    science.Algorithm: "cim.2.science.Algorithm",

    science.Grid: "cim.2.science.Grid",

    science.KeyProperties: "cim.2.science.KeyProperties",

    science.ConservationProperties: "cim.2.science.ConservationProperties",



    shared.DatetimeSet: "cim.2.shared.DatetimeSet",

    shared.ExternalDocument: "cim.2.shared.ExternalDocument",

    shared.DocMetaInfo: "cim.2.shared.DocMetaInfo",

    shared.DateTime: "cim.2.shared.DateTime",

    shared.Responsibility: "cim.2.shared.Responsibility",

    shared.RegularTimeset: "cim.2.shared.RegularTimeset",

    shared.Pid: "cim.2.shared.Pid",

    shared.OnlineResource: "cim.2.shared.OnlineResource",

    shared.NumberArray: "cim.2.shared.NumberArray",

    shared.QualityReview: "cim.2.shared.QualityReview",

    shared.DocReference: "cim.2.shared.DocReference",

    shared.IrregularDateset: "cim.2.shared.IrregularDateset",

    shared.Party: "cim.2.shared.Party",

    shared.Reference: "cim.2.shared.Reference",

    shared.TimesliceList: "cim.2.shared.TimesliceList",

    shared.TimePeriod: "cim.2.shared.TimePeriod",

    shared.Calendar: "cim.2.shared.Calendar",

    shared.Cimtext: "cim.2.shared.Cimtext",

    shared.KeyFloat: "cim.2.shared.KeyFloat",


    # ------------------------------------------------
    # Class properties.
    # ------------------------------------------------



    (designing.MultiTimeEnsemble, 'ensemble_members'): "cim.2.designing.MultiTimeEnsemble.ensemble_members",



    (designing.MultiEnsemble, 'ensemble_axis'): "cim.2.designing.MultiEnsemble.ensemble_axis",



    (designing.TemporalConstraint, 'start_date'): "cim.2.designing.TemporalConstraint.start_date",

    (designing.TemporalConstraint, 'start_flexibility'): "cim.2.designing.TemporalConstraint.start_flexibility",

    (designing.TemporalConstraint, 'required_calendar'): "cim.2.designing.TemporalConstraint.required_calendar",

    (designing.TemporalConstraint, 'required_duration'): "cim.2.designing.TemporalConstraint.required_duration",



    (designing.ForcingConstraint, 'data_link'): "cim.2.designing.ForcingConstraint.data_link",

    (designing.ForcingConstraint, 'origin'): "cim.2.designing.ForcingConstraint.origin",

    (designing.ForcingConstraint, 'forcing_type'): "cim.2.designing.ForcingConstraint.forcing_type",

    (designing.ForcingConstraint, 'additional_constraint'): "cim.2.designing.ForcingConstraint.additional_constraint",

    (designing.ForcingConstraint, 'group'): "cim.2.designing.ForcingConstraint.group",

    (designing.ForcingConstraint, 'code'): "cim.2.designing.ForcingConstraint.code",

    (designing.ForcingConstraint, 'category'): "cim.2.designing.ForcingConstraint.category",



    (designing.EnsembleRequirement, 'ensemble_type'): "cim.2.designing.EnsembleRequirement.ensemble_type",

    (designing.EnsembleRequirement, 'ensemble_member'): "cim.2.designing.EnsembleRequirement.ensemble_member",

    (designing.EnsembleRequirement, 'minimum_size'): "cim.2.designing.EnsembleRequirement.minimum_size",



    (designing.NumericalRequirement, 'additional_requirements'): "cim.2.designing.NumericalRequirement.additional_requirements",

    (designing.NumericalRequirement, 'conformance_is_requested'): "cim.2.designing.NumericalRequirement.conformance_is_requested",



    (designing.SimulationPlan, 'will_support_experiments'): "cim.2.designing.SimulationPlan.will_support_experiments",

    (designing.SimulationPlan, 'expected_model'): "cim.2.designing.SimulationPlan.expected_model",

    (designing.SimulationPlan, 'expected_platform'): "cim.2.designing.SimulationPlan.expected_platform",

    (designing.SimulationPlan, 'expected_performance_sypd'): "cim.2.designing.SimulationPlan.expected_performance_sypd",



    (designing.DomainProperties, 'required_extent'): "cim.2.designing.DomainProperties.required_extent",

    (designing.DomainProperties, 'required_resolution'): "cim.2.designing.DomainProperties.required_resolution",



    (designing.Project, 'requires_experiments'): "cim.2.designing.Project.requires_experiments",

    (designing.Project, 'previous_projects'): "cim.2.designing.Project.previous_projects",

    (designing.Project, 'sub_projects'): "cim.2.designing.Project.sub_projects",



    (designing.NumericalExperiment, 'related_experiments'): "cim.2.designing.NumericalExperiment.related_experiments",

    (designing.NumericalExperiment, 'requirements'): "cim.2.designing.NumericalExperiment.requirements",



    (designing.OutputTemporalRequirement, 'continuous_subset'): "cim.2.designing.OutputTemporalRequirement.continuous_subset",

    (designing.OutputTemporalRequirement, 'throughout'): "cim.2.designing.OutputTemporalRequirement.throughout",

    (designing.OutputTemporalRequirement, 'sliced_subset'): "cim.2.designing.OutputTemporalRequirement.sliced_subset",





    (data.VariableCollection, 'collection_name'): "cim.2.data.VariableCollection.collection_name",

    (data.VariableCollection, 'variables'): "cim.2.data.VariableCollection.variables",



    (data.Dataset, 'availability'): "cim.2.data.Dataset.availability",

    (data.Dataset, 'references'): "cim.2.data.Dataset.references",

    (data.Dataset, 'responsible_parties'): "cim.2.data.Dataset.responsible_parties",

    (data.Dataset, 'meta'): "cim.2.data.Dataset.meta",

    (data.Dataset, 'drs_datasets'): "cim.2.data.Dataset.drs_datasets",

    (data.Dataset, 'name'): "cim.2.data.Dataset.name",

    (data.Dataset, 'related_to_dataset'): "cim.2.data.Dataset.related_to_dataset",

    (data.Dataset, 'produced_by'): "cim.2.data.Dataset.produced_by",

    (data.Dataset, 'description'): "cim.2.data.Dataset.description",



    (data.Downscaling, 'downscaled_from'): "cim.2.data.Downscaling.downscaled_from",



    (data.Simulation, 'primary_ensemble'): "cim.2.data.Simulation.primary_ensemble",

    (data.Simulation, 'ran_for_experiments'): "cim.2.data.Simulation.ran_for_experiments",

    (data.Simulation, 'ensemble_identifier'): "cim.2.data.Simulation.ensemble_identifier",

    (data.Simulation, 'parent_simulation'): "cim.2.data.Simulation.parent_simulation",

    (data.Simulation, 'used'): "cim.2.data.Simulation.used",

    (data.Simulation, 'part_of_project'): "cim.2.data.Simulation.part_of_project",

    (data.Simulation, 'calendar'): "cim.2.data.Simulation.calendar",





    (platform.Machine, 'meta'): "cim.2.platform.Machine.meta",



    (platform.ComputePool, 'cpu_type'): "cim.2.platform.ComputePool.cpu_type",

    (platform.ComputePool, 'number_of_nodes'): "cim.2.platform.ComputePool.number_of_nodes",

    (platform.ComputePool, 'name'): "cim.2.platform.ComputePool.name",

    (platform.ComputePool, 'memory_per_node'): "cim.2.platform.ComputePool.memory_per_node",

    (platform.ComputePool, 'accelerators_per_node'): "cim.2.platform.ComputePool.accelerators_per_node",

    (platform.ComputePool, 'description'): "cim.2.platform.ComputePool.description",

    (platform.ComputePool, 'interconnect'): "cim.2.platform.ComputePool.interconnect",

    (platform.ComputePool, 'operating_system'): "cim.2.platform.ComputePool.operating_system",

    (platform.ComputePool, 'model_number'): "cim.2.platform.ComputePool.model_number",

    (platform.ComputePool, 'accelerator_type'): "cim.2.platform.ComputePool.accelerator_type",

    (platform.ComputePool, 'compute_cores_per_node'): "cim.2.platform.ComputePool.compute_cores_per_node",



    (platform.ComponentPerformance, 'speed'): "cim.2.platform.ComponentPerformance.speed",

    (platform.ComponentPerformance, 'cores_used'): "cim.2.platform.ComponentPerformance.cores_used",

    (platform.ComponentPerformance, 'nodes_used'): "cim.2.platform.ComponentPerformance.nodes_used",

    (platform.ComponentPerformance, 'component'): "cim.2.platform.ComponentPerformance.component",

    (platform.ComponentPerformance, 'component_name'): "cim.2.platform.ComponentPerformance.component_name",



    (platform.Performance, 'meta'): "cim.2.platform.Performance.meta",

    (platform.Performance, 'subcomponent_performance'): "cim.2.platform.Performance.subcomponent_performance",

    (platform.Performance, 'compiler'): "cim.2.platform.Performance.compiler",

    (platform.Performance, 'total_nodes_used'): "cim.2.platform.Performance.total_nodes_used",

    (platform.Performance, 'model'): "cim.2.platform.Performance.model",

    (platform.Performance, 'coupler_load'): "cim.2.platform.Performance.coupler_load",

    (platform.Performance, 'chsy'): "cim.2.platform.Performance.chsy",

    (platform.Performance, 'memory_bloat'): "cim.2.platform.Performance.memory_bloat",

    (platform.Performance, 'platform'): "cim.2.platform.Performance.platform",

    (platform.Performance, 'io_load'): "cim.2.platform.Performance.io_load",

    (platform.Performance, 'name'): "cim.2.platform.Performance.name",

    (platform.Performance, 'sypd'): "cim.2.platform.Performance.sypd",

    (platform.Performance, 'load_imbalance'): "cim.2.platform.Performance.load_imbalance",

    (platform.Performance, 'asypd'): "cim.2.platform.Performance.asypd",



    (platform.StoragePool, 'description'): "cim.2.platform.StoragePool.description",

    (platform.StoragePool, 'vendor'): "cim.2.platform.StoragePool.vendor",

    (platform.StoragePool, 'name'): "cim.2.platform.StoragePool.name",

    (platform.StoragePool, 'volume_available'): "cim.2.platform.StoragePool.volume_available",

    (platform.StoragePool, 'type'): "cim.2.platform.StoragePool.type",



    (platform.Partition, 'name'): "cim.2.platform.Partition.name",

    (platform.Partition, 'storage_pools'): "cim.2.platform.Partition.storage_pools",

    (platform.Partition, 'when_used'): "cim.2.platform.Partition.when_used",

    (platform.Partition, 'partition'): "cim.2.platform.Partition.partition",

    (platform.Partition, 'description'): "cim.2.platform.Partition.description",

    (platform.Partition, 'institution'): "cim.2.platform.Partition.institution",

    (platform.Partition, 'vendor'): "cim.2.platform.Partition.vendor",

    (platform.Partition, 'online_documentation'): "cim.2.platform.Partition.online_documentation",

    (platform.Partition, 'model_number'): "cim.2.platform.Partition.model_number",

    (platform.Partition, 'compute_pools'): "cim.2.platform.Partition.compute_pools",



    (platform.StorageVolume, 'units'): "cim.2.platform.StorageVolume.units",

    (platform.StorageVolume, 'volume'): "cim.2.platform.StorageVolume.volume",





    (drs.DrsAtomicDataset, 'temporal_constraint'): "cim.2.drs.DrsAtomicDataset.temporal_constraint",

    (drs.DrsAtomicDataset, 'geographical_constraint'): "cim.2.drs.DrsAtomicDataset.geographical_constraint",

    (drs.DrsAtomicDataset, 'variable_name'): "cim.2.drs.DrsAtomicDataset.variable_name",

    (drs.DrsAtomicDataset, 'ensemble_member'): "cim.2.drs.DrsAtomicDataset.ensemble_member",

    (drs.DrsAtomicDataset, 'mip_table'): "cim.2.drs.DrsAtomicDataset.mip_table",



    (drs.DrsPublicationDataset, 'frequency'): "cim.2.drs.DrsPublicationDataset.frequency",

    (drs.DrsPublicationDataset, 'realm'): "cim.2.drs.DrsPublicationDataset.realm",

    (drs.DrsPublicationDataset, 'institute'): "cim.2.drs.DrsPublicationDataset.institute",

    (drs.DrsPublicationDataset, 'experiment'): "cim.2.drs.DrsPublicationDataset.experiment",

    (drs.DrsPublicationDataset, 'version_number'): "cim.2.drs.DrsPublicationDataset.version_number",

    (drs.DrsPublicationDataset, 'model'): "cim.2.drs.DrsPublicationDataset.model",

    (drs.DrsPublicationDataset, 'product'): "cim.2.drs.DrsPublicationDataset.product",

    (drs.DrsPublicationDataset, 'activity'): "cim.2.drs.DrsPublicationDataset.activity",



    (drs.DrsTemporalIdentifier, 'end'): "cim.2.drs.DrsTemporalIdentifier.end",

    (drs.DrsTemporalIdentifier, 'suffix'): "cim.2.drs.DrsTemporalIdentifier.suffix",

    (drs.DrsTemporalIdentifier, 'start'): "cim.2.drs.DrsTemporalIdentifier.start",



    (drs.DrsGeographicalIndicator, 'spatial_domain'): "cim.2.drs.DrsGeographicalIndicator.spatial_domain",

    (drs.DrsGeographicalIndicator, 'bounding_box'): "cim.2.drs.DrsGeographicalIndicator.bounding_box",

    (drs.DrsGeographicalIndicator, 'operator'): "cim.2.drs.DrsGeographicalIndicator.operator",



    (drs.DrsEnsembleIdentifier, 'realisation_number'): "cim.2.drs.DrsEnsembleIdentifier.realisation_number",

    (drs.DrsEnsembleIdentifier, 'initialisation_method_number'): "cim.2.drs.DrsEnsembleIdentifier.initialisation_method_number",

    (drs.DrsEnsembleIdentifier, 'perturbation_number'): "cim.2.drs.DrsEnsembleIdentifier.perturbation_number",





    (activity.ParentSimulation, 'parent'): "cim.2.activity.ParentSimulation.parent",

    (activity.ParentSimulation, 'branch_time_in_child'): "cim.2.activity.ParentSimulation.branch_time_in_child",

    (activity.ParentSimulation, 'branch_time_in_parent'): "cim.2.activity.ParentSimulation.branch_time_in_parent",



    (activity.AxisMember, 'value'): "cim.2.activity.AxisMember.value",

    (activity.AxisMember, 'description'): "cim.2.activity.AxisMember.description",

    (activity.AxisMember, 'index'): "cim.2.activity.AxisMember.index",

    (activity.AxisMember, 'extra_detail'): "cim.2.activity.AxisMember.extra_detail",



    (activity.Activity, 'keywords'): "cim.2.activity.Activity.keywords",

    (activity.Activity, 'rationale'): "cim.2.activity.Activity.rationale",

    (activity.Activity, 'long_name'): "cim.2.activity.Activity.long_name",

    (activity.Activity, 'canonical_name'): "cim.2.activity.Activity.canonical_name",

    (activity.Activity, 'meta'): "cim.2.activity.Activity.meta",

    (activity.Activity, 'references'): "cim.2.activity.Activity.references",

    (activity.Activity, 'responsible_parties'): "cim.2.activity.Activity.responsible_parties",

    (activity.Activity, 'duration'): "cim.2.activity.Activity.duration",

    (activity.Activity, 'name'): "cim.2.activity.Activity.name",

    (activity.Activity, 'description'): "cim.2.activity.Activity.description",



    (activity.Conformance, 'target_requirement'): "cim.2.activity.Conformance.target_requirement",



    (activity.EnsembleAxis, 'target_requirement'): "cim.2.activity.EnsembleAxis.target_requirement",

    (activity.EnsembleAxis, 'short_identifier'): "cim.2.activity.EnsembleAxis.short_identifier",

    (activity.EnsembleAxis, 'extra_detail'): "cim.2.activity.EnsembleAxis.extra_detail",

    (activity.EnsembleAxis, 'member'): "cim.2.activity.EnsembleAxis.member",



    (activity.Ensemble, 'documentation'): "cim.2.activity.Ensemble.documentation",

    (activity.Ensemble, 'supported'): "cim.2.activity.Ensemble.supported",

    (activity.Ensemble, 'has_ensemble_axes'): "cim.2.activity.Ensemble.has_ensemble_axes",

    (activity.Ensemble, 'members'): "cim.2.activity.Ensemble.members",

    (activity.Ensemble, 'part_of'): "cim.2.activity.Ensemble.part_of",

    (activity.Ensemble, 'common_conformances'): "cim.2.activity.Ensemble.common_conformances",



    (activity.UberEnsemble, 'child_ensembles'): "cim.2.activity.UberEnsemble.child_ensembles",



    (activity.EnsembleMember, 'errata'): "cim.2.activity.EnsembleMember.errata",

    (activity.EnsembleMember, 'simulation'): "cim.2.activity.EnsembleMember.simulation",

    (activity.EnsembleMember, 'variant_id'): "cim.2.activity.EnsembleMember.variant_id",

    (activity.EnsembleMember, 'had_performance'): "cim.2.activity.EnsembleMember.had_performance",

    (activity.EnsembleMember, 'ran_on'): "cim.2.activity.EnsembleMember.ran_on",





    (software.Gridspec, 'description'): "cim.2.software.Gridspec.description",



    (software.Variable, 'prognostic'): "cim.2.software.Variable.prognostic",

    (software.Variable, 'description'): "cim.2.software.Variable.description",

    (software.Variable, 'name'): "cim.2.software.Variable.name",



    (software.DevelopmentPath, 'developed_in_house'): "cim.2.software.DevelopmentPath.developed_in_house",

    (software.DevelopmentPath, 'consortium_name'): "cim.2.software.DevelopmentPath.consortium_name",

    (software.DevelopmentPath, 'funding_sources'): "cim.2.software.DevelopmentPath.funding_sources",

    (software.DevelopmentPath, 'previous_version'): "cim.2.software.DevelopmentPath.previous_version",

    (software.DevelopmentPath, 'creators'): "cim.2.software.DevelopmentPath.creators",



    (software.ComponentBase, 'documentation'): "cim.2.software.ComponentBase.documentation",

    (software.ComponentBase, 'repository'): "cim.2.software.ComponentBase.repository",

    (software.ComponentBase, 'name'): "cim.2.software.ComponentBase.name",

    (software.ComponentBase, 'long_name'): "cim.2.software.ComponentBase.long_name",

    (software.ComponentBase, 'description'): "cim.2.software.ComponentBase.description",

    (software.ComponentBase, 'version'): "cim.2.software.ComponentBase.version",

    (software.ComponentBase, 'development_history'): "cim.2.software.ComponentBase.development_history",

    (software.ComponentBase, 'release_date'): "cim.2.software.ComponentBase.release_date",



    (software.SoftwareComponent, 'language'): "cim.2.software.SoftwareComponent.language",

    (software.SoftwareComponent, 'coupling_framework'): "cim.2.software.SoftwareComponent.coupling_framework",

    (software.SoftwareComponent, 'license'): "cim.2.software.SoftwareComponent.license",

    (software.SoftwareComponent, 'dependencies'): "cim.2.software.SoftwareComponent.dependencies",

    (software.SoftwareComponent, 'composition'): "cim.2.software.SoftwareComponent.composition",

    (software.SoftwareComponent, 'grid'): "cim.2.software.SoftwareComponent.grid",

    (software.SoftwareComponent, 'connection_points'): "cim.2.software.SoftwareComponent.connection_points",

    (software.SoftwareComponent, 'sub_components'): "cim.2.software.SoftwareComponent.sub_components",



    (software.EntryPoint, 'name'): "cim.2.software.EntryPoint.name",



    (software.Composition, 'couplings'): "cim.2.software.Composition.couplings",

    (software.Composition, 'description'): "cim.2.software.Composition.description",





    (science.ScienceContext, 'context'): "cim.2.science.ScienceContext.context",

    (science.ScienceContext, 'name'): "cim.2.science.ScienceContext.name",

    (science.ScienceContext, 'id'): "cim.2.science.ScienceContext.id",



    (science.SubProcess, 'implementation_overview'): "cim.2.science.SubProcess.implementation_overview",

    (science.SubProcess, 'references'): "cim.2.science.SubProcess.references",

    (science.SubProcess, 'properties'): "cim.2.science.SubProcess.properties",



    (science.Resolution, 'is_adaptive_grid'): "cim.2.science.Resolution.is_adaptive_grid",

    (science.Resolution, 'typical_x_degrees'): "cim.2.science.Resolution.typical_x_degrees",

    (science.Resolution, 'name'): "cim.2.science.Resolution.name",

    (science.Resolution, 'equivalent_resolution_km'): "cim.2.science.Resolution.equivalent_resolution_km",

    (science.Resolution, 'typical_y_degrees'): "cim.2.science.Resolution.typical_y_degrees",

    (science.Resolution, 'number_of_levels'): "cim.2.science.Resolution.number_of_levels",

    (science.Resolution, 'number_of_xy_gridpoints'): "cim.2.science.Resolution.number_of_xy_gridpoints",



    (science.ScientificDomain, 'name'): "cim.2.science.ScientificDomain.name",

    (science.ScientificDomain, 'references'): "cim.2.science.ScientificDomain.references",

    (science.ScientificDomain, 'id'): "cim.2.science.ScientificDomain.id",

    (science.ScientificDomain, 'differing_key_properties'): "cim.2.science.ScientificDomain.differing_key_properties",

    (science.ScientificDomain, 'realm'): "cim.2.science.ScientificDomain.realm",

    (science.ScientificDomain, 'overview'): "cim.2.science.ScientificDomain.overview",

    (science.ScientificDomain, 'meta'): "cim.2.science.ScientificDomain.meta",

    (science.ScientificDomain, 'simulates'): "cim.2.science.ScientificDomain.simulates",



    (science.Extent, 'western_boundary'): "cim.2.science.Extent.western_boundary",

    (science.Extent, 'is_global'): "cim.2.science.Extent.is_global",

    (science.Extent, 'z_units'): "cim.2.science.Extent.z_units",

    (science.Extent, 'northern_boundary'): "cim.2.science.Extent.northern_boundary",

    (science.Extent, 'eastern_boundary'): "cim.2.science.Extent.eastern_boundary",

    (science.Extent, 'top_vertical_level'): "cim.2.science.Extent.top_vertical_level",

    (science.Extent, 'region_known_as'): "cim.2.science.Extent.region_known_as",

    (science.Extent, 'southern_boundary'): "cim.2.science.Extent.southern_boundary",

    (science.Extent, 'bottom_vertical_level'): "cim.2.science.Extent.bottom_vertical_level",



    (science.Model, 'model_default_properties'): "cim.2.science.Model.model_default_properties",

    (science.Model, 'id'): "cim.2.science.Model.id",

    (science.Model, 'internal_software_components'): "cim.2.science.Model.internal_software_components",

    (science.Model, 'category'): "cim.2.science.Model.category",

    (science.Model, 'simulates'): "cim.2.science.Model.simulates",

    (science.Model, 'meta'): "cim.2.science.Model.meta",

    (science.Model, 'coupler'): "cim.2.science.Model.coupler",

    (science.Model, 'coupled_components'): "cim.2.science.Model.coupled_components",



    (science.Tuning, 'regional_metrics_used'): "cim.2.science.Tuning.regional_metrics_used",

    (science.Tuning, 'trend_metrics_used'): "cim.2.science.Tuning.trend_metrics_used",

    (science.Tuning, 'description'): "cim.2.science.Tuning.description",

    (science.Tuning, 'global_mean_metrics_used'): "cim.2.science.Tuning.global_mean_metrics_used",



    (science.Process, 'references'): "cim.2.science.Process.references",

    (science.Process, 'sub_processes'): "cim.2.science.Process.sub_processes",

    (science.Process, 'implementation_overview'): "cim.2.science.Process.implementation_overview",

    (science.Process, 'keywords'): "cim.2.science.Process.keywords",

    (science.Process, 'properties'): "cim.2.science.Process.properties",

    (science.Process, 'algorithms'): "cim.2.science.Process.algorithms",



    (science.Detail, 'from_vocab'): "cim.2.science.Detail.from_vocab",

    (science.Detail, 'with_cardinality'): "cim.2.science.Detail.with_cardinality",

    (science.Detail, 'select'): "cim.2.science.Detail.select",

    (science.Detail, 'content'): "cim.2.science.Detail.content",

    (science.Detail, 'detail_selection'): "cim.2.science.Detail.detail_selection",



    (science.Algorithm, 'diagnostic_variables'): "cim.2.science.Algorithm.diagnostic_variables",

    (science.Algorithm, 'prognostic_variables'): "cim.2.science.Algorithm.prognostic_variables",

    (science.Algorithm, 'references'): "cim.2.science.Algorithm.references",

    (science.Algorithm, 'implementation_overview'): "cim.2.science.Algorithm.implementation_overview",

    (science.Algorithm, 'forced_variables'): "cim.2.science.Algorithm.forced_variables",



    (science.Grid, 'name'): "cim.2.science.Grid.name",

    (science.Grid, 'horizontal_grid_layout'): "cim.2.science.Grid.horizontal_grid_layout",

    (science.Grid, 'vertical_grid_type'): "cim.2.science.Grid.vertical_grid_type",

    (science.Grid, 'meta'): "cim.2.science.Grid.meta",

    (science.Grid, 'horizontal_grid_type'): "cim.2.science.Grid.horizontal_grid_type",

    (science.Grid, 'additional_details'): "cim.2.science.Grid.additional_details",

    (science.Grid, 'vertical_grid_layout'): "cim.2.science.Grid.vertical_grid_layout",

    (science.Grid, 'grid_extent'): "cim.2.science.Grid.grid_extent",



    (science.KeyProperties, 'time_step'): "cim.2.science.KeyProperties.time_step",

    (science.KeyProperties, 'extra_conservation_properties'): "cim.2.science.KeyProperties.extra_conservation_properties",

    (science.KeyProperties, 'tuning_applied'): "cim.2.science.KeyProperties.tuning_applied",

    (science.KeyProperties, 'grid'): "cim.2.science.KeyProperties.grid",

    (science.KeyProperties, 'resolution'): "cim.2.science.KeyProperties.resolution",

    (science.KeyProperties, 'additional_detail'): "cim.2.science.KeyProperties.additional_detail",



    (science.ConservationProperties, 'corrected_conserved_prognostic_variables'): "cim.2.science.ConservationProperties.corrected_conserved_prognostic_variables",

    (science.ConservationProperties, 'flux_correction_was_used'): "cim.2.science.ConservationProperties.flux_correction_was_used",

    (science.ConservationProperties, 'correction_methodology'): "cim.2.science.ConservationProperties.correction_methodology",





    (shared.DatetimeSet, 'length'): "cim.2.shared.DatetimeSet.length",



    (shared.ExternalDocument, 'authorship'): "cim.2.shared.ExternalDocument.authorship",

    (shared.ExternalDocument, 'date'): "cim.2.shared.ExternalDocument.date",

    (shared.ExternalDocument, 'name'): "cim.2.shared.ExternalDocument.name",

    (shared.ExternalDocument, 'publication_detail'): "cim.2.shared.ExternalDocument.publication_detail",

    (shared.ExternalDocument, 'meta'): "cim.2.shared.ExternalDocument.meta",

    (shared.ExternalDocument, 'online_at'): "cim.2.shared.ExternalDocument.online_at",

    (shared.ExternalDocument, 'title'): "cim.2.shared.ExternalDocument.title",

    (shared.ExternalDocument, 'doi'): "cim.2.shared.ExternalDocument.doi",



    (shared.DocMetaInfo, 'drs_path'): "cim.2.shared.DocMetaInfo.drs_path",

    (shared.DocMetaInfo, 'sort_key'): "cim.2.shared.DocMetaInfo.sort_key",

    (shared.DocMetaInfo, 'create_date'): "cim.2.shared.DocMetaInfo.create_date",

    (shared.DocMetaInfo, 'author'): "cim.2.shared.DocMetaInfo.author",

    (shared.DocMetaInfo, 'source_key'): "cim.2.shared.DocMetaInfo.source_key",

    (shared.DocMetaInfo, 'update_date'): "cim.2.shared.DocMetaInfo.update_date",

    (shared.DocMetaInfo, 'project'): "cim.2.shared.DocMetaInfo.project",

    (shared.DocMetaInfo, 'type_sort_key'): "cim.2.shared.DocMetaInfo.type_sort_key",

    (shared.DocMetaInfo, 'id'): "cim.2.shared.DocMetaInfo.id",

    (shared.DocMetaInfo, 'source'): "cim.2.shared.DocMetaInfo.source",

    (shared.DocMetaInfo, 'external_ids'): "cim.2.shared.DocMetaInfo.external_ids",

    (shared.DocMetaInfo, 'institute'): "cim.2.shared.DocMetaInfo.institute",

    (shared.DocMetaInfo, 'drs_keys'): "cim.2.shared.DocMetaInfo.drs_keys",

    (shared.DocMetaInfo, 'type'): "cim.2.shared.DocMetaInfo.type",

    (shared.DocMetaInfo, 'version'): "cim.2.shared.DocMetaInfo.version",

    (shared.DocMetaInfo, 'language'): "cim.2.shared.DocMetaInfo.language",

    (shared.DocMetaInfo, 'type_display_name'): "cim.2.shared.DocMetaInfo.type_display_name",



    (shared.DateTime, 'offset'): "cim.2.shared.DateTime.offset",

    (shared.DateTime, 'value'): "cim.2.shared.DateTime.value",



    (shared.Responsibility, 'when'): "cim.2.shared.Responsibility.when",

    (shared.Responsibility, 'party'): "cim.2.shared.Responsibility.party",

    (shared.Responsibility, 'role'): "cim.2.shared.Responsibility.role",



    (shared.RegularTimeset, 'start_date'): "cim.2.shared.RegularTimeset.start_date",

    (shared.RegularTimeset, 'increment'): "cim.2.shared.RegularTimeset.increment",

    (shared.RegularTimeset, 'length'): "cim.2.shared.RegularTimeset.length",



    (shared.Pid, 'id'): "cim.2.shared.Pid.id",

    (shared.Pid, 'resolution_service'): "cim.2.shared.Pid.resolution_service",



    (shared.OnlineResource, 'description'): "cim.2.shared.OnlineResource.description",

    (shared.OnlineResource, 'name'): "cim.2.shared.OnlineResource.name",

    (shared.OnlineResource, 'protocol'): "cim.2.shared.OnlineResource.protocol",

    (shared.OnlineResource, 'linkage'): "cim.2.shared.OnlineResource.linkage",



    (shared.NumberArray, 'values'): "cim.2.shared.NumberArray.values",



    (shared.QualityReview, 'quality_status'): "cim.2.shared.QualityReview.quality_status",

    (shared.QualityReview, 'date'): "cim.2.shared.QualityReview.date",

    (shared.QualityReview, 'quality_description'): "cim.2.shared.QualityReview.quality_description",

    (shared.QualityReview, 'metadata_reviewer'): "cim.2.shared.QualityReview.metadata_reviewer",



    (shared.DocReference, 'id'): "cim.2.shared.DocReference.id",

    (shared.DocReference, 'relationship'): "cim.2.shared.DocReference.relationship",

    (shared.DocReference, 'context'): "cim.2.shared.DocReference.context",

    (shared.DocReference, 'type'): "cim.2.shared.DocReference.type",

    (shared.DocReference, 'version'): "cim.2.shared.DocReference.version",

    (shared.DocReference, 'constraint_vocabulary'): "cim.2.shared.DocReference.constraint_vocabulary",



    (shared.IrregularDateset, 'date_set'): "cim.2.shared.IrregularDateset.date_set",



    (shared.Party, 'organisation'): "cim.2.shared.Party.organisation",

    (shared.Party, 'meta'): "cim.2.shared.Party.meta",

    (shared.Party, 'name'): "cim.2.shared.Party.name",

    (shared.Party, 'address'): "cim.2.shared.Party.address",

    (shared.Party, 'url'): "cim.2.shared.Party.url",

    (shared.Party, 'orcid_id'): "cim.2.shared.Party.orcid_id",

    (shared.Party, 'email'): "cim.2.shared.Party.email",



    (shared.Reference, 'context'): "cim.2.shared.Reference.context",

    (shared.Reference, 'document'): "cim.2.shared.Reference.document",



    (shared.TimesliceList, 'members'): "cim.2.shared.TimesliceList.members",

    (shared.TimesliceList, 'units'): "cim.2.shared.TimesliceList.units",



    (shared.TimePeriod, 'length'): "cim.2.shared.TimePeriod.length",

    (shared.TimePeriod, 'units'): "cim.2.shared.TimePeriod.units",

    (shared.TimePeriod, 'calendar'): "cim.2.shared.TimePeriod.calendar",

    (shared.TimePeriod, 'date_type'): "cim.2.shared.TimePeriod.date_type",

    (shared.TimePeriod, 'date'): "cim.2.shared.TimePeriod.date",



    (shared.Calendar, 'standard_name'): "cim.2.shared.Calendar.standard_name",

    (shared.Calendar, 'description'): "cim.2.shared.Calendar.description",

    (shared.Calendar, 'name'): "cim.2.shared.Calendar.name",

    (shared.Calendar, 'month_lengths'): "cim.2.shared.Calendar.month_lengths",



    (shared.Cimtext, 'content'): "cim.2.shared.Cimtext.content",

    (shared.Cimtext, 'content_type'): "cim.2.shared.Cimtext.content_type",



    (shared.KeyFloat, 'key'): "cim.2.shared.KeyFloat.key",

    (shared.KeyFloat, 'value'): "cim.2.shared.KeyFloat.value",



    # ------------------------------------------------
    # Enums.
    # ------------------------------------------------


    designing.ExperimentalRelationships: "cim.2.designing.ExperimentalRelationships",

    designing.EnsembleTypes: "cim.2.designing.EnsembleTypes",

    designing.ForcingTypes: "cim.2.designing.ForcingTypes",



    data.DataAssociationTypes: "cim.2.data.DataAssociationTypes",



    platform.StorageSystems: "cim.2.platform.StorageSystems",

    platform.VolumeUnits: "cim.2.platform.VolumeUnits",



    drs.DrsFrequencyTypes: "cim.2.drs.DrsFrequencyTypes",

    drs.DrsTimeSuffixes: "cim.2.drs.DrsTimeSuffixes",

    drs.DrsGeographicalOperators: "cim.2.drs.DrsGeographicalOperators",

    drs.DrsRealms: "cim.2.drs.DrsRealms",



    activity.EnsembleTypes: "cim.2.activity.EnsembleTypes",

    activity.ForcingTypes: "cim.2.activity.ForcingTypes",



    software.ProgrammingLanguage: "cim.2.software.ProgrammingLanguage",

    software.CouplingFramework: "cim.2.software.CouplingFramework",



    science.ModelTypes: "cim.2.science.ModelTypes",

    science.SelectionCardinality: "cim.2.science.SelectionCardinality",



    shared.PeriodDateTypes: "cim.2.shared.PeriodDateTypes",

    shared.NilReason: "cim.2.shared.NilReason",

    shared.SlicetimeUnits: "cim.2.shared.SlicetimeUnits",

    shared.TimeUnits: "cim.2.shared.TimeUnits",

    shared.DocumentTypes: "cim.2.shared.DocumentTypes",

    shared.CalendarTypes: "cim.2.shared.CalendarTypes",

    shared.RoleCode: "cim.2.shared.RoleCode",

    shared.TextCode: "cim.2.shared.TextCode",

    shared.QualityStatus: "cim.2.shared.QualityStatus",


    # ------------------------------------------------
    # Enum members.
    # ------------------------------------------------



    (designing.ExperimentalRelationships, 'initialisation_for'): "cim.2.designing.ExperimentalRelationships.initialisation_for",

    (designing.ExperimentalRelationships, 'provides_constraints'): "cim.2.designing.ExperimentalRelationships.provides_constraints",

    (designing.ExperimentalRelationships, 'control_for'): "cim.2.designing.ExperimentalRelationships.control_for",

    (designing.ExperimentalRelationships, 'is_sibling'): "cim.2.designing.ExperimentalRelationships.is_sibling",



    (designing.EnsembleTypes, 'Forced'): "cim.2.designing.EnsembleTypes.Forced",

    (designing.EnsembleTypes, 'Resolution'): "cim.2.designing.EnsembleTypes.Resolution",

    (designing.EnsembleTypes, 'Perturbed Physics'): "cim.2.designing.EnsembleTypes.Perturbed-Physics",

    (designing.EnsembleTypes, 'Initialisation Method'): "cim.2.designing.EnsembleTypes.Initialisation-Method",

    (designing.EnsembleTypes, 'Initialisation'): "cim.2.designing.EnsembleTypes.Initialisation",

    (designing.EnsembleTypes, 'Staggered Start'): "cim.2.designing.EnsembleTypes.Staggered-Start",



    (designing.ForcingTypes, 'scenario'): "cim.2.designing.ForcingTypes.scenario",

    (designing.ForcingTypes, 'historical'): "cim.2.designing.ForcingTypes.historical",

    (designing.ForcingTypes, 'another simulation'): "cim.2.designing.ForcingTypes.another-simulation",

    (designing.ForcingTypes, 'idealised'): "cim.2.designing.ForcingTypes.idealised",





    (data.DataAssociationTypes, 'partOf'): "cim.2.data.DataAssociationTypes.partOf",

    (data.DataAssociationTypes, 'isComposedOf'): "cim.2.data.DataAssociationTypes.isComposedOf",

    (data.DataAssociationTypes, 'revisonOf'): "cim.2.data.DataAssociationTypes.revisonOf",





    (platform.StorageSystems, 'Unknown'): "cim.2.platform.StorageSystems.Unknown",

    (platform.StorageSystems, 'NFS'): "cim.2.platform.StorageSystems.NFS",

    (platform.StorageSystems, 'isilon'): "cim.2.platform.StorageSystems.isilon",

    (platform.StorageSystems, 'Panasas'): "cim.2.platform.StorageSystems.Panasas",

    (platform.StorageSystems, 'Other Disk'): "cim.2.platform.StorageSystems.Other-Disk",

    (platform.StorageSystems, 'Tape - Other'): "cim.2.platform.StorageSystems.Tape---Other",

    (platform.StorageSystems, 'Tape - MARS'): "cim.2.platform.StorageSystems.Tape---MARS",

    (platform.StorageSystems, 'Tape - MASS'): "cim.2.platform.StorageSystems.Tape---MASS",

    (platform.StorageSystems, 'Tape - Castor'): "cim.2.platform.StorageSystems.Tape---Castor",

    (platform.StorageSystems, 'Lustre'): "cim.2.platform.StorageSystems.Lustre",

    (platform.StorageSystems, 'GPFS'): "cim.2.platform.StorageSystems.GPFS",



    (platform.VolumeUnits, 'PB'): "cim.2.platform.VolumeUnits.PB",

    (platform.VolumeUnits, 'EB'): "cim.2.platform.VolumeUnits.EB",

    (platform.VolumeUnits, 'TiB'): "cim.2.platform.VolumeUnits.TiB",

    (platform.VolumeUnits, 'PiB'): "cim.2.platform.VolumeUnits.PiB",

    (platform.VolumeUnits, 'EiB'): "cim.2.platform.VolumeUnits.EiB",

    (platform.VolumeUnits, 'GB'): "cim.2.platform.VolumeUnits.GB",

    (platform.VolumeUnits, 'TB'): "cim.2.platform.VolumeUnits.TB",





    (drs.DrsFrequencyTypes, 'mon'): "cim.2.drs.DrsFrequencyTypes.mon",

    (drs.DrsFrequencyTypes, 'day'): "cim.2.drs.DrsFrequencyTypes.day",

    (drs.DrsFrequencyTypes, '6hr'): "cim.2.drs.DrsFrequencyTypes.6hr",

    (drs.DrsFrequencyTypes, '3hr'): "cim.2.drs.DrsFrequencyTypes.3hr",

    (drs.DrsFrequencyTypes, 'subhr'): "cim.2.drs.DrsFrequencyTypes.subhr",

    (drs.DrsFrequencyTypes, 'monClim'): "cim.2.drs.DrsFrequencyTypes.monClim",

    (drs.DrsFrequencyTypes, 'fx'): "cim.2.drs.DrsFrequencyTypes.fx",

    (drs.DrsFrequencyTypes, 'yr'): "cim.2.drs.DrsFrequencyTypes.yr",



    (drs.DrsTimeSuffixes, 'clim'): "cim.2.drs.DrsTimeSuffixes.clim",

    (drs.DrsTimeSuffixes, 'avg'): "cim.2.drs.DrsTimeSuffixes.avg",



    (drs.DrsGeographicalOperators, 'lnd-areaavg'): "cim.2.drs.DrsGeographicalOperators.lnd-areaavg",

    (drs.DrsGeographicalOperators, 'ocn-areaavg'): "cim.2.drs.DrsGeographicalOperators.ocn-areaavg",

    (drs.DrsGeographicalOperators, 'zonalavg'): "cim.2.drs.DrsGeographicalOperators.zonalavg",

    (drs.DrsGeographicalOperators, 'lnd-zonalavg'): "cim.2.drs.DrsGeographicalOperators.lnd-zonalavg",

    (drs.DrsGeographicalOperators, 'ocn-zonalavg'): "cim.2.drs.DrsGeographicalOperators.ocn-zonalavg",

    (drs.DrsGeographicalOperators, 'areaavg'): "cim.2.drs.DrsGeographicalOperators.areaavg",



    (drs.DrsRealms, 'land'): "cim.2.drs.DrsRealms.land",

    (drs.DrsRealms, 'landIce'): "cim.2.drs.DrsRealms.landIce",

    (drs.DrsRealms, 'seaIce'): "cim.2.drs.DrsRealms.seaIce",

    (drs.DrsRealms, 'aerosol'): "cim.2.drs.DrsRealms.aerosol",

    (drs.DrsRealms, 'atmosChem'): "cim.2.drs.DrsRealms.atmosChem",

    (drs.DrsRealms, 'ocnBgchem'): "cim.2.drs.DrsRealms.ocnBgchem",

    (drs.DrsRealms, 'atmos'): "cim.2.drs.DrsRealms.atmos",

    (drs.DrsRealms, 'ocean'): "cim.2.drs.DrsRealms.ocean",





    (activity.EnsembleTypes, 'Staggered Start'): "cim.2.activity.EnsembleTypes.Staggered-Start",

    (activity.EnsembleTypes, 'Forced'): "cim.2.activity.EnsembleTypes.Forced",

    (activity.EnsembleTypes, 'Resolution'): "cim.2.activity.EnsembleTypes.Resolution",

    (activity.EnsembleTypes, 'Perturbed Physics'): "cim.2.activity.EnsembleTypes.Perturbed-Physics",

    (activity.EnsembleTypes, 'Initialisation Method'): "cim.2.activity.EnsembleTypes.Initialisation-Method",

    (activity.EnsembleTypes, 'Initialisation'): "cim.2.activity.EnsembleTypes.Initialisation",



    (activity.ForcingTypes, 'historical'): "cim.2.activity.ForcingTypes.historical",

    (activity.ForcingTypes, 'scenario'): "cim.2.activity.ForcingTypes.scenario",

    (activity.ForcingTypes, 'another simulation'): "cim.2.activity.ForcingTypes.another-simulation",

    (activity.ForcingTypes, 'idealised'): "cim.2.activity.ForcingTypes.idealised",





    (software.ProgrammingLanguage, 'C'): "cim.2.software.ProgrammingLanguage.C",

    (software.ProgrammingLanguage, 'C++'): "cim.2.software.ProgrammingLanguage.C++",

    (software.ProgrammingLanguage, 'Python'): "cim.2.software.ProgrammingLanguage.Python",

    (software.ProgrammingLanguage, 'Fortran'): "cim.2.software.ProgrammingLanguage.Fortran",



    (software.CouplingFramework, 'Bespoke'): "cim.2.software.CouplingFramework.Bespoke",

    (software.CouplingFramework, 'Unknown'): "cim.2.software.CouplingFramework.Unknown",

    (software.CouplingFramework, 'None'): "cim.2.software.CouplingFramework.None",

    (software.CouplingFramework, 'OASIS'): "cim.2.software.CouplingFramework.OASIS",

    (software.CouplingFramework, 'OASIS3-MCT'): "cim.2.software.CouplingFramework.OASIS3-MCT",

    (software.CouplingFramework, 'ESMF'): "cim.2.software.CouplingFramework.ESMF",

    (software.CouplingFramework, 'NUOPC'): "cim.2.software.CouplingFramework.NUOPC",





    (science.ModelTypes, 'Process'): "cim.2.science.ModelTypes.Process",

    (science.ModelTypes, 'Atm Only'): "cim.2.science.ModelTypes.Atm-Only",

    (science.ModelTypes, 'Ocean Only'): "cim.2.science.ModelTypes.Ocean-Only",

    (science.ModelTypes, 'Regional'): "cim.2.science.ModelTypes.Regional",

    (science.ModelTypes, 'GCM'): "cim.2.science.ModelTypes.GCM",

    (science.ModelTypes, 'IGCM'): "cim.2.science.ModelTypes.IGCM",

    (science.ModelTypes, 'GCM-MLO'): "cim.2.science.ModelTypes.GCM-MLO",

    (science.ModelTypes, 'Mesoscale'): "cim.2.science.ModelTypes.Mesoscale",

    (science.ModelTypes, 'Planetary'): "cim.2.science.ModelTypes.Planetary",



    (science.SelectionCardinality, '1.N'): "cim.2.science.SelectionCardinality.1.N",

    (science.SelectionCardinality, '0.N'): "cim.2.science.SelectionCardinality.0.N",

    (science.SelectionCardinality, '0.1'): "cim.2.science.SelectionCardinality.0.1",

    (science.SelectionCardinality, '1.1'): "cim.2.science.SelectionCardinality.1.1",





    (shared.PeriodDateTypes, 'date is start'): "cim.2.shared.PeriodDateTypes.date-is-start",

    (shared.PeriodDateTypes, 'date is end'): "cim.2.shared.PeriodDateTypes.date-is-end",

    (shared.PeriodDateTypes, 'unused'): "cim.2.shared.PeriodDateTypes.unused",



    (shared.NilReason, 'nil:withheld'): "cim.2.shared.NilReason.nil:withheld",

    (shared.NilReason, 'nil:inapplicable'): "cim.2.shared.NilReason.nil:inapplicable",

    (shared.NilReason, 'nil:unknown'): "cim.2.shared.NilReason.nil:unknown",

    (shared.NilReason, 'nil:missing'): "cim.2.shared.NilReason.nil:missing",

    (shared.NilReason, 'nil:template'): "cim.2.shared.NilReason.nil:template",



    (shared.SlicetimeUnits, 'monthly'): "cim.2.shared.SlicetimeUnits.monthly",

    (shared.SlicetimeUnits, 'yearly'): "cim.2.shared.SlicetimeUnits.yearly",



    (shared.TimeUnits, 'years'): "cim.2.shared.TimeUnits.years",

    (shared.TimeUnits, 'months'): "cim.2.shared.TimeUnits.months",

    (shared.TimeUnits, 'days'): "cim.2.shared.TimeUnits.days",

    (shared.TimeUnits, 'seconds'): "cim.2.shared.TimeUnits.seconds",



    (shared.DocumentTypes, 'Grid'): "cim.2.shared.DocumentTypes.Grid",

    (shared.DocumentTypes, 'Machine'): "cim.2.shared.DocumentTypes.Machine",

    (shared.DocumentTypes, 'Model'): "cim.2.shared.DocumentTypes.Model",

    (shared.DocumentTypes, 'MultiEnsemble'): "cim.2.shared.DocumentTypes.MultiEnsemble",

    (shared.DocumentTypes, 'MultiTimeEnsemble'): "cim.2.shared.DocumentTypes.MultiTimeEnsemble",

    (shared.DocumentTypes, 'NumericalExperiment'): "cim.2.shared.DocumentTypes.NumericalExperiment",

    (shared.DocumentTypes, 'NumericalRequirement'): "cim.2.shared.DocumentTypes.NumericalRequirement",

    (shared.DocumentTypes, 'OutputTemporalRequirement'): "cim.2.shared.DocumentTypes.OutputTemporalRequirement",

    (shared.DocumentTypes, 'Party'): "cim.2.shared.DocumentTypes.Party",

    (shared.DocumentTypes, 'Performance'): "cim.2.shared.DocumentTypes.Performance",

    (shared.DocumentTypes, 'Project'): "cim.2.shared.DocumentTypes.Project",

    (shared.DocumentTypes, 'ScientificDomain'): "cim.2.shared.DocumentTypes.ScientificDomain",

    (shared.DocumentTypes, 'Simulation'): "cim.2.shared.DocumentTypes.Simulation",

    (shared.DocumentTypes, 'SimulationPlan'): "cim.2.shared.DocumentTypes.SimulationPlan",

    (shared.DocumentTypes, 'TemporalConstraint'): "cim.2.shared.DocumentTypes.TemporalConstraint",

    (shared.DocumentTypes, 'UberEnsemble'): "cim.2.shared.DocumentTypes.UberEnsemble",

    (shared.DocumentTypes, 'Conformance'): "cim.2.shared.DocumentTypes.Conformance",

    (shared.DocumentTypes, 'Dataset'): "cim.2.shared.DocumentTypes.Dataset",

    (shared.DocumentTypes, 'DomainProperties'): "cim.2.shared.DocumentTypes.DomainProperties",

    (shared.DocumentTypes, 'Downscaling'): "cim.2.shared.DocumentTypes.Downscaling",

    (shared.DocumentTypes, 'Ensemble'): "cim.2.shared.DocumentTypes.Ensemble",

    (shared.DocumentTypes, 'EnsembleRequirement'): "cim.2.shared.DocumentTypes.EnsembleRequirement",

    (shared.DocumentTypes, 'ExternalDocument'): "cim.2.shared.DocumentTypes.ExternalDocument",

    (shared.DocumentTypes, 'ForcingConstraint'): "cim.2.shared.DocumentTypes.ForcingConstraint",



    (shared.CalendarTypes, 'noleap'): "cim.2.shared.CalendarTypes.noleap",

    (shared.CalendarTypes, '365_day'): "cim.2.shared.CalendarTypes.365_day",

    (shared.CalendarTypes, 'all_leap'): "cim.2.shared.CalendarTypes.all_leap",

    (shared.CalendarTypes, '366_day'): "cim.2.shared.CalendarTypes.366_day",

    (shared.CalendarTypes, '360_day'): "cim.2.shared.CalendarTypes.360_day",

    (shared.CalendarTypes, 'julian'): "cim.2.shared.CalendarTypes.julian",

    (shared.CalendarTypes, 'standard'): "cim.2.shared.CalendarTypes.standard",

    (shared.CalendarTypes, 'none'): "cim.2.shared.CalendarTypes.none",

    (shared.CalendarTypes, 'proleptic_gregorian'): "cim.2.shared.CalendarTypes.proleptic_gregorian",

    (shared.CalendarTypes, 'gregorian'): "cim.2.shared.CalendarTypes.gregorian",



    (shared.RoleCode, 'user'): "cim.2.shared.RoleCode.user",

    (shared.RoleCode, 'sponsor'): "cim.2.shared.RoleCode.sponsor",

    (shared.RoleCode, 'author'): "cim.2.shared.RoleCode.author",

    (shared.RoleCode, 'owner'): "cim.2.shared.RoleCode.owner",

    (shared.RoleCode, 'collaborator'): "cim.2.shared.RoleCode.collaborator",

    (shared.RoleCode, 'custodian'): "cim.2.shared.RoleCode.custodian",

    (shared.RoleCode, 'publisher'): "cim.2.shared.RoleCode.publisher",

    (shared.RoleCode, 'metadata_reviewer'): "cim.2.shared.RoleCode.metadata_reviewer",

    (shared.RoleCode, 'resource provider'): "cim.2.shared.RoleCode.resource-provider",

    (shared.RoleCode, 'processor'): "cim.2.shared.RoleCode.processor",

    (shared.RoleCode, 'metadata_author'): "cim.2.shared.RoleCode.metadata_author",

    (shared.RoleCode, 'distributor'): "cim.2.shared.RoleCode.distributor",

    (shared.RoleCode, 'Principal Investigator'): "cim.2.shared.RoleCode.Principal-Investigator",

    (shared.RoleCode, 'originator'): "cim.2.shared.RoleCode.originator",

    (shared.RoleCode, 'point of contact'): "cim.2.shared.RoleCode.point-of-contact",



    (shared.TextCode, 'plaintext'): "cim.2.shared.TextCode.plaintext",



    (shared.QualityStatus, 'incomplete'): "cim.2.shared.QualityStatus.incomplete",

    (shared.QualityStatus, 'finalised'): "cim.2.shared.QualityStatus.finalised",

    (shared.QualityStatus, 'under_review'): "cim.2.shared.QualityStatus.under_review",

    (shared.QualityStatus, 'reviewed'): "cim.2.shared.QualityStatus.reviewed",



}