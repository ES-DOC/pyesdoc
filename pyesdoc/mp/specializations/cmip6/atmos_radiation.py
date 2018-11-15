"""

A realm process specialization.

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
DESCRIPTION = 'Characteristics of the atmosphere radiation process'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "Radiative agents in the atmosphere",
    'properties': [
        ('aerosols', 'ENUM:aerosol_types', '1.N',
            'Aerosols whose radiative effect is taken into account in the atmosphere model'),
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
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General radiative interactions e.g. with aerosols, cloud ice and cloud water '),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_GHG
# --------------------------------------------------------------------
DETAILS['shortwave_GHG'] = {
    'description': 'Representation of greenhouse gases in the shortwave radiation scheme',
    'properties': [
        ('greenhouse_gas_complexity', 'ENUM:ghg_types', '1.N',
            'Complexity of greenhouse gases whose shortwave radiative effects are taken into account '
            'in the atmosphere model'),
        ('ODS', 'ENUM:ODS', '0.N',
            'Ozone depleting substances whose shortwave radiative effects are explicitly taken into account '
            'in the atmosphere model'),
        ('other_flourinated_gases', 'ENUM:other_fluorinated_gases', '0.N',
            'Other flourinated gases whose shortwave radiative effects are explicitly taken into account '
            'in the atmosphere model'),
        ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_cloud_ice
# --------------------------------------------------------------------
DETAILS['shortwave_cloud_ice'] = {
    'description': 'Shortwave radiative properties of ice crystals in clouds',
    'properties': [
        ('physical_representation', 'ENUM:cloud_ice_physical_representation', '1.N',
            'Physical representation of cloud ice crystals in the shortwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud ice crystals in the shortwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_cloud_liquid
# --------------------------------------------------------------------
DETAILS['shortwave_cloud_liquid'] = {
    'description': 'Shortwave radiative properties of liquid droplets in clouds',
    'properties': [
        ('physical_representation', 'ENUM:cloud_liquid_physical_representation', '1.N',
            'Physical representation of cloud liquid droplets in the shortwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods_droplets', '1.N',
            'Optical methods applicable to cloud liquid droplets in the shortwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_cloud_inhomogeneity
# --------------------------------------------------------------------
DETAILS['shortwave_cloud_inhomogeneity'] = {
    'description': 'Cloud inhomogeneity in the shortwave radiation scheme',
    'properties': [
        ('cloud_inhomogeneity', 'ENUM:inhomogeneity_treatment', '1.1',
            'Method for taking into account horizontal cloud inhomogeneity'),
        ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_aerosols
# --------------------------------------------------------------------
DETAILS['shortwave_aerosols'] = {
    'description': 'Shortwave radiative properties of aerosols',
    'properties': [
        ('physical_representation', 'ENUM:aerosol_physical_representation', '1.N',
            'Physical representation of aerosols in the shortwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to aerosols in the shortwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_gases
# --------------------------------------------------------------------
DETAILS['shortwave_gases'] = {
    'description': 'Shortwave radiative properties of gases',
    'properties': [
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
        ('general_interactions', 'ENUM:radiative_interactions', '1.N',
            'General radiative interactions e.g. with aerosols, cloud ice and cloud water '),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: longwave_GHG
# --------------------------------------------------------------------
DETAILS['longwave_GHG'] = {
    'description': 'Representation of greenhouse gases in the longwave radiation scheme',
    'properties': [
        ('greenhouse_gas_complexity', 'ENUM:ghg_types', '1.N',
            'Complexity of greenhouse gases whose longwave radiative effects are taken into account '
            'in the atmosphere model'),
        ('ODS', 'ENUM:ODS', '0.N',
            'Ozone depleting substances whose longwave radiative effects are explicitly taken into account '
            'in the atmosphere model'),
        ('other_flourinated_gases', 'ENUM:other_fluorinated_gases', '0.N',
            'Other flourinated gases whose longwave radiative effects are explicitly taken into account '
            'in the atmosphere model'),
        ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: longwave_cloud_ice
# --------------------------------------------------------------------
DETAILS['longwave_cloud_ice'] = {
    'description': 'Longwave radiative properties of ice crystals in clouds',
    'properties': [
        ('physical_reprenstation', 'ENUM:cloud_ice_physical_representation', '1.N',
            'Physical representation of cloud ice crystals in the longwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to cloud ice crystals in the longwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: longwave_cloud_liquid
# --------------------------------------------------------------------
DETAILS['longwave_cloud_liquid'] = {
    'description': 'Longwave radiative properties of liquid droplets in clouds',
    'properties': [
        ('physical_representation', 'ENUM:cloud_liquid_physical_representation', '1.N',
            'Physical representation of cloud liquid droplets in the longwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods_droplets', '1.N',
            'Optical methods applicable to cloud liquid droplets in the longwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: longwave_cloud_inhomogeneity
# --------------------------------------------------------------------
DETAILS['longwave_cloud_inhomogeneity'] = {
    'description': 'Cloud inhomogeneity in the longwave radiation scheme',
    'properties': [
        ('cloud_inhomogeneity', 'ENUM:inhomogeneity_treatment', '1.1',
            'Method for taking into account horizontal cloud inhomogeneity'),
        ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: longwave_aerosols
# --------------------------------------------------------------------
DETAILS['longwave_aerosols'] = {
    'description': 'Longwave radiative properties of aerosols',
    'properties': [
        ('physical_representation', 'ENUM:aerosol_physical_representation', '1.N',
            'Physical representation of aerosols in the longwave radiation scheme'),
        ('optical_methods', 'ENUM:optical_methods', '1.N',
            'Optical methods applicable to aerosols in the longwave radiation scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: longwave_gases
# --------------------------------------------------------------------
DETAILS['longwave_gases'] = {
    'description': 'Longwave radiative properties of gases',
    'properties': [
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
        ('BC', 'black carbon / soot'),
        ('SOA', 'secondary organic aerosols'),
        ('POM', 'particulate organic matter'),
        ('polar stratospheric ice', None),
        ('NAT', 'nitric acid trihydrate'),
        ('NAD', 'nitric acid dihydrate'),
        ('STS', 'supercooled ternary solution aerosol particle'),
        ]
    }

ENUMERATIONS['ghg_types'] = {
    'description': 'Greenhouse gases whose radiative effect is taken into account in the atmosphere model',
    'is_open': True,
    'members': [
        ('CO2', 'Carbon Dioxide'),
        ('CH4', 'Methane'),
        ('N2O', 'Nitrous Oxide'),
        ('CFC-11 eq', 'Summarize the effect of non CO2, CH4, N2O and CFC-12 gases '
                      'with an equivalence concentration of CFC-11'),
        ('CFC-12 eq', 'Summarize the radiative effect of the Ozone Depleating Substances, ODSs, '
                      'with a CFC-12 equivalence concentration'),
        ('HFC-134a eq', 'Summarize the radiative effect of other fluorinated gases '
                         'with a HFC-134a equivalence concentration'),
        ('Explicit ODSs', 'Explicit representation of Ozone Depleting Substances '
                          'e.g. CFCs, HCFCs and Halons'),
        ('Explicit other fluorinated gases', 'Explicit representation of other fluorinated gases '
                                             'e.g. HFCs and PFCs'),
        ('O3', None),
        ('H2O', None),
        ]
    }

ENUMERATIONS['ODS'] = {
    'description': 'Ozone depleting substances, ODS, whose radiative effect is explicitly taken into account '
                   'in the atmosphere model',
    'is_open': True,
    'members': [
        ('CFC-12', 'CFC'),
        ('CFC-11', 'CFC'),
        ('CFC-113', 'CFC'),
        ('CFC-114', 'CFC'),
        ('CFC-115', 'CFC'),
        ('HCFC-22', 'HCFC'),
        ('HCFC-141b', 'HCFC'),
        ('HCFC-142b', 'HCFC'),
        ('Halon-1211', 'halon'),
        ('Halon-1301', 'halon'),
        ('Halon-2402', 'halon'),
        ('methyl chloroform', 'CH3CCl3'),
        ('carbon tetrachloride', 'CCl4'),
        ('methyl chloride', 'CH3Cl'),
        ('methylene chloride', 'CH2Cl2'),
        ('chloroform', 'CHCl3'),
        ('methyl bromide', 'Ch3Br'),
        ]
    }

ENUMERATIONS['other_fluorinated_gases'] = {
    'description': 'Other Fluorinated gases whose radiative effect is explicitly taken into account '
                   'in the atmosphere model',
    'is_open': True,
    'members': [
        ('HFC-134a', 'HFC'),
        ('HFC-23', 'HFC'),
        ('HFC-32', 'HFC'),
        ('HFC-125', 'HFC'),
        ('HFC-143a', 'HFC'),
        ('HFC-152a', 'HFC'),
        ('HFC-227ea', 'HFC'),
        ('HFC-236fa', 'HFC'),
        ('HFC-245fa', 'HFC'),
        ('HFC-365mfc', 'HFC'),
        ('HFC-43-10mee', 'HFC'),
        ('CF4', 'PFC'),
        ('C2F6', 'PFC'),
        ('C3F8', 'PFC'),
        ('C4F10', 'PFC'),
        ('C5F12', 'PFC'),
        ('C6F14', 'PFC'),
        ('C7F16', 'PFC'),
        ('C8F18', 'PFC'),
        ('c-C4F8', 'PFC'),
        ('NF3', None),
        ('SF6', None),
        ('SO2F2', None),
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
        ('emission/absorption,', None),
        ('scattering', None),
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

ENUMERATIONS['optical_methods_droplets'] = {
    'description': 'Optical methods used by radiation scheme',
    'is_open': True,
    'members': [
        ('geometric optics', 'For non-spherical particles'),
        ('Mie theory', 'For spherical particles'),
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


ENUMERATIONS['inhomogeneity_treatment'] = {
    'description': 'Cloud scheme inhomogeneity treatment',
    'is_open': True,
    'members': [
        ('Monte Carlo Independent Column Approximation', 'McICA'),
        ('Triplecloud', 'Regions of clear sky, optically thin cloud and optically thick cloud, Shonk et al 2010'),
        ('analytic', None),
        ]
    }

