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
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Land surface nitrogen cycle'

# --------------------------------------------------------------------
# NITROGEN CYCLE: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Properties of land surface nitrogen cycle',
    'properties': [
        ('tiling', 'str', '0.1',
             'Describe the notrogen cycle tiling, if any.'),
        ('time_step', 'int', '1.1',
             'Time step of nitrogen cycle in seconds'),
        ('prognostic_variables', 'str', '1.1',
             'List the prognostic variables of the nitrogen scheme'),

    ]
}

# --------------------------------------------------------------------
# NITROGEN CYCLE: process
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# NITROGEN CYCLE: process
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# NITROGEN CYCLE: process
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# NITROGEN CYCLE: process
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# NITROGEN CYCLE: ENUMERATIONS
# --------------------------------------------------------------------
