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
DESCRIPTION = 'Properties of ocean advection'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['momemtum_adv_scheme'] = {
    'description': 'Properties of lateral momemtum advection scheme in ocean',
    'details': ['details']
}

SUB_PROCESSES['lat_tra_adv_scheme'] = {
    'description': 'Properties of lateral tracer advection scheme in ocean',
    'details': ['details']
}

SUB_PROCESSES['vert_tra_adv_scheme'] = {
    'description': 'Properties of vertical momemtum advection scheme in ocean',
    'details': ['details']
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES: DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['momemtum_adv_scheme:details'] = {
    'description': 'Properties of lateral momemtum advection scheme in ocean',
    'properties': [
        ('type', 'ENUM:adv_mom_scheme_types', '1.1',
            'Type of lateral momemtum advection scheme in ocean'),
        ('mom_adv_scheme_name', 'str', '1.1',
            'Name of ocean momemtum advection scheme'),
        ('mom_adv_ALE', 'bool', '0.1',
            'Using ALE for vertical advection ? (if vertical coordinates are sigma)'),
        ]
}

SUB_PROCESS_DETAILS['lat_tra_adv_scheme:details'] = {
    'description':'Properties of lateral tracer advection scheme in ocean',
    'properties': [
        ('type', 'ENUM:adv_tra_scheme_types', '1.1',
            'Type of lateral tracer advection scheme in ocean'),
        ('flux_limiter', 'bool', '1.1',
            'Monotonic flux limiter for vertical tracer advection scheme in ocean ?'),
        ]
}

SUB_PROCESS_DETAILS['vert_tra_adv_scheme:details'] = {
    'description': 'Properties of vertical tracer advection scheme in ocean',
    'properties': [
        ('type', 'ENUM:adv_tra_scheme_types', '1.1',
            'Type of vertical tracer advection scheme in ocean'),
        ('flux_limiter', 'bool', '1.1',
            'Monotonic flux limiter for vertical tracer advection scheme in ocean ?'),
        ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['adv_mom_scheme_types'] = {
    'description': 'Type of lateral momemtum advection scheme in ocean',
    'is_open': False,
    'members': [
        ('Flux form', None),
        ('Vector form', None)
        ]
}

ENUMERATIONS['adv_tra_scheme_types'] = {
    'description': 'Type of tracer advection scheme in ocean',
    'is_open': True,
    'members':[
        ('Centred 2nd order', None),
        ('Centred 4th order', None),
        ('Total Variance Dissipation (TVD)', None),
        ('MUSCL', None),
        ('QUICKEST', None),
        ('Piecewise Parabolic method', None),
        ('Sweby', None),
        ('Prather 2nd moment (PSOM)', None)
        ]
}
