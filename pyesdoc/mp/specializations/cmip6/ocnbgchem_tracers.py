"""A realm process sepecialization.

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
DESCRIPTION = 'Ocean biogeochemistry tracers'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level properties of tracers in ocean biogeochemistry',
    'properties': [
        ('sulfur_cycle_present', 'bool', '1.1',
            'Is sulfur cycle modeled ?'),
        ('nutrients_present', 'ENUM:nutrients_species', '1.N',
            'List nutrient species present in ocean biogeochemistry model'),
        ('nitrous_species_if_N', 'ENUM:nitrous_species', '0.N',
            'If nitrogen present, list nitrous species.'),
        ('nitrous_processes_if_N', 'ENUM:nitrous_processes', '0.N',
            'If nitrogen present, list nitrous processes.'),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: detailed properties
# --------------------------------------------------------------------
DETAILS['ecosystem'] = {
    'description': 'Ecosystem properties in ocean biogeochemistry',
    'properties': [
        ('upper_trophic_levels_definition', 'str', '1.1',
            'Describe how upper trophic levels are defined in model (e.g. based on size)'),
        ('upper_trophic_levels_treatment', 'str', '1.1',
            'Describe how upper trophic levels are treated in model'),
        ]
    }

DETAILS['ecosystem:phytoplankton'] = {
    'description': 'Phytoplankton properties in ocean biogeochemistry',
    'properties': [
        ('type', 'ENUM:phytoplankton_types', '1.1',
            'Type of phytoplankton'),
        ('pft', 'ENUM:phytoplankton_pft_list', '0.N',
            'Phytoplankton functional types (PFT) (if applicable)'),
        ('size_classes','ENUM:phytoplankton_size_classes','0.N',
            'Phytoplankton size classes (if applicable)')
        ]
    }

DETAILS['ecosystem:zooplankton'] = {
    'description': 'Zooplankton properties in ocean biogeochemistry',
    'properties': [
        ('type', 'ENUM:zooplankton_types', '1.1',
            'Type of zooplankton'),
        ('size_classes','ENUM:zooplankton_size_classes','0.N',
            'Zooplankton size classes (if applicable)')
        ]
    }

DETAILS['disolved_organic_matter'] = {
    'description': 'Disolved organic matter properties in ocean biogeochemistry',
    'properties': [
        ('bacteria_present', 'bool', '1.1',
            'Is there bacteria representation ?'),
        ('lability', 'ENUM:lability_treatment', '1.1',
            'Describe treatment of lability in dissolved organic matter'),
        ]
    }


DETAILS['particules'] = {
    'description': 'Particulate carbon properties in ocean biogeochemistry',
    'properties': [
        ('method', 'ENUM:particules_method', '1.N',
            'How is particulate carbon represented in ocean biogeochemistry?'),
        ('types_if_prognostic', 'ENUM:prognostic_particules_types', '0.N',
            'If prognostic, type(s) of particulate matter taken into account'),
        ('size_if_prognostic', 'ENUM:prognostic_particules_sizes', '0.1',
            'If prognostic, describe if a particule size spectrum is used to represent distribution of particules in water volume'),
        ('size_if_discrete', 'str', '0.1',
            'If prognostic and discrete size, describe which size classes are used'),
        ('sinking_speed_if_prognostic', 'ENUM:prognostic_particules_sinking_speed', '0.1',
            'If prognostic, method for calculation of sinking speed of particules'),
        ]
    }

DETAILS['dic_alkalinity'] = {
    'description': 'DIC and alkalinity properties in ocean biogeochemistry',
    'properties': [
        ('carbon_isotopes', 'ENUM:carbon_isotopes_list', '1.N',
            'Which carbon isotopes are modelled (C13, C14)?'),
        ('abiotic_carbon', 'bool', '1.1',
            'Is abiotic carbon modelled ?'),
        ('alkalinity', 'ENUM:alkalinity_model_types', '1.1',
            'How is alkalinity modelled ?'),
        ]
    }


#
# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['nutrients_species'] = {
    'description': 'Nutrients species in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Nitrogen (N)', None),
        ('Phosphorous (P)', None),
        ('Silicon (S)', None),
        ('Iron (Fe)', None),
        ]
    }

ENUMERATIONS['nitrous_species'] = {
    'description': 'Nitrous species in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Nitrates (NO3)', None),
        ('Amonium (NH4)', None),
       ]
    }

ENUMERATIONS['nitrous_processes'] = {
    'description': 'Nitrous processes in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Dentrification', None),
        ('N fixation', None),
       ]
    }

ENUMERATIONS['phytoplankton_types'] = {
    'description': 'Phytoplankton types in ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('None', None),
        ('Generic', None),
        ('PFT including size based (specify both below)', 'Plankton functional type including size based'),
        ('Size based only (specify below)', None),
        ('PFT only (specify below)', None),
        ]
    }

ENUMERATIONS['phytoplankton_pft_list'] = {
    'description': 'Phytoplankton functional types list in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Diatoms', None),
        ('Nfixers', None),
        ('Calcifiers', None),
       ]
    }

ENUMERATIONS['phytoplankton_size_classes'] = {
    'description': 'Phytoplankton size classes in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Microphytoplankton', None),
        ('Nanophytoplankton', None),
        ('Picophytoplankton', None),
       ]
    }

ENUMERATIONS['zooplankton_types'] = {
    'description': 'Zooplankton types in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('None', None),
        ('Generic', None),
        ('Size based (specify below)', None),
        ]
    }

ENUMERATIONS['zooplankton_size_classes'] = {
    'description': 'Zooplankton size classes in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Microzooplankton', None),
        ('Mesozooplankton', None),
       ]
    }

ENUMERATIONS['lability_treatment'] = {
    'description': 'Lability treatment of dissolved organic matter in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('None', None),
        ('Labile', 'Less than a few days'),
        ('Semi-labile', 'Few days to a few years'),
        ('Refractory', 'Over a few years'),
        ]
    }

ENUMERATIONS['particules_method'] = {
    'description': 'Particulate carbon representation in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Diagnostic', None),
        ('Diagnostic (Martin profile)', None),
        ('Diagnostic (Balast)', None),
        ('Prognostic', None),
       ]
    }

ENUMERATIONS['prognostic_particules_types'] = {
    'description': 'Prognostic particulate carbon types in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('POC', None),
        ('PIC (calcite)', None),
        ('PIC (aragonite', None),
        ('BSi', None),
       ]
    }

ENUMERATIONS['prognostic_particules_sizes'] = {
    'description': 'Prognostic particulate carbon size in ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('No size spectrum used', None),
        ('Full size spectrum', None),
        ('Discrete size classes (specify which below)', None),
       ]
    }

ENUMERATIONS['prognostic_particules_sinking_speed'] = {
    'description': 'Prognostic particulate carbon sinking speed in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Constant', None),
        ('Function of particule size', None),
        ('Function of particule type (balast)', None),
       ]
    }

ENUMERATIONS['carbon_isotopes_list'] = {
    'description': 'List of carbon isotopes in ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('C13', None),
        ('C14)', None),
       ]
    }

ENUMERATIONS['alkalinity_model_types'] = {
    'description': 'Types of alkalinity modelling in ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('Prognostic', None),
        ('Diagnostic)', None),
       ]
    }
