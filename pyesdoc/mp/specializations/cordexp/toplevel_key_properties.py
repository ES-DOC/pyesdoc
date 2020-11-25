"""A model key-properties sepecialization.

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
CONTACT = 'Guillaume Levavasseur (IPSL)'

# --------------------------------------------------------------------
# AUTHORS: Set to top-level specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Guillaume Levavasseur (IPSL), Grigory Nikulin (SMHI)'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Key properties of the regional model'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level properties of the regional model'
    }

DETAILS['toplevel:model_type'] = {
    'description': "Type of Regional Climate Model",
    'properties': [
        ('model_family', 'ENUM:model_family_type', '1.1',
            "Type of Regional Climate Model"),
        ('details', 'l-str', '0.1',
            "Provide additional details on type of the Regional Climate Model"),
        ]
    }  

DETAILS['toplevel:genealogy'] = {
    'description': 'Genealogy and history of the model',
    'properties':[
        ('year_released', 'str', '1.1',
            'Year the model was released'),
        ('previous_name', 'str', '0.1',
            'Previously known as'),
        ('difference_to_previous', 'l-str', '0.1',
            'Briefly summarize the differences between this model and its previous version, if applicable'),
        ]
    }
    
DETAILS['toplevel:cordex_domain'] = {
    'description':'CORDEX domain',
    'properties': [
        ('domain','ENUM:cordex_domain', '0.1',
            "CORDEX domain"),
        ]
    }         
    
DETAILS['toplevel:model_calendar'] = {
    'description': 'Model calendar',
    'properties':[
        ('calendar','ENUM:calendar_used', '0.1',
            "What calender is uded by the model"),
        ]
    }
    
DETAILS['toplevel:spinup'] = {
    'description':'Spin-up',
    'properties': [
        ('details', 'l-str', '0.1',
            'Describe details if any spin-up is used'),
        ]
    }
    
DETAILS['toplevel:nudging'] = {
    'description':'Nudging',
    'properties': [
        ('details', 'l-str', '0.1',
            'Describe details if spectral nudging is used (variables, levels, etc.)'),
        ]
    }           

DETAILS['toplevel:software_properties'] = {
    'description': 'Software properties of the model',
    'properties':[
        ('repository','str', '0.1',
            "Location of code for this component."),
        ('code_version','str', '0.1',
            "Code version identifier."),
        ('code_languages','cs-str', '0.1',
            "Code language(s)."),
        ('components_structure','str', '0.1',
            "Describe how model realms are structured into independent software components (coupled via a coupler) and internal software components."),
        ('coupler','ENUM:coupler_framework', '0.1',
            "Overarching coupling framework for the model."),
        ]
    }
   
DETAILS['toplevel:flux_correction'] = {
    'description': 'Flux correction properties of the model',
    'properties':[
        ('details', 'l-str', '1.1',
            'Describe if/how flux corrections are applied in the model'),
        ]
    }
    
DETAILS['toplevel:reference'] = {
    'description': 'Latest reference',
    'properties':[
        ('details', 'l-str', '1.1',
            'Provide the latest reference describing the model'),
        ]
    }             

# --------------------------------------------------------------------
# REALM COUPLING: general questions
# --------------------------------------------------------------------
DETAILS['coupling'] = {
    'description': '',
    'properties':[
        ('atmosphere_double_flux', 'bool', '1.1',
             'Is the atmosphere passing a double flux to the ocean and sea ice (as opposed to a single one)?'),
        ('atmosphere_fluxes_calculation_grid', 'ENUM:atmosphere_fluxes_calculation_grid', '0.1',
             'Where are the air-sea fluxes calculated'),
        ('atmosphere_relative_winds', 'bool', '1.1',
            'Are relative or absolute winds used to compute the flux? I.e. do ocean surface currents enter the wind stress calculation?'),
    ]
}

# --------------------------------------------------------------------
# TUNING APPLIED: Any tuning used to optimise the parameters in this realm
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for model',
    'properties': [
        ('description', 'l-str', '1.1',
            "General overview description of tuning: explain and motivate the main targets and metrics/diagnostics retained. Document the relative weight given to climate performance metrics/diagnostics versus process oriented metrics/diagnostics, and on the possible conflicts with parameterization level tuning. In particular describe any struggle with a parameter value that required pushing it to its limits to solve a particular model deficiency."),
        ('regional_metrics_used', 'cs-str', '0.1',
            "List of regional metrics/diagnostics of mean state (e.g THC, AABW, regional means etc) used in tuning model/component"),
        ('trend_metrics_used', 'cs-str', '0.1',
            "List observed trend metrics/diagnostics used in tuning model/component (such as 20th century)"),
        ('energy_balance','str', '1.1',
            "Describe how energy balance was obtained in the full system: in the various components independently or at the components coupling stage?"),
        ('fresh_water_balance','str', '1.1',
            "Describe how fresh_water balance was obtained in the full system: in the various components independently or at the components coupling stage?")
        ]
    }

# --------------------------------------------------------------------
# GCM FORCING: GCM forcing used to drive RCM
# --------------------------------------------------------------------
DETAILS['gcm_forcing'] = {
    'description': 'GCM forcing'
}

DETAILS['gcm_forcing:atmos_lbc_eval'] = {
    'description': 'Atmospheric Lateral Boundary Conditions for the evaluation experiment',
    'properties': [
        ('atmos_lbc_eval_variables', 'l-str', '0.1',
            'What atmospheric variables are used to drive the regional model'),
        ('atmos_lbc_eval_frequency', 'l-str', '0.1',
            'At what frequency'),
        ('atmos_lbc_eval_top', 'l-str', '0.1',
            'Top boundary conditions'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of the Atmospheric Lateral Boundary Conditions for the evaluation experiment (e.g. citations, use of non-standard datasets, etc.).'),
    ]
}

DETAILS['gcm_forcing:atmos_lbc_scn'] = {
    'description': 'Atmospheric Lateral Boundary Conditions for the historical and scenario experiments',
    'properties': [
        ('atmos_lbc_scn_variables', 'l-str', '0.1',
            'What atmospheric variables are used to drive the regional model'),
        ('atmos_lbc_scn_frequency', 'l-str', '0.1',
            'At what frequency'),
        ('atmos_lbc_scn_top', 'l-str', '0.1',
            'Top boundary conditions'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of the Atmospheric Lateral Boundary Conditions for the historical and scenario experiments (e.g. citations, use of non-standard datasets, etc.).'),
    ]
}

DETAILS['gcm_forcing:ocean_lbc_eval'] = {
    'description': 'Lower Boundary Conditions for the evaluation experiment',
    'properties': [
        ('sst_lbc_eval_variable', 'l-str', '0.1',
            'What sea surface temperature is used to drive the regional model (driving reanalysis or observations)'),
        ('sst_lbc_eval_frequency', 'l-str', '0.1',
            'At what frequency'),
        ('sic_lbc_eval_variable', 'l-str', '0.1',
            'What sea-ice concentration is used to drive the regional model (driving reanalysis or observations)'),
        ('sic_lbc_eval_frequency', 'l-str', '0.1',
            'At what frequency'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of the Lower Boundary Conditions for the evaluation experiment (e.g. citations, use of non-standard datasets, etc.)'),
    ]
}

DETAILS['gcm_forcing:ocean_lbc_scn'] = {
    'description': 'Lower Boundary Conditions for the historical and scenario experiment',
    'properties': [
        ('sst_lbc_scn_frequency', 'l-str', '0.1',
            'At what frequency is sea surface temperature taken'),
        ('sic_lbc_scn_frequency', 'l-str', '0.1',
            'At what frequency is sea-ice concentration taken'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of the Lower Lateral Boundary Conditions for the historical and scenario experiments (e.g. citations, use of non-standard datasets, etc.).'),
    ]
}

DETAILS['gcm_forcing:aerosol_eval'] = {
    'description': 'Aerosol datasets and parameters used for the evaluation experiment',
    'properties': [
        ('aerosol_eval_dataset', 'l-str', '0.1',
            'What aerosol datasets and parameters are used to drive the regional model (driving reanalysis or observations)'),
        ('aerosol_eval_frequency', 'l-str', '0.1',
            'At what frequency (climatology, transient, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of aerosol for the evaluation experiment'),
    ]
}

DETAILS['gcm_forcing:aerosol_scn'] = {
    'description': 'Aerosol datasets and parameters are used for the historical and scenario experiments',
    'properties': [
        ('aerosol_scn_dataset', 'l-str', '0.1',
            'What aerosol datasets and parameters are used to drive the regional model'),
        ('aerosol_scn_frequency', 'l-str', '0.1',
            'At what frequency (climatology, transient, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of aerosol for the historical and scenario experiment'),
    ]
}

DETAILS['gcm_forcing:ozone_eval'] = {
    'description': 'Ozone datasets used for the evaluation experiment',
    'properties': [
        ('ozone_eval_dataset', 'l-str', '0.1',
            'What ozone dataset is used to drive the regional model (driving reanalysis or observations)'),
        ('ozone_eval_frequency', 'l-str', '0.1',
            'At what frequency (climatology, transient, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of ozone for the evaluation experiment'),
    ]
}

DETAILS['gcm_forcing:ozone_scn'] = {
    'description': 'Ozone datasets used for the historical and scenario experiments',
    'properties': [
        ('ozone_scn_dataset', 'l-str', '0.1',
            'What ozone dataset is used to drive the regional model'),
        ('ozone_scn_frequency', 'l-str', '0.1',
            'At what frequency (climatology, transient, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of ozone for the historical and scenario experiments'),
    ]
}

DETAILS['gcm_forcing:land_cover_eval'] = {
    'description': 'Land cover datasets used for the evaluation experiment',
    'properties': [
        ('land_cover_eval_dataset', 'l-str', '0.1',
            'What land cover dataset is used in the regional model'),
        ('land_cover_eval_frequency', 'l-str', '0.1',
            'At what frequency (climatology, transient, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of land cover for the evaluation experiment'),
    ]
}

DETAILS['gcm_forcing:land_cover_scn'] = {
    'description': 'Land cover datasets used for the historical and scenario experiments',
    'properties': [
        ('land_cover_scn_dataset', 'l-str', '0.1',
            'What land cover dataset is used in the regional model'),
        ('land_cover_scn_frequency', 'l-str', '0.1',
            'At what frequency (climatology, transient, etc.)'),
        ('additional_information', 'l-str', '0.1',
            'Additional information relating to the implementation of land cover for tthe historical and scenario experiments'),
    ]
}

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['model_family_type'] = {
    'description': 'Type of regional model',
    'is_open': True,
    'members': [
        ('Regional Atmospheric Climate Model', None),
        ('Regional Ocean Atmosphere Coupled Climate Model', None),
        ('Other', None),
        ]
    }
    
ENUMERATIONS['cordex_domain'] = {
    'description': 'Select the CORDEX domain',
    'is_open': True,
    'members': [
        ("EUR-11", None),
    ]
}

ENUMERATIONS['calendar_used'] = {
    'description': 'What calendar is used by the model',
    'is_open': True,
    'members': [
        ("GCM-based", None),
        ("Standard", None),
        
    ]
}    

ENUMERATIONS['coupler_framework'] = {
    'description': 'Coupling software framework.',
    'is_open': True,
    'members': [
        ("OASIS", "The OASIS coupler - prior to OASIS-MCT"),
        ("OASIS3-MCT", "The MCT variant of the OASIS coupler"),
        ("ESMF", "Vanilla Earth System Modelling Framework"),
        ("NUOPC", "National Unified Operational Prediction Capability variant of ESMF"),
        ("Bespoke", "Customised coupler developed for this model"),
        ("Unknown", "It is not known what/if-a coupler is used"),
        ("None", "No coupler is used")
        ]
    }

ENUMERATIONS['atmosphere_fluxes_calculation_grid'] = {
    'description': 'Where are the air-sea fluxes calculated',
    'is_open': True,
    'members': [
        ("Atmosphere grid", None),
        ("Ocean grid", None),
        ("Specific coupler grid", None),
    ]
}
