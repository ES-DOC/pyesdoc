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
AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Key properties of the model'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel:flux_correction'] = {
    'description': 'Flux correction properties of the model',
    'properties':[
        ('details', 'str', '1.1',
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
        ('code_languages','str', '0.N',
            "Code language(s)."),
        ('components_structure','str', '0.1',
            """Describe how model realms are structured into independent software components
               (coupled via a coupler) and internal software components."""),
        ('coupler','ENUM:coupler_framework', '0.1',
            "Overarching coupling framework for model."),
        ]
    }

# --------------------------------------------------------------------
# TUNING APPLIED: Any tuning used to optimise the parameters in this realm
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for model',
    'properties': [
        ('description', 'str', '1.1',
            """General overview description of tuning: explain and motivate the main targets and metrics retained.
            Document the relative weight given to climate performance metrics versus process oriented metrics,
            and on the possible conflicts with parameterization level tuning. In particular describe any struggle
            with a parameter value that required pushing it to its limits to solve a particular model deficiency."""),
        ('global_mean_metrics_used', 'str', '0.N',
            "List set of metrics of the global mean state used in tuning model"),
        ('regional_metrics_used', 'str', '0.N',
            "List of regional metrics of mean state (e.g THC, AABW, regional means etc) used in tuning model/component"),
        ('trend_metrics_used', 'str', '0.N',
            "List observed trend metrics used in tuning model/component (such as 20th century)"),
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
    'description': 'Global convervation properties of the model',
    'detail_sets':[
        'heat',
        'fresh_water',
        'salt',
        'momentum'
        ]
    }

DETAILS['conservation:heat'] = {
    'description':'Global heat convervation properties of the model',
    'properties': [
        ('global', 'str', '1.1',
            'Describe if/how heat is conserved globally'),
        ('atmos_ocean_interface', 'str', '0.1',
            'Describe if/how heat is conserved at the atmosphere/ocean coupling interface'),
        ('atmos_land_interface', 'str', '1.1',
            'Describe if/how heat is conserved at the atmosphere/land coupling interface'),
        ('atmos_sea-ice_interface', 'str', '0.1',
            'Describe if/how heat is conserved at the atmosphere/sea-ice coupling interface'),
        ('ocean_seaice_interface', 'str', '0.1',
            'Describe if/how heat is conserved at the ocean/sea-ice coupling interface'),
        ('land_ocean_interface', 'str', '0.1',
            'Describe if/how heat is conserved at the land/ocean coupling interface'),
        ]
    }

DETAILS['conservation:fresh_water'] = {
    'description':'Global fresh water convervation properties of the model',
    'properties': [
        ('global', 'str', '1.1',
            'Describe if/how fresh_water is conserved globally'),
        ('atmos_ocean_interface', 'str', '0.1',
            'Describe if/how fresh_water is conserved at the atmosphere/ocean coupling interface'),
        ('atmos_land_interface', 'str', '1.1',
            'Describe if/how fresh water is conserved at the atmosphere/land coupling interface'),
        ('atmos_sea-ice_interface', 'str', '0.1',
            'Describe if/how fresh water is conserved at the atmosphere/sea-ice coupling interface'),
        ('ocean_seaice_interface', 'str', '0.1',
            'Describe if/how fresh water is conserved at the ocean/sea-ice coupling interface'),
        ('runoff', 'str', '0.1',
            'Describe how runoff is distributed and conserved'),
        ('iceberg_calving', 'str', '0.1',
            'Describe if/how iceberg calving is modeled and conserved'),
        ('endoreic_basins', 'str', '0.1',
            'Describe if/how endoreic basins (no ocean access) are treated'),
        ('snow_accumulation', 'str', '0.1',
            'Describe how snow accumulation over land and over sea-ice is treated'),
        ]
    }

DETAILS['conservation:salt'] = {
    'description':'Global salt convervation properties of the model',
    'properties': [
        ('ocean_seaice_interface', 'str', '0.1',
            'Describe if/how salt is conserved at the ocean/sea-ice coupling interface'),
        ]
    }

DETAILS['conservation:momentum'] = {
    'description':'Global momentum convervation properties of the model',
    'properties': [
        ('details', 'str', '0.1',
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

