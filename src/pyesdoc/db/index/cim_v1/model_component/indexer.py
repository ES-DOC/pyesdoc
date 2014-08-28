"""
.. module:: indexer.py
   :platform: Unix, Windows
   :synopsis: Indexes a cim.v1.software.model_component document.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from . reducer import reduce as reduce_model
from .... import (
    models,
    utils
    )
from .... models import (
    NODE_TYPE_INSTITUTE,
    NODE_TYPE_PROJECT,
    NODE_TYPE_EXPERIMENT,
    NODE_TYPE_MODEL,
    NODE_TYPE_MODEL_COMPONENT,
    NODE_TYPE_MODEL_COMPONENT_PROPERTY,
    NODE_TYPE_MODEL_COMPONENT_PROPERTY_VALUE,
    NODE_TYPE_MODEL_PROPERTY,
    NODE_TYPE_MODEL_PROPERTY_VALUE
    )



class _ProcessingContextInfo(object):
    """Encapsulates contextual information used during mapping."""
    def __init__(self, project_id, m):
        self.project_id = project_id
        self.m, self.c_list = reduce_model(m)
        self.nodes = {}
        self.combinations = {}


def _create_node(ctx, key, typeof, fieldset):
    """Creates & caches a node."""
    ctx.nodes[key] = \
        utils.create_node(typeof, fieldset, ctx.project_id)


def _set_model_node(ctx):
    """Set model nodes."""
    fieldset = _get_model_fieldset(ctx)
    _create_node(ctx, ctx.m, NODE_TYPE_MODEL, fieldset)


def _set_component_node(ctx):
    """Set component nodes."""
    fieldset = _get_component_fieldset(ctx)
    _create_node(ctx, ctx.c, NODE_TYPE_MODEL_COMPONENT, fieldset)


def _set_property_node(ctx):
    """Set property node."""
    fieldset = _get_property_fieldset(ctx)
    _create_node(ctx, ctx.p, NODE_TYPE_MODEL_COMPONENT_PROPERTY, fieldset)


def _set_value_node(ctx):
    """Set value node."""
    fieldset = _get_value_fieldset(ctx)
    _create_node(ctx, ctx.v, NODE_TYPE_MODEL_COMPONENT_PROPERTY_VALUE, fieldset)


def _get_model_fieldset(ctx):
    """Returns model fields."""
    fieldset = []
    if ctx.m.meta.institute is not None:
        fieldset.append(utils.create_node_field(ctx.m.meta.institute.upper()))
    fieldset.append(utils.create_node_field(ctx.m.short_name.upper()))

    return tuple(fieldset)


def _get_component_fieldset(ctx):
    """Returns model component fields."""
    fieldset = []
    if ctx.c._depth > 1:
        fieldset.append(ctx.nodes[ctx.c._parent])
    fieldset.append(utils.create_node_field(ctx.c._long_display_name))

    return tuple(fieldset)


def _get_property_fieldset(ctx):
    """Returns model component property fields."""
    fieldset = []
    if ctx.p._parent:
        fieldset.append(ctx.nodes[ctx.p._parent])
    fieldset.append(utils.create_node_field(ctx.p._long_display_name))

    return tuple(fieldset)


def _get_value_fieldset(ctx):
    """Returns model component property value fields."""
    return (
        ctx.nodes[ctx.m],
        ctx.nodes[ctx.c],
        ctx.nodes[ctx.p],
        utils.create_node_field(ctx.v)
        )


def _create_node_combination(ctx, typeof, nodeset):
    """Creates & caches a node combination."""
    if nodeset not in ctx.combinations:
        ctx.combinations[nodeset] = \
            utils.create_node_combination(typeof, nodeset, ctx.project_id)

    return ctx.combinations[nodeset]


def _get_hierarchy(ctx, item):
    """Helper function to return hierarchy."""
    hierarchy = []
    while item:
        hierarchy.append(ctx.nodes[item])
        item = item.parent

    return tuple(reversed(hierarchy))


def _set_component_combination(ctx):
    """Set component combination."""
    nodeset = _get_hierarchy(ctx, ctx.c)
    ctx.combinations[ctx.c] = \
        _create_node_combination(ctx, NODE_COMBINATION_03, nodeset)


def _set_property_combination(ctx):
    """Set property combination."""
    nodeset = _get_hierarchy(ctx, ctx.p)
    ctx.combinations[ctx.p] = \
        _create_node_combination(ctx, NODE_COMBINATION_04, nodeset)


def _set_value_combination(ctx):
    """Set value combination."""
    nodeset = (
        ctx.nodes[ctx.m],
        ctx.combinations[ctx.c],
        ctx.combinations[ctx.p],
        ctx.nodes[ctx.v]
        )
    _create_node_combination(ctx, NODE_COMBINATION_01, nodeset)


def index(project_id, m):
    """Indexes a cim v1 model component document.

    :param int project_id: ID of associated project.
    :param m: A model component.
    :type m: ontologies.cim.v1.software.ModelComponent

    """
    def index_model(ctx):
        """Index model."""
        _set_model_node(ctx)
        for ctx.c, ctx.p_list in ctx.c_list:
            index_component(ctx)

    def index_component(ctx):
        """Index model component."""
        _set_component_node(ctx)
        for ctx.p, ctx.v_list in ctx.p_list:
            index_property(ctx)

    def index_property(ctx):
        """Index model component property."""
        _set_property_node(ctx)
        for ctx.v in ctx.v_list:
            index_value(ctx)

    def index_value(ctx):
        """Index model component property value."""
        _set_value_node(ctx)

    index_model(_ProcessingContextInfo(project_id, m))
