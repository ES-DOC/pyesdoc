"""A realm sepecialization.

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
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'CMIP5 version + Olivier Aumont (LOCEAN/IPSL)'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2017-01-31", "Eric Guilyardi",
        "Initialised"),
    ("0.2.0", "2017-03-03", "Eric Guilyardi",
        "Added plancton size as per specific request"),
    ("0.3.0", "2017-03-08", "Eric Guilyardi",
        "Science updates and short table draft with O. Aumont"),
    ]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Ocean Biogeochemistry Realm'

# --------------------------------------------------------------------
# REALM: Canonical name for the domain of this scientific realm
# --------------------------------------------------------------------
REALM = 'ocnbgchem'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
# Not used for this Realm.
GRID = None

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties for the realm which differ from model defaults
# --------------------------------------------------------------------
KEY_PROPERTIES = 'ocnbgchem_key_properties'

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'ocnbgchem_tracers',
    ]

# --------------------------------------------------------------------
# DETAILS: top level realm details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# ENUMERATIONS: top level realm enumerations
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()
