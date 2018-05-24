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
DESCRIPTION = 'Land surface nitrogen cycle'

# --------------------------------------------------------------------
# NITROGEN CYCLE: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Land surface nitrogen cycle top level properties',
    'properties': [
        ('tiling', 'l-str', '0.1',
             'Describe the notrogen cycle tiling, if any.'),
        ('time_step', 'int', '1.1',
             'Time step of nitrogen cycle in seconds'),
        ('prognostic_variables', 'cs-str', '1.1',
             'List the prognostic variables of the nitrogen scheme'),

    ]
}

# --------------------------------------------------------------------
# NITROGEN CYCLE: ENUMERATIONS
# --------------------------------------------------------------------
