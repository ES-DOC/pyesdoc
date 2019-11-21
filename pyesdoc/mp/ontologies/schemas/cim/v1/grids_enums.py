"""
.. module:: grids_enums.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 grids package enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""


def arc_type_enum():
    """Creates and returns instance of arc_type_enum enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('geodesic', None),
            ('great_circle', None),
            ('small_circle', None),
            ('complex', None)
        ],
    }


def discretization_enum():
    """Creates and returns instance of discretization_enum enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('logically_rectangular', None),
            ('structured_triangular', None),
            ('unstructured_triangular', None),
            ('pixel-based_catchment', None),
            ('unstructured_polygonal', None),
            ('spherical_harmonics', None),
            ('other', None)
        ],
    }


def feature_type_enum():
    """Creates and returns instance of feature_type_enum enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('point', None),
            ('edge', None)
        ],
    }


def geometry_type_enum():
    """Creates and returns instance of geometry_type_enum enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('ellipsoid', None),
            ('plane', None),
            ('sphere', None)
        ],
    }


def grid_node_position_enum():
    """Creates and returns instance of grid_node_position_enum enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('centre', None),
            ('plane', None),
            ('sphere', None)
        ],
    }


def grid_type_enum():
    """Creates and returns instance of grid_type_enum enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('cubed_sphere', None),
            ('displaced_pole', None),
            ('icosahedral_geodesic', None),
            ('reduced_gaussian', None),
            ('regular_lat_lon', None),
            ('spectral_gaussian', None),
            ('tripolar', None),
            ('yin_yang', None),
            ('composite', None),
            ('other', None)
        ],
    }


def horizontal_cs_enum():
    """Creates and returns instance of horizontal_cs_enum enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('cartesian', None),
            ('ellipsoidal', None),
            ('polar', None),
            ('spherical', None)
        ],
    }


def refinement_type_enum():
    """Creates and returns instance of refinement_type_enum enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('none', 'Tile boundaries have no refinement when the grid lines meeting at the tile boundary are continuous.'),
            ('integer', 'The refinement is integer when grid lines from the coarser grid are continuous on the finer grid, but not vice versa.'),
            ('rational','The refinement is rational when the adjacent or overlapping grid tiles have grid line counts that are coprime (i.e. no common factor other than 1).')
        ],
    }


def vertical_cs_enum():
    """Creates and returns instance of vertical_cs_enum enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('mass-based', None),
            ('space-based', None)
        ],
    }
