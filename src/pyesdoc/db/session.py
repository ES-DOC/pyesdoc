"""
.. module:: db.session.py
   :platform: Unix
   :synopsis: Repository connection manager.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

# Module imports.
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy.schema import CreateSchema

from . import models



# Module exports.
__all__ = [
    'assert_is_live',
    'commit',
    'create_repo',
    'do_ingest',
    'delete',
    'end',
    'insert',
    'query',
    'QUERY_LIMIT',
    'rollback',
    'start',
]


# Default query limit to apply.
QUERY_LIMIT = 200


class _State(object):
    """Encpasulates mutable module state.

    """
    # SQLAlchemy engine.
    sa_engine = None

    # SQLAlchemy session.
    sa_session = None


# Set sqlalchemy logging.
loggers = [
    ('sqlalchemy.dialects', logging.NOTSET),
    ('sqlalchemy.engine', logging.NOTSET),
    ('sqlalchemy.orm', logging.NOTSET),
    ('sqlalchemy.pool', logging.NOTSET)
]
logging.basicConfig()
for logger, level in loggers:
    logging.getLogger(logger).setLevel(level)


def assert_is_live():
    """Ensures that session has been established.

    """
    assert _State.sa_session is not None
    assert _State.sa_engine is not None


def assert_is_dead():
    """Ensures that session has been ended.

    """
    assert _State.sa_session is None
    assert _State.sa_engine is None


def create_repo():
    """Creates a repo.

    """
    # Create schemas.
    for p in models.PARTITIONS:
        _State.sa_engine.execute(CreateSchema(p))

    # Create tables.
    models.metadata.create_all(_State.sa_engine)

    # Seed tables.
    from .init import execute as seed_db
    seed_db()


def do_ingest():
    """Executes an ingestion.

    """
    from . import ingest

    # Invoke ingestor.
    ingest.execute()


def create(connection):
    """Creates a repo session.

    :param str connection: Repoistory connection string.

    """
    # Set engine.
    sa_engine = create_engine(unicode(connection), echo=False)

    # Set session.
    sa_session = sessionmaker(bind=sa_engine)()

    # Setup ORM binding.
    models.metadata.bind = sa_engine

    return sa_session


def start(connection=None):
    """Starts a repo session.

    :param connection: Repoistory connection string.
    :type connection: str

    """
    # Implicit end.
    end()

    # Connect (when instructed).
    if connection is not None:
        # Set engine.
        if isinstance(connection, Engine):
            _State.sa_engine = connection
        else:
            _State.sa_engine = create_engine(unicode(connection), echo=False)

        # Set session.
        _State.sa_session = sessionmaker(bind=_State.sa_engine)()

        # Setup ORM binding.
        models.metadata.bind = _State.sa_engine


def end():
    """Ends a session.

    """
    if _State.sa_engine is not None:
        _State.sa_engine = None
        models.metadata.bind = None
    if _State.sa_session is not None:
        _State.sa_session.close()
        _State.sa_session = None


def commit():
    """Commits a session.

    """
    if _State.sa_session is not None:
        _State.sa_session.commit()


def rollback():
    """Rolls back a session.

    """
    if _State.sa_session is not None:
        _State.sa_session.rollback()


def insert(instance, auto_commit=True):
    """Adds a newly created instance to the session and optionally commits the session.

    """
    if instance is not None and _State.sa_session is not None:
        _State.sa_session.add(instance)
        if auto_commit:
            commit()


def delete(instance, auto_commit=True):
    """Marks an instance for deletion and optionally commits the session.

    :param instance: An instance of an ES-DOC API domain model.
    :type instance: A sub-class of db.models.Entity

    :param auto_commit: Flag indicating whether to automatically issue a commit.
    :type auto_commit: bool

    """
    if instance is not None and _State.sa_session is not None:
        _State.sa_session.delete(instance)
        if auto_commit:
            commit()


def query(*args):
    """Intitiates a query operation against current session.

    :param type: The model type to be queried.
    :type type: class

    """
    if _State.sa_session is None:
        return None

    return _State.sa_session.query(*args)


def log():
    print _State.sa_engine

