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
DESCRIPTION = 'Land surface lakes'

# --------------------------------------------------------------------
# LAKES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Land surface lakes top level properties',
    'properties' : [
        ('coupling_with_rivers', 'bool', '1.1',
             'Are lakes coupled to the river routing model component?'),
        ('time_step', 'int', '1.1',
             'Time step of lake scheme in seconds'),
        ('quantities_exchanged_with_rivers', 'ENUM:quantities_exchanged_with_rivers_types', '0.N',
             'If coupling with rivers, which quantities are exchanged between the lakes and rivers'),
        ('vertical_grid', 'str', '0.1',
             'Describe the vertical grid of lakes'),
        ('prognostic_variables', 'cs-str', '1.1',
             'List the prognostic variables of the lake scheme'),
    ]
}

# --------------------------------------------------------------------
# LAKES: process
# --------------------------------------------------------------------
DETAILS['method'] = {
    'description': 'Lakes treatment',
    'properties' : [
        ('ice_treatment', 'bool', '1.1',
             'Is lake ice included?'),
        ('albedo', 'ENUM:lake_albedo_types', '1.1',
             'Describe the treatment of lake albedo'),
        ('dynamics', 'ENUM:lake_dynamics_types', '1.N',
             'Which dynamics of lakes are treated? horizontal, vertical, etc.'),
        ('dynamic_lake_extent', 'bool', '1.1',
             'Is a dynamic lake extent scheme included?'),
        ('endorheic_basins', 'bool', '1.1',
             'Basins not flowing to ocean included?'),
    ]
}

# --------------------------------------------------------------------
# LAKES: Wetlands
# --------------------------------------------------------------------
DETAILS['wetlands'] = {
    'description': 'Welands treatment',
    'properties' : [
        ('description', 'l-str', '0.1',
             'Describe the treatment of wetlands, if any'),
    ]
}

# --------------------------------------------------------------------
# LAKES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['quantities_exchanged_with_rivers_types'] = {
    'description': 'Quantities that are exchanged between the lakes and rivers',
    'is_open': True,
    'members': [
        ('heat', None),
        ('water', None),
        ('tracers', None),
    ]
}

ENUMERATIONS['lake_albedo_types'] = {
    'description': 'Describe the treatment of lake albedo',
    'is_open': True,
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}

ENUMERATIONS['lake_dynamics_types'] = {
    'description': 'Which dynamics of lakes are treated?',
    'is_open': True,
    'members': [
        ('No lake dynamics', None),
        ('vertical', None),
        ('horizontal', None),
    ]
}

