from . cim_v1.model_component.indexer import index as index_model
from . cim_v1.numerical_experiment.indexer import index as index_experiment
from .. import (
    cache,
    dao,
    models,
    utils
    )
from ...utils import runtime as rt



# Project whose facets are being indexed.
_PROJECT = "CMIP5"

# Encoding used to load documents.
_ENCODING = "json"

# Ontology used to load documents.
_ONTOLOGY = "cim.1"

# Ontology used to load documents.
_LANGUAGE = "en"

# CIM type helper vars.
_CIM_V1_EXPERIMENT = "cim.1.activity.numericalexperiment"
_CIM_V1_MODEL = "cim.1.software.modelcomponent"


class _ProcessingContextInfo(object):
    """Encapsulates processing context information."""
    def __init__(self):
        self.encoding = None
        self.experiments = []
        self.language = None
        self.models = []
        self.ontology = None
        self.project = None


def _init(ctx):
    """Initializes processing context."""
    ctx.project = cache.get_project(_PROJECT)
    ctx.encoding = cache.get_doc_encoding(_ENCODING)
    ctx.language = cache.get_doc_language(_LANGUAGE)
    ctx.ontology = cache.get_doc_ontology(_ONTOLOGY)


def _load_docs(ctx):
    """Loads documents to be indexed."""

    def get_docs(doc_type):
        """Gets documents filtered by document type."""
        # return dao.get_document_by_type(ctx.project.ID, doc_type, False)[:1]
        return dao.get_document_by_type(ctx.project.ID, doc_type, False)


    def decode(docs):
        """Gets decoded document collection."""
        docs = map(lambda doc: utils.get_pyesdoc(
            doc,
            ctx.ontology,
            ctx.encoding,
            ctx.language), docs)

        return sorted(docs, key=lambda doc: doc.short_name.upper())


    def get_collection(doc_type, key_formatter):
        """Gets document collection for processing."""
        collection = {}
        for doc in get_docs(doc_type):
            key = key_formatter(doc)
            if key not in collection or \
               doc.Version > collection[key].Version:
                collection[key] = doc

        return decode(collection.values())


    def get_key(doc):
        """Returns document key."""
        institute = cache.get_name(models.Institute, doc.Institute_ID)
        name = doc.Name.upper()

        return "{0}--{1}".format(institute, name)


    ctx.experiments = get_collection(_CIM_V1_EXPERIMENT, get_key)
    ctx.models = get_collection(_CIM_V1_MODEL, get_key)


def _index(ctx):
    """Indexes loaded documents."""
    def build(collection, indexer):
        """Builds index."""
        for doc in collection:
            indexer(ctx.project.ID, doc)

    build(ctx.experiments, index_experiment)
    build(ctx.models, index_model)


def execute():
    """Executes facet indexing from cmip5 project."""
    ctx = _ProcessingContextInfo()
    for func, msg in (
        (_init, "initializing context"),
        (_load_docs, "loading documents"),
        (_index, "building indexes"),
        ):
        rt.log("INDEXING :: {0} :: {1}".format(_PROJECT, msg))
        func(ctx)