"""A realm key-properties sepecialization.

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
DESCRIPTION = 'Land surface key properties'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General key properties in land surface',
    'properties': [
        ('model_name', 'str', '1.1',
             'Name of land surface model code (e.g. MOSES2.2)'),
        ('description', 'str', '1.1',
            'General description of the processes modelled (e.g. dymanic vegation, prognostic albedo, etc.)'),
        ('land_atmosphere_flux_exchanges', 'ENUM:land_atmosphere_flux_exchanges_types', '0.N',
            'Fluxes exchanged with the atmopshere.'),
        ('atmospheric_coupling_treatment', 'str', '1.1',
            'Describe the treatment of land surface coupling with the Atmosphere model component, which may be different for different quantities (e.g. dust: semi-implicit, water vapour: explicit)',),
        ('land_cover', 'ENUM:land_cover_types', '1.N',
            'Types of land cover defined in the land surface model'),
        ('land_cover_change', 'str', '0.1',
             'Describe how land cover change is managed (e.g. the use of net or gross transitions)'),
        ('tiling', 'str', '1.1',
             'Describe the general tiling procedure used in the land surface (if any). Include treatment of physiography, land/sea, (dynamic) vegetation coverage and orography/roughness'),
    ]
}

DETAILS['conservation_properties'] = {
    'description': 'TODO',
    'properties' : [
        ('energy', 'str', '0.1',
             'Describe if/how energy is conserved globally and to what level (e.g. within X [units]/year)'),
        ('water', 'str', '0.1',
             'Describe if/how water is conserved globally and to what level (e.g. within X [units]/year)'),
        ('carbon', 'str', '0.1',
             'Describe if/how carbon is conserved globally and to what level (e.g. within X [units]/year)'),
        ]
    }

DETAILS['timestepping_framework'] = {
    'description': 'TODO',
    'properties' : [
        ('timestep_dependent_on_atmosphere', 'bool', '1.1',
            'Is a time step dependent on the frequency of atmosphere coupling?'),
        ('time_step', 'int', '1.1',
            'Overall timestep of land surface model (i.e. time between calls)'),
        ('timestepping_method', 'str', '1.1',
            'General description of time stepping method and associated time step(s)'),
        ]
    }

DETAILS['software_properties'] = {
    'description': 'Software properties of land surface code',
    'properties':[
        ('repository','str', '0.1',
            "Location of code for this component."),
        ('code_version','str', '0.1',
            "Code version identifier."),
        ('code_languages','str', '0.N',
            "Code language(s)."),
    ]
}

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['land_atmosphere_flux_exchanges_types'] = {
    'description': 'TODO',
    'is_open': True,
    'members': [
        ('water', None),
        ('energy', None),        
        ('carbon', None),
        ('nitrogen', None),
        ('phospherous', None),
    ]
}

ENUMERATIONS['atmospheric_coupling_types'] = {
    'description': 'Treatments of land surface coupling with the Atmosphere model component',
    'is_open': True,
    'members': [
        ('implicit', None),
        ('semi-implicit', None),
        ('explicit', None),
        ]
    }

ENUMERATIONS['land_cover_types'] = {
    'description': 'Types of land cover defined in the land surface model',
    'is_open': True,
    'members': [
        ('bare soil', None),
        ('urban', None),
        ('lake', None),
        ('land ice', None),
        ('lake ice', None),
        ('vegetated', None),
        ]
    }

ENUMERATIONS['prognostic_vars_types'] = {
    'description': 'Prognostic variables included in the land surface scheme',
    'is_open': True,
    'members': [
        ('soil temperature', None),
        ('soil heat content', None),
        ('soil moisture', None),
        ('soil ice content', None),
        ('snow mass', None),
        ('snow albedo', None),
        ('snow density', None),
        ('snow water content', None),
        ('snow layer thickness', None),
        ('canopy water content', None),
        ('canopy heat content', None),
        ('canopy snow content', None),
        ('canopy skin temperature', None),
        ('canopy height', None),
        ('surface skin temperature', None),
        ('river water discharge', None),
        ('soil carbon', None),
        ('vegetation carbon', None),
        ('nitrogen', None),
        ]
    }
