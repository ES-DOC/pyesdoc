# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""
from typeset_for_activity_package import *
from typeset_for_data_package import *
from typeset_for_designing_package import *
from typeset_for_drs_package import *
from typeset_for_platform_package import *
from typeset_for_science_package import *
from typeset_for_shared_package import *
from typeset_for_software_package import *

import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_designing_package as designing
import typeset_for_drs_package as drs
import typeset_for_platform_package as platform
import typeset_for_science_package as science
import typeset_for_shared_package as shared
import typeset_for_software_package as software

import typeset_meta         # Assigns type info.



# Module exports.
__all__ = [
    'TYPES',
    # Packages
    'activity',
    'data',
    'designing',
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
    'Cimtext',
    'ComponentBase',
    'ComponentPerformance',
    'Composition',
    'ComputePool',
    'Conformance',
    'ConservationProperties',
    'Dataset',
    'DateTime',
    'DatetimeSet',
    'Detail',
    'DevelopmentPath',
    'DocMetaInfo',
    'DocReference',
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
    'ExternalDocument',
    'ForcingConstraint',
    'Grid',
    'Gridspec',
    'IrregularDateset',
    'KeyFloat',
    'KeyProperties',
    'Machine',
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
    'Project',
    'QualityReview',
    'Reference',
    'RegularTimeset',
    'Resolution',
    'Responsibility',
    'ScienceContext',
    'ScientificDomain',
    'Simulation',
    'SimulationPlan',
    'SoftwareComponent',
    'StoragePool',
    'StorageVolume',
    'SubProcess',
    'TemporalConstraint',
    'TimePeriod',
    'TimesliceList',
    'Tuning',
    'UberEnsemble',
    'Variable',
    'VariableCollection',
]


# Supported types.
TYPES = (
    activity.Activity,
    activity.AxisMember,
    activity.Conformance,
    activity.Ensemble,
    activity.EnsembleAxis,
    activity.EnsembleMember,
    activity.ParentSimulation,
    activity.UberEnsemble,
    data.Dataset,
    data.Downscaling,
    data.Simulation,
    data.VariableCollection,
    designing.DomainProperties,
    designing.EnsembleRequirement,
    designing.ForcingConstraint,
    designing.MultiEnsemble,
    designing.MultiTimeEnsemble,
    designing.NumericalExperiment,
    designing.NumericalRequirement,
    designing.OutputTemporalRequirement,
    designing.Project,
    designing.SimulationPlan,
    designing.TemporalConstraint,
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
    science.Detail,
    science.Extent,
    science.Grid,
    science.KeyProperties,
    science.Model,
    science.Process,
    science.Resolution,
    science.ScienceContext,
    science.ScientificDomain,
    science.SubProcess,
    science.Tuning,
    shared.Calendar,
    shared.Cimtext,
    shared.DateTime,
    shared.DatetimeSet,
    shared.DocMetaInfo,
    shared.DocReference,
    shared.ExternalDocument,
    shared.IrregularDateset,
    shared.KeyFloat,
    shared.NumberArray,
    shared.OnlineResource,
    shared.Party,
    shared.Pid,
    shared.QualityReview,
    shared.Reference,
    shared.RegularTimeset,
    shared.Responsibility,
    shared.TimePeriod,
    shared.TimesliceList,
    software.ComponentBase,
    software.Composition,
    software.DevelopmentPath,
    software.EntryPoint,
    software.Gridspec,
    software.SoftwareComponent,
    software.Variable,
)
