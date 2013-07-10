"""
.. module:: cim.v1.types.data.data_storage.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.233734.

"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid





class DataStorage(object):
    """An abstract class within the cim v1 type system.

    Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.
    """
    # Abstract Base Class module.
    # N.B. - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(DataStorage, self).__init__()
        self.format = str()                          # type = str
        self.location = str()                        # type = str
        self.modification_date = datetime.datetime.now()# type = datetime.datetime
        self.size = int()                            # type = int


    def as_dict(self):
        """Returns a deep dictionary representation.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'format', self.format, False, True, False)
        append(d, 'location', self.location, False, True, False)
        append(d, 'modification_date', self.modification_date, False, True, False)
        append(d, 'size', self.size, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

