"""A realm key-properties specialization.

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
DESCRIPTION = 'Ocean Biogeochemistry key properties'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General key properties in ocean biogeochemistry',
    'properties': [
        ('model_type', 'ENUM:model_family', '1.1',
            'Type of ocean biogeochemistry model'),
        ('elemental_stoichiometry', 'ENUM:elemental_stoichiometry_types', '1.1',
            'Describe elemental stoichiometry (fixed, variable, mix of the two)',),
        ('elemental_stoichiometry_details', 'cs-str', '1.1',
            'Describe which elements have fixed/variable stoichiometry',),
        ('prognostic_variables', 'cs-str', '1.1',
            'List of all prognostic tracer variables in the ocean biogeochemistry component'),
        ('diagnostic_variables', 'cs-str', '1.1',
            'List of all diagnotic tracer variables in the ocean biogeochemistry component (derived from prognostic variables'),
        ('damping', 'str', '0.1',
            'Describe any tracer damping used (such as artificial correction or relaxation to climatology,...)'),
        ]
    }

# --------------------------------------------------------------------
# KEY PROPERTIES: details
# --------------------------------------------------------------------
DETAILS['time_stepping_framework'] = {
    'description': 'Time stepping framework for ocean biogeochemistry',
    'properties' : []
    }

DETAILS['time_stepping_framework:passive_tracers_transport'] = {
    'description': 'Time stepping method for passive tracers transport in ocean biogeochemistry',
    'properties' : [
        ('method', 'ENUM:passive_tracers_transport', '1.1',
            'Time stepping framework for passive tracers'),
        ('timestep_if_not_from_ocean', 'int', '0.1',
            'Time step for passive tracers (if different from ocean)'),
        ]
    }

DETAILS['time_stepping_framework:biology_sources_sinks'] = {
    'description': 'Time stepping framework for biology sources and sinks in ocean biogeochemistry',
    'properties' : [
        ('method', 'ENUM:passive_tracers_transport', '1.1',
            'Time stepping framework for biology sources and sinks'),
        ('timestep_if_not_from_ocean', 'int', '0.1',
            'Time step for biology sources and sinks (if different from ocean)'),
        ]
    }

DETAILS['transport_scheme'] = {
    'description': 'Transport scheme in ocean biogeochemistry',
    'properties' : [
        ('type', 'ENUM:transport_types', '1.1',
            'Type of transport scheme'),
        ('scheme', 'ENUM:transport_scheme', '1.1',
            'Transport scheme used'),
        ('use_different_scheme', 'l-str', '0.1',
            'Decribe transport scheme if different than that of ocean model'),
        ]
    }

DETAILS['boundary_forcing'] = {
    'description': 'Properties of biogeochemistry boundary forcing',
    'properties': [
        ('atmospheric_deposition', 'ENUM:sources_atmos_deposition', '1.1',
            'Describe how atmospheric deposition is modeled'),
        ('river_input', 'ENUM:sources_river_input', '1.1',
            'Describe how river input is modeled'),
        ('sediments_from_boundary_conditions', 'cs-str', '0.1',
            'List which sediments are speficied from boundary condition'),
        ('sediments_from_explicit_model', 'cs-str', '0.1',
            'List which sediments are speficied from explicit sediment model'),
        ]
    }

DETAILS['gas_exchange'] = {
    'description': 'Properties of gas exchange in ocean biogeochemistry ',
    'properties': [
        ('CO2_exchange_present', 'bool', '1.1',
            'Is CO2 gas exchange modeled ?'),
        ('CO2_exchange_type', 'ENUM:gas_exchange_types', '0.1',
            'Describe CO2 gas exchange'),
        ('O2_exchange_present', 'bool', '1.1',
            'Is O2 gas exchange modeled ?'),
        ('O2_exchange_type', 'ENUM:gas_exchange_types', '0.1',
            'Describe O2 gas exchange'),
        ('DMS_exchange_present', 'bool', '1.1',
            'Is DMS gas exchange modeled ?'),
        ('DMS_exchange_type', 'str', '0.1',
            'Specify DMS gas exchange scheme type'),
        ('N2_exchange_present', 'bool', '1.1',
            'Is N2 gas exchange modeled ?'),
        ('N2_exchange_type', 'str', '0.1',
            'Specify N2 gas exchange scheme type'),
        ('N2O_exchange_present', 'bool', '1.1',
            'Is N2O gas exchange modeled ?'),
        ('N2O_exchange_type', 'str', '0.1',
            'Specify N2O gas exchange scheme type'),
        ('CFC11_exchange_present', 'bool', '1.1',
            'Is CFC11 gas exchange modeled ?'),
        ('CFC11_exchange_type', 'str', '0.1',
            'Specify CFC11 gas exchange scheme type'),
        ('CFC12_exchange_present', 'bool', '1.1',
            'Is CFC12 gas exchange modeled ?'),
        ('CFC12_exchange_type', 'str', '0.1',
            'Specify CFC12 gas exchange scheme type'),
        ('SF6_exchange_present', 'bool', '1.1',
            'Is SF6 gas exchange modeled ?'),
        ('SF6_exchange_type', 'str', '0.1',
            'Specify SF6 gas exchange scheme type'),
        ('13CO2_exchange_present', 'bool', '1.1',
            'Is 13CO2 gas exchange modeled ?'),
        ('13CO2_exchange_type', 'str', '0.1',
            'Specify 13CO2 gas exchange scheme type'),
        ('14CO2_exchange_present', 'bool', '1.1',
            'Is 14CO2 gas exchange modeled ?'),
        ('14CO2_exchange_type', 'str', '0.1',
            'Specify 14CO2 gas exchange scheme type'),
        ('other_gases', 'str', '0.1',
            'Specify any other gas exchange'),
        ]
    }

DETAILS['carbon_chemistry'] = {
    'description': 'Properties of carbon chemistry biogeochemistry',
    'properties': [
        ('type', 'ENUM:carbon_chemistry', '1.1',
            'Describe how carbon chemistry is modeled'),
        ('ph_scale', 'ENUM:ph_scale', '0.1',
            'If NOT OMIP protocol, describe pH scale.'),
        ('constants_if_not_OMIP', 'cs-str', '0.1',
            'If NOT OMIP protocol, list carbon chemistry constants.'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: TUNING APPLIED: Any tuning used to optimise the parameters
# --------------------------------------------------------------------
DETAILS['tuning_applied'] = {
    'description': 'Tuning methodology for ocean biogeochemistry component',
    'properties': [
        ('description', 'l-str', '1.1',
             "General overview description of tuning: explain and motivate the main targets and metrics retained. &"
             "Document the relative weight given to climate performance metrics versus process oriented metrics, &"
             "and on the possible conflicts with parameterization level tuning. In particular describe any struggle &"
             "with a parameter value that required pushing it to its limits to solve a particular model deficiency."),
        ('global_mean_metrics_used', 'cs-str', '0.1',
             "List set of metrics of the global mean state used in tuning model/component"),
        ('regional_metrics_used', 'cs-str', '0.1',
             "List of regional metrics of mean state used in tuning model/component"),
        ('trend_metrics_used', 'cs-str', '0.1',
             "List observed trend metrics used in tuning model/component"),
        ]
    }

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['model_family'] = {
    'description': 'Types of models for ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Geochemical', 'No living compartments'),
        ('NPZD', 'No plankton types'),
        ('PFT','Several plankton types'),
        ]
    }

ENUMERATIONS['elemental_stoichiometry_types'] = {
    'description': 'Types elemental stoichiometry for ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('Fixed', 'Fixed stoichiometry'),
        ('Variable', 'Variable stoichiometry'),
        ('Mix of both','Both fixed and mixed stoichiometry'),
        ]
    }


ENUMERATIONS['passive_tracers_transport'] = {
    'description': 'Types of time stepping framework for passive tracers ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('use ocean model transport time step', None),
        ('use specific time step', None),
        ]
    }

ENUMERATIONS['transport_types'] = {
    'description': 'Types of transport in ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('Offline', None),
        ('Online', None),
        ]
    }

ENUMERATIONS['transport_scheme'] = {
    'description': 'Types of transport in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Use that of ocean model', None),
        ]
    }

ENUMERATIONS['sources_atmos_deposition'] = {
    'description': 'Type of atmospheric deposition in ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('from file (climatology)', None),
        ('from file (interannual variations)', None),
        ('from Atmospheric Chemistry model', None),
        ]
    }

ENUMERATIONS['sources_river_input'] = {
    'description': 'Type of river input in ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('from file (climatology)', None),
        ('from file (interannual variations)', None),
        ('from Land Surface model', None),
        ]
    }

ENUMERATIONS['gas_exchange_types'] = {
    'description': 'Type of gas exchange in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('OMIP protocol', None),
        ]
    }

ENUMERATIONS['carbon_chemistry'] = {
    'description': 'Type of carbon chemistry in ocean biogeochemistry',
    'is_open': False,
    'members': [
        ('OMIP protocol', None),
        ('Other protocol', None),
        ]
    }

ENUMERATIONS['ph_scale'] = {
    'description': 'Type of carbon chemistry pH scale in ocean biogeochemistry',
    'is_open': True,
    'members': [
        ('Sea water', None),
        ('Free', None),
        ]
    }
