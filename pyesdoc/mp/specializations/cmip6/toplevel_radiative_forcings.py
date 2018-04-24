"""A model radiative forcings sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to top-level specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to top-level specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell, Eric Guilyardi'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Radiative forcings of the model for historical and scenario (aka Table 12.1 IPCC AR5)'

# --------------------------------------------------------------------
# GREENHOUSE GASES
# --------------------------------------------------------------------
DETAILS['greenhouse_gases'] = {
    'description': 'Greenhouse gas forcing agents'
}

DETAILS['greenhouse_gases:CO2'] = {
    'description': 'Carbon dioxide forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['greenhouse_gases:CH4'] = {
    'description': 'Methane forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['greenhouse_gases:N2O'] = {
    'description': 'Nitrous oxide forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['greenhouse_gases:tropospheric_O3'] = {
    'description': 'Troposheric ozone forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['greenhouse_gases:stratospheric_O3'] = {
    'description': 'Stratospheric ozone forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['greenhouse_gases:CFC'] = {
    'description': 'Ozone-depleting and non-ozone-depleting fluorinated gases forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('equivalence_concentration','ENUM:cfc_equivalence_concentration', '1.1',
            'Details of any equivalence concentrations used'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

# --------------------------------------------------------------------
# AEROSOLS
# --------------------------------------------------------------------
DETAILS['aerosols'] = {
    'description': 'Aerosol forcing agents'
}

DETAILS['aerosols:SO4'] = {
    'description': 'SO4 aerosol forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['aerosols:black_carbon'] = {
    'description': 'Black carbon aerosol forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['aerosols:organic_carbon'] = {
    'description': 'Organic carbon aerosol forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['aerosols:nitrate'] = {
    'description': 'Nitrate forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['aerosols:cloud_albedo_effect'] = {
    'description': 'Cloud albedo effect forcing (RFaci)',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('aerosol_effect_on_ice_clouds', 'bool', '1.1',
             'Radiative effects of aerosols on ice clouds are represented?'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).')
    ]
}

DETAILS['aerosols:cloud_lifetime_effect'] = {
    'description': 'Cloud lifetime effect forcing (ERFaci)',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('aerosol_effect_on_ice_clouds', 'bool', '1.1',
             'Radiative effects of aerosols on ice clouds are represented?'),
        ('RFaci_from_sulfate_only', 'bool', '1.1',
             'Radiative forcing from aerosol cloud interactions from sulfate aerosol only?'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['aerosols:dust'] = {
    'description': 'Dust forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['aerosols:tropospheric_volcanic'] = {
    'description': 'Tropospheric volcanic forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('historical_explosive_volcanic_aerosol_implementation','ENUM:explosive_volcanic_aerosol_implementation', '1.1',
            'How explosive volcanic aerosol is implemented in historical simulations'),
        ('future_explosive_volcanic_aerosol_implementation','ENUM:explosive_volcanic_aerosol_implementation', '1.1',
            'How explosive volcanic aerosol is implemented in future simulations'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['aerosols:stratospheric_volcanic'] = {
    'description': 'Stratospheric volcanic forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('historical_explosive_volcanic_aerosol_implementation','ENUM:explosive_volcanic_aerosol_implementation', '1.1',
            'How explosive volcanic aerosol is implemented in historical simulations'),
        ('future_explosive_volcanic_aerosol_implementation','ENUM:explosive_volcanic_aerosol_implementation', '1.1',
            'How explosive volcanic aerosol is implemented in future simulations'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['aerosols:sea_salt'] = {
    'description': 'Sea salt forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

# --------------------------------------------------------------------
# OTHER
# --------------------------------------------------------------------
DETAILS['other'] = {
    'description': 'Miscellaneous forcing agents'
}

DETAILS['other:land_use'] = {
    'description': 'Land use forcing',
    'properties': [
        ('provision', 'ENUM:forcing_provision', '1.N',
             'How this forcing agent is provided (e.g. via concentrations, emission precursors, prognostically derived, etc.)'),
        ('crop_change_only', 'bool', '1.1',
             'Land use change represented via crop change only?'),
        ('additional_information', 'l-str', '0.1',
             'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

DETAILS['other:solar'] = {
    'description': 'Solar forcing',
    'properties': [
        ('provision', 'ENUM:solar_forcing_provision', '1.N',
             'How solar forcing is provided'),
        ('additional_information', 'l-str', '0.1',
             'Additional information relating to the provision and implementation of this forcing agent (e.g. citations, use of non-standard datasets, explaining how multiple provisions are used, etc.).'),
    ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['forcing_provision'] = {
    'description': 'How a radiative forcing agent is provided',
    'is_open': True,
    'members': [
        ("N/A", "Not applicable - forcing agent is not included"),
        ("M",  "Emissions and concentrations determined by the model state rather than externally prescribed"),
        ("Y",  "Prescribed concentrations, distributions or time series data"),
        ("E",  "Concentrations calculated interactively driven by prescribed emissions or precursor emissions"),
        ("ES", "Surface emissions (and 3-D concentrations away from the surface) derived via the model from the prescribed surface concentration"),
        ("C",  "Fixed prescribed climatology of concentrations with no year-to-year variability"),
    ]
}

ENUMERATIONS['solar_forcing_provision'] = {
    'description': 'How solar forcing is provided',
    'is_open': True,
    'members': [
        ("N/A"       , "Not applicable - solar forcing is not included"),
        ("irradiance", "Solar irradiance forcing"),
        ("proton"    , "Proton pathway to solar forcing"),
        ("electron"  , "Electron pathway to solar forcing"),
        ("cosmic ray", "Cosmic ray pathway to solar forcing"),
    ]
}

ENUMERATIONS['cfc_equivalence_concentration'] = {
    'description': 'Details of any externally provided equivalence concentrations used for CFC gases',
    'description': '',
    'is_open': True,
    'members': [
        ("N/A", "Not applicabale (CFCs not included or emissions and concentrations determined by the model state)"),
        ("Option 1", "CFCs, including CFC-12, are provided as actual concentrations"),
        ("Option 2", "CFC-12 is provided as actual concentrations and any other gases are provided as an equivalence concentration of CFC-11"),
        ("Option 3", "Ozone depleting gases, including CFC-12, are provided as an equivalence concentration of CFC-12 and all other fluorinated gases are provided as an equivalence concentration of HFC-134a"),
    ]
}

ENUMERATIONS['explosive_volcanic_aerosol_implementation'] = {
    'description': 'Model implementation of explosive volcanic aerosols',
    'is_open': True,
    'members': [
        ("Type A", "Explosive volcanic aerosol returns rapidly to zero (or near-zero) background."),
        ("Type B", "Explosive volcanic aerosol returns rapidly to constant (average volcano)"),
        ("Type C", "Explosive volcanic aerosol returns slowly (over several decades) to constant (average volcano) background."),
        ("Type D", "Explosive volcanic aerosol set to zero"),
        ("Type E", "Explosive volcanic aerosol set to constant (average volcano) background")
    ]
}
