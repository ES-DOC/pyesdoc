# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.ontologies.utils.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encpasulates utility functions related to registered ontologies.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from collections import defaultdict

import cim
from pyesdoc import constants
from pyesdoc.ontologies import type_info




def get_type_key(name, version, package, typeof):
    """Returns type key.

    :param str name: Ontology name, e.g. cim.
    :param str version: Ontology version, e.g. 1.
    :param str package: Ontology package, e.g. activity.
    :param str typeof: Ontology type, e.g. Experiment.

    """
    return "{0}.{1}.{2}.{3}".format(name, version, package, typeof).lower()


def get_types(name=None, version=None):
    """Returns set of supported types.

    :param str name: Ontology name, e.g. cim.
    :param str version: Ontology version, e.g. 1.

    :returns: A tuple of supported types.
    :rtype: tuple

    """
    result = ()

    for o in type_info.ONTOLOGIES:
        if name is None or name == o.NAME:
            for v in o.VERSIONS:
                if version is None or version == v.ID:
                    result += v.type_info.TYPES

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
    return type_info.KEYS.values()


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
    return type_info.KEYS.get(doc_type, None)


def get_type_sortkey(doc_type):
    """Returns a document type sort key.

    :param class doc_type: A document type for which meta-information is to be returned.

    :returns: A type sort key (if found).
    :rtype: str

    """
    return type_info.SORT_KEYS.get(doc_type, u"")


def get_type_from_key(key):
    """Returns a type if supported.

    :param str key: Type key, e.g. cim.1.software.ModelComponent.

    :returns: A type (if found).
    :rtype: class or None

    """
    type_key = str(key).lower()
    for t in type_info.TYPES:
        if type_info.KEYS[t].lower() == type_key:
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
    for name, typeof, value in type_info.CONSTRAINTS[doc_type]:
        result[name].add((typeof, value))

    return result.items()


def get_constraint(constraints, constraint_type):
    """Returns first constraint within collection of the matching type.

    :param list constraints: A collection of constraints.
    :param str constraint_type: Type of constraint.

    :returns: Constrain meta-information.
    :rtype: tuple

    """
    for typeof, value in constraints:
        if typeof == constraint_type:
            return value


def get_constraints(doc_type, type_filter=None):
    """Returns constraints associated with a type.

    :param class doc_type: A document type for which meta-information is to be returned.
    :param str type_filtre: A constraint type filter.

    :returns: Type meta-information.
    :rtype: tuple

    """
    if type_filter:
        return [ct for ct in type_info.CONSTRAINTS[doc_type] if ct[1] == type_filter]

    return type_info.CONSTRAINTS[doc_type]


def get_property_constraint(container, name, typeof):
    """Returns property constraints associated with a type instance.

    :param class container: A document instance for which meta-information is to be returned.
    :param str name: Property name.
    :param str typeof: Type of property constraint to be returned.

    :returns: Constraint meta-information.
    :rtype: tuple

    """
    return get_constraint(type_info.CONSTRAINTS[type(container), name], typeof)


def get_property_constraints(container, name):
    """Returns property constraints associated with a type instance.

    :param class container: A document instance for which meta-information is to be returned.
    :param str name: Property name.

    :returns: Constraint meta-information.
    :rtype: tuple

    """
    constraints = type_info.CONSTRAINTS[type(container), name]

    return get_constraint(constraints, constants.CONSTRAINT_TYPE_CARDINALITY), \
           get_constraint(constraints, constants.CONSTRAINT_TYPE_TYPEOF), \
           get_constraint(constraints, constants.CONSTRAINT_TYPE_CONSTANT), \
           get_constraint(constraints, constants.CONSTRAINT_TYPE_REGEX)


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
