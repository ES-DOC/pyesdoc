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
CONTRIBUTORS = 'CMIP5 version + Olivier Aumont (LOCEAN/IPSL), Laurent Bopp (LSCE/IPSL)'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2017-01-31", "Eric Guilyardi",
        "Initialised"),
    ("0.2.0", "2017-03-03", "Eric Guilyardi",
        "Added plancton size as per specific request"),
    ("0.3.0", "2017-03-08", "Eric Guilyardi",
        "Science updates and short table draft with O. Aumont"),
    ("0.4.0", "2017-11-08", "Eric Guilyardi",
        "Science updates following community review with L. Bopp and O. Aumont"),
    ("0.5.0", "2017-12-12", "Eric Guilyardi",
        "Science updates following community review phase 3"),
    ("1.0.0", "2018-02-21", "Eric Guilyardi",
        "Version for release 1.0"),
    ("1.0.1", "2018-04-04", "David Hassell",
        "Replaced some occurences of 'str' with 'cs-str' and 'l-str'"),
    ("1.0.2", "2018-04-04", "David Hassell",
        "Removed some l-str"),
    ("1.0.3", "2018-09-05", "Eric Guilyardi",
        "Spelling mistake corrected in Tracers"),
    ("1.1.0", "2018-09-27", "David Hassell (NCAS)",
         "Added key_propoerties.tuning_applied"),
    ]

# --------------------------------------------------------------------
# CMIP5_MAPPINGS_SYNCED_AT: Latest version that has been synced with CMIP5 mappings.
# --------------------------------------------------------------------
CMIP5_MAPPINGS_SYNCED_AT = "1.0.0"

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Ocean Biogeochemistry'

# --------------------------------------------------------------------
# REALM: Canonical name for the domain of this scientific realm
# --------------------------------------------------------------------
REALM = 'ocnbgchem'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties for the realm which differ from model defaults
# --------------------------------------------------------------------
KEY_PROPERTIES = 'ocnbgchem_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
# Not used for this Realm.
GRID = None

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'ocnbgchem_tracers',
    ]
