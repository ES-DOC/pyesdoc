"""
.. module:: cim.v1.types.data.data_object.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.258214.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.cim_info import CimInfo
from pyesdoc.ontologies.cim.v1.types.shared.citation import Citation
from pyesdoc.ontologies.cim.v1.types.data.data_content import DataContent
from pyesdoc.ontologies.cim.v1.types.data.data_property import DataProperty
from pyesdoc.ontologies.cim.v1.types.data.data_status_type import DataStatusType
from pyesdoc.ontologies.cim.v1.types.data.data_distribution import DataDistribution
from pyesdoc.ontologies.cim.v1.types.data.data_extent import DataExtent
from pyesdoc.ontologies.cim.v1.types.data.data_hierarchy_level import DataHierarchyLevel
from pyesdoc.ontologies.cim.v1.types.shared.cim_reference import CimReference
from pyesdoc.ontologies.cim.v1.types.data.data_restriction import DataRestriction
from pyesdoc.ontologies.cim.v1.types.data.data_storage import DataStorage


class DataObject(DataSource):
    """A concrete class within the cim v1 type system.

    A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.
    """

    def __init__(self):
        """Constructor"""
        super(DataObject, self).__init__()
        self.acronym = str()                         # type = str
        self.child_object = []                       # type = data.DataObject
        self.cim_info = None                         # type = shared.CimInfo
        self.citations = []                          # type = shared.Citation
        self.content = []                            # type = data.DataContent
        self.data_property = []                      # type = data.DataProperty
        self.data_status = ''                        # type = data.DataStatusType
        self.description = str()                     # type = str
        self.distribution = None                     # type = data.DataDistribution
        self.extent = None                           # type = data.DataExtent
        self.geometry_model = str()                  # type = str
        self.hierarchy_level = None                  # type = data.DataHierarchyLevel
        self.keyword = str()                         # type = str
        self.parent_object = None                    # type = data.DataObject
        self.parent_object_reference = None          # type = shared.CimReference
        self.restriction = []                        # type = data.DataRestriction
        self.source_simulation = str()               # type = str
        self.storage = []                            # type = data.DataStorage


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
        d = dict(super(DataObject, self).as_dict())
        append(d, 'acronym', self.acronym, False, True, False)
        append(d, 'child_object', self.child_object, True, False, False)
        append(d, 'cim_info', self.cim_info, False, False, False)
        append(d, 'citations', self.citations, True, False, False)
        append(d, 'content', self.content, True, False, False)
        append(d, 'data_property', self.data_property, True, False, False)
        append(d, 'data_status', self.data_status, False, False, True)
        append(d, 'description', self.description, False, True, False)
        append(d, 'distribution', self.distribution, False, False, False)
        append(d, 'extent', self.extent, False, False, False)
        append(d, 'geometry_model', self.geometry_model, False, True, False)
        append(d, 'hierarchy_level', self.hierarchy_level, False, False, False)
        append(d, 'keyword', self.keyword, False, True, False)
        append(d, 'parent_object', self.parent_object, False, False, False)
        append(d, 'parent_object_reference', self.parent_object_reference, False, False, False)
        append(d, 'restriction', self.restriction, True, False, False)
        append(d, 'source_simulation', self.source_simulation, False, True, False)
        append(d, 'storage', self.storage, True, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

