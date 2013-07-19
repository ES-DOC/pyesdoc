"""
.. module:: cim.v1.types.software.time_transformation.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-17 14:43:15.224432.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.software.time_mapping_type import TimeMappingType


class TimeTransformation(object):
    """A concrete class within the cim v1 type system.

    The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.
    """

    def __init__(self):
        """Constructor"""
        super(TimeTransformation, self).__init__()
        self.description = str()                     # type = str
        self.mapping_type = ''                       # type = software.TimeMappingType


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
        append(d, 'mapping_type', self.mapping_type, False, False, True)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

