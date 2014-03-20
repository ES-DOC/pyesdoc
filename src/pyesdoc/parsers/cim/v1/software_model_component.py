"""
.. module:: software_model_component.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.software.modelcomponent document.


"""
# Module imports.
from collections import namedtuple

from ....ontologies.cim.v1 import ComponentProperty
from ....utils import convert



# Mappings between component type & component type display name.
_component_type_display_names = {
    'AerosolEmissionAndConc' : 'Emission & Concentration',
    'AerosolModel' :  'Model',
    'AerosolTransport' :  'Transport',
    'AtmosConvectTurbulCloud' : 'Convection Cloud Turbulence',
    'AtmosCloudScheme' : 'Cloud Scheme',
    'CloudSimulator' : 'Cloud Simulator',
    'AtmosDynamicalCore' : 'Dynamical Core',
    'AtmosAdvection' : 'Advection',
    'AtmosOrographyAndWaves' : 'Orography & Waves',
    'AtmosRadiation' : 'Radiation',
    'AtmosphericChemistry' : 'Atmospheric Chemistry',
    'AtmChemTransport' : 'Transport',
    'AtmChemPhotoChemistry' : 'Photo Chemistry',
    'AtmChemHeterogenChemistry' : 'Heterogen Chemistry',
    'StratosphericHeterChem' : 'Stratospheric',
    'TroposphericHeterChem' : 'Tropospheric',
    'AtmChemGasPhaseChemistry' : 'Gas Phase Chemistry',
    'AtmChemEmissionAndConc' : 'Emission & Concentration',
    'LandIce' : 'Land Ice',
    'LandIceGlaciers' : 'Glaciers',
    'LandIceSheet' : 'Sheet',
    'LandIceShelves' : 'Shelves',
    'LandIceShelves Dynamics' : 'Dynamics',
    'LandSurface' : 'Land Surface',
    'LandSurfaceAlbedo' : 'Albedo',
    'LandSurfaceCarbonCycle' : 'Carbon Cycle',
    'LandSurfaceEnergyBalance' : 'Energy Balance',
    'VegetationCarbonCycle' : 'Vegetation',
    'LandSurfaceLakes' : 'Lakes',
    'LandSurfaceSnow' : 'Snow',
    'LandSurfaceSoil' : 'Soil',
    'LandSurfaceVegetation' : 'Vegetation',
    'LandSurfSoilHeatTreatment' : 'Heat Treatment',
    'LandSurfSoilHydrology' : 'Hydrology',
    'Model' : 'Earth System Model',
    'OceanBioBoundaryForcing' : 'Boundary Forcing',
    'OceanBioChemistry' : 'Chemistry',
    'OceanBioGasExchange' : 'Gas Exchange',
    'OceanBiogeoChemistry' : 'Ocean Bio-Geo Chem.',
    'OceanBioTracers' : 'Tracers',
    'OceanBioTracersEcosystem' : 'Ecosystem',
    'OceanAdvection' : 'Advection',
    'OceanBoundaryForcing' : 'Boundary Forcing',
    'OceanBoundForcingTracers' : 'Tracers',
    'OceanInteriorMixing' : 'Interior Mixing',
    'OceanLateralPhysics' : 'Lateral Physics',
    'OceanLateralPhysMomentum' : 'Momentum',
    'OceanLateralPhysTracers' : 'Tracers',
    'OceanMixedLayer' : 'Mixed Layer',
    'OceanUpAndLowBoundaries' : 'Up & Low Boundaries',
    'OceanVerticalPhysics' : 'Vertical Physics',
    'SeaIce' : 'Sea Ice',
    'SeaIceDynamics' : 'Dynamics',
    'SeaIceThermodynamics' : 'Thermodynamics'
}



def _set_standard_property(p_tree, values, name, description):
    """Sets & returns a component standard property."""
    def append_value(p, v):
        if v is not None:
            p.values.append(str(v))

    p = ComponentProperty()
    p.short_name = p.long_name = name
    p.description = description

    try:
        iter(values)
    except ValueError:
        for v in values:
            append_value(p, v)
    else:
        append_value(p, values)

    p_tree.append(p)
    
    return p


def _set_standard_properties_descriptive(c, p_tree):
    """Sets descriptive standard properties."""
    _set_standard_property(p_tree,
                           c.description,
                           'Description',
                           'High-level component description')
    _set_standard_property(p_tree,
                           c.short_name,
                           'Short Name',
                           'Abbreviated component name')
    _set_standard_property(p_tree,
                           c.long_name,
                           'Long Name',
                           'Full component name')

                       
def _set_standard_properties_citations(c, p_tree):
    """Sets citation standard properties."""
    def get_citation_title(citation):
        return citation.title.strip()
    
    def get_citation_url(citation):
        if citation.location is None or citation.location.strip() == "":
            return "N/A"
        else:
            return citation.location.strip()

    p = _set_standard_property(p_tree,
                               None,
                               'Citations',
                               'Set of component citations')

    _set_standard_property(p.sub_properties,
                           [get_citation_title(i) for i in c.citations if i.title is not None],
                           'Title',
                           'Title')
    _set_standard_property(p.sub_properties,
                           [get_citation_url(i) for i in c.citations if i.title is not None],
                           'Location',
                           'Location')


def _set_standard_properties_pi(c, p_tree):
    """Sets principal investigator standard properties."""
    # Set PI.
    pi = None
    for rp in c.responsible_parties:
        if rp.role and rp.role.upper() == "PI":
            pi = rp
            break
            
    # Set PI properties.
    if pi:
        _set_standard_property(p_tree,
                               pi.individual_name,
                               'PI Name',
                               'PI Name')
        if pi.contact_info:
            _set_standard_property(p_tree,
                                   pi.contact_info.email,
                                   'PI Email Address',
                                   'PI Email Address')


def _set_standard_properties(c):
    """Set component standard properties."""
    # Create property group.
    p = _set_standard_property(c.properties,
                               None,
                               'Standard Properties',
                               'Set of properties common to all components')

    # Create sub-groups.
    for factory in [
        _set_standard_properties_descriptive,
        _set_standard_properties_pi,
        _set_standard_properties_citations
    ]:
        factory(c, p.sub_properties)


def _set_scientific_properties(c):
    """Set component scientific properties."""
    # TODO group existing properties under this umbrella
    pass


def _parse_components(c_tree):
    """Recursivley parses a component tree."""
    for c in c_tree:
        _set_standard_properties(c)
        _set_scientific_properties(c)
        _parse_components(c.sub_components)




def _parse_component_property(c, p):
    # ... extend component property tree
    c._property_tree.append(p)
    
    # ... parse sub-properties
    for p in p.sub_properties:
        _parse_component_property(c, p)


def _parse_component(doc, c):
    # ... extend component tree
    doc._component_tree.append(c)

    # ... build component property tree
    c._property_tree = []
    for p in c.properties:
        _parse_component_property(c, p)

    # ... parse sub-components
    for c in c.sub_components:
        _parse_component(doc, c)


# Component parsing context information.
ComponentContextInfo = namedtuple('ComponentContextInfo', ['c', 'parent', 'ancestors'])

# Component property parsing context information.
PropertyContextInfo = namedtuple('PropertyContextInfo', ['p', 'parent', 'ancestors'])


def _do_parse(parsers, ctx):    
    for parser in parsers:
        parser(ctx)


def _parse_property_01(ctx):
    ctx.p._ancestors = ctx.ancestors
    ctx.p._depth = len(ctx.ancestors)
    ctx.p._parent = ctx.parent
    ctx.p._property_tree = []


def _parse_property_02(ctx):
    """Sets property tree."""
    for a in ctx.p._ancestors:
        a._property_tree.append(ctx.p)


def _parse_property_03(ctx):
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


def _parse_property_04(ctx):
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


def _parse_property_05(ctx):
    """Process child properties."""
    for p in ctx.p.sub_properties:
        _do_parse(_property_parsers, 
                  PropertyContextInfo(p, ctx.p, ctx.ancestors + [ctx.p]))


# Set of property parsers.
_property_parsers = (
    _parse_property_01,
    _parse_property_02,
    _parse_property_03,
    _parse_property_04,
    _parse_property_05,
    )


def _parse_component_01(ctx):
    """Sets component extension properties."""
    ctx.c._ancestors = ctx.ancestors
    ctx.c._component_tree = []
    ctx.c._depth = len(ctx.ancestors)
    ctx.c._parent = ctx.parent
    ctx.c._property_list = []
    ctx.c._property_tree = []
    ctx.c._display_name = ctx.c.short_name


def _parse_component_02(ctx):
    """Sets component key."""
    ctx.c._key = ctx.c.type.lower()
    if len(ctx.c._ancestors):
        ctx.c._key = ctx.c._ancestors[-1]._key + '.' + ctx.c._key


def _parse_component_03(ctx):
    """Sets component tree."""
    for a in ctx.c._ancestors:
        a._component_tree.append(ctx.c)


def _parse_component_04(ctx):
    """Sets component tree display name."""
    if not ctx.c._parent:
        ctx.c._tree_display_name = ctx.c.short_name
    elif ctx.c.type in _component_type_display_names:
        ctx.c._tree_display_name = _component_type_display_names[ctx.c.type]
    else:
        ctx.c._tree_display_name = ctx.c.type


def _parse_component_05(ctx):
    """Sets component list display name."""
    if ctx.c._depth <= 1:
        ctx.c._list_display_name = ctx.c._tree_display_name
    else:
        ctx.c._list_display_name = ctx.c._parent._list_display_name
        ctx.c._list_display_name += " > "
        ctx.c._list_display_name += ctx.c._tree_display_name


def _parse_component_06(ctx):
    """Process child components."""
    for c in ctx.c.sub_components:
        _do_parse(_component_parsers, 
                  ComponentContextInfo(c, ctx.c, ctx.ancestors + [ctx.c]))


def _parse_component_07(ctx):
    """Sort child components."""
    ctx.c.sub_components = sorted(ctx.c.sub_components, key=lambda c: c._list_display_name)


def _parse_component_08(ctx):
    """Process child properties."""
    for p in ctx.c.properties:
        _do_parse(_property_parsers, PropertyContextInfo(p, None, []))
        ctx.c._property_tree += [p] + p._property_tree

    ctx.c._property_list = filter(lambda p: p._value is not None, ctx.c._property_tree)


# Set of component parsers.
_component_parsers = (
    _parse_component_01, 
    # _parse_component_02,
    # _parse_component_03,
    # _parse_component_04,
    # _parse_component_05,
    # _parse_component_06,
    # _parse_component_07,
    # _parse_component_08,
    )


def parse(doc):
    """Performs a parse over a model in readiness for later processing.

    :param doc: A model component.
    :type doc: pyesdoc.ontologies.cim.v1.software.ModelComponent

    :returns: A model component.
    :rtype: pyesdoc.ontologies.cim.v1.software.ModelComponent

    """
    # Set document type display name.
    doc._type_display_name = doc.doc_info.type_display_name = "Model"

    # Intiialize parsing context info.
    ctx = ComponentContextInfo(doc, None, [])

    # Parse document.
    _do_parse(_component_parsers, ctx)

    return doc