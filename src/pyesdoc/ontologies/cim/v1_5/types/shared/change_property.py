"""
.. module:: cim.v1_5.types.shared.change_property.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.688556.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1_5.types.shared.property import Property


class ChangeProperty(Property):
    """A concrete class within the cim v1.5 type system.

    A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.
    """

    def __init__(self):
        """Constructor"""
        super(ChangeProperty, self).__init__()
        self.description = str()                     # type = str
        self.id = str()                              # type = str


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
        d = dict(super(ChangeProperty, self).as_dict())
        append(d, 'description', self.description, False, True, False)
        append(d, 'id', self.id, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

