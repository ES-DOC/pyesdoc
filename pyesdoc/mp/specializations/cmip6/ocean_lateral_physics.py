"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
#
# Scientific context of the process
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of ocean lateral physics'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['ocean_transient_eddy_representation'] = {
    'description': 'Type of transient eddy representation in ocean',
    'properties': [
        ('scheme', 'ENUM:latphys_transient_eddy_types', '1.1',
            'Type of transient eddy representation in ocean'),
        ]
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['momentum'] = {
    'description': 'Properties of lateral physics for momentum in ocean',
    'details': [
        'operator',
        'eddy_viscosity_coeff'
        ]
 }

SUB_PROCESSES['tracers'] = {
    'description': 'Properties of lateral physics for tracers in ocean',
    'details': [
        'details',
        'operator',
        'eddy_viscosity_coeff',
        'eddy_induced_velocity'
        ]
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES: DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['momentum:operator'] = {
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

SUB_PROCESS_DETAILS['momentum:eddy_viscosity_coeff'] = {
    'description': 'Properties of eddy viscosity coeff in lateral physics momemtum scheme in the ocean',
    'properties': [
        ('type', 'ENUM:latphys_eddy_visc_coeff_types', '1.1',
            'Lateral physics momemtum eddy viscosity coeff type in the ocean'),
        ('eddy_visc_coeff_cst', 'int', '0.1',
            'If constant, value of eddy viscosity coeff in lateral physics momemtum scheme (in m2/s)'),
        ('eddy_visc_coeff_var', 'str', '0.1',
            'If space-varying, describe variations of eddy viscosity coeff in lateral physics momemtum scheme'),
        ('eddy_visc_coeff_background', 'int', '1.1',
            'Background value of eddy viscosity coeff in lateral physics momemtum scheme (in m2/s)'),
        ('eddy_visc_coeff_backscatter', 'bool', '1.1',
            'Is there backscatter in eddy viscosity coeff in lateral physics momemtum scheme ?')
        ]
}

SUB_PROCESS_DETAILS['tracers:details'] = {
    'description': 'Properties of lateral physics for tracers in ocean',
    'properties': [
        ('mesoscale_closure', 'bool', '1.1',
            'Is there a mesoscale closure in the lateral physics tracers scheme ?')
        ]
}

SUB_PROCESS_DETAILS['tracers:operator'] = {
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

SUB_PROCESS_DETAILS['tracers:eddy_viscosity_coeff'] = {
    'description': 'Properties of eddy viscosity coeff in lateral physics tracers scheme in the ocean',
    'properties': [
        ('type', 'ENUM:latphys_eddy_visc_coeff_types', '1.1',
            'Lateral physics tracers eddy viscosity coeff type in the ocean'),
        ('eddy_visc_coeff_cst', 'int', '0.1',
            'If constant, value of eddy viscosity coeff in lateral physics tracers scheme (in m2/s)'),
        ('eddy_visc_coeff_var', 'str', '0.1',
            'If space-varying, describe variations of eddy viscosity coeff in lateral physics tracers scheme'),
        ('eddy_visc_coeff_background', 'int', '1.1',
            'Background value of eddy viscosity coeff in lateral physics tracers scheme (in m2/s)'),
        ('eddy_visc_coeff_backscatter', 'bool', '1.1',
            'Is there backscatter in eddy viscosity coeff in lateral physics tracers scheme ?')
        ]
}

SUB_PROCESS_DETAILS['tracers:eddy_induced_velocity'] = {
    'description': 'Properties of eddy induced velocity (EIV) in lateral physics tracers scheme in the ocean',
    'properties': [
        ('type', 'ENUM:latphys_eiv_types', '1.1',
            'Type of EIV in lateral physics tracers in the ocean'),
        ('eiv_constant_val', 'int', '0.1',
            'If EIV scheme for tracers is constant, specify coefficient value (M2/s)'),
        ('eiv_flux_type', 'str', '1.1',
            'Type of EIV flux (advective or skew)'),
        ('eiv_added_diff', 'str', '1.1',
            'Type of EIV added diffusivity (constant, flow dependent or none)')
        ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

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
        ('Fourth order', 'Fourth order'),
        ('Flux limiter', None)
        ]
}

ENUMERATIONS['latphys_eddy_visc_coeff_types'] = {
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
