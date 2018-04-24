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
DESCRIPTION = 'Ocean Timestepping Framework'

# --------------------------------------------------------------------
# PROCESS: top level
# --------------------------------------------------------------------

DETAILS['toplevel'] = {
    'description': 'Properties of time stepping in ocean',
    'properties': [
        ('diurnal_cycle', 'ENUM:diurnal_cycle_types', '1.1',
            'Diurnal cycle type'),
        ]
    }

# Tracers time stepping
DETAILS['toplevel:tracers'] = {
    'description': 'Properties of tracers time stepping in ocean',
    'properties': [
        ('scheme', 'ENUM:ocean_timestepping_types', '1.1',
            'Tracers time stepping scheme'),
        ('time_step', 'int', '1.1',
            'Tracers time step (in seconds)'),
        ]
    }

# Baroclinic dynamics
DETAILS['toplevel:baroclinic_dynamics'] = {
    'description': 'Baroclinic dynamics in ocean',
    'properties': [
        ('type', 'ENUM:baroclinic_types', '1.1',
            'Baroclinic dynamics type'),
        ('scheme', 'ENUM:ocean_timestepping_types', '1.1',
            'Baroclinic dynamics scheme'),
        ('time_step', 'int', '0.1',
            'Baroclinic time step (in seconds)'),
        ]
    }

# Barotropic
DETAILS['toplevel:barotropic'] = {
    'description': 'Barotropic time stepping in ocean',
    'properties': [
        ('splitting', 'ENUM:barotropic_splitting_methods', '1.1',
            'Time splitting method'),
        ('time_step', 'int', '0.1',
            'Barotropic time step (in seconds)'),
        ]
    }

# Vertical
DETAILS['toplevel:vertical_physics'] = {
    'description': 'Vertical physics time stepping in ocean',
    'properties': [
        ('method', 'str', '1.1',
            'Details of vertical time stepping in ocean'),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['diurnal_cycle_types'] = {
    'description': 'Types of diurnal cycle resolution in ocean',
    'is_open': True,
    'members': [
        ('None', 'No diurnal cycle in ocean'),
        ('Via coupling', 'Diurnal cycle via coupling frequency'),
        ('Specific treatment', 'Specific treament'),
        ]
    }

ENUMERATIONS['ocean_timestepping_types'] = {
    'description': 'Type of timestepping scheme in ocean',
    'is_open': True,
    'members': [
        ('Leap-frog + Asselin filter', 'Leap-frog scheme with Asselin filter'),
        ('Leap-frog + Periodic Euler', 'Leap-frog scheme with Periodic Euler'),
        ('Predictor-corrector', 'Predictor-corrector scheme'),
        ('Runge-Kutta 2','Runge-Kutta 2 scheme'),
        ('AM3-LF', 'AM3-LF such as used in ROMS'),
        ('Forward-backward', 'Forward-backward scheme'),
        ('Forward operator', 'Forward operator scheme')
        ]
    }

ENUMERATIONS['baroclinic_types'] = {
    'description': 'Type of baroclinic dynamics in ocean',
    'is_open': True,
    'members': [
        ('Preconditioned conjugate gradient', None),
        ('Sub cyling', 'Sub cycling relative to tracers'),
        ]
    }

ENUMERATIONS['barotropic_splitting_methods'] = {
    'description': 'Methods for time splitting in ocean',
    'is_open': True,
    'members': [
        ('None', None),
        ('split explicit', None),
        ('implicit', None),
        ]
    }
