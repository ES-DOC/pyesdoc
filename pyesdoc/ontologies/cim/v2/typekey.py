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
    activity.Activity: ,
    activity.AxisMember: ,
    activity.Conformance: ,
    activity.Ensemble: ,
    activity.EnsembleAxis: ,
    activity.EnsembleMember: ,
    activity.ParentSimulation: ,
    activity.UberEnsemble: ,
    data.Dataset: ,
    data.Downscaling: ,
    data.Simulation: ,
    data.VariableCollection: ,
    designing.DomainProperties: ,
    designing.EnsembleRequirement: ,
    designing.ForcingConstraint: ,
    designing.MultiEnsemble: ,
    designing.MultiTimeEnsemble: ,
    designing.NumericalExperiment: ,
    designing.NumericalRequirement: ,
    designing.OutputTemporalRequirement: ,
    designing.Project: ,
    designing.SimulationPlan: ,
    designing.TemporalConstraint: ,
    drs.DrsAtomicDataset: ,
    drs.DrsEnsembleIdentifier: ,
    drs.DrsGeographicalIndicator: ,
    drs.DrsPublicationDataset: ,
    drs.DrsTemporalIdentifier: ,
    platform.ComponentPerformance: ,
    platform.ComputePool: ,
    platform.Machine: ,
    platform.Partition: ,
    platform.Performance: ,
    platform.StoragePool: ,
    platform.StorageVolume: ,
    science.Algorithm: ,
    science.ConservationProperties: ,
    science.Detail: ,
    science.Extent: ,
    science.Grid: ,
    science.KeyProperties: ,
    science.Model: ,
    science.Process: ,
    science.Resolution: ,
    science.ScienceContext: ,
    science.ScientificDomain: ,
    science.SubProcess: ,
    science.Tuning: ,
    shared.Calendar: ,
    shared.Cimtext: ,
    shared.DateTime: ,
    shared.DatetimeSet: ,
    shared.DocMetaInfo: ,
    shared.DocReference: ,
    shared.ExternalDocument: ,
    shared.IrregularDateset: ,
    shared.KeyFloat: ,
    shared.NumberArray: ,
    shared.OnlineResource: ,
    shared.Party: ,
    shared.Pid: ,
    shared.QualityReview: ,
    shared.Reference: ,
    shared.RegularTimeset: ,
    shared.Responsibility: ,
    shared.TimePeriod: ,
    shared.TimesliceList: ,
    software.ComponentBase: ,
    software.Composition: ,
    software.DevelopmentPath: ,
    software.EntryPoint: ,
    software.Gridspec: ,
    software.SoftwareComponent: ,
    software.Variable: ,

}