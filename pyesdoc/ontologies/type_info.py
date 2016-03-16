# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.ontologies.type_info.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encpasulates type information related to registered ontologies.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from collections import defaultdict



# Set of registered ontologies.
ONTOLOGIES = ()

# Set of registered packages.
PACKAGES = ()

# Set of registered classes.
CLASSES = ()

# Class properties.
CLASS_PROPERTIES = {}

# Class own properties.
CLASS_OWN_PROPERTIES = {}

# Base classes.
BASE_CLASSES = defaultdict(tuple)

# Classes with base classes.
BASE_CLASSED = ()

# Sub classes.
SUB_CLASSES = defaultdict(tuple)

# Classes that have been sub classed.
SUB_CLASSED = ()

# Set of registered enums.
ENUMS = ()

# Set of registered types.
TYPES = ()

# Help text.
HELP = {}

# Map of types to keys.
KEYS = {}

# Map of types to constraints.
CONSTRAINTS = {}

# Set of registered document types.
DOCUMENT_TYPES = ()

# Map of types to sort keys.
SORT_KEYS = {}


def register(o):
    """Registers an ontology for use.

    :param o: Ontology being registered.
    :type o: module

    """
    global BASE_CLASSED
    global SUB_CLASSED
    global ONTOLOGIES
    global PACKAGES
    global TYPES
    global DOCUMENT_TYPES
    global CLASSES
    global ENUMS

    if o in ONTOLOGIES:
        return

    ONTOLOGIES += (o,)
    try:
        SORT_KEYS.update(o.SORT_KEYS)
    except AttributeError:
        pass

    for v in [v.type_info for v in o.VERSIONS]:
        PACKAGES += v.PACKAGES
        TYPES += v.TYPES
        DOCUMENT_TYPES += v.DOCUMENT_TYPES
        CLASSES += v.CLASSES
        CLASS_PROPERTIES.update(v.CLASS_PROPERTIES)
        CLASS_OWN_PROPERTIES.update(v.CLASS_OWN_PROPERTIES)
        BASE_CLASSES.update(v.BASE_CLASSES)
        BASE_CLASSED += v.BASE_CLASSED
        SUB_CLASSES.update(v.SUB_CLASSES)
        SUB_CLASSED += v.SUB_CLASSED
        ENUMS += v.ENUMS
        KEYS.update(v.KEYS)
        CONSTRAINTS.update(v.CONSTRAINTS)
        HELP.update(v.HELP)


# Auto register cim.
from pyesdoc.ontologies import cim
register(cim)


# Remove import dross.
del defaultdict
del cim
