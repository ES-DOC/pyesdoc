"""
.. module:: software_model_component_1.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.software.modelcomponent document.


"""
from collections import namedtuple

from pyesdoc.utils.convert import capitalize
from pyesdoc.utils.convert import str_to_spaced_case
from pyesdoc.utils.convert import str_to_unicode




# Property extension context information.
_ExtensionContextInfo = \
    namedtuple('_ExtensionContextInfo', ['c', 'p', 'parent', 'ancestors'])


class _PropertyExtensionInfo(object):
    """Property extension properties.

    """
    def __init__(self):
        self.display_name = unicode()
        self.full_display_name = unicode()
        self.long_display_name = unicode()
        self.short_display_name = unicode()


def _extend_property_01(ctx):
    """Sets property extension properties.

    """
    ctx.p.ext = _PropertyExtensionInfo()
    ctx.p.ext.ancestors = ctx.ancestors
    ctx.p.ext.depth = len(ctx.ancestors)
    ctx.p.ext.parent = ctx.parent


def _extend_property_02(ctx):
    """Formats property values.

    """
    ctx.p.values = filter(None, ctx.p.values)
    ctx.p.values = map(str_to_unicode, ctx.p.values)
    ctx.p.values = filter(len, ctx.p.values)
    ctx.p.values = map(lambda v: v[0].upper() + v[1:], ctx.p.values)


def _extend_property_03(ctx):
    """Sets property display names.

    """
    # Short name.
    name = ctx.p.short_name
    if len(name) and not name[0].isdigit():
        name = str_to_spaced_case(name)
        name = map(capitalize, name.split(" "))
        name = reduce(lambda x, s: s if x is None else x + " " + s, name, None)
    ctx.p.ext.short_display_name = name

    # Display name.
    if ctx.p.ext.depth:
        ctx.p.ext.display_name += ctx.p.ext.parent.ext.display_name
        ctx.p.ext.display_name += u" > "
    ctx.p.ext.display_name += ctx.p.ext.short_display_name

    # Long name.
    if not ctx.p.ext.depth:
        ctx.p.ext.long_display_name = ctx.c.ext.long_display_name
        ctx.p.ext.long_display_name += u" >> "
    else:
        ctx.p.ext.long_display_name = ctx.p.ext.parent.ext.long_display_name
        ctx.p.ext.long_display_name += u" > "
    ctx.p.ext.long_display_name += ctx.p.ext.short_display_name

    # Full name.
    if not ctx.p.ext.depth:
        ctx.p.ext.full_display_name = ctx.c.ext.full_display_name
        ctx.p.ext.full_display_name += u" >> "
    else:
        ctx.p.ext.full_display_name = ctx.p.ext.parent.ext.full_display_name
        ctx.p.ext.full_display_name += u" > "
    ctx.p.ext.full_display_name += ctx.p.ext.short_display_name


def _extend_property_04(ctx):
    """Process child properties.

    """
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
    for func in (
        _extend_property_01,
        _extend_property_02,
        _extend_property_03,
        _extend_property_04,
        ):
        try:
            func(ctx)
        except Exception as err:
            print func, err
            raise err
