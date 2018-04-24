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
        ('order', 'int', '1.1',
            "Order of lateral tracer advection scheme in ocean"),
        ('flux_limiter', 'bool', '1.1',
            "Monotonic flux limiter for lateral tracer advection scheme in ocean ?"),
        ('effective_order', 'float', '1.1',
            "Effective order of limited lateral tracer advection scheme in ocean"),
        ('name', 'str', '1.1',
            "Descriptive text for lateral tracer advection scheme in ocean (e.g. MUSCL, PPM-H5, PRATHER,...)"),
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
        ('name', 'str', '1.1',
            "Descriptive text for vertical tracer advection scheme in ocean (e.g. MUSCL, PPM-H5, PRATHER,...)"),
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
