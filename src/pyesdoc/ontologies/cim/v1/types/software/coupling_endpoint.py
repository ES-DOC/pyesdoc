"""
.. module:: cim.v1.types.software.coupling_endpoint.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.267198.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.software.coupling_property import CouplingProperty


class CouplingEndpoint(object):
    """A concrete class within the cim v1 type system.

    The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).
    """

    def __init__(self):
        """Constructor"""
        super(CouplingEndpoint, self).__init__()
        self.data_source = None                      # type = shared.DataSource
        self.data_source_reference = None            # type = shared.CimReference
        self.instance_id = str()                     # type = str
        self.properties = []                         # type = software.CouplingProperty


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
        append(d, 'data_source', self.data_source, False, False, False)
        append(d, 'data_source_reference', self.data_source_reference, False, False, False)
        append(d, 'instance_id', self.instance_id, False, True, False)
        append(d, 'properties', self.properties, True, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

