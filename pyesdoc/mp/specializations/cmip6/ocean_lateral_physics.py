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
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Ocean lateral physics'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level lateral physics properties',
    'properties': [
        ('scheme', 'ENUM:latphys_transient_eddy_types', '1.1',
            'Type of transient eddy representation in ocean'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Momentum.
# --------------------------------------------------------------------
DETAILS['momentum'] = {
    'description': 'Properties of lateral physics for momentum in ocean'
    }

DETAILS['momentum:operator'] = {
    'description': 'Properties of lateral physics operator for momentum in ocean',
    'properties': [
        ('direction', 'ENUM:latphys_operator_direc_types', '1.1',
            'Direction of lateral physics momemtum scheme in the ocean'),
        ('order', 'ENUM:latphys_operator_order_types', '1.1',
            'Order of lateral physics momemtum scheme in the ocean'),
        ('discretisation', 'ENUM:latphys_operator_discret_types', '1.1',
            'Discretisation of lateral physics momemtum scheme in the ocean'),
        ]
    }

DETAILS['momentum:eddy_viscosity_coeff'] = {
    'description': 'Properties of eddy viscosity coeff in lateral physics momemtum scheme in the ocean',
    'properties': [
        ('type', 'ENUM:latphys_eddy_coeff_types', '1.1',
            'Lateral physics momemtum eddy viscosity coeff type in the ocean'),
        ('constant_coefficient', 'int', '0.1',
            'If constant, value of eddy viscosity coeff in lateral physics momemtum scheme (in m2/s)'),
        ('variable_coefficient', 'str', '0.1',
            'If space-varying, describe variations of eddy viscosity coeff in lateral physics momemtum scheme'),
        ('coeff_background', 'str', '1.1',
            'Describe background eddy viscosity coeff in lateral physics momemtum scheme (give values in m2/s)'),
        ('coeff_backscatter', 'bool', '1.1',
            'Is there backscatter in eddy viscosity coeff in lateral physics momemtum scheme ?')
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Tracers.
# --------------------------------------------------------------------
DETAILS['tracers'] = {
    'description': 'Properties of lateral physics for tracers in ocean',
    'properties': [
        ('mesoscale_closure', 'bool', '1.1',
            'Is there a mesoscale closure in the lateral physics tracers scheme ?'),
        ('submesoscale_mixing', 'bool', '1.1',
            'Is there a submesoscale mixing parameterisation (i.e Fox-Kemper) in the lateral physics tracers scheme ?')
        ]
    }

DETAILS['tracers:operator'] = {
    'description': 'Properties of lateral physics operator for tracers in ocean',
    'properties': [
        ('direction', 'ENUM:latphys_operator_direc_types', '1.1',
            'Direction of lateral physics tracers scheme in the ocean'),
        ('order', 'ENUM:latphys_operator_order_types', '1.1',
            'Order of lateral physics tracers scheme in the ocean'),
        ('discretisation', 'ENUM:latphys_operator_discret_types', '1.1',
            'Discretisation of lateral physics tracers scheme in the ocean'),
        ]
    }

DETAILS['tracers:eddy_diffusity_coeff'] = {
    'description': 'Properties of eddy diffusity coeff in lateral physics tracers scheme in the ocean',
    'properties': [
        ('type', 'ENUM:latphys_eddy_coeff_types', '1.1',
            'Lateral physics tracers eddy diffusity coeff type in the ocean'),
        ('constant_coefficient', 'int', '0.1',
            'If constant, value of eddy diffusity coeff in lateral physics tracers scheme (in m2/s)'),
        ('variable_coefficient', 'str', '0.1',
            'If space-varying, describe variations of eddy diffusity coeff in lateral physics tracers scheme'),
        ('coeff_background', 'int', '1.1',
            'Describe background eddy diffusity coeff in lateral physics tracers scheme (give values in m2/s)'),
        ('coeff_backscatter', 'bool', '1.1',
            'Is there backscatter in eddy diffusity coeff in lateral physics tracers scheme ?')
        ]
}

DETAILS['tracers:eddy_induced_velocity'] = {
    'description': 'Properties of eddy induced velocity (EIV) in lateral physics tracers scheme in the ocean',
    'properties': [
        ('type', 'ENUM:latphys_eiv_types', '1.1',
            'Type of EIV in lateral physics tracers in the ocean'),
        ('constant_val', 'int', '0.1',
            'If EIV scheme for tracers is constant, specify coefficient value (M2/s)'),
        ('flux_type', 'str', '1.1',
            'Type of EIV flux (advective or skew)'),
        ('added_diffusivity', 'str', '1.1',
            'Type of EIV added diffusivity (constant, flow dependent or none)')
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['latphys_transient_eddy_types'] = {
    'description': 'Type of transient eddy representation in ocean',
    'is_open': False,
    'members': [
        ('None', 'No transient eddies in ocean'),
        ('Eddy active', 'Full resolution of eddies'),
        ('Eddy admitting', 'Some eddy activity permitted by resolution'),
        ]
    }

ENUMERATIONS['latphys_operator_direc_types'] = {
    'description':'Type of lateral physics direction in ocean',
    'is_open': True,
    'members':[
        ('Horizontal', None),
        ('Isopycnal', None),
        ('Isoneutral', None),
        ('Geopotential', None),
        ('Iso-level', None)
        ]
    }

ENUMERATIONS['latphys_operator_order_types'] = {
    'description':'Type of lateral physics order in ocean',
    'is_open': True,
    'members':[
        ('Harmonic', 'Second order'),
        ('Bi-harmonic', 'Fourth order')
        ]
    }

ENUMERATIONS['latphys_operator_discret_types'] = {
    'description':'Type of lateral physics discretisation in ocean',
    'is_open': True,
    'members':[
        ('Second order', 'Second order'),
        ('Higher order', 'Higher order'),
        ('Flux limiter', None)
        ]
    }

ENUMERATIONS['latphys_eddy_coeff_types'] = {
    'description':'Type of lateral physics eddy viscosity coeff in ocean',
    'is_open': True,
    'members':[
        ('Constant', None),
        ('Space varying', None),
        ('Time + space varying (Smagorinsky)', None)
        ]
    }

ENUMERATIONS['latphys_eiv_types'] = {
    'description':'Type of lateral physics eddy induced velocity in ocean',
    'is_open': True,
    'members':[
        ('GM', 'Gent & McWilliams')
        ]
    }
