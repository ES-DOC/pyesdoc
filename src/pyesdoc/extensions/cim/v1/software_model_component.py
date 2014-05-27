"""
.. module:: software_model_component.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.software.modelcomponent document.


"""
# Module imports.
from collections import namedtuple

from . software_model_component_property_1 import (
    extend as extend_property,
    )
from . software_model_component_property_2 import (
    set_standard_properties,
    set_scientific_properties,
    set_qc_properties
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
    'OceanBiogeoChemistry' : 'Ocean Bio-Geo Chemistry',
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


# Component extension context information.
_ComponentContextInfo = \
    namedtuple('ComponentContextInfo', ['c', 'ext', 'parent', 'ancestors'])


def _get_sort_key(item):
    """Returns a sort key."""
    return item._full_display_name


def _extend_component_01(ctx):
    """Initializes component extension properties."""
    ctx.c._ancestors = ctx.ancestors
    ctx.c._component_tree = []
    ctx.c._depth = len(ctx.ancestors)
    ctx.c._parent = ctx.parent
    ctx.c._properties = []
    ctx.c._qc_properties = []
    ctx.c._qc_property_tree = []
    ctx.c._scientific_properties = []
    ctx.c._scientific_property_tree = []
    ctx.c._standard_properties = []
    ctx.c._standard_property_tree = []


def _extend_component_02(ctx):
    """Sets component key."""
    # Create key based upon component type plus ancestor key.
    ctx.c._key = str() if ctx.c.type is None else ctx.c.type.lower()
    if len(ctx.c._ancestors):
        ctx.c._key = ctx.c._ancestors[-1]._key + '.' + ctx.c._key


def _extend_component_03(ctx):
    """Sets component tree."""
    # Append component to tree of each direct ancestor.
    for a in ctx.c._ancestors:
        a._component_tree.append(ctx.c)


def _extend_component_04(ctx):
    """Sets component display names."""
    # Short name.
    if not ctx.c._parent:
        ctx.c._short_display_name = ctx.c.short_name
    elif ctx.c.type in _COMPONENT_TYPE_DISPLAY_NAMES:
        ctx.c._short_display_name = _COMPONENT_TYPE_DISPLAY_NAMES[ctx.c.type]
    else:
        ctx.c._short_display_name = ctx.c.type

    # Long name.
    ctx.c._long_display_name = ""
    if ctx.c._depth > 1:
        ctx.c._long_display_name += ctx.c._parent._long_display_name
        ctx.c._long_display_name += " > "
    ctx.c._long_display_name += ctx.c._short_display_name

    # Full name.
    ctx.c._full_display_name = ""
    if ctx.c._depth > 0:
        ctx.c._full_display_name += ctx.c._parent._full_display_name
        ctx.c._full_display_name += " > "
    ctx.c._full_display_name += ctx.c._short_display_name


def _extend_component_05(ctx):
    """Process child components."""
    for c in ctx.c.sub_components:
        _extend_component(c, c, ctx.c, ctx.ancestors + [ctx.c])


def _extend_component_06(ctx):
    """Sort components."""
    ctx.c.sub_components = sorted(ctx.c.sub_components, key=_get_sort_key)
    ctx.c._component_tree = sorted(ctx.c._component_tree, key=_get_sort_key)


def _extend_component(c, ext, parent=None, ancestors=[]):
    """Extends a component."""
    ctx = _ComponentContextInfo(c, ext, parent, ancestors)
    for f in (
        _extend_component_01,
        _extend_component_02,
        _extend_component_03,
        _extend_component_04,
        _extend_component_05,
        _extend_component_06,
        ):
        f(ctx)


def _set_type_display_info(ctx):
    """Sets document type information."""
    ctx.meta.type_display_name = ctx.ext.type_display_name = "Model"
    ctx.ext.type_sortkey = ctx.meta.type_sortkey = "AA"


def _set_component_hierarchy(ctx):
    """Extends component hierarchy."""
    _extend_component(ctx.doc, ctx.ext)


def _set_component_property_sets(ctx):
    """Extends component property sets."""
    def set_properties(builder, c, p_list):
        builder(c)
        for p in p_list:
            extend_property(c, p)
            c._properties.append(p)

    for c in [ctx.doc] + ctx.doc._component_tree:
        set_properties(set_scientific_properties, c, c._scientific_properties)
        set_properties(set_standard_properties, c, c._standard_properties)
        set_properties(set_qc_properties, c, c._qc_properties)


def _set_component_property_trees(ctx):
    """Extends component property tree."""
    def build_tree(p_list, p_tree, sort=False):
        for p in p_list:
            p_tree.append(p)
            build_tree(p.sub_properties, p_tree)
        if sort:
            p_tree = sorted(p_tree, key=_get_sort_key)

    for c in [ctx.doc] + ctx.doc._component_tree:
        build_tree(c._scientific_properties, c._scientific_property_tree, True)
        build_tree(c._standard_properties, c._standard_property_tree, True)
        build_tree(c._qc_properties, c._qc_property_tree, True)


def _set_component_meta_info(ctx):
    """Extends component meta info."""
    for c in ctx.doc._component_tree:
        if not c.meta.language:
            c.meta.language = ctx.doc.meta.language
        if not c.meta.project:
            c.meta.project = ctx.doc.meta.project
        if not c.meta.source:
            c.meta.source = ctx.doc.meta.source
        if not c.meta.type:
            c.meta.type = ctx.doc.meta.type


def _set_component_type_info(ctx):
    """Extends component type info."""
    for c in [ctx.doc] + ctx.doc._component_tree:
        if not c.type:
            c.type = c.meta.type
        if c.meta.type not in c.types:
            c.types = [c.meta.type] + c.types


# Set of extension functions.
EXTENDERS = (
    _set_type_display_info,
    _set_component_hierarchy,
    _set_component_property_sets,
    _set_component_property_trees,
    _set_component_meta_info,
    _set_component_type_info
    )
