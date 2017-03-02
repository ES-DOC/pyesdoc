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
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Ocean advection'

# --------------------------------------------------------------------
# SUB-PROCESS: Momentum.
# --------------------------------------------------------------------
DETAILS['momentum'] = {
    'description': 'Properties of lateral momemtum advection scheme in ocean',
    'properties': [
        ('type', 'ENUM:adv_mom_scheme_types', '1.1',
            'Type of lateral momemtum advection scheme in ocean'),
        ('scheme_name', 'str', '1.1',
            'Name of ocean momemtum advection scheme'),
        ('ALE', 'bool', '0.1',
            'Using ALE for vertical advection ? (if vertical coordinates are sigma)'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Lateral tracers.
# --------------------------------------------------------------------
DETAILS['lateral_tracers'] = {
    'description':'Properties of lateral tracer advection scheme in ocean',
    'properties': [
        ('type', 'ENUM:adv_tra_scheme_types', '1.1',
            "Type of lateral tracer advection scheme in ocean"),
        ('flux_limiter', 'bool', '1.1',
            "Monotonic flux limiter for vertical tracer advection scheme in ocean ?"),
        ('passive_tracers','ENUM:passive_tracers_list','0.N',
            "Passive tracers advected"),
        ('passive_tracers_advection','str','0.1',
            "Is advection of passive tracers different than active ? if so, describe.")
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Vertical tracers.
# --------------------------------------------------------------------
DETAILS['vertical_tracers'] = {
    'description': 'Properties of vertical tracer advection scheme in ocean',
    'properties': [
        ('type', 'ENUM:adv_tra_scheme_types', '1.1',
            "Type of vertical tracer advection scheme in ocean"),
        ('flux_limiter', 'bool', '1.1',
            "Monotonic flux limiter for vertical tracer advection scheme in ocean ?"),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
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
    'members': [
        ('Centred 2nd order', None),
        ('Centred 4th order', None),
        ('Total Variance Dissipation (TVD)', None),
        ('MUSCL', None),
        ('QUICKEST', None),
        ('Piecewise Parabolic method', None),
        ('Sweby', None),
        ('Prather 2nd moment (PSOM)', None),
        ('3rd order upwind', None)
        ]
    }

ENUMERATIONS['passive_tracers_list'] = {
    'description': 'Passive tracers in ocean',
    'is_open': True,
    'members': [
        ('Ideal age', None),
        ('CFC 11', None),
        ('CFC 12', None),
        ('SF6', None)
        ]
    }
