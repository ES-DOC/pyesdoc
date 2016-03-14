# -*- coding: utf-8 -*-
"""
.. module:: cim.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim package initializer.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 13:14:13.903808.

"""
from collections import defaultdict

import v1
import v2



# Ontology name.
NAME = 'cim'

# Ontology versions.
VERSIONS = (v1, v2)

# Ontology packages.
PACKAGES = tuple(i for i in (j for j in (v.PACKAGES for v in VERSIONS)))

# Ontology types.
TYPES = tuple(i for i in (j for j in (v.TYPES for v in VERSIONS)))

# Ontology types.
DOCUMENT_TYPES = tuple(i for i in (j for j in (v.DOCUMENT_TYPES for v in VERSIONS)))

# Ontology classes.
CLASSES = tuple(i for i in (j for j in (v.CLASSES for v in VERSIONS)))

# Ontology enum.
ENUMS = tuple(i for i in (j for j in (v.ENUMS for v in VERSIONS)))

# Class properties.
CLASS_PROPERTIES = {}
for v in VERSIONS:
    CLASS_PROPERTIES.update(v.CLASS_PROPERTIES)

# Class own properties.
CLASS_OWN_PROPERTIES = {}
for v in VERSIONS:
    CLASS_OWN_PROPERTIES.update(v.CLASS_OWN_PROPERTIES)

# Base classes.
BASE_CLASSES = defaultdict(tuple)
for v in VERSIONS:
    BASE_CLASSES.update(v.BASE_CLASSES)

# Classes with base classes.
BASE_CLASSED = tuple(i for i in (j for j in (v.BASE_CLASSED for v in VERSIONS)))

# Sub classes.
SUB_CLASSES = defaultdict(tuple)
for v in VERSIONS:
    SUB_CLASSES.update(v.SUB_CLASSES)

# Classes that have been sub classed.
SUB_CLASSED = tuple(i for i in (j for j in (v.SUB_CLASSED for v in VERSIONS)))

# Ontology type keys.
KEYS = {}
for v in VERSIONS:
    KEYS.update(v.KEYS)

# Ontology constraints.
CONSTRAINTS = {}
for v in VERSIONS:
    CONSTRAINTS.update(v.CONSTRAINTS)

# Help text.
HELP = {}
for v in VERSIONS:
    HELP.update({k: v.strip() if v else None for k, v in v.HELP.items()})

# Map of document types to display names.
DISPLAY_NAMES = {
    v1.activity.NumericalExperiment: u"Experiment",
    v1.activity.SimulationRun: u"Simulation",
    v1.data.DataObject: u"Data Object",
    v1.grids.GridSpec: u"Grid Spec",
    v1.misc.DocumentSet: u"Simulation",
    v1.quality.CimQuality: u"Dataset QC",
    v1.software.ModelComponent: u"Model",
    v2.designing.NumericalExperiment: u"Experiment"
}

# Map of document types to sort keys.
SORT_KEYS = {
    v1.activity.Ensemble: u"BC",
    v1.activity.NumericalExperiment: u"AB",
    v1.activity.SimulationRun: u"AC",
    v1.data.DataObject: u"CA",
    v1.grids.GridSpec: u"BB",
    v1.misc.DocumentSet: u"AC",
    v1.quality.CimQuality: u"CB",
    v1.shared.Platform: u"BA",
    v1.software.ModelComponent: u"AA",
    v2.designing.NumericalExperiment: u"AB"
}

