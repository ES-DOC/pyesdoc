"""
.. module:: cim.v1.types.activity.numerical_activity.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.032223.

"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.activity.activity import Activity
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference




class NumericalActivity(Activity):
    """An abstract class within the cim v1 type system.

    
    """
    # Abstract Base Class module.
    # N.B. - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(NumericalActivity, self).__init__()
        self.description = str()                     # type = str
        self.long_name = str()                       # type = str
        self.short_name = str()                      # type = str
        self.supports = []                           # type = activity.Experiment
        self.supports_references = []                # type = shared.CimReference


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
        d = dict(super(NumericalActivity, self).as_dict())
        append(d, 'description', self.description, False, True, False)
        append(d, 'long_name', self.long_name, False, True, False)
        append(d, 'short_name', self.short_name, False, True, False)
        append(d, 'supports', self.supports, True, False, False)
        append(d, 'supports_references', self.supports_references, True, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm
from pyesdoc.ontologies.cim.v1.types.activity.experiment import Experiment

