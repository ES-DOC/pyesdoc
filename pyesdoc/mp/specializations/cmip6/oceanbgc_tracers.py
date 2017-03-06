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
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

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
            'Definition of upper trophic level (e.g. based on size) ?'),
        ('upper_trophic_levels_treatment', 'str', '1.1',
            'Define how upper trophic level are treated'),
        ]
    }

DETAILS['ecosystem:phytoplancton'] = {
    'description': 'Phytoplancton properties in ocean biogeochemistry',
    'properties': [
        ('type', 'ENUM:plancton_types', '1.1',
            'Type of phytoplancton'),
        ('list', 'ENUM:phytoplancton_list', '0.N',
            'List species of phytoplancton if applicable'),
        ('size_range','str','0.1',
            'Size range of phytoplancton (if applicable)')
        ]
    }

DETAILS['ecosystem:zooplancton'] = {
    'description': 'Zooplancton properties in ocean biogeochemistry',
    'properties': [
        ('type', 'ENUM:plancton_types', '1.1',
            'Type of zooplancton'),
        ('list', 'ENUM:zooplancton_list', '0.N',
            'List species of zooplancton if applicable'),
        ('size_range','str','0.1',
            'Size range of zooplancton (if applicable)')
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
        ('method', 'ENUM:particules_method', '1.1',
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
        ('Silicium (S)', None),
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

ENUMERATIONS['plancton_types'] = {
    'description': 'Plancton types in ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('None', None),
        ('Generic', None),
        ('List (specify below)', None),       ]
    }


ENUMERATIONS['phytoplancton_list'] = {
    'description': 'Phytoplancton list in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Diatoms', None),
        ('Nfixers', None),
        ('Calcifiers', None),
        ('Picophytoplancton', None),
       ]
    }

ENUMERATIONS['zooplancton_list'] = {
    'description': 'Zooplancton list in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Microzooplancton', None),
        ('Mesozooplancton', None),
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
