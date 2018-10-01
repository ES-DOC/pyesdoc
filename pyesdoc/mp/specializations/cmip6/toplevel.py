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
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-09-01", "Eric Guilyardi",
        "Initialised"),
    ("0.2.0", "2016-11-08", "Eric Guilyardi et al",
        "Changed syntax to simplify and remove CIM2 dependencies"),
    ("0.3.0", "2017-01-30", "David Hassell, Eric Guilyardi",
        "Added forcings"),
    ("0.4.0", "2017-05-02", "David Hassell",
        "Updated solar forcing"),
    ("0.5.0", "2017-11-22", "David Hassell",
        "Updates from community review: Alistair Sellar (MOHC), Oyvind Seland (MET-Norway)"),
    ("0.6.0", "2018-04-04", "David Hassell",
        "Replaced some occurences of 'str' with 'cs-str' and 'l-str'"),
    ("1.0.2", "2018-04-04", "David Hassell",
        "Removed some l-str"),
    ("1.1.0", "2018-09-19", "David Hassell",
        "Added CMIP5_differences"),
    ("1.1.1", "2018-09-20", "David Hassell",
        "removed duplicate 'overview'"),
    ]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific top-level
# --------------------------------------------------------------------
DESCRIPTION = 'Model top level'

# --------------------------------------------------------------------
# KEY PROPERTIES: File name (without the .py suffix) containing key properties of the top level model.
# --------------------------------------------------------------------
KEY_PROPERTIES = 'toplevel_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = None

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
