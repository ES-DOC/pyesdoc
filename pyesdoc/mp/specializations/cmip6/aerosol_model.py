"""A process specialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe, David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Aerosol model'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level aerosol model properties',
    'properties': [
        ('processes', 'ENUM:model_processes', '1.N',
            'Processes included in the Aerosol model.'),
        ('coupling', 'ENUM:coupling', '0.N',
            'Other model components coupled to the Aerosol model'),
        ('gas_phase_precursors', 'ENUM:gas_phase_precursors', '1.N',
            'List of gas phase aerosol precursors.'),
        ('scheme_type', 'ENUM:scheme_types', '1.N',
             'Type(s) of aerosol scheme used by the aerosols model (potentially multiple: some species may be covered by one type of aerosol scheme and other species covered by another type).'),
        ('bulk_scheme_species', 'ENUM:species', '1.N',
             'List of species covered by the bulk scheme.'),
        ('model_scheme_framework', 'ENUM:scheme_frameworks', '1.1',
             'Aerosols classification framework used in the modal aerosol scheme.'),
        ('model_scheme_species', 'ENUM:species', '1.N',
             'List of species covered by the modal scheme.'),
        ('bin_scheme_framework', 'ENUM:scheme_frameworks', '1.1',
             'Aerosols classification framework used in the bin aerosol scheme.'),
        ('bin_scheme_species', 'ENUM:species', '1.N',
             'List of species covered by the bin scheme.'),
        ('classification_framework', 'ENUM:scheme_frameworks', '0.1',
             'Aerosols classification framework.'),
        ('classification_framework_characterisitics', 'str', '0.1',
             'Characteristics of the aerosol scheme used.'),
        ('classification_framework_species', 'ENUM:species', '0.1',
             'List of species covered by the scheme.'),
    ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['model_processes'] = {
    'description': 'Processes included in the Aerosol model.',
    'is_open': False,
    'members': [
        ('Dry deposition', None),
        ('Sedimentation', None),
        ('Wet deposition (impaction scavenging)', None),
        ('Wet deposition (nucleation scavenging)', None),
        ('Coagulation', None),
        ('Oxidation (gas phase)', None),
        ('Oxidation (in cloud)', None),
        ('Condensation', None),
        ('Ageing', None),
        ('Advection (horizontal)', None),
        ('Advection (vertical)', None),
        ('Heterogeneous chemistry', None),
    ]
}

ENUMERATIONS['coupling'] = {
    'description':'Other model components coupled to the Aerosol model.',
    'is_open': True,
    'members':[
        ('Radiation', None),
        ('Land surface', None),
        ('Heterogeneous chemistry', None),
        ('Clouds', None),
    ]
}

ENUMERATIONS['gas_phase_precursors'] = {
    'description': 'List of gas phase aerosol precursors.',
    'is_open': True,
    'members':[
        ('DMS', None),
        ('SO2', None),
        ('Ammonia', None),
        ('Iodene', None),
        ('Terpene', None),
        ('Isoprene', None),
    ]
}

ENUMERATIONS['scheme_types'] = {
    'description': 'Type(s) of aerosol scheme used by the aerosols model (potentially multiple: some species may be covered by one type of aerosol scheme and other species covered by another type).',
    'is_open': True,
    'members':[
        ('Bulk', None),
        ('Modal', None),
        ('Bin', None),
    ]
}

ENUMERATIONS['species'] = {
    'description':'List of species.',
    'is_open': True,
    'members':[
        ('Sulphate', None),
        ('Nitrate', None),
        ('Sea salt', None),
        ('Dust', None),
        ('Ice', None),
        ('Organic', None),
        ('Black carbon / soot', None),
        ('SOA (secondary organic aerosols)', None),
        ('POM (particulate organic matter)', None),
        ('Polar stratospheric ice', None),
        ('NAT (Nitric acid trihydrate)', None),
        ('NAD (Nitric acid dihydrate)', None),
        ('STS (supercooled ternary solution aerosol particule)', None),
    ]
}

ENUMERATIONS['scheme_frameworks'] = {
    'description': 'Aerosols classification framework',
    'is_open': True,
    'members':[
        ('Single moment', None),
        ('Microphysical', None),
    ]
}

