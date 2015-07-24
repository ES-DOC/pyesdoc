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
    'Cimtext',
    'Tuning',
    'Downscaling',
    'Activity',
    'DrsTemporalIdentifier',
    'Algorithm',
    'TimePeriod',
    'Responsibility',
    'Project',
    'Dataset',
    'EntryPoint',
    'CimLink',
    'ParentSimulation',
    'ForcingConstraint',
    'EnsembleMember',
    'NumberArray',
    'ComponentPerformance',
    'Extent',
    'DateTime',
    'EnsembleAxis',
    'Process',
    'EnsembleRequirement',
    'DrsAtomicDataset',
    'Party',
    'OutputTemporalRequirement',
    'GridSummary',
    'MultiEnsemble',
    'SimulationPlan',
    'ScientificDomain',
    'Resolution',
    'AxisMember',
    'DevelopmentPath',
    'TemporalConstraint',
    'VariableCollection',
    'ConservationProperties',
    'Machine',
    'ComputePool',
    'Citation',
    'ProcessDetail',
    'DrsPublicationDataset',
    'Performance',
    'NumericalRequirement',
    'DomainProperties',
    'StorageVolume',
    'MinimalMeta',
    'DatetimeSet',
    'Calendar',
    'IrregularDateset',
    'Partition',
    'Simulation',
    'MultiTimeEnsemble',
    'Meta',
    'Composition',
    'UberEnsemble',
    'OnlineResource',
    'Reference',
    'Variable',
    'StandaloneDocument',
    'Conformance',
    'StoragePool',
    'RelatedData',
    'NumericalExperiment',
    'Pid',
    'SoftwareComponent',
    'ComponentBase',
    'Model',
    'DrsGeographicalIndicator',
    'DrsEnsembleIdentifier',
    'TimesliceList',
    'KeyFloat',
    'RegularTimeset',
    'Ensemble',
    'Gridspec',
    'VocabMember',
]



# Supported types.
TYPES = (
    shared.Cimtext,
    science.Tuning,
    activity.Downscaling,
    activity.Activity,
    drs.DrsTemporalIdentifier,
    science.Algorithm,
    shared.TimePeriod,
    shared.Responsibility,
    activity.Project,
    data.Dataset,
    software.EntryPoint,
    shared.CimLink,
    activity.ParentSimulation,
    activity.ForcingConstraint,
    activity.EnsembleMember,
    shared.NumberArray,
    platform.ComponentPerformance,
    science.Extent,
    shared.DateTime,
    activity.EnsembleAxis,
    science.Process,
    activity.EnsembleRequirement,
    drs.DrsAtomicDataset,
    shared.Party,
    activity.OutputTemporalRequirement,
    science.GridSummary,
    activity.MultiEnsemble,
    activity.SimulationPlan,
    science.ScientificDomain,
    science.Resolution,
    activity.AxisMember,
    software.DevelopmentPath,
    activity.TemporalConstraint,
    data.VariableCollection,
    science.ConservationProperties,
    platform.Machine,
    platform.ComputePool,
    shared.Citation,
    science.ProcessDetail,
    drs.DrsPublicationDataset,
    platform.Performance,
    activity.NumericalRequirement,
    activity.DomainProperties,
    platform.StorageVolume,
    shared.MinimalMeta,
    shared.DatetimeSet,
    shared.Calendar,
    shared.IrregularDateset,
    platform.Partition,
    activity.Simulation,
    activity.MultiTimeEnsemble,
    shared.Meta,
    software.Composition,
    activity.UberEnsemble,
    shared.OnlineResource,
    shared.Reference,
    software.Variable,
    shared.StandaloneDocument,
    activity.Conformance,
    platform.StoragePool,
    data.RelatedData,
    activity.NumericalExperiment,
    shared.Pid,
    software.SoftwareComponent,
    software.ComponentBase,
    software.Model,
    drs.DrsGeographicalIndicator,
    drs.DrsEnsembleIdentifier,
    shared.TimesliceList,
    shared.KeyFloat,
    shared.RegularTimeset,
    activity.Ensemble,
    software.Gridspec,
    shared.VocabMember,
)
