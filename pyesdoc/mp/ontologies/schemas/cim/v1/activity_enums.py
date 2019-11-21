"""
.. module:: activity_enums.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 activity package enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def conformance_type():
    """Creates and returns instance of conformance_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('not-xxx', None),
            ('not conformant', 'Describes a simulation that is purpefully non-conformant to an experimental requirement.'),
            ('standard config', 'Describes a simulation that is naturally conformant to an experimental requirement.'),
            ('via inputs', 'Describes a simulation that conforms to an experimental requirement by using particular inputs.'),
            ('via model mods', 'Describes a simulation that conforms to an experimental requirement by changing the configuration of the software model implementing that simulation.'),
            ('combination', 'Describes a simulation that conforms to an experimental requirement by using more than one method.'),
        ],
    }


def downscaling_type():
    """Creates and returns instance of downscaling_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('statistical', None),
            ('dynamic', None),
        ],
    }


def ensemble_type():
    """Creates and returns instance of ensemble_type enum.

    """
    return {
        'type': 'enum',
        'is_open': True,
        'members': [],
    }


def experiment_relationship_type():
    """Creates and returns instance of experiment_relationship_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('previousRealisation', None),
            ('continuationOf', None),
            ('controlExperiment', None),
            ('higherResolutionVersionOf', None),
            ('lowerResolutionVersionOf', None),
            ('increaseEnsembleOf', None),
            ('modifiedInputMethodOf', None),
            ('shorterVersionOf', None),
            ('extensionOf', None),
        ],
    }


def frequency_type():
    """Creates and returns instance of frequency_type enum.

    """
    return {
        'type': 'enum',
        'is_open': True,
        'members': [],
    }


def project_type():
    """Creates and returns instance of project_type enum.

    """
    return {
        'type': 'enum',
        'is_open': True,
        'members': [],
    }


def resolution_type():
    """Creates and returns instance of resolution_type enum.

    """
    return {
        'type': 'enum',
        'is_open': True,
        'members': [],
    }


def simulation_relationship_type():
    """Creates and returns instance of simulation_relationship_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('extensionOf', None),
            ('responseTo', None),
            ('continuationOf', None),
            ('previousSimulation', None),
            ('higherResolutionVersionOf', None),
            ('lowerResolutionVersionOf', None),
            ('fixedVersionOf', None),
            ('followingSimulation', None),
        ],
    }


def simulation_type():
    """Creates and returns instance of simulation_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('simulationRun', None),
            ('assimilation', None),
            ('simulationComposite', None),
        ],
    }
