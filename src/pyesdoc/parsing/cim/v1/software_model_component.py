"""
.. module:: software_model_component.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.software.modelcomponent document.


"""
# Module imports.
from collections import namedtuple

from . software_model_component_property import (
    parse as parse_property,
    set_standard_properties,
    set_scientific_properties
    )



# Mappings between component type & component type display name.
_COMPONENT_TYPE_DISPLAY_NAMES = {
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


# Component parsing context information.
_ComponentContextInfo = \
    namedtuple('ComponentContextInfo', \
               ['c', 'ext', 'parent', 'ancestors'])


def _parse_component_01(ctx):
    """Sets component extension properties."""
    ctx.c._ancestors = ctx.ancestors
    ctx.c._component_tree = []
    ctx.c._depth = len(ctx.ancestors)
    ctx.c._parent = ctx.parent
    ctx.c._property_list = []
    ctx.c._property_tree = []
    ctx.c._display_name = ctx.c.short_name
    ctx.c._standard_properties = []


def _parse_component_02(ctx):
    """Sets component key."""
    # Create key based upon component type plus ancestor key.
    ctx.c._key = ctx.c.type.lower()
    if len(ctx.c._ancestors):
        ctx.c._key = ctx.c._ancestors[-1]._key + '.' + ctx.c._key


def _parse_component_03(ctx):
    """Sets component tree."""
    # Append component to tree of each direct ancestor.
    for a in ctx.c._ancestors:
        a._component_tree.append(ctx.c)


def _parse_component_04(ctx):
    """Sets component tree display name."""
    if not ctx.c._parent:
        ctx.c._tree_display_name = ctx.c.short_name
    elif ctx.c.type in _COMPONENT_TYPE_DISPLAY_NAMES:
        ctx.c._tree_display_name = _COMPONENT_TYPE_DISPLAY_NAMES[ctx.c.type]
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
        _do_component_parse(_ComponentContextInfo(c, c, ctx.c, ctx.ancestors + [ctx.c]))


def _parse_component_07(ctx):
    """Sort child components."""
    def get_sort_key(c):
        return c._list_display_name

    ctx.c.sub_components = sorted(ctx.c.sub_components, key=get_sort_key)


def _parse_component_08(ctx):
    """Set component property tree."""
    for p in ctx.c.properties:
        parse_property(ctx.c, p)
        ctx.c._property_tree += [p] + p._property_tree


def _parse_component_09(ctx):
    """Set flattened component property tree."""
    ctx.c._property_list = filter(lambda p: p._value is not None,
                                  ctx.c._property_tree)


def _parse_component_10(ctx):
    """Set standard/scientific properties."""
    set_standard_properties(ctx.c)
    set_scientific_properties(ctx.c)


# Set of component parsers.
_COMPONENT_PARSERS = (
    _parse_component_01,
    _parse_component_02,
    _parse_component_03,
    _parse_component_04,
    _parse_component_05,
    _parse_component_06,
    _parse_component_07,
    _parse_component_08,
    _parse_component_09,
    _parse_component_10,
    )


def _do_component_parse(ctx):
    """Parses a component."""
    for f in _COMPONENT_PARSERS:
        f(ctx)


def _set_type_display_name(ctx):
    """Sets document type display name."""
    ctx.meta.type_display_name = ctx.ext.type_display_name = "Model"


def _set_component_hierarchy(ctx):
    """Parses component hierarchy."""
    _do_component_parse(_ComponentContextInfo(ctx.doc, ctx.ext, None, []))


def _set_component_meta_info(ctx):
    """Parses component hierarchy."""
    for c in ctx.doc._component_tree:
        if not c.meta.language:
            c.meta.language = ctx.doc.meta.language
        if not c.meta.project:
            c.meta.project = ctx.doc.meta.project
        if not c.meta.source:
            c.meta.source = ctx.doc.meta.source
        if not c.meta.type:
            c.meta.type = ctx.doc.meta.type


# Set of parsing functions.
PARSERS = (
    _set_type_display_name,
    _set_component_hierarchy,
    _set_component_meta_info
    )
