# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:45:43.343143.

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
    'Citation',
    'CimLink',
    'EnsembleMember',
    'ForcingConstraint',
    'Tuning',
    'Extent',
    'DrsTemporalIdentifier',
    'EnsembleAxis',
    'Algorithm',
    'OutputTemporalRequirement',
    'Reference',
    'Dataset',
    'GridSummary',
    'Ensemble',
    'EntryPoint',
    'Project',
    'ScientificDomain',
    'DateTime',
    'DrsPublicationDataset',
    'Performance',
    'TemporalConstraint',
    'MultiEnsemble',
    'Activity',
    'Calendar',
    'NumericalRequirement',
    'DrsAtomicDataset',
    'ProcessDetail',
    'Party',
    'SimulationPlan',
    'Pid',
    'StandaloneDocument',
    'Resolution',
    'Simulation',
    'DevelopmentPath',
    'ConservationProperties',
    'MinimalMeta',
    'DomainProperties',
    'ComputePool',
    'MultiTimeEnsemble',
    'Meta',
    'ComponentPerformance',
    'OnlineResource',
    'UberEnsemble',
    'AxisMember',
    'KeyFloat',
    'IrregularDateset',
    'ComponentBase',
    'Model',
    'TimesliceList',
    'NumericalExperiment',
    'Downscaling',
    'Composition',
    'Partition',
    'EnsembleRequirement',
    'VariableCollection',
    'StoragePool',
    'TimePeriod',
    'NumberArray',
    'RegularTimeset',
    'Cimtext',
    'Gridspec',
    'Variable',
    'SoftwareComponent',
    'RelatedData',
    'Responsibility',
    'DrsGeographicalIndicator',
    'StorageVolume',
    'DrsEnsembleIdentifier',
    'DatetimeSet',
    'Machine',
    'ParentSimulation',
    'Conformance',
    'Process',
    'VocabMember',
]



# Supported types.
TYPES = (
    shared.Citation,
    shared.CimLink,
    activity.EnsembleMember,
    activity.ForcingConstraint,
    science.Tuning,
    science.Extent,
    drs.DrsTemporalIdentifier,
    activity.EnsembleAxis,
    science.Algorithm,
    activity.OutputTemporalRequirement,
    shared.Reference,
    data.Dataset,
    science.GridSummary,
    activity.Ensemble,
    software.EntryPoint,
    activity.Project,
    science.ScientificDomain,
    shared.DateTime,
    drs.DrsPublicationDataset,
    platform.Performance,
    activity.TemporalConstraint,
    activity.MultiEnsemble,
    activity.Activity,
    shared.Calendar,
    activity.NumericalRequirement,
    drs.DrsAtomicDataset,
    science.ProcessDetail,
    shared.Party,
    activity.SimulationPlan,
    shared.Pid,
    shared.StandaloneDocument,
    science.Resolution,
    activity.Simulation,
    software.DevelopmentPath,
    science.ConservationProperties,
    shared.MinimalMeta,
    activity.DomainProperties,
    platform.ComputePool,
    activity.MultiTimeEnsemble,
    shared.Meta,
    platform.ComponentPerformance,
    shared.OnlineResource,
    activity.UberEnsemble,
    activity.AxisMember,
    shared.KeyFloat,
    shared.IrregularDateset,
    software.ComponentBase,
    software.Model,
    shared.TimesliceList,
    activity.NumericalExperiment,
    activity.Downscaling,
    software.Composition,
    platform.Partition,
    activity.EnsembleRequirement,
    data.VariableCollection,
    platform.StoragePool,
    shared.TimePeriod,
    shared.NumberArray,
    shared.RegularTimeset,
    shared.Cimtext,
    software.Gridspec,
    software.Variable,
    software.SoftwareComponent,
    data.RelatedData,
    shared.Responsibility,
    drs.DrsGeographicalIndicator,
    platform.StorageVolume,
    drs.DrsEnsembleIdentifier,
    shared.DatetimeSet,
    platform.Machine,
    activity.ParentSimulation,
    activity.Conformance,
    science.Process,
    shared.VocabMember,
)
