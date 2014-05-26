"""
.. module:: software_model_component.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.software.modelcomponent document.


"""
# Module imports.
from collections import namedtuple

from .... utils import convert



# Property extension context information.
_ExtensionContextInfo = \
    namedtuple('_ExtensionContextInfo', ['c', 'p', 'parent', 'ancestors'])


def _extend_property_01(ctx):
    """Sets property extension properties."""
    ctx.p._ancestors = ctx.ancestors
    ctx.p._depth = len(ctx.ancestors)
    ctx.p._parent = ctx.parent


def _extend_property_02(ctx):
    """Sets property key."""
    key = ctx.c._key + '>'
    if len(ctx.p._ancestors):
        key += ctx.p._ancestors[-1].short_name.lower().strip() + '.'
    key += ctx.p.short_name.lower().strip()
    ctx.p._key = key


def _extend_property_03(ctx):
    """Sets property value."""
    # Format existing values.
    ctx.p.values = map(lambda v: str(v).strip(), ctx.p.values)
    ctx.p.values = [v for v in ctx.p.values if len(v)]
    ctx.p.values = map(lambda v: v[0].upper() + v[1:], ctx.p.values)

    if len(ctx.p.values):
        ctx.p._value = reduce(lambda x, v: v if x is None else x + " | " + v, ctx.p.values, None)
        ctx.p._value = ctx.p._value[0].upper() + ctx.p._value[1:]
    else:
        ctx.p._value = None


def _extend_property_04(ctx):
    """Sets property display names."""
    ctx.p._display_name = ""
    ctx.p._full_display_name = ""
    ctx.p._long_display_name = ""
    ctx.p._short_display_name = ""

    # Short name.
    name = ctx.p.short_name
    if len(name) and not name[0].isdigit():
        name = convert.str_to_spaced_case(name)
        name = map(convert.capitalize, name.split(" "))
        name = reduce(lambda x, s: s if x is None else x + " " + s, name, None)
    ctx.p._short_display_name = name

    # Display name.
    if ctx.p._depth:
        ctx.p._display_name += ctx.p._parent._display_name
        ctx.p._display_name += " > "
    ctx.p._display_name += ctx.p._short_display_name

    # Long name.
    if not ctx.p._depth:
        ctx.p._long_display_name = ctx.c._long_display_name
        ctx.p._long_display_name += " >> "
    else:
        ctx.p._long_display_name = ctx.p._parent._long_display_name
        ctx.p._long_display_name += " > "
    ctx.p._long_display_name += ctx.p._short_display_name

    # Full name.
    if not ctx.p._depth:
        ctx.p._full_display_name = ctx.c._full_display_name
        ctx.p._full_display_name += " >> "
    else:
        ctx.p._full_display_name = ctx.p._parent._full_display_name
        ctx.p._full_display_name += " > "
    ctx.p._full_display_name += ctx.p._short_display_name


def _extend_property_05(ctx):
    """Process child properties."""
    for p in ctx.p.sub_properties:
        extend(ctx.c, p, ctx.p, ctx.ancestors + [ctx.p])


def extend(c, p, parent=None, ancestors=[]):
    """Extends a property in readiness for later processing.

    :param c: A model component.
    :type c: pyesdoc.ontologies.cim.v1.software.ModelComponent

    :param p: A model component property.
    :type p: pyesdoc.ontologies.cim.v1.software.ComponentProperty

    :param parent: Parent model component property.
    :type parent: pyesdoc.ontologies.cim.v1.software.ComponentProperty

    :param list ancestors: Ancestor model component properties.

    """
    ctx = _ExtensionContextInfo(c, p, parent, ancestors)
    for f in (
        _extend_property_01,
        _extend_property_02,
        _extend_property_03,
        _extend_property_04,
        _extend_property_05,
        ):
        f(ctx)
