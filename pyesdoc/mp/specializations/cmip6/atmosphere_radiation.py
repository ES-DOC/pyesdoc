"""

A realm process sepecialization.

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
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of the atmosphere radiation process'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "Radiative agents in the atmosphere model",
    'properties': [
        ('aerosols', 'ENUM:aerosol_types', '1.N',
            'Aerosols whose radiative effect is taken into account in the atmosphere model'),
        ('greenhouse_gases', 'ENUM:ghg_types', '1.N',
            'Greenhouse gases whose radiative effect is taken into account in the atmosphere model'),
        ('cloud_ice', 'ENUM:cloud_ice_properties', '1.N',
            'Radiative properties of ice crystals in clouds'),
        ('cloud_liquid', 'ENUM:cloud_liquid_properties', '1.N',
            'Radiative properties of liquid droplets in clouds'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: longwave_radiation
# --------------------------------------------------------------------
DETAILS['longwave_radiation'] = {
    'description': 'Properties of the longwave radiation scheme',
    'properties': [
        ('scheme_type', 'ENUM:longwave_scheme_type', '1.1',
            'Longwave radiation scheme type'),
        ('scheme_method', 'ENUM:longwave_scheme_method', '1.1',
            'Longwave radiation scheme method'),
        ('spectral_intervals', 'int', '1.1',
            'Longwave radiation scheme spectral intervals'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_radiation
# --------------------------------------------------------------------
DETAILS['shortwave_radiation'] = {
    'description': 'Properties of the shortwave radiation scheme',
    'properties': [
        ('scheme_type', 'ENUM:shortwave_scheme_type', '1.1',
            'Shortwave radiation scheme type'),
        ('spectral_intervals', 'int', '1.1',
            'Shortwave radiation scheme spectral intervals'),
        ]
    }


# --------------------------------------------------------------------
# SUB-PROCESS: single_scattering_properties
# --------------------------------------------------------------------
DETAILS['single_scattering_properties'] = {
    'description': 'Single scattering properties of ice clouds',
    'properties': [
        ('single_scattering', 'ENUM:single_scattering_properties_methods', '0.N',
            'Methods for calculating single scattering properties of ice crystals'),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['aerosol_types'] = {
    'description': 'Aerosols whose radiative effect is taken into account in the atmospheric model.',
    'is_open': True,
    'members': [
        ('sulphate', None),
        ('nitrate', None),
        ('sea salt', None),
        ('dust', None),
        ('ice', None),
        ('organic', None),
        ('BC (black carbon / soot)', None),
        ('SOA (secondary organic aerosols)', None),
        ('POM (particulate organic matter)', None),
        ('polar stratospheric ice', None),
        ('NAT (nitric acid trihydrate)', None),
        ('NAD (nitric acid dihydrate)', None),
        ('STS (supercooled ternary solution aerosol particle)', None),
        ]
    }

ENUMERATIONS['ghg_types'] = {
    'description': 'Greenhouse gases whose radiative effect is taken into account in the atmospheric model',
    'is_open': True,
    'members': [
        ('H2O', None),
        ('CO2', None),
        ('CH4', None),
        ('N2O', None),
        ('O3', None),
        ('CFCs', None),
        ('HFCs', None),
        ('PFCs', None),
        ('SF6', None),
        ('NF3', None),
        ]
    }


ENUMERATIONS['cloud_ice_properties'] = {
    'description': 'Radiative properties of ice crystals in clouds',
    'is_open': True,
    'members': [
        ('treated as spherical particles', None),
        ('effective crystal radius', None),
        ('treated as non-spherical particles', None),
        ('mean projected area',
            'randomly oriented irregular ice crystals present a greater mean projected area than spheres'),
        ('bi-modal size distribution',
            'small mode diameters: a few tens of microns, large mode diameters: typically hundreds of microns'),
        ('ensemble of ice crystals', 'complex shapes represented with an ensemble of symmetric shapes'),
        ('ice water path', 'Integrated ice water path through the cloud kg m-2',),
        ('crystal asymmetry', None),
        ('crystal aspect ratio', None),
        ('emissivity', None),
        ('absorption', None),
        ('backward scattering', None),
        ('side scattering', None),
        ]
    }

ENUMERATIONS['single_scattering_properties_methods'] = {
    'description': 'Methods for calculating single scattering properties of ice crystals',
    'is_open': True,
    'members': [
        ('T-Matrix', 'an exact method'),
        ('geometrical optics', 'for particles that are much larger than the wavelength of light'),
        ('finite difference time domain', 'FDTD'),
        ('anomalous diffraction approximation', 'ADA'),
    ]
}

ENUMERATIONS['cloud_liquid_properties'] = {
    'description': 'Radiative properties of liquid droplets in clouds',
    'is_open': True,
    'members': [
        ('droplet scattering', None),
        ('droplet absorption', None),
        ('cloud droplet number concentration', 'CDNC'),
        ('effective cloud droplet radii', None),
        ('droplet size distribution', None),
        ('liquid water path', 'Integrated liquid water path through the cloud kg m-2',),
        ('broadband reflectivity', 'albedo'),
        ('broadband transmissivity', None),
        ('broadband absorbtivity', None),
        ]
    }

ENUMERATIONS['longwave_scheme_type'] = {
    'description': 'Type of scheme used for longwave radiation parameterisation',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('wide-band model (Morcrette)', None),
        ('K-correlated', None),
        ('K-correlated (RRTM)', None),
        ]
    }

ENUMERATIONS['longwave_scheme_method'] = {
    'description': 'Method for the radiative transfer calculations used in the longwave scheme',
    'is_open': True,
    'members': [
        ('two-stream', None),
        ('layer interaction', None),
        ('adaptive', 'exploits spatial and temporal correlations in optical characteristics')
        ]
    }

ENUMERATIONS['shortwave_scheme_type'] = {
    'description': 'Type of scheme used for shortwave radiation parameterisation',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('wide-band model (Fouquart)', None),
        ('bulk-scheme', 'highly parameterized methods that use bulk expressions'),
        ('two-stream', None),
        ('two-stream (delta-Eddington)', 'approximation for solar radiation calculations'),
        ]
    }
