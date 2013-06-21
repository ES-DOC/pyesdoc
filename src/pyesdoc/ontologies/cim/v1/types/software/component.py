"""
.. module:: cim.v1.types.software.component.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.287424.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.data_source import DataSource
from pyesdoc.ontologies.cim.v1.types.shared.citation import Citation
from pyesdoc.ontologies.cim.v1.types.shared.citation import Citation
from pyesdoc.ontologies.cim.v1.types.software.composition import Composition
from pyesdoc.ontologies.cim.v1.types.software.coupling_framework_type import CouplingFrameworkType
from pyesdoc.ontologies.cim.v1.types.software.entry_point import EntryPoint
from pyesdoc.ontologies.cim.v1.types.software.deployment import Deployment
from pyesdoc.ontologies.cim.v1.types.grids.grid_spec import GridSpec
from pyesdoc.ontologies.cim.v1.types.software.component_language import ComponentLanguage
from pyesdoc.ontologies.cim.v1.types.shared.license import License
from pyesdoc.ontologies.cim.v1.types.software.component_property import ComponentProperty
from pyesdoc.ontologies.cim.v1.types.shared.responsible_party import ResponsibleParty
from pyesdoc.ontologies.cim.v1.types.shared.responsible_party import ResponsibleParty


class Component(DataSource):
    """A concrete class within the cim v1 type system.

    A SofwareComponent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested "child" components. Every component can have "componentProperties" which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component's composition must be owned by that component or a child of that component; child components cannot couple together their parents' properties.
    """

    def __init__(self):
        """Constructor"""
        super(Component, self).__init__()
        self.children = []                           # type = software.Component
        self.citation_list = []                      # type = shared.Citation
        self.citations = []                          # type = shared.Citation
        self.composition = None                      # type = software.Composition
        self.coupling_framework = ''                 # type = software.CouplingFrameworkType
        self.dependencies = []                       # type = software.EntryPoint
        self.deployments = []                        # type = software.Deployment
        self.description = str()                     # type = str
        self.funding_sources = []                    # type = str
        self.grid = None                             # type = grids.GridSpec
        self.is_embedded = bool()                    # type = bool
        self.language = None                         # type = software.ComponentLanguage
        self.license = None                          # type = shared.License
        self.long_name = str()                       # type = str
        self.online_resource = str()                 # type = str
        self.parent = None                           # type = software.Component
        self.previous_version = str()                # type = str
        self.properties = []                         # type = software.ComponentProperty
        self.property_tree = []                      # type = software.ComponentProperty
        self.release_date = datetime.datetime.now()  # type = datetime.datetime
        self.responsible_parties = []                # type = shared.ResponsibleParty
        self.responsible_party_list = []             # type = shared.ResponsibleParty
        self.short_name = str()                      # type = str


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
        d = dict(super(Component, self).as_dict())
        append(d, 'children', self.children, True, False, False)
        append(d, 'citation_list', self.citation_list, True, False, False)
        append(d, 'citations', self.citations, True, False, False)
        append(d, 'composition', self.composition, False, False, False)
        append(d, 'coupling_framework', self.coupling_framework, False, False, True)
        append(d, 'dependencies', self.dependencies, True, False, False)
        append(d, 'deployments', self.deployments, True, False, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'funding_sources', self.funding_sources, True, True, False)
        append(d, 'grid', self.grid, False, False, False)
        append(d, 'is_embedded', self.is_embedded, False, True, False)
        append(d, 'language', self.language, False, False, False)
        append(d, 'license', self.license, False, False, False)
        append(d, 'long_name', self.long_name, False, True, False)
        append(d, 'online_resource', self.online_resource, False, True, False)
        append(d, 'parent', self.parent, False, False, False)
        append(d, 'previous_version', self.previous_version, False, True, False)
        append(d, 'properties', self.properties, True, False, False)
        append(d, 'property_tree', self.property_tree, True, False, False)
        append(d, 'release_date', self.release_date, False, True, False)
        append(d, 'responsible_parties', self.responsible_parties, True, False, False)
        append(d, 'responsible_party_list', self.responsible_party_list, True, False, False)
        append(d, 'short_name', self.short_name, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

