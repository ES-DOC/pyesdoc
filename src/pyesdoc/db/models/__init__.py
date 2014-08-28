"""
.. module:: __init__.py
   :copyright: Copyright "Jun 29, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of database models supported by ES-DOC API.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from . utils import (
    Entity,
    EntityConvertor,
    metadata
    )
from . docs import (
    Document,
    DocumentDRS,
    DocumentExternalID,
    DocumentSummary,
    DOCUMENT_VERSIONS,
    DOCUMENT_VERSION_LATEST,
    DOCUMENT_VERSION_ALL
    )
from . facets import (
    Node,
    NodeField,
    NODE_TYPES,
    NODE_TYPE_INSTITUTE,
    NODE_TYPE_PROJECT,
    NODE_TYPE_EXPERIMENT,
    NODE_TYPE_MODEL,
    NODE_TYPE_MODEL_COMPONENT,
    NODE_TYPE_MODEL_COMPONENT_PROPERTY,
    NODE_TYPE_MODEL_COMPONENT_PROPERTY_VALUE,
    NODE_TYPE_MODEL_PROPERTY,
    NODE_TYPE_MODEL_PROPERTY_VALUE,
    )
from . vocab import (
    DocumentEncoding,
    DocumentLanguage,
    DocumentOntology,
    DocumentType,
    DOCUMENT_TYPE_ALL,
    Institute,
    Project
)
from ...utils import runtime as rt



# Set of supported model domain partiions (maps to db schemas).
PARTITIONS = set([
    'docs',
    'facets',
    'vocab'
    ])

# Set of supported model types - useful for testing scenarios.
SUPPORTED_TYPES = (
    # ... docs
    Document,
    DocumentDRS,
    DocumentExternalID,
    DocumentSummary,
    # ... facets
    Node,
    NodeField,
    # ... vocab
    DocumentEncoding,
    DocumentLanguage,
    DocumentOntology,
    DocumentType,
    Institute,
    Project
)

# Supported cacheable types.
CACHEABLE_TYPES = (
    DocumentEncoding,
    DocumentLanguage,
    DocumentOntology,
    DocumentType,
    Institute,
    Project,
    NodeField,
    )

# Expose entity conversion methods.
to_dict = EntityConvertor.to_dict
to_dict_for_json = EntityConvertor.to_dict_for_json
to_json = EntityConvertor.to_json
to_string = EntityConvertor.to_string


# Runtime support functions.
def assert_type(mtype):
    """Asserts that passed model type is supported.

    :param class type: A supported entity type.

    """

    def get_msg():
        """Returns error message."""
        return "Unsupported model type ({0}).".format(mtype.__class__.__name__)

    rt.assert_iter_item(SUPPORTED_TYPES, mtype, get_msg)


def assert_instance(instance):
    """Asserts that passed model instance is of a supported type.

    :param Entity instance: A model instance being processed.

    """
    assert_type(instance.__class__)


def assert_iter(collection):
    """Asserts that all collection models instances are of a supported type.

    :param iterable collection: A collection of model instance.

    """
    for instance in collection:
        assert_instance(instance)
