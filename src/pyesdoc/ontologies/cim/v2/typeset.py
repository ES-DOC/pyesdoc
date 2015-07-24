# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
from typeset_for_data_package import *
from typeset_for_platform_package import *
from typeset_for_drs_package import *
from typeset_for_shared_package import *
from typeset_for_software_package import *
from typeset_for_science_package import *
from typeset_for_activity_package import *

import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_drs_package as drs
import typeset_for_shared_package as shared
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_activity_package as activity

import typeset_meta         # Assigns type info.



# Module exports.
__all__ = [
    'TYPES',
    'data',
    'platform',
    'drs',
    'shared',
    'software',
    'science',
    'activity',
    'EnsembleRequirement',
    'ForcingConstraint',
    'Tuning',
    'ParentSimulation',
    'KeyFloat',
    'DomainProperties',
    'TimesliceList',
    'CimLink',
    'Reference',
    'EnsembleAxis',
    'VocabMember',
    'EntryPoint',
    'Cimtext',
    'OnlineResource',
    'Meta',
    'EnsembleMember',
    'DrsPublicationDataset',
    'MinimalMeta',
    'ComponentBase',
    'Downscaling',
    'Composition',
    'SimulationPlan',
    'VariableCollection',
    'DrsEnsembleIdentifier',
    'Activity',
    'TimePeriod',
    'NumericalExperiment',
    'Machine',
    'UberEnsemble',
    'IrregularDateset',
    'RelatedData',
    'Responsibility',
    'ConservationProperties',
    'Resolution',
    'Ensemble',
    'ComputePool',
    'Project',
    'StandaloneDocument',
    'Citation',
    'ComponentPerformance',
    'AxisMember',
    'MultiEnsemble',
    'StorageVolume',
    'NumberArray',
    'StoragePool',
    'Extent',
    'DrsTemporalIdentifier',
    'Performance',
    'Calendar',
    'DevelopmentPath',
    'OutputTemporalRequirement',
    'Party',
    'Simulation',
    'Gridspec',
    'GridSummary',
    'Partition',
    'Model',
    'ScientificDomain',
    'Variable',
    'MultiTimeEnsemble',
    'Pid',
    'Conformance',
    'TemporalConstraint',
    'Algorithm',
    'DatetimeSet',
    'DateTime',
    'SoftwareComponent',
    'ProcessDetail',
    'DrsGeographicalIndicator',
    'NumericalRequirement',
    'DrsAtomicDataset',
    'RegularTimeset',
    'Process',
    'Dataset',
]



# Supported types.
TYPES = (
    activity.EnsembleRequirement,
    activity.ForcingConstraint,
    science.Tuning,
    activity.ParentSimulation,
    shared.KeyFloat,
    activity.DomainProperties,
    shared.TimesliceList,
    shared.CimLink,
    shared.Reference,
    activity.EnsembleAxis,
    shared.VocabMember,
    software.EntryPoint,
    shared.Cimtext,
    shared.OnlineResource,
    shared.Meta,
    activity.EnsembleMember,
    drs.DrsPublicationDataset,
    shared.MinimalMeta,
    software.ComponentBase,
    activity.Downscaling,
    software.Composition,
    activity.SimulationPlan,
    data.VariableCollection,
    drs.DrsEnsembleIdentifier,
    activity.Activity,
    shared.TimePeriod,
    activity.NumericalExperiment,
    platform.Machine,
    activity.UberEnsemble,
    shared.IrregularDateset,
    data.RelatedData,
    shared.Responsibility,
    science.ConservationProperties,
    science.Resolution,
    activity.Ensemble,
    platform.ComputePool,
    activity.Project,
    shared.StandaloneDocument,
    shared.Citation,
    platform.ComponentPerformance,
    activity.AxisMember,
    activity.MultiEnsemble,
    platform.StorageVolume,
    shared.NumberArray,
    platform.StoragePool,
    science.Extent,
    drs.DrsTemporalIdentifier,
    platform.Performance,
    shared.Calendar,
    software.DevelopmentPath,
    activity.OutputTemporalRequirement,
    shared.Party,
    activity.Simulation,
    software.Gridspec,
    science.GridSummary,
    platform.Partition,
    software.Model,
    science.ScientificDomain,
    software.Variable,
    activity.MultiTimeEnsemble,
    shared.Pid,
    activity.Conformance,
    activity.TemporalConstraint,
    science.Algorithm,
    shared.DatetimeSet,
    shared.DateTime,
    software.SoftwareComponent,
    science.ProcessDetail,
    drs.DrsGeographicalIndicator,
    activity.NumericalRequirement,
    drs.DrsAtomicDataset,
    shared.RegularTimeset,
    science.Process,
    data.Dataset,
)
