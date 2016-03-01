# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typekeys.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of constraints over the cim.v1.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_grids_package as grids
import typeset_for_misc_package as misc
import typeset_for_quality_package as quality
import typeset_for_shared_package as shared
import typeset_for_software_package as software



# Map of ontology types to type keys.
TYPE_KEYS = {
    activity.Activity: 'cim.1.activity.Activity',
    activity.BoundaryCondition: 'cim.1.activity.BoundaryCondition',
    activity.Conformance: 'cim.1.activity.Conformance',
    activity.DownscalingSimulation: 'cim.1.activity.DownscalingSimulation',
    activity.Ensemble: 'cim.1.activity.Ensemble',
    activity.EnsembleMember: 'cim.1.activity.EnsembleMember',
    activity.Experiment: 'cim.1.activity.Experiment',
    activity.ExperimentRelationship: 'cim.1.activity.ExperimentRelationship',
    activity.ExperimentRelationshipTarget: 'cim.1.activity.ExperimentRelationshipTarget',
    activity.InitialCondition: 'cim.1.activity.InitialCondition',
    activity.LateralBoundaryCondition: 'cim.1.activity.LateralBoundaryCondition',
    activity.MeasurementCampaign: 'cim.1.activity.MeasurementCampaign',
    activity.NumericalActivity: 'cim.1.activity.NumericalActivity',
    activity.NumericalExperiment: 'cim.1.activity.NumericalExperiment',
    activity.NumericalRequirement: 'cim.1.activity.NumericalRequirement',
    activity.NumericalRequirementOption: 'cim.1.activity.NumericalRequirementOption',
    activity.OutputRequirement: 'cim.1.activity.OutputRequirement',
    activity.PhysicalModification: 'cim.1.activity.PhysicalModification',
    activity.Simulation: 'cim.1.activity.Simulation',
    activity.SimulationComposite: 'cim.1.activity.SimulationComposite',
    activity.SimulationRelationship: 'cim.1.activity.SimulationRelationship',
    activity.SimulationRelationshipTarget: 'cim.1.activity.SimulationRelationshipTarget',
    activity.SimulationRun: 'cim.1.activity.SimulationRun',
    activity.SpatioTemporalConstraint: 'cim.1.activity.SpatioTemporalConstraint',
    data.DataContent: 'cim.1.data.DataContent',
    data.DataDistribution: 'cim.1.data.DataDistribution',
    data.DataExtent: 'cim.1.data.DataExtent',
    data.DataExtentGeographical: 'cim.1.data.DataExtentGeographical',
    data.DataExtentTemporal: 'cim.1.data.DataExtentTemporal',
    data.DataExtentTimeInterval: 'cim.1.data.DataExtentTimeInterval',
    data.DataHierarchyLevel: 'cim.1.data.DataHierarchyLevel',
    data.DataObject: 'cim.1.data.DataObject',
    data.DataProperty: 'cim.1.data.DataProperty',
    data.DataRestriction: 'cim.1.data.DataRestriction',
    data.DataStorage: 'cim.1.data.DataStorage',
    data.DataStorageDb: 'cim.1.data.DataStorageDb',
    data.DataStorageFile: 'cim.1.data.DataStorageFile',
    data.DataStorageIp: 'cim.1.data.DataStorageIp',
    data.DataTopic: 'cim.1.data.DataTopic',
    grids.CoordinateList: 'cim.1.grids.CoordinateList',
    grids.GridExtent: 'cim.1.grids.GridExtent',
    grids.GridMosaic: 'cim.1.grids.GridMosaic',
    grids.GridProperty: 'cim.1.grids.GridProperty',
    grids.GridSpec: 'cim.1.grids.GridSpec',
    grids.GridTile: 'cim.1.grids.GridTile',
    grids.GridTileResolutionType: 'cim.1.grids.GridTileResolutionType',
    grids.SimpleGridGeometry: 'cim.1.grids.SimpleGridGeometry',
    grids.VerticalCoordinateList: 'cim.1.grids.VerticalCoordinateList',
    misc.DocumentSet: 'cim.1.misc.DocumentSet',
    quality.CimQuality: 'cim.1.quality.CimQuality',
    quality.Evaluation: 'cim.1.quality.Evaluation',
    quality.Measure: 'cim.1.quality.Measure',
    quality.Report: 'cim.1.quality.Report',
    shared.Calendar: 'cim.1.shared.Calendar',
    shared.Change: 'cim.1.shared.Change',
    shared.ChangeProperty: 'cim.1.shared.ChangeProperty',
    shared.Citation: 'cim.1.shared.Citation',
    shared.ClosedDateRange: 'cim.1.shared.ClosedDateRange',
    shared.Compiler: 'cim.1.shared.Compiler',
    shared.Daily360: 'cim.1.shared.Daily360',
    shared.DataSource: 'cim.1.shared.DataSource',
    shared.DateRange: 'cim.1.shared.DateRange',
    shared.DocGenealogy: 'cim.1.shared.DocGenealogy',
    shared.DocMetaInfo: 'cim.1.shared.DocMetaInfo',
    shared.DocReference: 'cim.1.shared.DocReference',
    shared.DocRelationship: 'cim.1.shared.DocRelationship',
    shared.DocRelationshipTarget: 'cim.1.shared.DocRelationshipTarget',
    shared.License: 'cim.1.shared.License',
    shared.Machine: 'cim.1.shared.Machine',
    shared.MachineCompilerUnit: 'cim.1.shared.MachineCompilerUnit',
    shared.OpenDateRange: 'cim.1.shared.OpenDateRange',
    shared.PerpetualPeriod: 'cim.1.shared.PerpetualPeriod',
    shared.Platform: 'cim.1.shared.Platform',
    shared.Property: 'cim.1.shared.Property',
    shared.RealCalendar: 'cim.1.shared.RealCalendar',
    shared.Relationship: 'cim.1.shared.Relationship',
    shared.ResponsibleParty: 'cim.1.shared.ResponsibleParty',
    shared.Standard: 'cim.1.shared.Standard',
    shared.StandardName: 'cim.1.shared.StandardName',
    software.Component: 'cim.1.software.Component',
    software.ComponentLanguage: 'cim.1.software.ComponentLanguage',
    software.ComponentLanguageProperty: 'cim.1.software.ComponentLanguageProperty',
    software.ComponentProperty: 'cim.1.software.ComponentProperty',
    software.Composition: 'cim.1.software.Composition',
    software.Connection: 'cim.1.software.Connection',
    software.ConnectionEndpoint: 'cim.1.software.ConnectionEndpoint',
    software.ConnectionProperty: 'cim.1.software.ConnectionProperty',
    software.Coupling: 'cim.1.software.Coupling',
    software.CouplingEndpoint: 'cim.1.software.CouplingEndpoint',
    software.CouplingProperty: 'cim.1.software.CouplingProperty',
    software.Deployment: 'cim.1.software.Deployment',
    software.EntryPoint: 'cim.1.software.EntryPoint',
    software.ModelComponent: 'cim.1.software.ModelComponent',
    software.Parallelisation: 'cim.1.software.Parallelisation',
    software.ProcessorComponent: 'cim.1.software.ProcessorComponent',
    software.Rank: 'cim.1.software.Rank',
    software.SpatialRegridding: 'cim.1.software.SpatialRegridding',
    software.SpatialRegriddingProperty: 'cim.1.software.SpatialRegriddingProperty',
    software.SpatialRegriddingUserMethod: 'cim.1.software.SpatialRegriddingUserMethod',
    software.StatisticalModelComponent: 'cim.1.software.StatisticalModelComponent',
    software.TimeLag: 'cim.1.software.TimeLag',
    software.TimeTransformation: 'cim.1.software.TimeTransformation',
    software.Timing: 'cim.1.software.Timing',

}