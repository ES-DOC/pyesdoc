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
DESCRIPTION = 'Ocean boundary forcing'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Top level properties of boundary forcing',
    'properties': [
        ('surface_pressure', 'str', '1.1',
            'Describe how surface pressure is transmitted to ocean (via sea-ice, nothing specific,...)'),
        ('momentum_flux_correction', 'l-str', '0.1',
            'Describe any type of ocean surface momentum flux correction and, if applicable, how it is applied and where.'),
        ('tracers_flux_correction', 'l-str', '0.1',
            'Describe any type of ocean surface tracers flux correction and, if applicable, how it is applied and where.'),
        ('wave_effects', 'l-str', '1.1',
            'Describe if/how wave effects are modelled at ocean surface.'),
        ('river_runoff_budget', 'l-str', '1.1',
            'Describe how river runoff from land surface is routed to ocean and any global adjustment done.'),
        ('geothermal_heating', 'l-str', '1.1',
            'Describe if/how geothermal heating is present at ocean bottom.'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Momentum.
# --------------------------------------------------------------------
DETAILS['momentum'] = {
    'description': 'Key properties of momentum boundary forcing in the ocean'
    }

DETAILS['momentum:bottom_friction'] = {
    'description': 'Properties of momentum bottom friction in ocean',
    'properties': [
        ('type', 'ENUM:mom_bottom_friction_types', '1.1',
            'Type of momentum bottom friction in ocean'),
        ]
    }

DETAILS['momentum:lateral_friction'] = {
   'description': 'Properties of momentum lateral friction in ocean',
    'properties': [
        ('type', 'ENUM:mom_lateral_friction_types', '1.1',
            'Type of momentum lateral friction in ocean'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Tracers.
# --------------------------------------------------------------------
DETAILS['tracers'] = {
    'description': 'Key properties of tracer boundary forcing in the ocean'
    }

DETAILS['tracers:sunlight_penetration'] = {
    'description': 'Properties of sunlight penetration scheme in ocean',
    'properties': [
         ('scheme', 'ENUM:sunlight_penetration_scheme_types', '1.1',
            'Type of sunlight penetration scheme in ocean'),
         ('ocean_colour', 'bool', '1.1',
            'Is the ocean sunlight penetration scheme ocean colour dependent ?'),
         ('extinction_depth_description', 'l-str', '0.1',
            'Describe extinctions depths for sunlight penetration scheme (if applicable).'),
         ('extinction_depths', 'cs-str', '0.1',
            'List extinctions depths for sunlight penetration scheme (if applicable).'),
        ]
    }

DETAILS['tracers:fresh_water_forcing'] = {
    'description': 'Properties of surface fresh water forcing in ocean',
    'properties': [
        ('from_atmopshere', 'ENUM:surface_fresh_water_forcing_atmos_types', '1.1',
            'Type of surface fresh water forcing from atmos in ocean'),
        ('from_sea_ice', 'ENUM:surface_fresh_water_forcing_seaice_types', '1.1',
            'Type of surface fresh water forcing from sea-ice in ocean'),
        ('forced_mode_restoring', 'str', '1.1',
            'Type of surface salinity restoring in forced mode (OMIP)'),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['mom_bottom_friction_types'] = {
    'description': 'Type of momentum bottom friction in ocean',
    'is_open': True,
    'members': [
        ('Linear', None),
        ('Non-linear', None),
        ('Non-linear (drag function of speed of tides)', None),
        ('Constant drag coefficient', None),
        ('None', None),
        ]
    }

ENUMERATIONS['mom_lateral_friction_types'] = {
    'description': 'Type of momentum lateral friction in ocean',
    'is_open': True,
    'members': [
        ('None', None),
        ('Free-slip', None),
        ('No-slip', None),
        ]
    }

ENUMERATIONS['sunlight_penetration_scheme_types'] = {
    'description': 'Type of sunlight penetration scheme in ocean',
    'is_open': True,
    'members': [
        ('1 extinction depth', None),
        ('2 extinction depth', None),
        ('3 extinction depth', None),
        ]
    }

ENUMERATIONS['surface_fresh_water_forcing_atmos_types'] = {
    'description': 'Types of surface fresh water forcing from atmosphere in ocean',
    'is_open': True,
    'members': [
        ('Freshwater flux', None),
        ('Virtual salt flux', None),
        ]
    }

ENUMERATIONS['surface_fresh_water_forcing_seaice_types'] = {
    'description': 'Types of surface fresh water forcing from sea-ice in ocean',
    'is_open': True,
    'members': [
        ('Freshwater flux', None),
        ('Virtual salt flux', None),
        ('Real salt flux', None),
        ]
    }
