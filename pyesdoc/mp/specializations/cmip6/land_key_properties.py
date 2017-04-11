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
        ('basic_approximations', 'str', '1.1',
            'Decription of the basic approximations made in the LandSurface model'),
        ('land_atmosphere_flux_exchanges', 'ENUM:land_atmosphere_flux_exchanges_types', '0.N',
            'TODO.'),
        ('atmospheric_coupling', 'ENUM:atmospheric_coupling_types', '1.1',
            'Specify the treatment of land surface coupling with the Atmosphere model component',),
        ('land_cover', 'ENUM:land_cover_types', '1.N',
            'Types of land cover defined in the land surface model'),
        ('prognostic_variables', 'ENUM:prognostic_vars_types', '1.N',
             'List of prognostic variables in the land surface component.'),
        ('tiling', 'bool', '1.1',
             'Is tiling used in the land surface?'),
        ]
    }

DETAILS['conservation_properties'] = {
    'description': 'TODO',
    'properties' : [
        ('energy', 'str', '0.1',
             'Describe if/how energy is conserved and to what level'),
        ('water', 'str', '0.1',
             'Describe if/how water is conserved and to what level'),
        ('carbon', 'str', '0.1',
             'Describe if/how carbon is conserved and to what level'),
        ('energy', 'str', '0.1',
             'Describe if/how energy is conserved and to what level'),
        ]
    }

DETAILS['timestepping_framework'] = {
    'description': 'TODO',
    'properties' : [
        ('timestep_dependent_on_atmosphere', 'bool', '1.1',
            'Is a time step dependent on the atmosphere coupling?'),
        ('timestepping_method', 'str', '1.1',
            'Describe time stepping method and associated time step(s)'),
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
        ('ice', None), # Do we need land-ice and lake ice?
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
        ('snow ', None),
        ('canopy water content', None),
        ('canopy heat content', None),
        ('canopy snow content', None),
        ('canopy skin temperature', None),
        ('canopy height', None),
        ('surface skin temperature', None),
        ('river water discharge', None),
        ('carbon', None),
        ('nitrogen', None),
        ]
    }
