# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Typeset information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 14:48:44.250099.

"""
from typeset_for_activity_package import *
from typeset_for_data_package import *
from typeset_for_platform_package import *
from typeset_for_shared_package import *

import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_platform_package as platform
import typeset_for_shared_package as shared

import typeset_meta         # Assigns type info.



# Module exports.
__all__ = [
    'TYPES',
    'activity',
    'data',
    'platform',
    'shared',
    'VocabMember',
    'Simulation',
    'Dataset',
    'OnlineResource',
    'NumberArray',
    'NumericalRequirement',
    'TimePeriod',
    'StoragePool',
    'MultiTimeEnsemble',
    'Ensemble',
    'IrregularDateSet',
    'Project',
    'Activity',
    'EnsembleRequirement',
    'EnsembleRequirement',
    'CimLink',
    'Calendar',
    'Citation',
    'NumericalExperiment',
    'Conformance',
    'CimText',
    'Partition',
    'Responsibility',
    'Configuration',
    'DateTime',
    'StorageVolume',
    'TimesliceList',
    'RegularTimeSet',
    'ComputePool',
    'AxisMember',
    'Machine',
    'MultiEnsemble',
    'SimulationPlan',
    'Performance',
    'OutputTemporalRequirement',
    'ComponentPerformance',
    'Party',
    'DatetimeSet',
    'TemporalConstraint',
    'Meta',
    'MemberDescription',
    'ForcingConstraint',
]



# Supported types.
TYPES = (
    shared.VocabMember,
    activity.Simulation,
    data.Dataset,
    shared.OnlineResource,
    shared.NumberArray,
    activity.NumericalRequirement,
    shared.TimePeriod,
    platform.StoragePool,
    activity.MultiTimeEnsemble,
    activity.Ensemble,
    shared.IrregularDateSet,
    activity.Project,
    activity.Activity,
    activity.EnsembleRequirement,
    activity.EnsembleRequirement,
    shared.CimLink,
    shared.Calendar,
    shared.Citation,
    activity.NumericalExperiment,
    activity.Conformance,
    shared.CimText,
    platform.Partition,
    shared.Responsibility,
    activity.Configuration,
    shared.DateTime,
    platform.StorageVolume,
    shared.TimesliceList,
    shared.RegularTimeSet,
    platform.ComputePool,
    activity.AxisMember,
    platform.Machine,
    activity.MultiEnsemble,
    activity.SimulationPlan,
    platform.Performance,
    activity.OutputTemporalRequirement,
    platform.ComponentPerformance,
    shared.Party,
    shared.DatetimeSet,
    activity.TemporalConstraint,
    shared.Meta,
    activity.MemberDescription,
    activity.ForcingConstraint,
)
