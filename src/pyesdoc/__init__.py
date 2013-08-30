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

import ontologies as ontologies
import serialization as serialization
import utils as utils
import validation as validation
from serialization import (
    ESDOC_ENCODING_DICT,
    ESDOC_ENCODING_JSON,
    ESDOC_ENCODING_XML,
    METAFOR_CIM_XML_ENCODING
    )


# Module exports.
__all__ = [
    'create',
    'decode',
    'encode',
    'is_supported_ontology',
    'is_supported_type',
    'is_valid',
    'list_types',
    'ontologies',
    'publish',
    'retrieve',
    'unpublish',
    'validate',
]




def _raise(msg):
    """Raise exception."""
    raise utils.PYESDOC_Exception(msg)


def _assert_ontology(ontology_name, ontology_version):
    """Asserts ontology name/version."""
    if not ontologies.is_supported(ontology_name, ontology_version):
        msg = "Ontology {0} v{1} is unsupported."
        msg = msg.format(ontology_name, ontology_version)
        _raise(msg)


def _assert_type(ontology_name, ontology_version, type_name):
    """Asserts document type."""
    if not ontologies.is_supported(ontology_name, ontology_version, type_name):
        msg = "Type {0}.v{1}.{2} is unsupported."
        msg = msg.format(ontology_name, ontology_version, type_name)
        _raise(msg)


def _assert_document(instance, msg):
    """Asserts document instance."""
    if instance is None:
        _raise(msg if msg is not None else "Document instance is null.")


def _assert_representation(representation, msg):
    """Asserts document representation."""
    if representation is None:
        _raise(msg if msg is not None else "Document representation is null.")


def decode(representation, encoding):
    """Decodes a pyesdoc document representation.

    :param representation: A document representation (e.g. json).
    :type representation: str

    :param encoding: A document encoding (dict|json|xml|metafor-cim-1-xml).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    _assert_representation(representation, "Documents cannot be decoded from null objects.")

    return serialization.decode(representation, encoding)


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


def publish(document):
    """Publishes an instance to remote API.

    :param document: A pyesdoc document instance.
    :type document: object

    """
    # Defensive programming.
    _assert_document(document, "Cannot publish null documents.")
    if not is_valid(document):
        _raise("Cannot publish invalid documents.")

    # TODO invoke internal module to publish to remote API.
    raise NotImplementedError("TODO - publish instance")


def unpublish(document):
    """Unpublishes a document from remote API.

    :param document: A pyesdoc document instance.
    :type document: object
    
    """
    # Defensive programming.
    _assert_document(document, "Cannot unpublish null documents.")

    # TODO invoke internal module to unpublish document from remote API.
    raise NotImplementedError("TODO - unpublish document")


def retrieve(uid, version):
    """Retrieves a document instance from remote repository.

    :param uid: Document UID.
    :type uid: uuid.uuid

    :param version: Document version.
    :type version: int


    """
    # Defensive programming.
    if uuid is None or not isinstance(uid, uuid.UUID):
        _raise("Invalid document unique identifier.")
    if version is None or not isinstance(version, int):
        _raise("Invalid document version.")

    # TODO invoke internal module to retrieve from remote API.
    raise NotImplementedError("TODO - unpublish instance")


def list_types(ontology_name=None, ontology_version=None):
    """Lists the set of supported document types, optionally filtered by ontology name & version.

    :param ontology_name: Name of a supported ontology (e.g. CIM).
    :type ontology_name: str

    :param ontology_version: Version of a supported ontology (e.g. v1).
    :type ontology_version: str

    :returns: List of supported document types.
    :rtype: list
    
    """
    return ontologies.list(ontology_name, ontology_version)


def is_supported_ontology(ontology_name, ontology_version):
    """Returns a flag indicating whether an ontology is supported or not.

    :param ontology_name: Name of a supported ontology (e.g. CIM).
    :type ontology_name: str

    :param ontology_version: Version of a supported ontology (e.g. v1).
    :type ontology_version: str

    :returns: True if supported, false otherwise.
    :rtype: bool

    """
    return ontologies.is_supported(ontology_name, ontology_version)


def is_supported_type(ontology_name, ontology_version, type_name=None):
    """Returns a flag indicating whether a type is supported or not.

    :param ontology_name: Name of a supported ontology (e.g. CIM).
    :type ontology_name: str

    :param ontology_version: Version of a supported ontology (e.g. v1).
    :type ontology_version: str

    :param type_name: Name of a supported type (e.g. model).
    :type type_name: str

    :returns: True if supported, false otherwise.
    :rtype: bool

    """
    return ontologies.is_supported(ontology_name, ontology_version, type_name)


def create(ontology_name, ontology_version, type_name):
    """Creates a document.

    :param ontology_name: Name of a supported ontology (e.g. CIM).
    :type ontology_name: str

    :param ontology_version: Version of a supported ontology (e.g. v1).
    :type ontology_version: str

    :param type_name: Name of a supported type (e.g. model).
    :type type_name: str

    :returns: A pyesdoc document instance.
    :rtype: pyesdoc object

    """
    # Defensive programming.
    _assert_type(ontology_name, ontology_version, type_name)

    return ontologies.create(ontology_name, ontology_version, type_name)


def validate(document):
    """Validates a document.

    :param document: A pyesdoc document instance.
    :type document: object

    :returns: A list of validation errors.
    :rtype: list

    """
    # Defensive programming.
    _assert_document(document, "Cannot validate null documents.")

    raise NotImplementedError("TODO - validate document")


def is_valid(document):
    """Validates a document.

    :param document: A pyesdoc document instance.
    :type document: object

    :returns: Either True or False depending upon the document's validation state.
    :rtype: bool

    """
    return not bool(validate(document))
