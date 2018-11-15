"""A model key-properties sepecialization.

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
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# AUTHORS: Set to top-level specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi, David Hassell'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Key properties of the model'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level properties of full coupled model'
    }

DETAILS['toplevel:flux_correction'] = {
    'description': 'Flux correction properties of the model',
    'properties':[
        ('details', 'l-str', '1.1',
            'Describe if/how flux corrections are applied in the model'),
        ]
    }

DETAILS['toplevel:genealogy'] = {
    'description': 'Genealogy and history of the model',
    'properties':[
        ('year_released', 'str', '1.1',
            'Year the model was released'),
        ('CMIP3_parent', 'str', '0.1',
            'CMIP3 parent if any'),
        ('CMIP5_parent', 'str', '0.1',
            'CMIP5 parent if any'),
        ('CMIP5_differences', 'l-str', '0.1',
            'Briefly summarize the differences between this model and its CMIP5 parent, if applicable'),
        ('previous_name', 'str', '0.1',
            'Previously known as'),
        ]
    }

DETAILS['toplevel:software_properties'] = {
    'description': 'Software properties of model',
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
            "Overarching coupling framework for model."),
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
        ('global_mean_metrics_used', 'cs-str', '0.1',
            "List set of metrics/diagnostics of the global mean state used in tuning model"),
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
# CONSERVATION PROPERTIES: Global conservation properties of the model.
# --------------------------------------------------------------------
DETAILS['conservation'] = {
    'description': 'Global convervation properties of the model'
    }

DETAILS['conservation:heat'] = {
    'description':'Global heat convervation properties of the model',
    'properties': [
        ('global', 'l-str', '1.1',
            'Describe if/how heat is conserved globally'),
        ('atmos_ocean_interface', 'l-str', '0.1',
            'Describe if/how heat is conserved at the atmosphere/ocean coupling interface'),
        ('atmos_land_interface', 'l-str', '1.1',
            'Describe if/how heat is conserved at the atmosphere/land coupling interface'),
        ('atmos_sea-ice_interface', 'l-str', '0.1',
            'Describe if/how heat is conserved at the atmosphere/sea-ice coupling interface'),
        ('ocean_seaice_interface', 'l-str', '0.1',
            'Describe if/how heat is conserved at the ocean/sea-ice coupling interface'),
        ('land_ocean_interface', 'l-str', '0.1',
            'Describe if/how heat is conserved at the land/ocean coupling interface'),
        ]
    }

DETAILS['conservation:fresh_water'] = {
    'description':'Global fresh water convervation properties of the model',
    'properties': [
        ('global', 'l-str', '1.1',
            'Describe if/how fresh_water is conserved globally'),
        ('atmos_ocean_interface', 'l-str', '0.1',
            'Describe if/how fresh_water is conserved at the atmosphere/ocean coupling interface'),
        ('atmos_land_interface', 'l-str', '1.1',
            'Describe if/how fresh water is conserved at the atmosphere/land coupling interface'),
        ('atmos_sea-ice_interface', 'l-str', '0.1',
            'Describe if/how fresh water is conserved at the atmosphere/sea-ice coupling interface'),
        ('ocean_seaice_interface', 'l-str', '0.1',
            'Describe if/how fresh water is conserved at the ocean/sea-ice coupling interface'),
        ('runoff', 'l-str', '0.1',
            'Describe how runoff is distributed and conserved'),
        ('iceberg_calving', 'l-str', '0.1',
            'Describe if/how iceberg calving is modeled and conserved'),
        ('endoreic_basins', 'l-str', '0.1',
            'Describe if/how endoreic basins (no ocean access) are treated'),
        ('snow_accumulation', 'l-str', '0.1',
            'Describe how snow accumulation over land and over sea-ice is treated'),
        ]
    }

DETAILS['conservation:salt'] = {
    'description':'Global salt convervation properties of the model',
    'properties': [
        ('ocean_seaice_interface', 'l-str', '0.1',
            'Describe if/how salt is conserved at the ocean/sea-ice coupling interface'),
        ]
    }

DETAILS['conservation:momentum'] = {
    'description':'Global momentum convervation properties of the model',
    'properties': [
        ('details', 'l-str', '0.1',
            'Describe if/how momentum is conserved in the model'),
        ]
    }

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
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
           
