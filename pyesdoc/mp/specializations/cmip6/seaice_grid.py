"""A realm grid sepecialization.

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
DESCRIPTION = 'Sea Ice grid'

# --------------------------------------------------------------------
# DISCRETISATION: Description of the horizontal discretization and numerics.
# --------------------------------------------------------------------
DETAILS['discretisation'] = {
    'description': 'Sea ice discretisation'
    }

DETAILS['discretisation:horizontal'] = {
    'description': 'Sea ice discretisation in the horizontal',
    'properties': [
        ('grid', 'ENUM:horizontal_grid', '1.1',
            "On which grid is the sea ice horizontal discretisation?"),
        ('grid_type', 'ENUM:grid_structure', '1.1',
            "What is the structure type of the sea ice grid?"),
        ('scheme', 'ENUM:numerical_scheme', '1.1',
            "What is the horizontal discretization (advection) scheme?"),
        ('thermodynamics_time_step', 'int', '1.1',
            "What is the time step in the sea ice model thermodynamic component in seconds."),
        ('dynamics_time_step', 'int', '1.1',
            "What is the time step in the sea ice model dynamic component in seconds."),
        ('additional_details', 'l-str', '0.1',
            "Specify any additional horizontal discretisation details.")
        ]
    }

DETAILS['discretisation:vertical'] = {
    'description': 'Sea ice vertical properties',
    'properties': [
        ('layering', 'ENUM:vertical_layering', '1.N',
            "What type of sea ice vertical layers are implemented for purposes of thermodynamic calculations?"),
        ('number_of_layers', 'int', '1.1',
            "If using multi-layers specify how many."),
        ('additional_details', 'l-str', '0.1',
            "Specify any additional vertical grid details.")
        ]
    }



# --------------------------------------------------------------------
# SEAICE-CATEGROIES: Description of sea ice categories.
# --------------------------------------------------------------------
DETAILS['seaice_categories'] = {
    'description': 'What method is used to represent sea ice categories?',
    'properties': [
        ('has_mulitple_categories', 'bool', '1.1',
            "Set to true if the sea ice model has multiple sea ice categories."),
        ('number_of_categories', 'int', '1.1',
            "If using sea ice categories specify how many."),
        ('category_limits', 'cs-str', '1.1',
            "If using sea ice categories specify each of the category limits."),
        ('ice_thickness_distribution', 'l-str', '1.1',
            "Describe the sea ice thickness distribution."),
        ('other', 'l-str', '0.1',
            """If the sea ice model does not use sea ice categories specify any 
            additional details. For example models that paramterise 
            the ice thickness distribution ITD (i.e there is no explicit ITD) but 
            there is assumed distribution and fluxes are computed accordingly."""),
        ]
    }

# --------------------------------------------------------------------
# Snow on ice grid information
# --------------------------------------------------------------------
DETAILS['snow_on_seaice'] = {
    'description': 'Snow on sea ice details',
    'properties': [
        ('has_snow_on_ice', 'bool', '1.1',
            "Is snow on ice represented in this model?"),
        ('number_of_snow_levels', 'int', '1.1',
            "Number of vertical levels of snow on ice?"),
        ('snow_fraction', 'l-str', '1.1',
            "Describe how the snow fraction on sea ice is determined."),
        ('additional_details', 'l-str', '0.1',
            "Specify any additional details related to snow on ice.")
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['horizontal_grid'] = {
    'description': 'Horizontal discretisation grids',
    'is_open': True,
    'members': [
        ('Ocean grid',
            'Sea ice is horizontally discretised on the ocean grid.'),
        ('Atmosphere Grid',
            'Sea ice is horizontally discretised on the atmospheric grid.'),
        ('Own Grid',
            'Sea ice is horizontally discretised on its own independent grid.'),
        ]
    }

ENUMERATIONS['vertical_layering'] = {
    'description': 'Sea ice layering types',
    'is_open': True,
    'members': [
        ('Zero-layer',
            'Simulation has no internal ice thermodynamics.'),
        ('Two-layers',
            'Simulation uses two layers (i.e. one ice and one snow layer).'),
        ('Multi-layers',
            'Simulation uses more than two layers.'),
       ]
    }

ENUMERATIONS['numerical_scheme'] = {
    'description': 'Numerical advection schemes',
    'is_open': True,
    'members': [
        ('Finite differences', None),
        ('Finite elements', None),
        ('Finite volumes',  None),
       ]
    }

ENUMERATIONS['grid_structure'] = {
    'description': 'Grid structure types',
    'is_open': True,
    'members': [
        ('Structured grid', None),
        ('Unstructured grid', None),
        ('Adaptive grid', 'Computational grid changes during the run'),
    ]
    }
