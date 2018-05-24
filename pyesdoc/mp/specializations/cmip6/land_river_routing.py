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
DESCRIPTION = 'Land surface river routing'

# --------------------------------------------------------------------
# RIVER ROUTNG: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Land surface river routing top level properties',
    'properties' : [
        ('tiling', 'l-str', '0.1',
             'Describe the river routing, if any.'),
        ('time_step', 'int', '1.1',
             'Time step of river routing scheme in seconds'),        
        ('grid_inherited_from_land_surface', 'bool', '1.1',
             'Is the grid inherited from land surface?'),
        ('grid_description', 'str', '0.1',
             'General description of grid, if not inherited from land surface'),
        ('number_of_reservoirs', 'int', '1.1',
             'Enter the number of reservoirs'),
        ('water_re_evaporation', 'ENUM:water_re_evaporation_types', '1.N',
             'TODO'),
        ('coupled_to_atmosphere', 'bool', '0.1',
             'Is river routing coupled to the atmosphere model component?'),
        ('coupled_to_land', 'l-str', '0.1',
             'Describe the coupling between land and rivers'),
        ('quantities_exchanged_with_atmosphere', 'ENUM:quantities_exchanged_with_atmosphere_types', '0.N',
             'If couple to atmosphere, which quantities are exchanged between river routing and the atmosphere model components?'),
        ('basin_flow_direction_map', 'ENUM:basin_flow_direction_map_types', '1.1',
             'What type of basin flow direction map is being used?'),
        ('flooding', 'l-str', '0.1',
             'Describe the representation of flooding, if any'),
        ('prognostic_variables', 'cs-str', '1.1',
             'List the prognostic variables of the river routing'),
    ],
}

# --------------------------------------------------------------------
# RIVER ROUTING: process
# --------------------------------------------------------------------
DETAILS['oceanic_discharge'] = {
    'description': 'Oceanic discharge treatment in river routing',
    'properties' : [
        ('discharge_type', 'ENUM:discharge_types', '1.1',
             'Specify how rivers are discharged to the ocean'),
        ('quantities_transported', 'ENUM:quantities_transported_types', '1.N',
             'Quantities that are exchanged from river-routing to the ocean model component'),
    ]
}

# --------------------------------------------------------------------
# RIVER ROUTING: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['prognostic_variable_types'] = {
    'description': 'Specify the prognostic variables within the river routing scheme',
    'is_open': True,
    'members': [
        ('heat', None),
        ('water', None),
        ('tracers', None),
        ]
    }

ENUMERATIONS['water_re_evaporation_types'] = {
    'description': 'TODO',
    'is_open': True,
    'members': [
        ('flood plains', None),
        ('irrigation', None),
    ]
}

ENUMERATIONS['quantities_exchanged_with_atmosphere_types'] = {
    'description': 'Quantities that are exchanged between river routing and the atmosphere model components',
    'is_open': True,
    'members': [
        ('heat', None),
        ('water', None),
        ('tracers', None),
    ]
}

ENUMERATIONS['basin_flow_direction_map_types'] = {
    'description': 'What type of basin flow direction map is being used?',
    'is_open': True,
    'members': [
        ('present day', None),
        ('adapted for other periods', None),
    ]
}

ENUMERATIONS['discharge_types'] = {
    'description': 'Specify how rivers are discharged to the ocean',
    'is_open': True,
    'members': [
        ('direct (large rivers)', None),
        ('diffuse', None),
    ]
}

ENUMERATIONS['quantities_transported_types'] = {
    'description': 'Quantities that are exchanged from river-routing to the ocean model component',
    'is_open': True,
    'members': [
        ('heat', None),
        ('water', None),
        ('tracers', None),
    ]
}
