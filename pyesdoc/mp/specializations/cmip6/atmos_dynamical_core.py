"""

A realm process specialization.

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
DESCRIPTION = 'Characteristics of the dynamical core'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "General dynamical core properties",
    'properties': [
        ('timestepping_type', 'ENUM:timestepping_type', '1.1',
            'Timestepping framework type'),
        ('prognostic_variables', 'ENUM:prognostic_variables', '1.N',
            'List of the model prognostic variables'),
        ]
    }

# --------------------------------------------------------------------
# Top boundary layer
# --------------------------------------------------------------------
DETAILS['top_boundary'] = {
    'description': 'Type of boundary layer at the top of the model',
    'properties': [
        ('top_boundary_condition', 'ENUM:top_boundary_condition', '1.1',
            'Top boundary condition'),
        ('top_heat', 'str', '1.1',
            'Top boundary heat treatment'),
        ('top_wind', 'str', '1.1',
            'Top boundary wind treatment'),
        ]
    }

# --------------------------------------------------------------------
# Lateral boundary conditions
# --------------------------------------------------------------------
DETAILS['lateral_boundary'] = {
    'description': 'Type of lateral boundary condition (if the model is a regional model)',
    'properties': [
        ('condition', 'ENUM:lateral_boundary', '0.1',
             'Type of lateral boundary condition'),
        ]
    }

# --------------------------------------------------------------------
# Horizontal diffusion
# --------------------------------------------------------------------
DETAILS['diffusion_horizontal'] = {
    'description': 'Horizontal diffusion scheme',
    'properties': [
        ('scheme_name', 'str', '0.1',
             'Horizontal diffusion scheme name'),
        ('scheme_method', 'ENUM:diffusion_horizontal_scheme_method', '1.1',
             'Horizontal diffusion scheme method'),
        ]
    }

# --------------------------------------------------------------------
# Advection
# --------------------------------------------------------------------
DETAILS['advection'] = {
    'description': 'Dynamical core advection'
    }

DETAILS['advection:tracers'] = {
    'description': 'Tracer advection scheme',
    'properties': [
        ('scheme_name', 'ENUM:advection_tracers_scheme_name', '0.1',
            'Tracer advection scheme name'),
        ('scheme_characteristics', 'ENUM:advection_tracers_scheme_characteristics', '1.N',
            'Tracer advection scheme characteristics'),
        ('conserved_quantities', 'ENUM:advection_tracers_conserved_quantities', '1.N',
            'Tracer advection scheme conserved quantities'),
        ('conservation_method', 'ENUM:advection_tracers_conservation_method', '1.1',
            'Tracer advection scheme conservation method'),
        ]
    }

DETAILS['advection:momentum'] = {
    'description': 'Momentum advection scheme',
    'properties': [
        ('scheme_name', 'ENUM:advection_momentum_scheme_name', '0.1',
            'Momentum advection schemes name'),
        ('scheme_characteristics', 'ENUM:advection_momentum_scheme_characteristics', '1.N',
            'Momentum advection scheme characteristics'),
        ('scheme_staggering_type', 'ENUM:advection_momentum_scheme_staggering_type', '1.1',
            'Momentum advection scheme staggering type'),
        ('conserved_quantities', 'ENUM:advection_momentum_conserved_quantities', '1.N',
            'Momentum advection scheme conserved quantities'),
        ('conservation_method', 'ENUM:advection_momentum_conservation_method', '1.1',
            'Momentum advection scheme conservation method'),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['timestepping_type'] = {
    'description': 'Type of time stepping scheme',
    'is_open': True,
    'members': [
        ('Adams-Bashforth', None),
        ('explicit', None),
        ('implicit', None),
        ('semi-implicit', None),
        ('leap frog', None),
        ('multi-step', None),
        ('Runge Kutta fifth order', None),
        ('Runge Kutta second order', None),
        ('Runge Kutta third order', None),
        ]
    }

ENUMERATIONS['top_boundary_condition'] = {
    'description': 'Type of boundary layer at the top of the model',
    'is_open': True,
    'members': [
        ('sponge layer', None),
        ('radiation boundary condition', None),
        ]
    }

ENUMERATIONS['lateral_boundary'] = {
    'description': 'Type of lateral boundary condition (if the model is a regional model)',
    'is_open': True,
    'members': [
        ('sponge layer', None),
        ('radiation boundary condition', None),
        ]
    }

ENUMERATIONS['prognostic_variables'] = {
    'description': 'List of the model prognostic variables',
    'is_open': True,
    'members': [
        ('surface pressure', None),
        ('wind components', None),
        ('divergence/curl', None),
        ('temperature', None),
        ('potential temperature', None),
        ('total water', None),
        ('water vapour', None),
        ('water liquid', None),
        ('water ice', None),
        ('total water moments', None),
        ('clouds', None),
        ('radiation', None),
        ]
    }

# Made this a string attribute: no obvious convention for consistent scheme naming convention
# ENUMERATIONS['diffusion_horizontal_scheme_name'] = {
#    'description': 'Commonly used name for the horizontal diffusion scheme',
#    'is_open': True,
#    'members': []
#    }

ENUMERATIONS['diffusion_horizontal_scheme_method'] = {
    'description': 'Numerical method used by the horizontal diffusion scheme',
    'is_open': True,
    'members': [
        ('iterated Laplacian', None),
        ('bi-harmonic', None)
        ]
    }

ENUMERATIONS['advection_tracers_scheme_name'] = {
    'description': 'Commonly used name for the tracer advection scheme',
    'is_open': True,
    'members': [
            ('Heun', None),
            ('Roe and VanLeer', None),
            ('Roe and Superbee', None),
            ('Prather', None),
            ('UTOPIA', None),
        ]
    }

ENUMERATIONS['advection_tracers_scheme_characteristics'] = {
    'description': 'Characteristics of the numerical scheme used for the advection of tracers',
    'is_open': True,
    'members': [
            ('Eulerian', None),
            ('modified Euler', None),
            ('Lagrangian', None),
            ('semi-Lagrangian', None),
            ('cubic semi-Lagrangian', None),
            ('quintic semi-Lagrangian', None),
            ('mass-conserving', None),
            ('finite volume', None),
            ('flux-corrected', None),
            ('linear', None),
            ('quadratic', None),
            ('quartic', None),
        ]
    }


ENUMERATIONS['advection_tracers_conserved_quantities'] = {
    'description': 'Quantities conserved through the tracers advection scheme',
    'is_open': True,
    'members': [
        ('dry mass', None),
        ('tracer mass', None),
        ]
    }

ENUMERATIONS['advection_tracers_conservation_method'] = {
    'description': 'Method used to ensure conservation in the tracers advection scheme',
    'is_open': True,
    'members': [
        ('conservation fixer', None),
        ('Priestley algorithm', None),
        ]
    }

ENUMERATIONS['advection_momentum_scheme_name'] = {
    'description': 'Commonly used name for the momentum advection scheme',
    'is_open': True,
    'members': [
        ('VanLeer', None),
        ('Janjic', None),
        ('SUPG (Streamline Upwind Petrov-Galerkin)', None),
        ]
    }

ENUMERATIONS['advection_momentum_scheme_characteristics'] = {
    'description': 'Characteristics of the numerical scheme used for the advection of momentum',
    'is_open': True,
    'members': [
        ('2nd order', None),
        ('4th order', None),
        ('cell-centred', None),
        ('staggered grid', None),
        ('semi-staggered grid', None),
        ]
    }

ENUMERATIONS['advection_momentum_scheme_staggering_type'] = {
    'description': 'If scheme characteristics specify staggered grid, describe the type of staggering',
    'is_open': True,
    'members': [
        ('Arakawa B-grid', None),
        ('Arakawa C-grid', None),
        ('Arakawa D-grid', None),
        ('Arakawa E-grid', None),
        ]
    }

ENUMERATIONS['advection_momentum_conserved_quantities'] = {
    'description': 'Quantities conserved through the tracers advection scheme',
    'is_open': True,
    'members': [
        ("Angular momentum", None),
        ("Horizontal momentum", None),
        ("Enstrophy", None),
        ("Mass", None),
        ("Total energy", None),
        ("Vorticity", None),
        ]
    }

# TODO: is this information nescessary?
ENUMERATIONS['advection_momentum_conservation_method'] = {
    'description': 'Method used to ensure conservation in the momentum advection scheme',
    'is_open': True,
    'members': [
            ('conservation fixer', None),
        ]
    }
