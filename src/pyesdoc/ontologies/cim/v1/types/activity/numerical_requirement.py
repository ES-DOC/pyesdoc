"""
.. module:: cim.v1.types.activity.numerical_requirement.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.175563.

"""

# Module imports.
import abc
from abc import ABCMeta
from abc import abstractmethod
from abc import abstractproperty
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference




class NumericalRequirement(object):
    """An abstract class within the cim v1 type system.

    A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.
    """
    # Abstract Base Class module.
    # N.B. - see http://docs.python.org/library/abc.html
    __metaclass__ = ABCMeta

    def __init__(self):
        """Constructor"""
        super(NumericalRequirement, self).__init__()
        self.description = str()                     # type = str
        self.id = str()                              # type = str
        self.name = str()                            # type = str
        self.options = []                            # type = activity.NumericalRequirementOption
        self.requirement_type = str()                # type = str
        self.source = None                           # type = shared.DataSource
        self.source_reference = None                 # type = shared.CimReference


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
        append(d, 'description', self.description, False, True, False)
        append(d, 'id', self.id, False, True, False)
        append(d, 'name', self.name, False, True, False)
        append(d, 'options', self.options, True, False, False)
        append(d, 'requirement_type', self.requirement_type, False, True, False)
        append(d, 'source', self.source, False, False, False)
        append(d, 'source_reference', self.source_reference, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm
from pyesdoc.ontologies.cim.v1.types.activity.numerical_requirement_option import NumericalRequirementOption

