"""A process specialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotee Pascoe, David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Atmospheric chemistry transport'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level lateral physics properties',
    'properties': [
        ('scheme', 'ENUM:transport_scheme_types', '1.1',
            'Type of atmospheric chemistry transport scheme'),
        ('mass_conservation', 'ENUM:mass_conservation_methods', '1.N',
            'Method used to ensure mass conservation'),
        ('convection', 'ENUM:convection_types', '1.N',
            'Transport by convection'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Turbulence
# --------------------------------------------------------------------
DETAILS['turbulence'] = {
    'description': 'Properties of lateral physics for momentum in ocean',
    'properties': [
        ('dimensions', 'ENUM:turbulence_dimensions', '1.1',
            'Dimension of the turbulence scheme in chemistry transport'),
        ('coupling_with_chemical_reactivity', 'bool', '1.1',
             'Is the chemistry transport scheme turbulence coupled with chemical reactivity?'),
        
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['transport_scheme_types'] = {
    'description': 'Type of atmospheric chemistry transport scheme',
    'is_open': False,
    'members': [
        ('Eulerian', None),
        ('Semi-lagrangian', None),
        ('Eulerian and semi-lagrangian', None),
        ('Lagrangian', None),
        ]
    }

ENUMERATIONS['mass_conservation_methods'] = {
    'description':'Method used to ensure mass conservation',
    'is_open': True,
    'members':[
        ('Mass adjustment', None),
        ('Concentrations positivity', None),
        ('Gradients monotonicity', None),
    ]
}

ENUMERATIONS['convection_types'] = {
    'description':'Transport by convection',
    'is_open': True,
    'members':[
        ('Convective fluxes connected to tracers', None),
        ('Vertical velocities connected to tracers', None),
    ]
}

ENUMERATIONS['turbulence_dimensions'] = {
    'description':'TDimension of the turbulence scheme in chemistry transport',
    'is_open': True,
    'members':[
        ('2D', 'Two-dimensional'),
        ('3D', 'Three-dimensional'),
    ]
}
