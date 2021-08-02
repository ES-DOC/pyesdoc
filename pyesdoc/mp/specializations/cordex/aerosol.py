"""A sepecialization.

For further information goto http://wordpress.es-doc.org/cordex-model-specializations.

"""
# --------------------------------------------------------------------
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# CONTRIBUTORS: Set to specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = 'Yves Balkanski (LSCE), Michael Schulz (MET Norway)'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, who, comment).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
	("0.1.0", "2021-06-01", "David Hassell (NCAS)",
         "Initialised from CMIP6"),
    ]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this specialization
# --------------------------------------------------------------------
DESCRIPTION = 'Atmospheric aerosols'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties (differing from defaults (grid, timestep etc))
# --------------------------------------------------------------------
KEY_PROPERTIES = 'aerosol_key_properties'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'aerosol_grid'

# --------------------------------------------------------------------
# PROCESSES: Simulated processes
# --------------------------------------------------------------------
PROCESSES = [
    'aerosol_transport',
    'aerosol_emissions',
    'aerosol_concentrations',
    'aerosol_optical_radiative_properties',
    'aerosol_model',
    ]
