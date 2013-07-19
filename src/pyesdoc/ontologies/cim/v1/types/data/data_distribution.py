"""
.. module:: cim.v1.types.data.data_distribution.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.181155.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.responsible_party import ResponsibleParty


class DataDistribution(object):
    """A concrete class within the cim v1 type system.

    Describes how a DataObject is distributed.
    """

    def __init__(self):
        """Constructor"""
        super(DataDistribution, self).__init__()
        self.access = str()                          # type = str
        self.fee = str()                             # type = str
        self.format = str()                          # type = str
        self.responsible_party = None                # type = shared.ResponsibleParty


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
        append(d, 'access', self.access, False, True, False)
        append(d, 'fee', self.fee, False, True, False)
        append(d, 'format', self.format, False, True, False)
        append(d, 'responsible_party', self.responsible_party, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

