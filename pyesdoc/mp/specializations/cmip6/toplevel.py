"""A top level model.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# CONTACT: Set to top-level specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS: Set to top-level specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to top-level specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'Roland Seferian (CNRM), Tim Johns (UKMO)'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-09-01", "Initialised", "Eric Guilyardi"),
    ("0.2.0", "2016-11-08", "Changed syntax to simplify and remove CIM2 dependencies", "Eric Guilyardi et al"),
    ("0.3.0", "2017-01-30", "Added forcings", "David Hassell, Eric Guilyardi"),
    ]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific top-level
# --------------------------------------------------------------------
DESCRIPTION = 'Top level model'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = None

# --------------------------------------------------------------------
# KEY PROPERTIES: File name (without the .py suffix) containing key properties of the top level model.
# --------------------------------------------------------------------
KEY_PROPERTIES = 'toplevel_key_properties'

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the model
# --------------------------------------------------------------------
PROCESSES = [
    'toplevel_radiative_forcings',
    ]

# --------------------------------------------------------------------
# SIMULATES: Realms simulated by the model
# N.B. Official realms names are from https://github.com/WCRP-CMIP/CMIP6_CVs/blob/master/CMIP6_realm.json
# N.B. Creation tool should include an on/off switch to allow for partial configurations (AMIP, AOGCM)
# --------------------------------------------------------------------
# TODO: ## WARNING these names are not coherent with those in ES-DOC realms specialisation repos (atmosphere instead of atmos,...)
SIMULATES = [
    "aerosol",
    "atmos",
    "atmosChem",
    "land",
    "landIce",
    "ocean",
    "ocnBgchem",
    "seaIce",
]
