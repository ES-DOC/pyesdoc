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
from typeset_for_shared_package import *
from typeset_for_science_package import *
from typeset_for_platform_package import *
from typeset_for_software_package import *
from typeset_for_data_package import *
from typeset_for_drs_package import *
from typeset_for_activity_package import *

import typeset_for_shared_package as shared
import typeset_for_science_package as science
import typeset_for_platform_package as platform
import typeset_for_software_package as software
import typeset_for_data_package as data
import typeset_for_drs_package as drs
import typeset_for_activity_package as activity

import typeset_meta         # Assigns type info.



# Module exports.
__all__ = [
    'TYPES',
    # Packages
    'activity',
    'data',
    'drs',
    'platform',
    'science',
    'shared',
    'software',
	# Types
    'Activity',
    'Algorithm',
    'AxisMember',
    'Calendar',
    'CimLink',
    'Cimtext',
    'Citation',
    'ComponentBase',
    'ComponentPerformance',
    'Composition',
    'ComputePool',
    'Conformance',
    'ConservationProperties',
    'Dataset',
    'DateTime',
    'DatetimeSet',
    'DevelopmentPath',
    'DomainProperties',
    'Downscaling',
    'DrsAtomicDataset',
    'DrsEnsembleIdentifier',
    'DrsGeographicalIndicator',
    'DrsPublicationDataset',
    'DrsTemporalIdentifier',
    'Ensemble',
    'EnsembleAxis',
    'EnsembleMember',
    'EnsembleRequirement',
    'EntryPoint',
    'Extent',
    'ForcingConstraint',
    'GridSummary',
    'Gridspec',
    'IrregularDateset',
    'KeyFloat',
    'Machine',
    'Meta',
    'MinimalMeta',
    'Model',
    'MultiEnsemble',
    'MultiTimeEnsemble',
    'NumberArray',
    'NumericalExperiment',
    'NumericalRequirement',
    'OnlineResource',
    'OutputTemporalRequirement',
    'ParentSimulation',
    'Partition',
    'Party',
    'Performance',
    'Pid',
    'Process',
    'ProcessDetail',
    'Project',
    'Reference',
    'RegularTimeset',
    'RelatedData',
    'Resolution',
    'Responsibility',
    'ScientificDomain',
    'Simulation',
    'SimulationPlan',
    'SoftwareComponent',
    'StandaloneDocument',
    'StoragePool',
    'StorageVolume',
    'TemporalConstraint',
    'TimePeriod',
    'TimesliceList',
    'Tuning',
    'UberEnsemble',
    'Variable',
    'VariableCollection',
    'VocabMember',
]


# Supported types.
TYPES = (
    activity.Activity,
    activity.AxisMember,
    activity.Conformance,
    activity.DomainProperties,
    activity.Downscaling,
    activity.Ensemble,
    activity.EnsembleAxis,
    activity.EnsembleMember,
    activity.EnsembleRequirement,
    activity.ForcingConstraint,
    activity.MultiEnsemble,
    activity.MultiTimeEnsemble,
    activity.NumericalExperiment,
    activity.NumericalRequirement,
    activity.OutputTemporalRequirement,
    activity.ParentSimulation,
    activity.Project,
    activity.Simulation,
    activity.SimulationPlan,
    activity.TemporalConstraint,
    activity.UberEnsemble,
    data.Dataset,
    data.RelatedData,
    data.VariableCollection,
    drs.DrsAtomicDataset,
    drs.DrsEnsembleIdentifier,
    drs.DrsGeographicalIndicator,
    drs.DrsPublicationDataset,
    drs.DrsTemporalIdentifier,
    platform.ComponentPerformance,
    platform.ComputePool,
    platform.Machine,
    platform.Partition,
    platform.Performance,
    platform.StoragePool,
    platform.StorageVolume,
    science.Algorithm,
    science.ConservationProperties,
    science.Extent,
    science.GridSummary,
    science.Process,
    science.ProcessDetail,
    science.Resolution,
    science.ScientificDomain,
    science.Tuning,
    shared.Calendar,
    shared.CimLink,
    shared.Cimtext,
    shared.Citation,
    shared.DateTime,
    shared.DatetimeSet,
    shared.IrregularDateset,
    shared.KeyFloat,
    shared.Meta,
    shared.MinimalMeta,
    shared.NumberArray,
    shared.OnlineResource,
    shared.Party,
    shared.Pid,
    shared.Reference,
    shared.RegularTimeset,
    shared.Responsibility,
    shared.StandaloneDocument,
    shared.TimePeriod,
    shared.TimesliceList,
    shared.VocabMember,
    software.ComponentBase,
    software.Composition,
    software.DevelopmentPath,
    software.EntryPoint,
    software.Gridspec,
    software.Model,
    software.SoftwareComponent,
    software.Variable,
)
