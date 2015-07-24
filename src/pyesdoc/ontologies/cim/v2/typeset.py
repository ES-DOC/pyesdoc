# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:58:29.518782.

"""
from typeset_for_data_package import *
from typeset_for_platform_package import *
from typeset_for_drs_package import *
from typeset_for_activity_package import *
from typeset_for_software_package import *
from typeset_for_science_package import *
from typeset_for_shared_package import *

import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_drs_package as drs
import typeset_for_activity_package as activity
import typeset_for_software_package as software
import typeset_for_science_package as science
import typeset_for_shared_package as shared

import typeset_meta         # Assigns type info.



# Module exports.
__all__ = [
    'TYPES',
    'data',
    'platform',
    'drs',
    'activity',
    'software',
    'science',
    'shared',
    'Project',
    'ProcessDetail',
    'Cimtext',
    'ComputePool',
    'ParentSimulation',
    'MultiEnsemble',
    'DrsTemporalIdentifier',
    'Process',
    'Gridspec',
    'Responsibility',
    'Algorithm',
    'Dataset',
    'EntryPoint',
    'CimLink',
    'DateTime',
    'NumberArray',
    'ComponentPerformance',
    'Composition',
    'Simulation',
    'Performance',
    'DrsAtomicDataset',
    'OnlineResource',
    'Party',
    'SimulationPlan',
    'Citation',
    'ComponentBase',
    'UberEnsemble',
    'Machine',
    'DevelopmentPath',
    'Calendar',
    'Activity',
    'Resolution',
    'MultiTimeEnsemble',
    'Tuning',
    'MinimalMeta',
    'DomainProperties',
    'Model',
    'EnsembleRequirement',
    'TimesliceList',
    'Ensemble',
    'Downscaling',
    'DrsPublicationDataset',
    'TemporalConstraint',
    'VariableCollection',
    'StorageVolume',
    'StoragePool',
    'DatetimeSet',
    'ForcingConstraint',
    'RegularTimeset',
    'NumericalExperiment',
    'EnsembleAxis',
    'Meta',
    'AxisMember',
    'KeyFloat',
    'Partition',
    'Extent',
    'StandaloneDocument',
    'Variable',
    'TimePeriod',
    'IrregularDateset',
    'NumericalRequirement',
    'RelatedData',
    'ConservationProperties',
    'GridSummary',
    'SoftwareComponent',
    'EnsembleMember',
    'DrsGeographicalIndicator',
    'OutputTemporalRequirement',
    'DrsEnsembleIdentifier',
    'Reference',
    'Conformance',
    'Pid',
    'VocabMember',
    'ScientificDomain',
]



# Supported types.
TYPES = (
    activity.Project,
    science.ProcessDetail,
    shared.Cimtext,
    platform.ComputePool,
    activity.ParentSimulation,
    activity.MultiEnsemble,
    drs.DrsTemporalIdentifier,
    science.Process,
    software.Gridspec,
    shared.Responsibility,
    science.Algorithm,
    data.Dataset,
    software.EntryPoint,
    shared.CimLink,
    shared.DateTime,
    shared.NumberArray,
    platform.ComponentPerformance,
    software.Composition,
    activity.Simulation,
    platform.Performance,
    drs.DrsAtomicDataset,
    shared.OnlineResource,
    shared.Party,
    activity.SimulationPlan,
    shared.Citation,
    software.ComponentBase,
    activity.UberEnsemble,
    platform.Machine,
    software.DevelopmentPath,
    shared.Calendar,
    activity.Activity,
    science.Resolution,
    activity.MultiTimeEnsemble,
    science.Tuning,
    shared.MinimalMeta,
    activity.DomainProperties,
    software.Model,
    activity.EnsembleRequirement,
    shared.TimesliceList,
    activity.Ensemble,
    activity.Downscaling,
    drs.DrsPublicationDataset,
    activity.TemporalConstraint,
    data.VariableCollection,
    platform.StorageVolume,
    platform.StoragePool,
    shared.DatetimeSet,
    activity.ForcingConstraint,
    shared.RegularTimeset,
    activity.NumericalExperiment,
    activity.EnsembleAxis,
    shared.Meta,
    activity.AxisMember,
    shared.KeyFloat,
    platform.Partition,
    science.Extent,
    shared.StandaloneDocument,
    software.Variable,
    shared.TimePeriod,
    shared.IrregularDateset,
    activity.NumericalRequirement,
    data.RelatedData,
    science.ConservationProperties,
    science.GridSummary,
    software.SoftwareComponent,
    activity.EnsembleMember,
    drs.DrsGeographicalIndicator,
    activity.OutputTemporalRequirement,
    drs.DrsEnsembleIdentifier,
    shared.Reference,
    activity.Conformance,
    shared.Pid,
    shared.VocabMember,
    science.ScientificDomain,
)
