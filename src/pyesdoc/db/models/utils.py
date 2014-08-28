"""
.. module:: utils.py
   :copyright: Copyright "Jun 29, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Domain model utility classes and functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import datetime
import json
import types

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData
    )
from sqlalchemy.ext.declarative import declarative_base

from ...utils import (
    convert,
    runtime as rt
    )


# Module exports.
__all__ = [
    'metadata',
    'create_fk',
    'Entity',
    'EntityConvertor'
]


# Common sqlalchemy metadata container.
metadata = MetaData()



def create_fk(name, required=False, default=None):
    """Factory function to return a foreign key

    """
    if default is None:
        return Column(Integer,
                      ForeignKey(name),
                      nullable=not required)
    else:
        return Column(Integer,
                      ForeignKey(name),
                      nullable=not required,
                      default=default)



class BaseEntity(object):
    """Base entity sub-classed from all Prodiguer models.

    """
    # Entity attributes.
    ID = Column(Integer, primary_key=True)


    def __init__(self):
        """Constructor.

        """
        super(BaseEntity, self).__init__()


    def __repr__(self):
        """Debugging representation.

        """
        return self.as_json()


    def as_dict(self):
        """Returns a dictionary representation.

        """
        return EntityConvertor.to_dict(self)


    def as_json(self):
        """Returns a json representation.

        """
        return EntityConvertor.to_json(self)


    def as_string(self):
        """Returns a string representation.

        """
        return self.as_json()


    @property
    def is_new(self):
        """Returns a flag indicating whether the entity instance is new or not.

        """
        return True if self.ID is None else False


    @classmethod
    def get_default_sort_key(cls):
        """Gets default sort key.

        """
        if hasattr(cls, 'FullName'):
            return lambda instance: instance.FullName.upper()
        elif hasattr(cls, 'Name'):
            return lambda instance: instance.Name.upper()
        elif hasattr(cls, 'OrdinalPosition'):
            return lambda instance: str(instance.OrdinalPosition)
        else:
            lambda instance: instance.ID


    @classmethod
    def get_sorted(cls, collection, sort_key=None):
        """Gets sorted collection of instances.

        """
        if sort_key is None:
            sort_key=cls.get_default_sort_key()

        return sorted(collection, key=sort_key)



# Mixin with sql alchemy.
Entity = declarative_base(metadata=metadata, cls=BaseEntity)


def _format_for_json(obj):
    """Formats an object in readiness for conversion to json."""
    if isinstance(obj, datetime.datetime):
        return obj.isoformat().replace('T', ' ')
    elif isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, datetime.time):
        return obj.isoformat()
    else:
        return obj


class JSONEncoder(json.JSONEncoder):
    """Extends standard json encoding so as to handle specific types.

    """
    def default(self, obj):
        """Encodes default values."""
        return json.JSONEncoder.default(self, _format_for_json(obj))


class EntityConvertor(object):
    """Encapsulates all entity conversion functions.

    """
    @classmethod
    def to_dict(cls, target, key_formatter=None, json_formatting=False):
        """Returns a dictionary representation.

        """
        def _as_dict(entity):
            """Converts entity to a dictionary."""
            if not entity:
                return {}

            # Build a dictionary from entity ORM spec.
            result = {}
            for col in entity.__table__.columns:
                key = key_formatter(col.name) if key_formatter else col.name
                value = getattr(entity, col.name)
                if json_formatting:
                    value = _format_for_json(value)
                result[key] = value

            # Allow entity to perform custom formatting.
            if hasattr(entity, 'format_dict'):
                entity.format_dict(result, key_formatter, json_formatting)

            return result

        try:
            iter(target)
        except TypeError:
            return _as_dict(target)
        else:
            return [_as_dict(i) for i in target]


    @classmethod
    def to_dict_for_json(cls, target):
        """Returns a dictionary with keys formatted for json.

        """
        return cls.to_dict(target,
                           key_formatter=convert.str_to_camel_case,
                           json_formatting=True)


    @classmethod
    def to_json(cls, target):
        """Returns a json representation.

        """
        as_dict = cls.to_dict(target, convert.str_to_camel_case)

        return unicode(JSONEncoder().encode(as_dict))


    @classmethod
    def to_string(cls, target):
        """Returns a string representation.

        """
        return cls.to_json(target)


