"""
.. module:: core.py
   :copyright: Copyright "Jun 12, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Core caching functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import random

from .. import (
    dao,
    models
    )



# Cache.
_cache = {}


def load(mtype=None):
    """Loads cache.

    """
    mtypes = [mtype] if mtype is not None else models.CACHEABLE_TYPES
    for mtype in mtypes:
        if mtype in _cache:
            del _cache[mtype]
        _cache[mtype] = dao.get_all(mtype)


def unload(mtype=None):
    """Unloads cache.

    """
    if mtype is not None:
        for key in _cache.keys():
            del _cache[key]
    elif mtype in _cache:
        del _cache[mtype]


def exists(mtype, item_id):
    """Determines whether a cache item exists or not.

    :param class mtype: Cache model type.
    :param item_id: Cache item identifier.
    :type item_id: str | int

    :returns: True if item is cached, False otherwise.
    :rtype: bool

    """
    # JIT load.
    load()

    if mtype not in _cache or item_id is None:
        return False
    elif isinstance(item_id, int):
        return len([i for i in _cache[mtype] if i.ID == item_id]) == 1
    else:
        item_id = str(item_id).upper()
        return len([i for i in _cache[mtype] if i.cache_name.upper() == item_id]) == 1


def get(mtype, item_id=None):
    """Returns a cached item.

    :param class mtype: Cache entity type.
    :param id: Cache item id.
    :type item_id: str | int

    :returns: An entity if item is cached, None otherwise.
    :rtype: A subclass of Entity

    """
    # JIT load.
    load()

    if item_id is None:
        return None if mtype not in _cache else _cache[mtype]
    elif not exists(mtype, item_id):
        return None
    elif isinstance(item_id, int):
        return [i for i in _cache[mtype] if i.ID == item_id][0]
    else:
        item_id = str(item_id).upper()
        return [i for i in _cache[mtype] if i.cache_name.upper() == item_id][0]


def get_name(mtype, item_id):
    """Returns a cached item name.

    :param class mtype: Cache entity type.
    :param id: Cache item id.
    :type item_id: str | int

    :returns: An entity name if item is cached, None otherwise.
    :rtype: str | None

    """
    if item_id is None:
        return None

    # JIT load.
    load()

    item = get(mtype, item_id)

    return None if item is None else item.cache_name


def get_id(mtype, item_id):
    """Returns a cached item id.

    :param class mtype: Cache entity type.
    :param id: Cache item id.
    :type item_id: str | int

    :returns: An entity id if item is cached, None otherwise.
    :rtype: int | None

    """
    # JIT load.
    load()

    item = get(mtype, item_id)

    if isinstance(item, mtype):
        return item.ID
    else:
        return None


def get_random(mtype):
    """Returns a random cache item.

    :param class mtype: Cache entity type.

    :returns: A random item from the cache.
    :rtype: Sub-class of types.Entity

    """
    # JIT load.
    load()

    return _cache[mtype][random.randint(0, len(_cache[mtype]) - 1)]


def get_random_name(mtype):
    """Returns a random cache item name.

    :param class mtype: Cache entity type.

    :returns: The name of a random cached item.
    :rtype: str

    """
    return get_random(mtype).name


def get_random_id(mtype):
    """Returns a random cache item id.

    :param class mtype: Cache entity type.

    :returns: The id of a random cached item.
    :rtype: int

    """
    return get_random(mtype).ID


def add(item):
    """Adds an item to the cache.

    :param object item: Item to be cached.

    """
    if item is None:
        raise ValueError("Cannot cache null items")
    if not hasattr(item, 'cache_name'):
        raise ValueError("Cannot cache items without a cache key")

    mtype = type(item)
    if mtype not in _cache:
        _cache[mtype] = [item]
    elif item not in _cache[mtype]:
        _cache[mtype].append(item)



def get_names(mtype, name_formatter=lambda x : x.lower()):
    """Returns list of names.

    :param class mtype: Cache entity type.
    :param function name_formatter: Cache item name formatter.

    :returns: List of names.
    :rtype: list

    """
    if mtype not in _cache:
        raise ValueError("Cache collection ({0}) does not exist.".format(mtype))

    return [name_formatter(i.cache_name) for i in _cache[mtype]]


def get_count(mtype=None):
    """Returns the count of cached collections.

    :param class mtype: Cache entity type.

    :returns: The count of cached items.
    :rtype: int

    """
    if mtype is None:
        return len(_cache)
    elif mtype in _cache:
        return len(_cache[mtype])
    else:
        return 0
