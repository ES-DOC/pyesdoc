"""
.. module:: software_model_component.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.software.modelcomponent document.


"""
from collections import namedtuple

from pyesdoc._extensions.cim.v1.software_model_component_type_map import METAFOR_ESDOC_MODEL_COMPONENT_MAP
from pyesdoc._extensions.cim.v1.software_model_component_property_1 import extend as extend_property
from pyesdoc._extensions.cim.v1.software_model_component_property_2 import set_standard_properties
from pyesdoc._extensions.cim.v1.software_model_component_property_2 import set_scientific_properties
from pyesdoc._extensions.cim.v1.software_model_component_property_2 import set_qc_properties



def get_extenders():
    """Returns set of extension functions.

    """
    return (
        _set_component_hierarchy,
        _set_component_property_sets,
        _set_component_property_trees,
        _set_component_meta_info,
        _set_component_type_info
        )


# Mappings between component type & component type display name.
_COMPONENT_TYPE_DISPLAY_NAMES = \
    {k: v.split(">")[-1].strip() for k, v in iter(METAFOR_ESDOC_MODEL_COMPONENT_MAP.items())}


# Component extension context information.
_ComponentContextInfo = \
    namedtuple('ComponentContextInfo', ['c', 'ext', 'parent', 'ancestors'])


class _ComponentExtensionInfo(object):
    """Component extension properties.

    """
    pass


def _get_sort_key(item):
    """Returns a sort key.

    """
    return item.ext.full_display_name


def _extend_component_00(ctx):
    """Pre component extension tasks.

    """
    # Remove sub-components with invalid type names.
    for sc in ctx.c.sub_components:
        if sc.type.lower() == 'other' and \
           sc.short_name.replace(" ", "").lower() in \
                ['new', 'surfexoceansurface']:
            ctx.c.sub_components.remove(sc)

    # Rename component short name.
    if ctx.c.short_name == 'Ocean straits and horizontal diffusion':
        ctx.c.short_name = 'Ocean Straits'

    # If component type was specified as other then derive it from short name.
    if ctx.c.type.lower() == 'other':
        ctx.c.type = ctx.c.short_name.replace(" ", "")


def _extend_component_01(ctx):
    """Initializes component extension properties.

    """
    if not hasattr(ctx.c, "ext"):
        ctx.c.ext = _ComponentExtensionInfo()
    if not hasattr(ctx.c.ext, "full_display_name"):
        ctx.c.ext.full_display_name = unicode()
    if not hasattr(ctx.c.ext, "long_display_name"):
        ctx.c.ext.long_display_name = unicode()
    if not hasattr(ctx.c.ext, "short_display_name"):
        ctx.c.ext.short_display_name = unicode()
    if not hasattr(ctx.c.ext, "type_display_name"):
        ctx.c.ext.type_display_name = unicode()

    ctx.c.ext.ancestors = ctx.ancestors
    ctx.c.ext.component_tree = []
    ctx.c.ext.depth = len(ctx.ancestors)
    ctx.c.ext.parent = ctx.parent
    ctx.c.ext.properties = []
    ctx.c.ext.qc_properties = []
    ctx.c.ext.qc_property_tree = []
    ctx.c.ext.displayable_qc_properties = []
    ctx.c.ext.scientific_properties = []
    ctx.c.ext.scientific_property_tree = []
    ctx.c.ext.displayable_scientific_properties = []
    ctx.c.ext.standard_properties = []
    ctx.c.ext.standard_property_tree = []
    ctx.c.ext.displayable_standard_properties = []


def _extend_component_02(ctx):
    """Append component to tree of each direct ancestor.

    """
    for a in ctx.c.ext.ancestors:
        a.ext.component_tree.append(ctx.c)


def _extend_component_03(ctx):
    """Sets component display names.

    """
    # Type display name.
    if ctx.c.type in _COMPONENT_TYPE_DISPLAY_NAMES:
        ctx.c.ext.type_display_name = _COMPONENT_TYPE_DISPLAY_NAMES[ctx.c.type]
    else:
        ctx.c.ext.type_display_name = ctx.c.type

    # Short name.
    if not ctx.c.ext.parent:
        ctx.c.ext.short_display_name = ctx.c.short_name
    elif ctx.c.type in _COMPONENT_TYPE_DISPLAY_NAMES:
        ctx.c.ext.short_display_name = _COMPONENT_TYPE_DISPLAY_NAMES[ctx.c.type]
    else:
        ctx.c.ext.short_display_name = ctx.c.type

    # Long name.
    ctx.c.ext.long_display_name = unicode()
    if ctx.c.ext.depth > 1:
        ctx.c.ext.long_display_name += ctx.c.ext.parent.ext.long_display_name
        ctx.c.ext.long_display_name += u" > "
    ctx.c.ext.long_display_name += ctx.c.ext.short_display_name

    # Full name.
    if ctx.c.ext.depth > 0:
        ctx.c.ext.full_display_name += ctx.c.ext.parent.ext.full_display_name
        ctx.c.ext.full_display_name += u" > "
        ctx.c.ext.full_display_name += ctx.c.ext.short_display_name


def _extend_component_04(ctx):
    """Recursively extend child components.

    """
    for c in ctx.c.sub_components:
        _extend_component(c, c, ctx.c, ctx.ancestors + [ctx.c])


def _extend_component_05(ctx):
    """Sort components.

    """
    ctx.c.sub_components = sorted(ctx.c.sub_components, key=_get_sort_key)
    ctx.c.ext.component_tree = sorted(ctx.c.ext.component_tree, key=_get_sort_key)


def _extend_component(c, ext, parent=None, ancestors=[]):
    """Extends a component.

    """
    ctx = _ComponentContextInfo(c, ext, parent, ancestors)
    _extend_component_00(ctx)
    _extend_component_01(ctx)
    _extend_component_02(ctx)
    _extend_component_03(ctx)
    _extend_component_04(ctx)
    _extend_component_05(ctx)


def _set_component_hierarchy(ctx):
    """Extends component hierarchy.

    """
    _extend_component(ctx.doc, ctx.ext)


def _set_component_property_sets(ctx):
    """Extends component property sets.

    """
    def set_properties(builder, c, p_list):
        builder(c)
        for p in p_list:
            extend_property(c, p)
            c.ext.properties.append(p)

    for c in [ctx.doc] + ctx.doc.ext.component_tree:
        set_properties(set_scientific_properties, c, c.ext.scientific_properties)
        set_properties(set_standard_properties, c, c.ext.standard_properties)
        set_properties(set_qc_properties, c, c.ext.qc_properties)


def _set_component_property_trees(ctx):
    """Extends component property tree.

    """
    def build_tree(p_list, p_tree):
        """Builds a flatted property tree.

        """
        for p in p_list:
            p_tree.append(p)
            build_tree(p.sub_properties, p_tree)


    def get_displayable(p_tree):
        """Returns only displayable properties within a tree.

        """
        return [p for p in p_tree if p.values and p.values[0].lower() != 'none']

    for c in [ctx.doc] + ctx.doc.ext.component_tree:
        # ... build trees
        build_tree(c.ext.scientific_properties, c.ext.scientific_property_tree)
        build_tree(c.ext.standard_properties, c.ext.standard_property_tree)
        build_tree(c.ext.qc_properties, c.ext.qc_property_tree)
        # ... sort trees
        c.ext.scientific_property_tree = sorted(c.ext.scientific_property_tree, key=_get_sort_key)
        c.ext.standard_property_tree = sorted(c.ext.standard_property_tree, key=_get_sort_key)
        c.ext.qc_property_tree = sorted(c.ext.qc_property_tree, key=_get_sort_key)
        # ... set displayable properties
        c.ext.displayable_scientific_properties = get_displayable(c.ext.scientific_property_tree)
        c.ext.displayable_standard_properties = get_displayable(c.ext.standard_property_tree)
        c.ext.displayable_qc_properties = get_displayable(c.ext.qc_property_tree)


def _set_component_meta_info(ctx):
    """Extends component meta info.

    """
    for c in ctx.doc.ext.component_tree:
        for field in ('project', 'source', 'type'):
            if not getattr(c.meta, field):
                setattr(c.meta, field, getattr(ctx.doc.meta, field))


def _set_component_type_info(ctx):
    """Extends component type info.

    """
    for c in [ctx.doc] + ctx.doc.ext.component_tree:
        if not c.type:
            c.type = c.meta.type
        if c.meta.type not in c.types:
            c.types = [c.meta.type] + c.types
