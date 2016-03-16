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
DOC_STRINGS = {}

# Map of types to keys.
KEYS = {}

# Map of types to constraints.
CONSTRAINTS = {}

# Set of registered document types.
DOCUMENT_TYPES = ()


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
        DOC_STRINGS.update(v.DOC_STRINGS)


def _get_type(target):
    """Returns type from target.

    """
    if target in TYPES:
        return target
    return type(target)


def get_own_properties(kls):
    """Returns set of class own properties.

    :param kls: A class or class instance within one of the registered ontologies.

    :returns: Set of a class's own properties.
    :rtype: set

    """
    kls = _get_type(kls)

    return set(CLASS_OWN_PROPERTIES.get(kls, []))


def get_properties(kls):
    """Returns set of class properties.

    :param kls: A class or class instance within one of the registered ontologies.

    :returns: Set of class properties.
    :rtype: set

    """
    kls = _get_type(kls)

    return set(CLASS_PROPERTIES.get(kls, []))


def get_is_document_type(kls):
    """Returns flag indicating whether a class is a document type.

    :param kls: A class or class instance within one of the registered ontologies.

    :returns: True if class is considered to be a "document".
    :rtype: bool

    """
    kls = _get_type(kls)

    return kls in DOCUMENT_TYPES


def get_sub_classes(kls):
    """Returns set of sub-classes.

    """
    kls = _get_type(kls)

    return [KEYS[i] for i in SUB_CLASSES[kls]]


def get_is_sub_classed(kls):
    """Returns flag indicating whether a class is sub-classed or not.

    :param kls: A class or class instance within one of the registered ontologies.

    :returns: True if class is sub-classed.
    :rtype: bool

    """
    kls = _get_type(kls)

    return kls in SUB_CLASSED


def get_bases(kls):
    """Returns set of base classes.

    """
    kls = _get_type(kls)

    return [KEYS[i] for i in BASE_CLASSES[kls]]


def get_has_base_class(kls):
    """Returns flag indicating whether a class has a base class or not.

    :param kls: A class or class instance within one of the registered ontologies.

    :returns: True if class has a base class.
    :rtype: bool

    """
    kls = _get_type(kls)

    return kls in BASE_CLASSED


def get_doc_string(typeof, attribute=None):
    """Returns a documentation string.

    :param typeof: A type within one of the registered ontologies.
    :param attribute: Name of either a class property or an enum member.

    :returns: A documentation string.
    :rtype: str

    """
    typeof = _get_type(typeof)

    if attribute:
        return DOC_STRINGS.get((typeof, attribute), "").strip()
    return DOC_STRINGS.get(typeof, "").strip()


def get_key(typeof, attribute=None):
    """Returns a type's key.

    :param typeof: A type within one of the registered ontologies.
    :param attribute: Name of either a class property or an enum member.

    :returns: A key.
    :rtype: str

    """
    typeof = _get_type(typeof)

    if attribute:
        return KEYS.get((typeof, attribute), "").strip()
    return KEYS.get(typeof, "").strip()


def get_constraints(typeof, attribute=None):
    """Returns a type's constraints.

    :param typeof: A type within one of the registered ontologies.
    :param attribute: Name of either a class property or an enum member.

    :returns: A key.
    :rtype: str

    """
    typeof = _get_type(typeof)

    if attribute:
        return set(CONSTRAINTS.get((typeof, attribute), ""))

    return {p: get_constraints(typeof, p) for p in get_properties(typeof)}


# Auto register cim.
from pyesdoc.ontologies import cim
register(cim)


# Remove import dross.
del defaultdict
del cim
