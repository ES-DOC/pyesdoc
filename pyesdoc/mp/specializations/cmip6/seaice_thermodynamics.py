"""

A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.
"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Sea Ice Thermodynamics'

# --------------------------------------------------------------------
# SUB-PROCESS: Processes related to energy in sea ice thermodynamics
# --------------------------------------------------------------------
DETAILS['energy'] = {
    'description': 'Processes related to energy in sea ice thermodynamics.',
    'properties': [
        ('enthalpy_formulation', 'ENUM:energy_formulation', '1.1',
            "What is the energy formulation?"),
        ('thermal_conductivity', 'ENUM:thermal_conductivity_type', '1.1',
            "What type of thermal conductivity is used?"),
        ('heat_diffusion', 'ENUM:heat_diffusion_type', '1.1',
            "What is the method of heat diffusion?"),
        ('basal_heat_flux', 'ENUM:basal_heat_flux_method', '1.1',
            "Method by which basal ocean heat flux is handled?"),
        ('fixed_salinity_value', 'float', '0.1',
             """If you have selected {Thermal properties depend on S-T (with fixed salinity)},
             supply fixed salinity value for each sea ice layer."""),
        ('heat_content_of_precipitation', 'l-str', '1.1',
            "Describe the method by which the heat content of precipitation is handled."),
        ('precipitation_effects_on_salinity', 'l-str', '0.1',
             """If precipitation (freshwater) that falls on sea ice affects the ocean surface
             salinity please provide further details.""")
    ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Mass.
# --------------------------------------------------------------------
DETAILS['mass'] = {
    'description': 'Processes related to mass in sea ice thermodynamics.',
    'properties': [
        ('new_ice_formation', 'l-str', '1.1',
             "Describe the method by which new sea ice is formed in open water."),
        ('ice_vertical_growth_and_melt', 'l-str', '1.1',
             "Describe the method that governs the vertical growth and melt of sea ice."),
        ('ice_lateral_melting', 'ENUM:lateral_melting_types', '1.1',
             "What is the method of sea ice lateral melting?"),
        ('ice_surface_sublimation', 'l-str', '1.1',
             "Describe the method that governs sea ice surface sublimation."),
        ('frazil_ice', 'l-str', '1.1',
             "Describe the method of frazil ice formation."),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Salt.
# --------------------------------------------------------------------
DETAILS['salt'] = {
    'description': 'Processes related to salt in sea ice thermodynamics.',
    'properties': [
        ('has_multiple_sea_ice_salinities', 'bool', '1.1',
            """Does the sea ice model use two different salinities: one for
            thermodynamic calculations; and one for the salt budget?"""),
        ('sea_ice_salinity_thermal_impacts', 'bool', '1.1',
            "Does sea ice salinity impact the thermal properties of sea ice?"),
    ]
}

DETAILS['salt:mass_transport']={
    'description':'Mass transport of salt.',
    'properties': [
        ('salinity_type', 'ENUM:salinity_method', '1.1',
            "How is salinity determined in the mass transport of salt calculation?"),
        ('constant_salinity_value', 'float', '0.1',
             "If using a constant salinity value specify this value in PSU?"),
        ('additional_details', 'l-str', '0.1',
            "Describe the salinity profile used."),
        ]
    }

DETAILS['salt:thermodynamics']={
    'description':'Salt thermodynamics',
    'properties': [
        ('salinity_type', 'ENUM:salinity_method', '1.1',
            "How is salinity determined in the thermodynamic calculation?"),
        ('constant_salinity_value', 'float', '0.1',
             "If using a constant salinity value specify this value in PSU?"),
        ('additional_details', 'l-str', '0.1',
            "Describe the salinity profile used."),
        ]
    }


# --------------------------------------------------------------------
# SUB-PROCESS: Ice Thickness Distribution.
# --------------------------------------------------------------------
DETAILS['ice_thickness_distribution'] = {
    'description': 'Ice thickness distribution details.',
    'properties': [
        ('representation', 'ENUM:ice_thickness_representation', '1.1',
            "How is the sea ice thickness distribution represented?"),
        ]
    }


# --------------------------------------------------------------------
# SUB-PROCESS: Ice floe-size Distribution.
# --------------------------------------------------------------------
DETAILS['ice_floe_size_distribution'] = {
    'description': 'Ice floe-size distribution details.',
    'properties': [
        ('representation', 'ENUM:ice_floe_size', '1.1',
            "How is the sea ice floe-size represented?"),
        ('additional_details', 'l-str', '0.1',
            "Provide further details on any parameterisation of floe-size."),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Melt Ponds
# --------------------------------------------------------------------
DETAILS['melt_ponds'] = {
    'description': 'Characteristics of melt ponds.',
    'properties': [
        ('are_included', 'bool', '1.1',
            "Are melt ponds included in the sea ice model?"),
        ('formulation', 'ENUM:melt_pond_formulation', '1.1',
            "What method of melt pond formulation is used?"),
        ('impacts', 'ENUM:melt_pond_impacts', '1.N',
            "What do melt ponds have an impact on?")
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Snow thermodynamic processes.
# --------------------------------------------------------------------
DETAILS['snow_processes'] = {
    'description': 'Thermodynamic processes in snow on sea ice',
    'properties': [
        ('has_snow_aging', 'bool', '1.1', "Set to True if the sea ice model has a snow aging scheme."),
        ('snow_aging_scheme', 'l-str', '0.1', "Describe the snow aging scheme."),
        ('has_snow_ice_formation', 'bool', '1.1', "Set to True if the sea ice model has snow ice formation."),
        ('snow_ice_formation_scheme', 'l-str', '0.1', "Describe the snow ice formation scheme."),
        ('redistribution', 'str', '1.1', "What is the impact of ridging on snow cover?"),
        ('heat_diffusion', 'ENUM:snow_process_types', '1.1',
            "What is the heat diffusion through snow methodology in sea ice thermodynamics?"),
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['energy_formulation'] = {
    'description': 'Thermodynamic energy formulations',
    'is_open': True,
    'members': [
        ('Pure ice latent heat (Semtner 0-layer)', None),
        ('Pure ice latent and sensible heat', None),
        ('Pure ice latent and sensible heat + brine heat reservoir (Semtner 3-layer)', None),
        ('Pure ice latent and sensible heat + explicit brine inclusions (Bitz and Lipscomb)', None),
    ]
}

ENUMERATIONS['thermal_conductivity_type'] = {
    'description': 'Types of thermal conductivity',
    'is_open': True,
    'members': [
        ('Pure ice', None),
        ('Saline ice', None),
    ]
}

ENUMERATIONS['basal_heat_flux_method'] = {
    'description': 'Basal ocean heat flux methodology.',
    'is_open': True,
    'members': [
        ('Heat Reservoir', 'Brine inclusions treated as a heat reservoir.'),
        ('Thermal Fixed Salinity', 'Thermal properties depend on S-T (with fixed salinity).'),
        ('Thermal Varying Salinity', 'Thermal properties depend on S-T (with varying salinity.'),
    ]
}

ENUMERATIONS['heat_diffusion_type'] = {
    'description': 'Heat diffusion types.',
    'is_open': True,
    'members': [
        ('Conduction fluxes', None),
        ('Conduction and radiation heat fluxes', None),
        ('Conduction, radiation and latent heat transport', None),
    ]
}

ENUMERATIONS['lateral_melting_types'] = {
    'description': 'Ice lateral melting methods',
    'is_open': True,
    'members': [
        ('Floe-size dependent (Bitz et al 2001)', None),
        ('Virtual thin ice melting (for single-category)', None),
    ]
}

ENUMERATIONS['ice_thickness_representation'] = {
    'description': 'Types of sea ice thickness representation.',
    'is_open': True,
    'members': [
        ('Explicit', None),
        ('Virtual (enhancement of thermal conductivity, thin ice melting)', None),
    ]
}

ENUMERATIONS['ice_floe_size'] = {
    'description': 'Ice floe-size representation.',
    'is_open': True,
    'members': [
        ('Explicit', None),
        ('Parameterised', None),
    ]
}

ENUMERATIONS['thermo_brine_types'] = {
    'description': 'Brine inclusion methodologies.',
    'is_open': True,
    'members': [
        ('Heat Reservoir', 'Brine inclusions treated as a heat reservoir.'),
        ('Thermal Fixed Salinity', 'Thermal properties depend on S-T (with fixed salinity).'),
        ('Thermal Varying Salinity', 'Thermal properties depend on S-T (with varying salinity.'),
    ]
}

ENUMERATIONS['melt_pond_formulation'] = {
    'description': 'Formulations of melt ponds.',
    'is_open': True,
    'members': [
        ('Flocco and Feltham (2010)', None),
        ('Level-ice melt ponds', None),
    ]
}

ENUMERATIONS['melt_pond_impacts'] = {
    'description': 'Impacts of melt ponds.',
    'is_open': True,
    'members': [
        ('Albedo', None),
        ('Freshwater', None),
        ('Heat', None),
    ]
}

ENUMERATIONS['snow_process_types'] = {
    'description': 'Types of snow processes.',
    'is_open': True,
    'members': [
        ('Single-layered heat diffusion', None),
        ('Multi-layered heat diffusion', None),
    ]
}

ENUMERATIONS['salinity_method'] = {
    'description': 'Method of describing the value of salinity.',
    'is_open': True,
    'members': [
        ('Constant', None),
        ('Prescribed salinity profile', None),
        ('Prognostic salinity profile', None),
    ]
}
