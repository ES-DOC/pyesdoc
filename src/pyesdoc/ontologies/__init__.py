"""
.. module:: pyesdoc.ontologies.__init__.py
   :copyright: Copyright "Jun 14, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Ontologies sub-package init.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import cim


# Set of ontologies supported out of the box.
_defaults = (cim,)


class _State(object):
    """Module state bag.

    """
    # Set of supported ontologies.
    ontologies = []


def _get_type_key(o, v, p, t):
    """Returns type key."""
    return "{0}.{1}.{2}.{3}".format(o, v, p, t)


def register(o):
    """Registers an ontology for use.

    :param o: Ontology being registered.
    :type o: module

    """
    if o not in _State.ontologies:
        _State.ontologies.append(o)


# Auto register default ontologies.
for o in _defaults:
    register(o)

    
def get_types(name=None, version=None):
    """Returns set of supported types.

    :param name: Ontology name, e.g. cim.
    :type name: str

    :param version: Ontology version, e.g. 1.
    :type version: str

    :returns: A tuple of supported types.
    :rtype: tuple

    """
    result = ()

    for o in _State.ontologies:
        if name is None or name == o.NAME:
            for v in o.VERSIONS:
                if version is None or version == v.ID:
                    result += v.TYPES

    return result


def get_type(name, version, package, type):
    """Returns a type if supported.

    :param name: Ontology name, e.g. cim.
    :type name: str

    :param version: Ontology version, e.g. 1.
    :type version: str

    :param package: Ontology package, e.g. activity.
    :type package: str

    :param type: Ontology type, e.g. Experiment.
    :type type: str

    :returns: A type (if found).
    :rtype: class or None

    """
    type_key = _get_type_key(name, version, package, type)
    for t in get_types(name, version):
        if t.type_key == type_key:
            return t

    return None


def is_supported(name, version, package=None, type=None):
    """Returns a flag indicating whether ontology/type is supported.

    :param name: Ontology name, e.g. cim.
    :type name: str

    :param version: Ontology version, e.g. 1.
    :type version: str

    :param package: Ontology package, e.g. activity.
    :type package: str

    :param type: Ontology type, e.g. Experiment.
    :type type: str

    :returns: A flag indicating whether ontology is supported.
    :rtype: bool

    """
    if (package is not None and type is None) or \
       (package is None and type is not None):
       raise ValueError("Both pakcage and type must be specified.")

    if package is None and type is None:
        return len(get_types(name, version)) > 0
    else:
        return get_type(name, version, package, type) is not None



def get_type_info(type, types=get_types()):
    """Returns meta-information associated with a type.

    :param type: A type for which meta-information is to be returned.
    :type type: class

    :returns: Type meta-information.
    :rtype: tuple
    
    """
    ti = type.type_info
    for base in type.__bases__:
        if base in types:
            ti += get_type_info(base, types)

    return ti