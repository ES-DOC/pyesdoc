# Module imports.
from . import (
    execute_cmip5,
    execute_core,
    )
from .. import (
    cache,
    dao,
    models,
    session
    )
from ...utils import runtime as rt



# Set of model types updated during indexing.
_MODEL_TYPES = (
    models.Node,
    models.NodeField,
    )

# Set of indexers keyed by project.
_indexers = {
    'cmip5': execute_cmip5
}


def _log(msg):
    """Writes a log message."""
    rt.log("INDEXING :: {0} ...".format(msg))


def _log_stats():
    """Writes facet stats to log."""
    for ntype in models.NODE_TYPES:
        print ntype, dao.get_node_count(type_of=ntype)


def _reset():
    """Resets data."""
    for mtype in _MODEL_TYPES:
        dao.delete_by_type(mtype)


def do(reset=False):
    """Executes node indexation process.

    :param bool reset: Flag indicating whether indexation will also be reset.

    """
    _log("starts")

    _log("initialising cache")
    cache.load()

    if reset:
        _log("resetting existing facets")
        _reset()

    _log("building new facets")
    # for indexer in [execute_core]:
    for indexer in [execute_core] + _indexers.values():
        indexer.execute()

    _log("logging stats")
    _log_stats()

