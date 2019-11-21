"""
.. module:: software_model_component_type_map.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes mappings of software model component types.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""



# Map from metafor to es-doc model component types.
METAFOR_ESDOC_MODEL_COMPONENT_MAP = {
    # Aerosols
    'Aerosols': 'Aerosols',
    'AerosolEmissionAndConc' : 'Aerosols > Emission & Concentration',
    'AerosolModel' :  'Aerosols > Model',
    'AerosolTransport' :  'Aerosols > Transport',

    # Atmosphere
    'Atmosphere': 'Atmosphere',
    'AtmosConvectTurbulCloud' : 'Atmosphere > Convection Cloud Turbulence',
    'AtmosCloudScheme' : 'Atmosphere > Convection Cloud Turbulence > Cloud Scheme',
    'CloudSimulator' : 'Atmosphere > Convection Cloud Turbulence > Cloud Simulator',
    'AtmosDynamicalCore' : 'Atmosphere > Dynamical Core',
    'AtmosAdvection' : 'Atmosphere > Dynamical Core > Advection',
    'AtmosOrographyAndWaves' : 'Atmosphere > Orography & Waves',
    'AtmosRadiation' : 'Atmosphere > Radiation',
    'OzoneParameterization' : 'Atmosphere > Ozone Parameterization',

    # Atmospheric Chemistry
    'AtmosphericChemistry' : 'Atmospheric Chemistry',
    'AtmChemTransport' : 'Atmospheric Chemistry > Transport',
    'AtmChemPhotoChemistry' : 'Atmospheric Chemistry > Photo Chemistry',
    'AtmChemHeterogenChemistry' : 'Atmospheric Chemistry > Heterogen Chemistry',
    'StratosphericHeterChem' : 'Atmospheric Chemistry > Heterogen Chemistry > Stratospheric',
    'TroposphericHeterChem' : 'Atmospheric Chemistry > Heterogen Chemistry > Tropospheric',
    'AtmChemGasPhaseChemistry' : 'Atmospheric Chemistry > Gas Phase Chemistry',
    'AtmChemEmissionAndConc' : 'Atmospheric Chemistry > Emission & Concentration',

    # Land Ice
    'LandIce' : 'Land Ice',
    'LandIceGlaciers' : 'Land Ice > Glaciers',
    'LandIceSheet' : 'Land Ice > Sheet',
    'IceSheetDynamics' : 'Land Ice > Sheet > Dynamics',
    'LandIceShelves' : 'Land Ice > Shelves',
    'LandIceShelvesDynamics' : 'Land Ice > Shelves > Dynamics',

    # Land Surface
    'LandSurface' : 'Land Surface',
    'LandSurfaceAlbedo' : 'Land Surface > Albedo',
    'LandSurfaceCarbonCycle' : 'Land Surface > Carbon Cycle',
    'LandSurfaceEnergyBalance' : 'Land Surface > Energy Balance',
    'VegetationCarbonCycle' : 'Land Surface > Carbon Cycle > Vegetation',
    'LandSurfaceLakes' : 'Land Surface > Lakes',
    'LandSurfaceSnow' : 'Land Surface > Snow',
    'LandSurfaceSoil' : 'Land Surface > Soil',
    'LandSurfaceVegetation' : 'Land Surface > Vegetation',
    'LandSurfSoilHeatTreatment' : 'Land Surface > Soil > Heat Treatment',
    'LandSurfSoilHydrology' : 'Land Surface > Soil > Hydrology',
    'RiverRouting': 'Land Surface > River Routing',

    # Ocean
    'Ocean' : 'Ocean',
    'OceanAdvection' : 'Ocean > Advection',
    'OceanBoundaryForcing' : 'Ocean > Boundary Forcing',
    'OceanBoundForcingTracers' : 'Ocean > Boundary Forcing > Tracers',
    'OceanInteriorMixing' : 'Ocean > Vertical Physics > Interior Mixing',
    'OceanLateralPhysics' : 'Ocean > Lateral Physics',
    'OceanLateralPhysMomentum' : 'Ocean > Lateral Physics > Momentum',
    'OceanLateralPhysTracers' : 'Ocean > Lateral Physics > Tracers',
    'OceanMixedLayer' : 'Ocean > Vertical Physics > Mixed Layer',
    'OceanStraits' : 'Ocean > Lateral Physics > Straits',
    'OceanUpAndLowBoundaries' : 'Ocean > Upper & Lower Boundaries',
    'OceanVerticalPhysics' : 'Ocean > Vertical Physics',

    # Ocean Bio-Geo Chemistry
    'OceanBiogeoChemistry' : 'Ocean Bio-Geo Chemistry',
    'OceanBioBoundaryForcing' : 'Ocean Bio-Geo Chemistry > Boundary Forcing',
    'OceanBioChemistry' : 'Ocean Bio-Geo Chemistry > Chemistry',
    'OceanBioGasExchange' : 'Ocean Bio-Geo Chemistry > Gas Exchange',
    'OceanBioTracers' : 'Ocean Bio-Geo Chemistry > Tracers',
    'OceanBioTracersEcosystem' : 'Ocean Bio-Geo Chemistry > Tracers > Ecosystem',

    # Other
    'Model' : 'Earth System Model',
    'model' : 'Earth System Model',
    'cim.1.software.ModelComponent' : 'Earth System Model',
    'cim.1.software.modelcomponent' : 'Earth System Model',

    # Sea Ice
    'SeaIce' : 'Sea Ice',
    'SeaIceAlbedo' : 'Sea Ice > Albedo',
    'SeaIceDynamics' : 'Sea Ice > Dynamics',
    'SeaIceThermodynamics' : 'Sea Ice > Thermodynamics'
}

# Map from es-doc to metafor model component types.
ESDOC_METAFOR_MODEL_COMPONENT_MAP = \
    {v: k for k, v in METAFOR_ESDOC_MODEL_COMPONENT_MAP.items()}
