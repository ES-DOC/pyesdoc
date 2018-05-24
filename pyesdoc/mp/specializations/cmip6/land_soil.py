"""A realm process sepecialization.

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
DESCRIPTION = 'Land surface soil'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Land surface soil top level properties',
    'properties': [
         ('heat_water_coupling', 'str', '1.1',
             'Describe the coupling between heat and water in the soil'),
         ('number_of_soil layers', 'int', '1.1',
             'The number of soil layers'),
         ('prognostic_variables', 'cs-str', '1.1',
             'List the prognostic variables of the soil scheme'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: Soil map
# --------------------------------------------------------------------
DETAILS['soil_map'] = {
    'description': 'Key properties of the land surface soil map',
    'properties': [
        ('description', 'l-str', '1.1',
             'General description of soil map'),
        ('structure', 'str', '0.1',
             'Describe the soil structure map'),
        ('texture', 'str', '0.1',
             'Describe the soil texture map'),
        ('organic_matter', 'str', '0.1',
             'Describe the soil organic matter map'),
        ('albedo', 'str', '0.1',
             'Describe the soil albedo map'),
        ('water_table', 'str', '0.1',
             'Describe the soil water table map, if any'),
        ('continuously_varying_soil_depth', 'bool', '1.1',
             'Does the soil properties vary continuously with depth?'),
        ('soil_depth', 'str', '0.1',
             'Describe the soil depth map'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Snow-free albedo
# --------------------------------------------------------------------
DETAILS['snow_free_albedo'] = {
    'description': 'Snow free albedo',
    'properties' : [
        ('prognostic', 'bool', '1.1',
             'Is snow free albedo prognostic?'),
        ('functions', 'ENUM:snow_free_albedo_function_types', '0.N',
             'If prognostic, describe the dependancies on snow free albedo calculations'),
        ('direct_diffuse', 'ENUM:direct_diffuse_types', '0.1',
             'If prognostic, describe the distinction between direct and diffuse albedo'),
        ('number_of_wavelength_bands', 'int', '0.1',
             'If prognostic, enter the number of wavelength bands used'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: Hydrology
# --------------------------------------------------------------------
DETAILS['hydrology'] = {
    'description': 'Key properties of the soil hydrology',
    'properties': [
        ('description', 'l-str', '1.1',
             'General description of the soil hydrological model'),
        ('time_step', 'int', '1.1',
             'Time step of river soil hydrology in seconds'),                
        ('tiling', 'l-str', '0.1',
             'Describe the soil hydrology tiling, if any.'),
        ('vertical_discretisation', 'l-str' , '1.1',
             'Describe the typical vertical discretisation'),
        ('number_of_ground_water_layers', 'int', '1.1',
             'The number of soil layers that may contain water'),
        ('lateral_connectivity', 'ENUM:lateral_connectivity_types', '1.N',
             'Describe the lateral connectivity between tiles'),
        ('method', 'ENUM:water_storage_method_types', '1.1',
             'The hydrological dynamics scheme in the land surface model'),
    ]
}

DETAILS['hydrology:freezing'] = {
    'description': 'Frozen soil treatment',
    'properties': [
        ('number_of_ground_ice_layers', 'int', '1.1',
            'How many soil layers may contain ground ice'),
        ('ice_storage_method', 'str', '1.1',
            'Describe the method of ice storage'),
        ('permafrost', 'l-str', '1.1',
            'Describe the treatment of permafrost, if any, within the land surface scheme'),
        ]
    }

DETAILS['hydrology:drainage'] = {
    'description': 'Drainage treatment in the soil',
    'properties': [
        ('description', 'l-str', '1.1',
            'General describe how drainage is included in the land surface scheme'),
        ('types', 'ENUM:drainage_types', '0.N',
            'Different types of runoff represented by the land surface model'),
    ]
}

# --------------------------------------------------------------------
# SUB-PROCESS: Heat treatment
# --------------------------------------------------------------------
DETAILS['heat_treatment'] = {
    'description': 'Soil heat treatment',
    'properties': [
        ('description', 'l-str', '1.1',
             'General description of how heat treatment properties are defined'),
        ('time_step', 'int', '1.1',
             'Time step of soil heat scheme in seconds'),                
        ('tiling', 'l-str', '0.1',
             'Describe the soil heat treatment tiling, if any.'),
        ('vertical_discretisation', 'l-str' , '1.1',
             'Describe the typical vertical discretisation'),
        ('heat_storage', 'ENUM:heat_storage_types', '1.1',
             'Specify the method of heat storage'),
        ('processes', 'ENUM:heat_treatment_process_types', '1.N',
             'Describe processes included in the treatment of soil heat'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['lateral_connectivity_types'] = {
    'description': 'Describe the lateral connectivity between tiles',
    'is_open': True,
    'members': [
        ('perfect connectivity', 'Common soil for multiple tiles'),
        ('Darcian flow', 'Darcian flow among hillslope tiles'),
    ]
}

ENUMERATIONS['drainage_types'] = {
    'description': 'Different types of runoff represented by the land surface model',
    'is_open': True,
    'members': [
        ('Gravity drainage', None),
        ('Horton mechanism', None),
        ('topmodel-based', None),
        ('Dunne mechanism', None),
        ('Lateral subsurface flow', None),
        ('Baseflow from groundwater', None),
    ]
}

ENUMERATIONS['water_storage_method_types'] = {
    'description': 'Describe the method by which water is stored in the land surface scheme/model',
    'is_open': True,
    'members': [
        ('Bucket', None),
        ('Force-restore', None),
        ('Choisnel', None),
        ('Explicit diffusion', None),
        ]
    }

ENUMERATIONS['heat_storage_types'] = {
    'description': 'Method of heat storage',
    'is_open': True,
    'members': [
        ('Force-restore', None),
        ('Explicit diffusion', None),
        ]
    }

ENUMERATIONS['heat_treatment_process_types'] = {
    'description': 'Processes included in the treatment of soil heat',
    'is_open': True,
    'members': [
        ('soil moisture freeze-thaw', None),
        ('coupling with snow temperature', None),
    ]
}
    
ENUMERATIONS['snow_free_albedo_function_types'] = {
    'description': 'Describe the dependancies on snow free albedo calculations',
    'is_open': True,
    'members': [
        ('vegetation type', None),
        ('soil humidity', None),
        ('vegetation state', None),        
    ]
}
    
ENUMERATIONS['direct_diffuse_types'] = {
    'description': 'Describe the distinction between direct and diffuse albedo',
    'is_open': True,
    'members': [
        ('distinction between direct and diffuse albedo', None),
        ('no distinction between direct and diffuse albedo', None),        
    ]
}
    
