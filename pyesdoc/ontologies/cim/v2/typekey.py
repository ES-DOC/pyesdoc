# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typekey.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of constraints over the cim.v2.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_designing_package as designing
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform
import typeset_for_science_package as science
import typeset_for_shared_package as shared
import typeset_for_software_package as software



# Map of ontology types to type keys.
TYPE_KEYS = {
    activity.Activity: 'cim.2.activity.Activity',
    activity.AxisMember: 'cim.2.activity.AxisMember',
    activity.Conformance: 'cim.2.activity.Conformance',
    activity.Ensemble: 'cim.2.activity.Ensemble',
    activity.EnsembleAxis: 'cim.2.activity.EnsembleAxis',
    activity.EnsembleMember: 'cim.2.activity.EnsembleMember',
    activity.ParentSimulation: 'cim.2.activity.ParentSimulation',
    activity.UberEnsemble: 'cim.2.activity.UberEnsemble',
    data.Dataset: 'cim.2.data.Dataset',
    data.Downscaling: 'cim.2.data.Downscaling',
    data.Simulation: 'cim.2.data.Simulation',
    data.VariableCollection: 'cim.2.data.VariableCollection',
    designing.DomainProperties: 'cim.2.designing.DomainProperties',
    designing.EnsembleRequirement: 'cim.2.designing.EnsembleRequirement',
    designing.ForcingConstraint: 'cim.2.designing.ForcingConstraint',
    designing.MultiEnsemble: 'cim.2.designing.MultiEnsemble',
    designing.MultiTimeEnsemble: 'cim.2.designing.MultiTimeEnsemble',
    designing.NumericalExperiment: 'cim.2.designing.NumericalExperiment',
    designing.NumericalRequirement: 'cim.2.designing.NumericalRequirement',
    designing.OutputTemporalRequirement: 'cim.2.designing.OutputTemporalRequirement',
    designing.Project: 'cim.2.designing.Project',
    designing.SimulationPlan: 'cim.2.designing.SimulationPlan',
    designing.TemporalConstraint: 'cim.2.designing.TemporalConstraint',
    drs.DrsAtomicDataset: 'cim.2.drs.DrsAtomicDataset',
    drs.DrsEnsembleIdentifier: 'cim.2.drs.DrsEnsembleIdentifier',
    drs.DrsGeographicalIndicator: 'cim.2.drs.DrsGeographicalIndicator',
    drs.DrsPublicationDataset: 'cim.2.drs.DrsPublicationDataset',
    drs.DrsTemporalIdentifier: 'cim.2.drs.DrsTemporalIdentifier',
    platform.ComponentPerformance: 'cim.2.platform.ComponentPerformance',
    platform.ComputePool: 'cim.2.platform.ComputePool',
    platform.Machine: 'cim.2.platform.Machine',
    platform.Partition: 'cim.2.platform.Partition',
    platform.Performance: 'cim.2.platform.Performance',
    platform.StoragePool: 'cim.2.platform.StoragePool',
    platform.StorageVolume: 'cim.2.platform.StorageVolume',
    science.Algorithm: 'cim.2.science.Algorithm',
    science.ConservationProperties: 'cim.2.science.ConservationProperties',
    science.Detail: 'cim.2.science.Detail',
    science.Extent: 'cim.2.science.Extent',
    science.Grid: 'cim.2.science.Grid',
    science.KeyProperties: 'cim.2.science.KeyProperties',
    science.Model: 'cim.2.science.Model',
    science.Process: 'cim.2.science.Process',
    science.Resolution: 'cim.2.science.Resolution',
    science.ScienceContext: 'cim.2.science.ScienceContext',
    science.ScientificDomain: 'cim.2.science.ScientificDomain',
    science.SubProcess: 'cim.2.science.SubProcess',
    science.Tuning: 'cim.2.science.Tuning',
    shared.Calendar: 'cim.2.shared.Calendar',
    shared.Cimtext: 'cim.2.shared.Cimtext',
    shared.DateTime: 'cim.2.shared.DateTime',
    shared.DatetimeSet: 'cim.2.shared.DatetimeSet',
    shared.DocMetaInfo: 'cim.2.shared.DocMetaInfo',
    shared.DocReference: 'cim.2.shared.DocReference',
    shared.ExternalDocument: 'cim.2.shared.ExternalDocument',
    shared.IrregularDateset: 'cim.2.shared.IrregularDateset',
    shared.KeyFloat: 'cim.2.shared.KeyFloat',
    shared.NumberArray: 'cim.2.shared.NumberArray',
    shared.OnlineResource: 'cim.2.shared.OnlineResource',
    shared.Party: 'cim.2.shared.Party',
    shared.Pid: 'cim.2.shared.Pid',
    shared.QualityReview: 'cim.2.shared.QualityReview',
    shared.Reference: 'cim.2.shared.Reference',
    shared.RegularTimeset: 'cim.2.shared.RegularTimeset',
    shared.Responsibility: 'cim.2.shared.Responsibility',
    shared.TimePeriod: 'cim.2.shared.TimePeriod',
    shared.TimesliceList: 'cim.2.shared.TimesliceList',
    software.ComponentBase: 'cim.2.software.ComponentBase',
    software.Composition: 'cim.2.software.Composition',
    software.DevelopmentPath: 'cim.2.software.DevelopmentPath',
    software.EntryPoint: 'cim.2.software.EntryPoint',
    software.Gridspec: 'cim.2.software.Gridspec',
    software.SoftwareComponent: 'cim.2.software.SoftwareComponent',
    software.Variable: 'cim.2.software.Variable',

}