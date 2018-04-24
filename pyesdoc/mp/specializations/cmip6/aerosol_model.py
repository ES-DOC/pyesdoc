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
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Aerosol model'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level aerosol model properties',
    'properties': [
        ('overview', 'l-str', '1.1',
            'Overview of atmospheric aerosol model'),
        ('processes', 'ENUM:model_processes', '1.N',
            'Processes included in the aerosol model.'),
        ('coupling', 'ENUM:coupling', '0.N',
            'Other model components coupled to the aerosol model'),
        ('gas_phase_precursors', 'ENUM:gas_phase_precursors', '1.N',
            'Gas phase aerosol precursors.'),
        ('scheme_type', 'ENUM:scheme_types', '1.N',
             'Type(s) of aerosol scheme used by the aerosol model (potentially multiple: some species may be covered by one type of aerosol scheme and other species covered by another type).'),
        ('bulk_scheme_species', 'ENUM:species', '1.N',
             'Species covered by the bulk scheme.'),
    ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['model_processes'] = {
    'description': 'Processes included in the aerosol model.',
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
        ('Nucleation', None),
    ]
}

ENUMERATIONS['coupling'] = {
    'description':'Other model components coupled to the aerosol model.',
    'is_open': True,
    'members':[
        ('Radiation', None),
        ('Land surface', None),
        ('Heterogeneous chemistry', None),
        ('Clouds', None),
        ('Ocean', None),
        ('Cryosphere', None),
        ('Gas phase chemistry', None),
    ]
}

ENUMERATIONS['gas_phase_precursors'] = {
    'description': 'Gas phase aerosol precursors.',
    'is_open': True,
    'members':[
        ('DMS', None),
        ('SO2', None),
        ('Ammonia', None),
        ('Iodine', None),
        ('Terpene', None),
        ('Isoprene', None),
        ('VOC', None),
        ('NOx', None),
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
    'description':'Aerosol species.',
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

