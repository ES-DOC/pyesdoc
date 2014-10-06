"""
.. module:: software_model_component.py
   :platform: Unix, Windows
   :synopsis: Extends a cim.v1.software.modelcomponent document.


"""
# Module imports.
from collections import namedtuple

from .software_model_component_property_1 import (
    extend as extend_property,
    )
from .software_model_component_property_2 import (
    set_standard_properties,
    set_scientific_properties,
    set_qc_properties
    )



def get_extenders():
    """Returns set of extension functions."""
    return (
        _set_type_display_info,
        _set_component_hierarchy,
        _set_component_property_sets,
        _set_component_property_trees,
        _set_component_meta_info,
        _set_component_type_info
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


class _ComponentExtensionInfo(object):
    """Conponent extension properties.

    """
    pass


def _get_sort_key(item):
    """Returns a sort key.

    """
    return item.ext.full_display_name


def _extend_component_01(ctx):
    """Initializes component extension properties.

    """
    if not hasattr(ctx.c, "ext"):
        ctx.c.ext = _ComponentExtensionInfo()

    ctx.c.ext.ancestors = ctx.ancestors
    ctx.c.ext.component_tree = []
    ctx.c.ext.depth = len(ctx.ancestors)
    ctx.c.ext.parent = ctx.parent
    ctx.c.ext.properties = []
    ctx.c.ext.qc_properties = []
    ctx.c.ext.qc_property_tree = []
    ctx.c.ext.scientific_properties = []
    ctx.c.ext.scientific_property_tree = []
    ctx.c.ext.standard_properties = []
    ctx.c.ext.standard_property_tree = []


def _extend_component_02(ctx):
    """Sets component tree.

    """
    # Append component to tree of each direct ancestor.
    for a in ctx.c.ext.ancestors:
        a.ext.component_tree.append(ctx.c)


def _extend_component_03(ctx):
    """Sets component display names.

    """
    # Short name.
    if not ctx.c.ext.parent:
        ctx.c.ext.short_display_name = ctx.c.short_name
    elif ctx.c.type in _COMPONENT_TYPE_DISPLAY_NAMES:
        ctx.c.ext.short_display_name = _COMPONENT_TYPE_DISPLAY_NAMES[ctx.c.type]
    else:
        ctx.c.ext.short_display_name = ctx.c.type

    # Long name.
    ctx.c.ext.long_display_name = ""
    if ctx.c.ext.depth > 1:
        ctx.c.ext.long_display_name += ctx.c.ext.parent.ext.long_display_name
        ctx.c.ext.long_display_name += " > "
    ctx.c.ext.long_display_name += ctx.c.ext.short_display_name

    # Full name.
    ctx.c.ext.full_display_name = ""
    if ctx.c.ext.depth > 0:
        ctx.c.ext.full_display_name += ctx.c.ext.parent.ext.full_display_name
        ctx.c.ext.full_display_name += " > "
    ctx.c.ext.full_display_name += ctx.c.ext.short_display_name


def _extend_component_04(ctx):
    """Process child components.

    """
    # Recursively extend child components.
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
    for f in (
        _extend_component_01,
        _extend_component_02,
        _extend_component_03,
        _extend_component_04,
        _extend_component_05,
        ):
        f(ctx)


def _set_type_display_info(ctx):
    """Sets document type information.

    """
    ctx.meta.type_display_name = "Model"
    ctx.meta.type_sort_key = "AA"


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
    def sort_tree(p_tree):
        return sorted(p_tree, key=_get_sort_key)

    def build_tree(p_list, p_tree):
        for p in p_list:
            p_tree.append(p)
            build_tree(p.sub_properties, p_tree)

    for c in [ctx.doc] + ctx.doc.ext.component_tree:
        build_tree(c.ext.scientific_properties, c.ext.scientific_property_tree)
        build_tree(c.ext.standard_properties, c.ext.standard_property_tree)
        build_tree(c.ext.qc_properties, c.ext.qc_property_tree)

        c.ext.scientific_property_tree = sort_tree(c.ext.scientific_property_tree)
        c.ext.standard_properties = sort_tree(c.ext.standard_properties)
        c.ext.qc_property_tree = sort_tree(c.ext.qc_property_tree)


def _set_component_meta_info(ctx):
    """Extends component meta info.

    """
    fields = ('language', 'project', 'source', 'type')
    for c in ctx.doc.ext.component_tree:
        for field in fields:
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
