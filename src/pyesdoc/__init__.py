"""
.. module:: pyesdoc.__init__.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Package initialisor.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""
# Module imports.
import uuid

from . import ontologies
from . import publishing
from . import serialization
from . import utils
from . import validation
from publishing import (
    ESDOC_DOC_VERSION_LATEST,
    ESDOC_DOC_VERSION_ALL
    )
from serialization import (
    ESDOC_ENCODINGS,
    ESDOC_ENCODINGS_CUSTOM,
    ESDOC_ENCODING_DICT,
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML,
    METAFOR_CIM_XML_ENCODING
    )
from utils import PYESDOC_Exception


# Module exports.
__all__ = [
    'create',
    'decode',
    'encode',
    'ESDOC_DEFAULT_ENCODING',
    'ESDOC_DEFAULT_LANGUAGE',
    'ESDOC_DOC_VERSION_LATEST',
    'ESDOC_DOC_VERSION_ALL',
    'ESDOC_ENCODINGS',
    'ESDOC_ENCODINGS_CUSTOM',
    'ESDOC_ENCODING_DICT',
    'ESDOC_ENCODING_JSON',
    'ESDOC_ENCODING_XML',
    'set_option',
    'is_supported',
    'is_valid',
    'list_types',
    'METAFOR_CIM_XML_ENCODING',
    'ontologies',
    'publish',
    'PYESDOC_Exception',
    'retrieve',
    'set_option',
    'unpublish',
    'validate',
]



# Default language.
ESDOC_DEFAULT_LANGUAGE = 'en'

# Default encoding.
ESDOC_DEFAULT_ENCODING = ESDOC_ENCODING_JSON


def _assert_document(instance, msg):
    """Asserts document instance."""
    if instance is None:
        _raise(msg if msg is not None else "Document instance is null.")


def _assert_ontology(n, v):
    """Asserts ontology name/version."""
    if not ontologies.is_supported(n, v):
        _raise("Ontology {0} v{1} is unsupported.".format(n, v))


def _assert_type(o, v, p, t):
    """Asserts document type."""
    if not ontologies.is_supported(o, v, p, t):
        _raise("Type {0}.v{1}.{2} is unsupported.".format(o, v, p, t))


def _assert_representation(representation, msg):
    """Asserts document representation."""
    if representation is None:
        _raise(msg if msg is not None else "Document representation is null.")


def _raise(msg):
    """Raise exception."""
    raise utils.PYESDOC_Exception(msg)


def _set_doc_info_attribute(doc, name, value):
    """Sets an attribute upon the doc_info object."""
    _assert_document(doc, "Cannot set values upon null documents.")

    setattr(doc.doc_info, name, str(value).lower())


def decode(repr, encoding):
    """Decodes a pyesdoc document representation.

    :param repr: A document representation (e.g. json).
    :type repr: str

    :param encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    _assert_representation(repr, "Documents cannot be decoded from null objects.")

    return serialization.decode(repr, encoding)


def encode(doc, encoding):
    """Encodes a pyesdoc document instance.

    :param doc: pyesdoc document instance.
    :type doc: object

    :param encoding: A document encoding (dict|json|xml).
    :type encoding: str

    :returns: A pyesdoc document representation.
    :rtype: unicode | dict

    """
    # Defensive programming.
    _assert_document(doc, "Cannot encode null documents.")

    return serialization.encode(doc, encoding)


def publish(doc):
    """Publishes an instance to remote API.

    :param document: A pyesdoc document instance.
    :type document: object

    """
    # Defensive programming.
    _assert_document(doc, "Cannot publish null documents.")
    if not is_valid(doc):
        _raise("Cannot publish invalid documents.")

    return publishing.publish(doc)


def unpublish(uid, version=ESDOC_DOC_VERSION_ALL):
    """Unpublishes a document from remote API.

    :param uid: Document UID.
    :type uid: uuid.UUID

    :param version: Document version.
    :type version: int | str
    
    """
    # Defensive programming.
    if not isinstance(uid, uuid.UUID):
        _raise("Invalid document uid (must be an instance of uuid.UUID).")
    if not version == ESDOC_DOC_VERSION_ALL and \
       not version == ESDOC_DOC_VERSION_LATEST and \
       not isinstance(version, int):
        _raise("Invalid document version (must be either 'all', 'latest' or an integer.")
        
    return publishing.unpublish(uid, version)


def retrieve(uid, version=ESDOC_DOC_VERSION_LATEST):
    """Retrieves a document instance from remote repository.

    :param uid: Document UID.
    :type uid: uuid.UUID

    :param version: Document version.
    :type version: int | str

    """
    # Defensive programming.
    if not isinstance(uid, uuid.UUID):
        _raise("Invalid document uid (must be an instance of uuid.UUID).")
    if version != ESDOC_DOC_VERSION_LATEST and not isinstance(version, int):
        _raise("Invalid document version (must be either 'latest' or an integer.")
        
    return publishing.retrieve(uid, version)


def list_types(ontology_name=None, ontology_version=None):
    """Lists the set of supported document types, optionally filtered by ontology name & version.

    :param ontology_name: Name of a supported ontology (e.g. CIM).
    :type ontology_name: str

    :param ontology_version: Version of a supported ontology (e.g. v1).
    :type ontology_version: str

    :returns: List of supported document types.
    :rtype: list
    
    """    
    return ontologies.list_types(ontology_name, ontology_version)


def is_supported(ontology_name,
                 ontology_version,
                 ontology_package=None,
                 ontology_type=None):
    """Returns a flag indicating whether an ontology is supported or not.

    :param ontology_name: Ontology name, e.g. cim.
    :type ontology_name: str

    :param ontology_version: Ontology version, e.g. 1.
    :type ontology_version: str

    :param ontology_package: Ontology package, e.g. activity.
    :type ontology_package: str

    :param ontology_type: Ontology type, e.g. Experiment.
    :type ontology_type: str

    :returns: True if supported, false otherwise.
    :rtype: bool

    """    
    return ontologies.is_supported(ontology_name, 
                                   ontology_version,
                                   ontology_package,
                                   ontology_type)


def create(ontology_name, 
           ontology_version,
           ontology_package,
           ontology_type):
    """Creates a document.

    :param ontology_name: Ontology name, e.g. cim.
    :type ontology_name: str

    :param ontology_version: Ontology version, e.g. 1.
    :type ontology_version: str

    :param ontology_package: Ontology package, e.g. activity.
    :type ontology_package: str

    :param ontology_type: Ontology type, e.g. Experiment.
    :type ontology_type: str

    :returns: A pyesdoc document instance.
    :rtype: pyesdoc object

    """
    # Defensive programming.
    _assert_type(ontology_name, ontology_version, ontology_package, ontology_type)

    doc = ontologies.create(ontology_name,
                            ontology_version,
                            ontology_package,
                            ontology_type)

    # Auto assign defaults if dealing with a publishable document.
    if hasattr(doc, 'doc_info'):
        set_language(doc, ESDOC_DEFAULT_LANGUAGE)

    return doc


def set_language(doc, language):
    """Sets a document's language code.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :param language: A language code.
    :type language: str

    """
    _set_doc_info_attribute(doc, 'language', language)


def set_project(doc, project):
    """Sets a document's project code.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :param project: A project code.
    :type project: str

    """
    _set_doc_info_attribute(doc, 'project', project)


def set_institute(doc, institute):
    """Sets a document's institute code.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :param institute: An institute code.
    :type institute: str

    """
    _set_doc_info_attribute(doc, 'institute', institute)


def validate(doc):
    """Validates a document.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :returns: A list of validation errors.
    :rtype: list

    """
    # Defensive programming.
    _assert_document(doc, "Cannot validate null documents.")

    # TODO - validate against validation
    return validation.validate(doc)


def is_valid(doc):
    """Validates a document.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :returns: Either True or False depending upon the document's validation state.
    :rtype: bool

    """
    return len(validate(doc)) == 0


def set_option(name, value):
    """Sets a library option.

    :param name: Option name.
    :type name: str

    :param value: Option value.
    :type value: str

    """
    if name not in _OPTIONS:
        _raise("pyesdoc option is unsupported :: option = {0}.".format(name))

    _OPTIONS[name] = str(value)
