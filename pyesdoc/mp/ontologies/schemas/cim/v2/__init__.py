"""
.. module:: cim.v2.__init__.py
   :license: MIT
   :platform: Unix, Windows
   :synopsis: CIM v2 ontology schema (first post CMIP6 update)
"""
from . import activity_classes
from . import data_classes
from . import designing_classes
from . import drs_entities
from . import platform_classes
from . import science_classes
from . import science_enums
from . import shared_classes
from . import shared_classes_doc
from . import software_classes
from . import software_enums
from . import cmip_classes
from . import iso_classes
from . import iso_enums
from . import time as time_classes


# Ontology name.
NAME = "cim"

# Ontology version.
VERSION = "2"

# Ontology doc string.
DOC = "ESDOC CIM ontology schema - version 2.2"


def activity():
    """Types that describe context against which climate models are run."""
    return {activity_classes}


def cmip():
    """Extensions for CMIP6."""
    return {cmip_classes}


def data():
    """Types that describe output that climate models emit."""
    return {data_classes}


def designing():
    """Types that describe project design features."""
    return {designing_classes}


def drs():
    """Types that describe the directory structures to which climate model output is written."""
    return {drs_entities}


def iso():
    """Types that implement ISO classes used in other packages."""
    return {iso_classes, iso_enums}


def platform():
    """Types that describe hardware upon which climate models are run."""
    return {platform_classes}


def science():
    """Types that describe the science being performed."""
    return {science_classes, science_enums}


def shared():
    """Shared types that might be imported from other packages within the ontology."""
    return {shared_classes, shared_classes_doc}


def software():
    """Types that describe the software that constitutes a climate model."""
    return {software_classes, software_enums}


def time():
    """Types that describe the software that constitutes a climate model."""
    return {time_classes}
