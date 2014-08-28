"""
.. module:: core.py
   :platform: Unix
   :synopsis: Set of core repo data access operations.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import inspect

import sqlalchemy as sa

from .. import (
    models,
    session
    )
from ...utils import runtime as rt


# Module exports.
__all__ = [
    'delete',
    'delete_by_type',
    'delete_by_facet',
    'delete_by_id',
    'delete_by_name',
    'get_active',
    'get_all',
    'get_by_facet',
    'get_by_id',
    'get_by_name',
    'get_count',
    'get_inactive',
    'insert',
    'sort'
]



def sort(type, collection):
    """Sorts collection via type sort key.

    :param type: A supported entity type.
    :type type: class

    :param collection: Collection of entities.
    :type collection: list

    :returns: Sorted collection.
    :rtype: list

    """
    # Defensive programming.
    models.assert_type(type)

    return [] if collection is None else type.get_sorted(collection)


def _get_active(type, is_active_state):
    """Gets instances filtered by their IsActive state.

    :param type: A supported entity type.
    :type type: class

    :param is_active_state: Entity IsActive field value.
    :type is_active_state: bool

    :returns: Entity collection.
    :rtype: list

    """
    # Defensive programming.
    models.assert_type(type)

    return get_by_facet(type, type.IsActive==is_active_state, get_iterable=True)


def get_active(type):
    """Gets all active instances.

    :param type: A supported entity type.
    :type type: class

    :returns: Active entity collection.
    :rtype: list

    """
    return _get_active(type, True)


def get_inactive(type):
    """Gets all inactive instances.

    :param type: A supported entity type.
    :type type: class

    :returns: Inactive entity collection.
    :rtype: list

    """
    return _get_active(type, False)


def get_all(mtype):
    """Gets all instances of the entity.

    :param class mtype: A supported entity type.

    :returns: Entity collection.
    :rtype: list

    """
    return get_by_facet(mtype, None, get_iterable=True)


def get_by_facet(mtype,
                 filter,
                 order_by=None,
                 get_iterable=False):
    """Gets entity instance by facet.

    :param class mtype: A supported entity type.

    :param filter: Filter expression.
    :type filter: expression

    :param order_by: Sort expression.
    :type order_by: expression

    :param get_iterable: Flag indicating whether to return an iterable or not.
    :type get_iterable: bool

    :returns: Entity or entity collection.
    :rtype: Sub-class of db.models.Entity

    """
    # Defensive programming.
    models.assert_type(mtype)

    q = session.query(mtype)
    if filter is not None:
        if inspect.isfunction(filter):
            filter(q)
        else:
            q = q.filter(filter)
    if order_by is not None:
        if inspect.isfunction(order_by):
            order_by(q)
        else:
            q = q.order_by(order_by)

    # Return accordingly.
    # ... first
    if not get_iterable:
        return q.first()
    # ... sorted collection
    elif order_by is None:
        return sort(mtype, q.all())
    # ... ordered collection
    else:
        return q.all()


def get_by_id(type, id):
    """Gets entity instance by id.

    :param type: A supported entity type.
    :type type: class

    :param id: ID of entity.
    :type id: int

    :returns: Entity with matching ID.
    :rtype: Sub-class of db.models.Entity

    """
    return get_by_facet(type, type.ID==id)


def get_by_name(type, name):
    """Gets an entity instance by it's name.

    :param type: A supported entity type.
    :type type: class

    :param name: Name of entity.
    :type name: str

    :returns: Entity with matching name.
    :rtype: Sub-class of db.models.Entity

    """
    return get_by_facet(type, sa.func.upper(type.Name)==name.upper())


def get_count(mtype, filter=None):
    """Gets count of entity instances.

    :param class mtype: A supported entity type.
    :param function filter: A filter function to be applied.

    :returns: Entity collection count.
    :rtype: int

    """
    # Defensive programming.
    models.assert_type(mtype)

    q = session.query(mtype)
    if filter is not None:
        q = q.filter(filter)

    return q.count()


def insert(target):
    """Marks target instance(s) for insertion.

    :param target: Target instance(s) for insertion.
    :type target: Sub-class of db.models.Entity or list

    """
    if rt.is_iterable(target):
        models.assert_iter(target)
        for target in target:
            session.insert(target)
    else:
        models.assert_instance(target)
        session.insert(target)


def delete(target):
    """Marks target instance(s) for deletion.

    :param target: Target instance(s) for deletion.
    :type target: Sub-class of db.models.Entity or list

    """
    if rt.is_iterable(target):
        models.assert_iter(target)
        for target in target:
            session.delete(target)
    else:
        models.assert_instance(target)
        session.delete(target)


def delete_by_type(mtype, callback=None):
    """Deletes all entities of passed type.

    :param class mtype: A supported entity type.
    :param function callback: Pointer to a function that will perform callback.

    """
    # Defensive programming.
    models.assert_type(mtype)

    if callback is None:
        delete_by_facet(mtype, mtype.ID>0)
    else:
        for instance in get_all(mtype):
            callback(instance.ID)


def delete_by_facet(type, filter):
    """Delete entity instance by id.

    :param type: A supported entity type.
    :type type: class

    :param filter: Filter to apply.
    :type filter: expression or functino pointer

    """
    # Defensive programming.
    models.assert_type(type)

    q = session.query(type)
    if inspect.isfunction(filter):
        filter(q)
    else:
        q = q.filter(filter)
    q.delete()


def delete_by_id(type, id):
    """Delete entity instance by id.

    :param type: A supported entity type.
    :type type: class

    :param id: ID of entity.
    :type id: int

    """
    delete_by_facet(type, type.ID==id)


def delete_by_name(type, name):
    """Deletes an entity instance by it's name.

    :param type: A supported entity type.
    :type type: class

    :param name: Name of entity.
    :type name: str

    """
    delete_by_facet(type, type.Name==name)
