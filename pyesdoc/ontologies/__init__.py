# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.ontologies.__init__.py

   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Ontologies sub-package init.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from collections import defaultdict

import cim
from pyesdoc import constants
from pyesdoc.utils import runtime as rt


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

# Map of types to display names.
DISPLAY_NAMES = {}


def get_type_key(name, version, package, typeof):
    """Returns type key.

    :param str name: Ontology name, e.g. cim.
    :param str version: Ontology version, e.g. 1.
    :param str package: Ontology package, e.g. activity.
    :param str typeof: Ontology type, e.g. Experiment.

    """
    return "{0}.{1}.{2}.{3}".format(name, version, package, typeof).lower()


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
    try:
        DISPLAY_NAMES.update(o.DISPLAY_NAMES)
    except AttributeError:
        pass

    for v in o.VERSIONS:
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


def get_types(name=None, version=None):
    """Returns set of supported types.

    :param str name: Ontology name, e.g. cim.
    :param str version: Ontology version, e.g. 1.

    :returns: A tuple of supported types.
    :rtype: tuple

    """
    result = ()

    for o in ONTOLOGIES:
        if name is None or name == o.NAME:
            for v in o.VERSIONS:
                if version is None or version == v.ID:
                    result += v.TYPES

    return result


def list_stats(ontology):
    """Lists stats related to an ontology.

    :param module ontology: An ontology module.


    """
    rt.log("ONTOLOGY :: {} v{}".format(ontology.NAME, ontology.VERSION))
    rt.log("\tpackages :: {}".format(len(ontology.PACKAGES)))
    rt.log("\tclasses :: {}".format(len(ontology.CLASSES)))
    rt.log("\tenums :: {}".format(len(ontology.ENUMS)))


def list_types(name=None, version=None):
    """Returns list of supported type keys and types.

    :param str name: Ontology name, e.g. cim.
    :param str version: Ontology version, e.g. 1.

    :returns: A tuple of supported typekeys and types.
    :rtype: tuple

    """
    types = get_types(name, version)
    types = [tuple(t.type_key.split('.')) for t in types]

    return tuple(types)


def get_doc_types():
    """Returns list of supported document type keys and types.

    :returns: A tuple of supported typekeys and types.
    :rtype: tuple

    """
    return [tuple(t.type_key.split('.')) for t in DOCUMENT_TYPES]


def get_doc_type_keyset():
    """Returns set of supported document type keys.

    :returns: Set of supported document type keys.
    :rtype: set

    """
    return KEYS.values()


def get_type(name, version, package, typeof):
    """Returns a type if supported.

    :param str name: Ontology name, e.g. cim.
    :param str version: Ontology version, e.g. 1.
    :param str package: Ontology package, e.g. activity.
    :param str typeof: Ontology type, e.g. Experiment.

    :returns: A type (if found).
    :rtype: class or None

    """
    return get_type_from_key(get_type_key(name, version, package, typeof))


def get_type_key(doc_type):
    """Returns a document type key.

    :param class doc_type: A document type for which meta-information is to be returned.

    :returns: A type key (if found).
    :rtype: str or None

    """
    return KEYS.get(doc_type, None)


def get_type_sortkey(doc_type):
    """Returns a document type sort key.

    :param class doc_type: A document type for which meta-information is to be returned.

    :returns: A type sort key (if found).
    :rtype: str

    """
    return SORT_KEYS.get(doc_type, u"")


def get_type_display_name(doc_type):
    """Returns a document type display name.

    :param class doc_type: A document type for which meta-information is to be returned.

    :returns: A type disaply name (if found).
    :rtype: str

    """
    return DISPLAY_NAMES.get(doc_type, u"")


def get_type_from_key(key):
    """Returns a type if supported.

    :param str key: Type key, e.g. cim.1.software.ModelComponent.

    :returns: A type (if found).
    :rtype: class or None

    """
    type_key = str(key).lower()
    for t in TYPES:
        if KEYS[t].lower() == type_key:
            return t


def is_supported(name, version, package=None, typeof=None):
    """Returns a flag indicating whether ontology/type is supported.

    :param str name: Ontology name, e.g. cim.
    :param str version: Ontology version, e.g. 1.
    :param str package: Ontology package, e.g. activity.
    :param str typeof: Ontology type, e.g. Experiment.

    :returns: A flag indicating whether ontology is supported.
    :rtype: bool

    """
    if (package is not None and typeof is None) or \
       (package is None and typeof is not None):
       raise ValueError("The ontology package and type are unspecified.")

    if package is None and typeof is None:
        return len(get_types(name, version)) > 0
    else:
        return get_type(name, version, package, typeof) is not None


def create(name, version, package, typeof):
    """Creates a document.

    :param str name: Ontology name, e.g. cim.
    :param str version: Ontology version, e.g. 1.
    :param str package: Ontology package, e.g. activity.
    :param str typeof: Ontology type, e.g. Experiment.

    :returns: A pyesdoc document instance.
    :rtype: pyesdoc object

    """
    typeof = get_type(name, version, package, typeof)

    return None if typeof is None else typeof()


def get_decoder_info(doc_type):
    """Returns meta-information associated with a type used for decoding purposes.

    :param class doc_type: A document type for which meta-information is to be returned.

    :returns: Type meta-information.
    :rtype: tuple

    """
    result = {name: typeof for name, _, typeof in get_constraints(doc_type, constants.CONSTRAINT_TYPE_TYPEOF)}
    for name, _, cardinality in get_constraints(doc_type, constants.CONSTRAINT_TYPE_CARDINALITY):
        result[name] = (name, result[name], bool(cardinality.split(".")[1] == 'N'))

    return result.values()


def get_validation_info(doc_type):
    """Returns meta-information associated with a type used for validation purposes.

    :param class doc_type: A document type for which meta-information is to be returned.

    :returns: Type meta-information.
    :rtype: tuple

    """
    result = defaultdict(set)
    for name, typeof, value in CONSTRAINTS[doc_type]:
        result[name].add((typeof, value))

    return result.items()


def get_constraints(doc_type, type_filter=None):
    """Returns constraints associated with a type.

    :param class doc_type: A document type for which meta-information is to be returned.
    :param str type_filtre: A constraint type filter.

    :returns: Type meta-information.
    :rtype: tuple

    """
    if type_filter:
        return [ct for ct in CONSTRAINTS[doc_type] if ct[1] == type_filter]

    return CONSTRAINTS[doc_type]


def associate(left, attr, right):
    """Creates and returns an association between two documents.

    :param left: A document.
    :type left:  A pyesdoc object.

    :param attr: Name of attribute upon left document to which the association will be assigned.
    :type attr:  str

    :param right: A document.
    :type right:  A pyesdoc object.

    :returns: A document reference.
    :rtype:  object

    """
    # Defensive Programming.
    rt.assert_doc(left)
    rt.assert_doc(right)
    if not hasattr(left, attr):
        raise ValueError("Cannot set association upon invalid attribute.")

    # Create reference.
    # TODO alter reference based upon ontology type.
    ref = cim.v1.DocReference()
    ref.id = right.meta.id
    ref.version = right.meta.version

    # Set association.
    setattr(left, attr, ref)

    return ref


# Auto register cim.
register(cim)
