"""
.. module:: software_model_component.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.software.modelcomponent document.


"""
# Module imports.
from collections import namedtuple

from ....ontologies.cim.v1 import ComponentProperty
from ....utils import convert



# Component property parsing context information.
PropertyContextInfo = namedtuple('PropertyContextInfo', ['c', 'p', 'parent', 'ancestors'])


def _parse_property_01(ctx):
    """Sets property extension properties."""
    ctx.p._ancestors = ctx.ancestors
    ctx.p._depth = len(ctx.ancestors)
    ctx.p._parent = ctx.parent


def _parse_property_02(ctx):
    """Sets property key."""
    key = ctx.c._key + '>'
    if len(ctx.p._ancestors):
        key += ctx.p._ancestors[-1].short_name.lower().strip() + '.'
    key += ctx.p.short_name.lower().strip()
    ctx.p._key = key


def _parse_property_03(ctx):
    """Extend component property tree."""
    ctx.c._property_tree.append(ctx.p)


def _parse_property_04(ctx):
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


def _parse_property_05(ctx):
    """Sets property display names."""
    # Tree display name.
    name = convert.str_to_spaced_case(ctx.p.short_name)
    for old, new in [("2 D- ", "2D-"), ("3 D- ", "3D-")]:
        name = name.replace(old, new)
    name = map(lambda s: s[0].upper() + s[1:], name.split(" "))
    name = reduce(lambda x, s: s if x is None else x + " " + s, name, None)
    ctx.p._tree_display_name = name

    # List display name.
    if ctx.p._depth == 0:
        ctx.p._list_display_name = ctx.p._tree_display_name
    else:
        ctx.p._list_display_name = ctx.p._parent._list_display_name
        ctx.p._list_display_name += " > "
        ctx.p._list_display_name += ctx.p._tree_display_name


def _parse_property_06(ctx):
    """Process child properties."""
    for p in ctx.p.sub_properties:
        parse(ctx.c, p, ctx.p, ctx.ancestors + [ctx.p])


# Set of property parsers.
_property_parsers = (
    _parse_property_01,
    _parse_property_02,
    _parse_property_03,
    _parse_property_04,
    _parse_property_05,
    _parse_property_06,
    )


def parse(c, p, parent=None, ancestors=[]):
    """Performs a parse over a property in readiness for later processing.

    :param c: A model component.
    :type c: pyesdoc.ontologies.cim.v1.software.ModelComponent

    :param p: A model component property.
    :type p: pyesdoc.ontologies.cim.v1.software.ComponentProperty

    :param parent: Parent model component property.
    :type parent: pyesdoc.ontologies.cim.v1.software.ComponentProperty

    :param ancestors: Ancestor model component properties.
    :type ancestors: list

    """
    ctx = PropertyContextInfo(c, p, parent, ancestors)
    for f in _property_parsers:
        f(ctx)


def _create_property(p_tree, values, name, description):
    """Sets & returns a component standard property."""
    def append_value(p, v):
        if v is not None:
            p.values.append(str(v))

    # Instantiate.
    p = ComponentProperty()
    p.short_name = p.long_name = name
    p.description = description

    # Append each value.
    if values:
        try:
            iter(values)
        except ValueError:
            for v in values:
                append_value(p, v)
        else:
            append_value(p, values)

    # Append to tree.
    p_tree.append(p)

    return p


def _set_standard_properties_descriptive(c, p_tree):
    """Sets descriptive standard properties."""
    _create_property(p_tree,
                     c.description,
                     'Description',
                     'High-level component description')
    _create_property(p_tree,
                     c.short_name,
                     'Short Name',
                     'Abbreviated component name')
    _create_property(p_tree,
                     c.long_name,
                     'Long Name',
                     'Full component name')


def _set_standard_properties_pi(c, p_tree):
    """Sets principal investigator standard properties.

    :param c: A model component.
    :type c: pyesdoc.ontologies.cim.v1.software.ModelComponent

    :param p_tree: A set of component properties.
    :type p_tree: list

    """
    # Set PI.
    pi = None
    for rp in c.responsible_parties:
        if rp.role and rp.role.upper() == "PI":
            pi = rp
            break

    # Set PI properties.
    if pi:
        _create_property(p_tree,
                         pi.individual_name,
                         'PI Name',
                         'PI Name')
        if pi.contact_info:
            _create_property(p_tree,
                             pi.contact_info.email,
                             'PI Email Address',
                             'PI Email Address')


def _set_standard_properties_citations(c, p_tree):
    """Sets citation standard properties."""
    def get_citation_title(citation):
        return citation.title.strip()

    def get_citation_url(citation):
        if citation.location is None or citation.location.strip() == "":
            return "N/A"
        else:
            return citation.location.strip()

    # Set container property.
    p = _create_property(p_tree,
                         None,
                         'Citations',
                         'Set of component citations')

    # Set citation title.
    _create_property(p.sub_properties,
                     [get_citation_title(i) for i in c.citations if i.title is not None],
                     'Title',
                     'Title')

    # Set citation location.
    _create_property(p.sub_properties,
                     [get_citation_url(i) for i in c.citations if i.title is not None],
                     'Location',
                     'Location')


def set_standard_properties(c):
    """Sets standard properties for a component.

    :param c: A model component.
    :type c: pyesdoc.ontologies.cim.v1.software.ModelComponent

    """
    # Create property group.
    p = _create_property(c._standard_properties,
                         None,
                         'Standard Properties',
                         'Set of properties common to all components')
    # Create sub-groups.
    for setter in [
        _set_standard_properties_descriptive,
        _set_standard_properties_pi,
        _set_standard_properties_citations
    ]:
        setter(c, p.sub_properties)


def set_scientific_properties(c):
    """Sets scientific properties for a component.

    :param c: A model component.
    :type c: pyesdoc.ontologies.cim.v1.software.ModelComponent

    """
    pass
