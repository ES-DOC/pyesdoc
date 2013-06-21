"""
.. module:: cim.v1.types.software.component_property.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.289017.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.citation import Citation
from pyesdoc.ontologies.cim.v1.types.software.component_property_intent_type import ComponentPropertyIntentType
from pyesdoc.ontologies.cim.v1.types.shared.unit_type import UnitType


class ComponentProperty(DataSource):
    """A concrete class within the cim v1 type system.

    ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.
    """

    def __init__(self):
        """Constructor"""
        super(ComponentProperty, self).__init__()
        self.children = []                           # type = software.ComponentProperty
        self.citations = []                          # type = shared.Citation
        self.description = str()                     # type = str
        self.grid = str()                            # type = str
        self.intent = ''                             # type = software.ComponentPropertyIntentType
        self.is_represented = bool()                 # type = bool
        self.long_name = str()                       # type = str
        self.short_name = str()                      # type = str
        self.standard_names = []                     # type = str
        self.units = ''                              # type = shared.UnitType
        self.values = []                             # type = str


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
        d = dict(super(ComponentProperty, self).as_dict())
        append(d, 'children', self.children, True, False, False)
        append(d, 'citations', self.citations, True, False, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'grid', self.grid, False, True, False)
        append(d, 'intent', self.intent, False, False, True)
        append(d, 'is_represented', self.is_represented, False, True, False)
        append(d, 'long_name', self.long_name, False, True, False)
        append(d, 'short_name', self.short_name, False, True, False)
        append(d, 'standard_names', self.standard_names, True, True, False)
        append(d, 'units', self.units, False, False, True)
        append(d, 'values', self.values, True, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

