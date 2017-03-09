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
AUTHORS = 'Charlotte Pascoe, Robert Pincus'

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
    'description': "Radiative agents in the atmosphere",
    'properties': [
        ('aerosols', 'ENUM:aerosol_types', '1.N',
            'Aerosols whose radiative effect is taken into account in the atmosphere model'),
        ('greenhouse_gases', 'ENUM:ghg_types', '1.N',
            'Greenhouse gases whose radiative effect is taken into account in the atmosphere model'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_radiation
# --------------------------------------------------------------------
DETAILS['shortwave_radiation'] = {
    'description': 'Properties of the shortwave radiation scheme',
    'properties': [
        ('name', 'str', '0.1',
            'Commonly used name for the shortwave radiation scheme'),
        ('spectral_integration', 'ENUM:spectral_integration', '1.1',
            'Shortwave radiation scheme spectral integration'),
        ('transport_calculation', 'ENUM:transport_calculation', '1.N',
            'Shortwave radiation transport calculation methods'),
        ('spectral_intervals', 'int', '1.1',
            'Shortwave radiation scheme number of spectral intervals'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: sw_cloud_ice
# --------------------------------------------------------------------
DETAILS['sw_cloud_ice'] = {
    'description': 'Shortwave radiative properties of ice crystals in clouds',
    'properties': [
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General shortwave radiative interactions with cloud ice crystals'),
        ('physical_representation', 'ENUM:cloud_ice_physical_representation', '1.N',
            'Physical representation of cloud ice crystals in the shortwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud ice crystals in the shortwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: sw_cloud_liquid
# --------------------------------------------------------------------
DETAILS['sw_cloud_liquid'] = {
    'description': 'Shortwave radiative properties of liquid droplets in clouds',
    'properties': [
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General shortwave radiative interactions with cloud liquid droplets'),
        ('physical_representation', 'ENUM:cloud_liquid_physical_representation', '1.N',
            'Physical representation of cloud liquid droplets in the shortwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud liquid droplets in the shortwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: sw_aerosols
# --------------------------------------------------------------------
DETAILS['sw_aerosols'] = {
    'description': 'Shortwave radiative properties of aerosols',
    'properties': [
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General shortwave radiative interactions with aerosols'),
        ('physical_representation', 'ENUM:aerosol_physical_representation', '1.N',
            'Physical representation of aerosols in the shortwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to aerosols in the shortwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: sw_gases
# --------------------------------------------------------------------
DETAILS['sw_gases'] = {
    'description': 'Shortwave radiative properties of gases',
    'properties': [
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General shortwave radiative interactions with gases'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to gases in the shortwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: longwave_radiation
# --------------------------------------------------------------------
DETAILS['longwave_radiation'] = {
    'description': 'Properties of the longwave radiation scheme',
    'properties': [
        ('name', 'str', '0.1',
            'Commonly used name for the longwave radiation scheme.'),
        ('spectral_integration', 'ENUM:spectral_integration', '1.1',
            'Longwave radiation scheme spectral integration'),
        ('transport_calculation', 'ENUM:transport_calculation', '1.N',
            'Longwave radiation transport calculation methods'),
        ('spectral_intervals', 'int', '1.1',
            'Longwave radiation scheme number of spectral intervals'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: lw_cloud_ice
# --------------------------------------------------------------------
DETAILS['lw_cloud_ice'] = {
    'description': 'Longwave radiative properties of ice crystals in clouds',
    'properties': [
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General longwave radiative interactions with cloud ice crystals'),
        ('physical_reprenstation', 'ENUM:cloud_ice_physical_representation', '1.N',
            'Physical representation of cloud ice crystals in the longwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud ice crystals in the longwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: lw_cloud_liquid
# --------------------------------------------------------------------
DETAILS['lw_cloud_liquid'] = {
    'description': 'Longwave radiative properties of liquid droplets in clouds',
    'properties': [
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General longwave radiative interactions with cloud liquid droplets'),
        ('physical_representation', 'ENUM:cloud_liquid_physical_representation', '1.N',
            'Physical representation of cloud liquid droplets in the longwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud liquid droplets in the longwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: lw_aerosols
# --------------------------------------------------------------------
DETAILS['lw_aerosols'] = {
    'description': 'Longwave radiative properties of aerosols',
    'properties': [
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General longwave radiative interactions with aerosols'),
        ('physical_representation', 'ENUM:aerosol_physical_representation', '1.N',
            'Physical representation of aerosols in the longwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to aerosols in the longwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: lw_gases
# --------------------------------------------------------------------
DETAILS['lw_gases'] = {
    'description': 'Longwave radiative properties of gases',
    'properties': [
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General longwave radiative interactions with gases'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to gases in the longwave radiation scheme'),
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

ENUMERATIONS['spectral_integration'] = {
    'description': 'Spectral integration of the radiation scheme',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('correlated-k', None),
        ('exponential sum fitting', None),
        ]
    }

ENUMERATIONS['transport_calculation'] = {
    'description': 'Radiation transport calculation methods',
    'is_open': True,
    'members': [
        ('two-stream', None),
        ('layer interaction', None),
        ('bulk', 'highly parameterised methods that use bulk expressions'),
        ('adaptive', 'exploits spatial and temporal correlations in optical characteristics'),
        ('multi-stream', None)
        ]
    }

ENUMERATIONS['radiative_interactions'] = {
    'description': 'General radiative interactions',
    'is_open': True,
    'members': [
        ('scattering', None),
        ('emission/absorption', None),
    ]
}

ENUMERATIONS['cloud_ice_physical_representation'] = {
    'description': 'Physical representation of ice crystals in clouds',
    'is_open': True,
    'members': [
        ('bi-modal size distribution',
            'small mode diameters: a few tens of microns, large mode diameters: typically hundreds of microns'),
        ('ensemble of ice crystals', 'complex shapes represented with an ensemble of symmetric shapes'),
        ('mean projected area',
            'randomly oriented irregular ice crystals present a greater mean projected area than spheres'),
        ('ice water path', 'Integrated ice water path through the cloud kg m-2',),
        ('crystal asymmetry', None),
        ('crystal aspect ratio', None),
        ('effective crystal radius', None),
        ]
    }

ENUMERATIONS['cloud_liquid_physical_representation'] = {
    'description': 'Physical_radiative representation of liquid droplets in clouds',
    'is_open': True,
    'members': [
        ('cloud droplet number concentration', 'CDNC'),
        ('effective cloud droplet radii', None),
        ('droplet size distribution', None),
        ('liquid water path', 'Integrated liquid water path through the cloud kg m-2',),
        ]
    }

ENUMERATIONS['aerosol_physical_representation'] = {
    'description': 'Physical radiative representation of aerosols',
    'is_open': True,
    'members': [
        ('number concentration', None),
        ('effective radii', None),
        ('size distribution', None),
        ('asymmetry', None),
        ('aspect ratio', None),
        ('mixing state', 'For shortwave radiative interaction'),
        ]
    }

ENUMERATIONS['optical_methods'] = {
    'description': 'Optical methods used by radiation scheme',
    'is_open': True,
    'members': [
        ('T-matrix', 'For non-spherical particles'),
        ('geometric optics', 'For non-spherical particles'),
        ('finite difference time domain (FDTD)', 'For non-spherical particles'),
        ('Mie theory', 'For spherical particles'),
        ('anomalous diffraction approximation', None),
        ]
    }

ENUMERATIONS['cloud_ice_radiation_processes'] = {
    'description': 'Optical radiative processes for ice crystals in clouds',
    'is_open': True,
    'members': [
        ('emissivity', None),
        ('absorption', None),
        ('backward scattering', None),
        ('side scattering', None),
        ]
    }

ENUMERATIONS['cloud_liquid_radiation_processes'] = {
    'description': 'Optical radiative processes for liquid droplets in clouds',
    'is_open': True,
    'members': [
        ('droplet scattering', None),
        ('droplet absorption', None),
        ('broadband reflectivity', 'albedo'),
        ('broadband transmissivity', None),
        ('broadband absorbtivity', None),
        ]
    }

ENUMERATIONS['shortwave_scheme_type'] = {
    'description': 'Type of scheme used for shortwave radiation parameterisation',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('bulk-scheme', 'highly parameterised methods that use bulk expressions'),
        ('two-stream', None),
        ('two-stream (delta-Eddington)', 'approximation for solar radiation calculations'),
        ]
    }

ENUMERATIONS['single_scattering_properties_methods'] = {
    'description': 'Methods for calculating single scattering properties of atmospheric constituents',
    'is_open': True,
    'members': [
        ('T-Matrix', 'an exact method'),
        ('geometrical optics', 'for particles that are much larger than the wavelength of light'),
        ('finite difference time domain', 'FDTD'),
        ('anomalous diffraction approximation', 'ADA'),
        ('k-distribution', None),
        ('band model', None),
        ('exponential sum fitting', None),
    ]
}



