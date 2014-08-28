"""
.. module:: facets.py
   :copyright: Copyright "Jun 29, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: ES-DOC API db models - facets domain partition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from sqlalchemy import (
    Column,
    Enum,
    Text,
    Unicode,
    UniqueConstraint,
)

from . utils import (
    create_fk,
    Entity
    )

# Domain model partition.
_DOMAIN_PARTITION = 'facets'

# Node types.
NODE_TYPE_INSTITUTE = u"Institute"
NODE_TYPE_PROJECT = u"Project"
NODE_TYPE_EXPERIMENT = u"Experiment"
NODE_TYPE_MODEL = u"Model"
NODE_TYPE_MODEL_COMPONENT = u"ModelComponent"
NODE_TYPE_MODEL_COMPONENT_PROPERTY = u"ModelComponentProperty"
NODE_TYPE_MODEL_COMPONENT_PROPERTY_VALUE = u"ModelComponentPropertyValue"
NODE_TYPE_MODEL_PROPERTY = u"ModelProperty"
NODE_TYPE_MODEL_PROPERTY_VALUE = u"ModelPropertyValue"

# Node typeset.
NODE_TYPES = [
    NODE_TYPE_INSTITUTE,
    NODE_TYPE_PROJECT,
    NODE_TYPE_EXPERIMENT,
    NODE_TYPE_MODEL,
    NODE_TYPE_MODEL_COMPONENT,
    NODE_TYPE_MODEL_COMPONENT_PROPERTY,
    NODE_TYPE_MODEL_COMPONENT_PROPERTY_VALUE,
    NODE_TYPE_MODEL_PROPERTY,
    NODE_TYPE_MODEL_PROPERTY_VALUE
]

# Node type enum.
_NODE_TYPE_ENUM_NAME = 'NodeTypeEnum'

# Node type enumeration.
NodeTypeEnum = Enum(NODE_TYPE_INSTITUTE,
                    NODE_TYPE_PROJECT,
                    NODE_TYPE_EXPERIMENT,
                    NODE_TYPE_MODEL,
                    NODE_TYPE_MODEL_COMPONENT,
                    NODE_TYPE_MODEL_COMPONENT_PROPERTY,
                    NODE_TYPE_MODEL_COMPONENT_PROPERTY_VALUE,
                    NODE_TYPE_MODEL_PROPERTY,
                    NODE_TYPE_MODEL_PROPERTY_VALUE,
                    schema=_DOMAIN_PARTITION,
                    name=_NODE_TYPE_ENUM_NAME)


class Node(Entity):
    """A facet derived from a map/reduce job over a document attribute.

    """
    # SQLAlchemy directives.
    __tablename__ = 'tbl_node'
    __table_args__ = (
        UniqueConstraint('project_id', 'type_of', 'field'),
        {'schema' : _DOMAIN_PARTITION}
    )

    # Foreign keys.
    project_id = create_fk('vocab.tblProject.ID', required=True, default=1)

    # Field set.
    type_of = Column(NodeTypeEnum, nullable=False)
    field = Column(Unicode(511), nullable=False)
    sort_field = Column(Unicode(511), nullable=True)
    display_field = Column(Unicode(511), nullable=True)

    # Helper fields.
    parent = None


class NodeField(Entity):
    """Node field information.

    """
    # SQLAlchemy directives.
    __tablename__ = 'tbl_node_field'
    __table_args__ = (
        {'schema' : _DOMAIN_PARTITION}
    )

    # Field set.
    text = Column(Text, nullable=False, unique=True)


    @property
    def cache_name(self):
        """Gets instance cache key name.

        """
        return self.text
