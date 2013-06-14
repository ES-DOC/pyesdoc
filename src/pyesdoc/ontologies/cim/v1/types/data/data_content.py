"""
.. module:: cim.v1.types.data.data_content.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.043289.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.data.data_topic import DataTopic


class DataContent(DataSource):
    """A concrete class within the cim v1 type system.

    The contents of the data object; like ISO: MD_ContentInformation.
    """

    def __init__(self):
        """Constructor"""
        super(DataContent, self).__init__()
        self.aggregation = str()                     # type = str
        self.frequency = str()                       # type = str
        self.topic = None                            # type = data.DataTopic


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
        d = dict(super(DataContent, self).as_dict())
        append(d, 'aggregation', self.aggregation, False, True, False)
        append(d, 'frequency', self.frequency, False, True, False)
        append(d, 'topic', self.topic, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

