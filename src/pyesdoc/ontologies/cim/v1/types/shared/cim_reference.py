"""
.. module:: cim.v1.types.shared.cim_reference.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.274356.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.change import Change


class CimReference(object):
    """A concrete class within the cim v1 type system.

    A reference to another cim entity
    """

    def __init__(self):
        """Constructor"""
        super(CimReference, self).__init__()
        self.changes = []                            # type = shared.Change
        self.description = str()                     # type = str
        self.external_id = str()                     # type = str
        self.id = uuid.uuid4()                       # type = uuid.UUID
        self.name = str()                            # type = str
        self.type = str()                            # type = str
        self.version = str()                         # type = str


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
        append(d, 'changes', self.changes, True, False, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'external_id', self.external_id, False, True, False)
        append(d, 'id', self.id, False, True, False)
        append(d, 'name', self.name, False, True, False)
        append(d, 'type', self.type, False, True, False)
        append(d, 'version', self.version, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

