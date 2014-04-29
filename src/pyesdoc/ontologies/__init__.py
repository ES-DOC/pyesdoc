"""
.. module:: pyesdoc.ontologies.__init__.py
   :copyright: Copyright "Jun 14, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Ontologies sub-package init.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import cim
from .. utils import runtime as rt



# Set of registered ontologies.
ONTOLOGIES = ()

# Set of ontologies supported out of the box.
_DEFAULT_ONTOLOGIES = (cim,)

# Set of registered types.
TYPES = ()


def get_type_key(name, version, package, type):
    """Returns type key.

    :param name: Ontology name, e.g. cim.
    :type name: str

    :param version: Ontology version, e.g. 1.
    :type version: str

    :param package: Ontology package, e.g. activity.
    :type package: str

    :param type: Ontology type, e.g. Experiment.
    :type type: str

    """
    return "{0}.{1}.{2}.{3}".format(name, version, package, type).lower()


def register(o):
    """Registers an ontology for use.

    :param o: Ontology being registered.
    :type o: module

    """
    global ONTOLOGIES
    global TYPES

    if o not in ONTOLOGIES:
        ONTOLOGIES += (o,)
        for v in o.VERSIONS:
            TYPES += v.TYPES


# Auto register default ontologies.
for o in _DEFAULT_ONTOLOGIES:
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

    for o in ONTOLOGIES:
        if name is None or name == o.NAME:
            for v in o.VERSIONS:
                if version is None or version == v.ID:
                    result += v.TYPES

    return result


def list_types(name=None, version=None):
    """Returns list of supported type keys and types.

    :param name: Ontology name, e.g. cim.
    :type name: str

    :param version: Ontology version, e.g. 1.
    :type version: str

    :returns: A tuple of supported typekeys and types.
    :rtype: tuple

    """
    types = get_types(name, version)
    types = [tuple(t.type_key.split('.')) for t in types]

    return tuple(types)


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
    type_key = get_type_key(name, version, package, type)

    return get_type_from_key(type_key)


def get_type_from_key(key):
    """Returns a type if supported.

    :param key: Type key, e.g. cim.1.software.ModelComponent.
    :type key: str

    :returns: A type (if found).
    :rtype: class or None

    """
    type_key = str(key).lower()
    for t in TYPES:
        if t.type_key.lower() == type_key:
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
       raise ValueError("The ontology package and type are unspecified.")

    if package is None and type is None:
        return len(get_types(name, version)) > 0
    else:
        return get_type(name, version, package, type) is not None


def create(name, version, package, type):
    """Creates a document.

    :param name: Ontology name, e.g. cim.
    :type name: str

    :param version: Ontology version, e.g. 1.
    :type version: str

    :param package: Ontology package, e.g. activity.
    :type package: str

    :param type: Ontology type, e.g. Experiment.
    :type type: str

    :returns: A pyesdoc document instance.
    :rtype: pyesdoc object

    """
    type = get_type(name, version, package, type)

    return None if type is None else type()


def get_type_info(doc_type):
    """Returns meta-information associated with a type.

    :param class doc_type: A document type for which meta-information is to be returned.

    :returns: Type meta-information.
    :rtype: tuple

    """
    ti = doc_type.type_info
    for base in doc_type.__bases__:
        if base in TYPES:
            ti += get_type_info(base)

    return ti


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
    rt.assert_doc("left", left)
    rt.assert_doc("right", right)
    if not hasattr(left, attr):
        rt.throw("Cannot set association upon invalid attribute.")

    # Create reference.
    # TODO alter reference based upon ontology type.
    ref = cim.v1.DocReference()
    ref.id = right.meta.id
    ref.version = right.meta.version

    # Set association.
    setattr(left, attr, ref)

    return ref