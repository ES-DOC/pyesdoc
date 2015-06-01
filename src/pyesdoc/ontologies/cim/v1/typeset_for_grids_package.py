# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_grids_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.grids package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-01 16:50:10.360525.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class CoordinateList(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of coordinate_list class.

    """
    def __init__(self):
        """Constructor.

        """
        super(CoordinateList, self).__init__()

        self.has_constant_offset = None                   # bool
        self.length = None                                # int
        self.uom = None                                   # str


class GridExtent(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of grid_extent class.

    """
    def __init__(self):
        """Constructor.

        """
        super(GridExtent, self).__init__()

        self.maximum_latitude = None                      # str
        self.maximum_longitude = None                     # str
        self.minimum_latitude = None                      # str
        self.minimum_longitude = None                     # str
        self.units = None                                 # str


class GridMosaic(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of grid_mosaic class.

    """
    def __init__(self):
        """Constructor.

        """
        super(GridMosaic, self).__init__()

        self.citations = []                               # shared.Citation
        self.description = None                           # str
        self.extent = None                                # grids.GridExtent
        self.has_congruent_tiles = None                   # bool
        self.id = None                                    # str
        self.is_leaf = None                               # bool
        self.long_name = None                             # str
        self.mnemonic = None                              # str
        self.mosaic_count = None                          # int
        self.mosaics = []                                 # grids.GridMosaic
        self.short_name = None                            # str
        self.tile_count = None                            # int
        self.tiles = []                                   # grids.GridTile
        self.type = None                                  # str


class GridProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of grid_property class.

    """
    def __init__(self):
        """Constructor.

        """
        super(GridProperty, self).__init__()



class GridSpec(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of grid_spec class.

    """
    def __init__(self):
        """Constructor.

        """
        super(GridSpec, self).__init__()

        self.esm_exchange_grids = []                      # grids.GridMosaic
        self.esm_model_grids = []                         # grids.GridMosaic
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo


class GridTile(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of grid_tile class.

    """
    def __init__(self):
        """Constructor.

        """
        super(GridTile, self).__init__()

        self.area = None                                  # str
        self.cell_array = None                            # str
        self.cell_ref_array = None                        # str
        self.coord_file = None                            # str
        self.coordinate_pole = None                       # str
        self.description = None                           # str
        self.discretization_type = None                   # grids.DiscretizationEnum
        self.extent = None                                # grids.GridExtent
        self.geometry_type = None                         # grids.GeometryTypeEnum
        self.grid_north_pole = None                       # str
        self.horizontal_crs = None                        # str
        self.horizontal_resolution = None                 # grids.GridTileResolutionType
        self.id = None                                    # str
        self.is_conformal = None                          # bool
        self.is_regular = None                            # bool
        self.is_terrain_following = None                  # bool
        self.is_uniform = None                            # bool
        self.long_name = None                             # str
        self.mnemonic = None                              # str
        self.nx = None                                    # int
        self.ny = None                                    # int
        self.nz = None                                    # int
        self.refinement_scheme = None                     # grids.RefinementTypeEnum
        self.short_name = None                            # str
        self.simple_grid_geom = None                      # grids.SimpleGridGeometry
        self.vertical_crs = None                          # str
        self.vertical_resolution = None                   # grids.GridTileResolutionType
        self.zcoords = None                               # grids.VerticalCoordinateList


class GridTileResolutionType(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of grid_tile_resolution_type class.

    """
    def __init__(self):
        """Constructor.

        """
        super(GridTileResolutionType, self).__init__()

        self.description = None                           # str
        self.properties = []                              # grids.GridProperty


class SimpleGridGeometry(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of simple_grid_geometry class.

    """
    def __init__(self):
        """Constructor.

        """
        super(SimpleGridGeometry, self).__init__()

        self.dim_order = None                             # str
        self.is_mesh = None                               # bool
        self.num_dims = None                              # int
        self.xcoords = None                               # grids.CoordinateList
        self.ycoords = None                               # grids.CoordinateList
        self.zcoords = None                               # grids.CoordinateList


class VerticalCoordinateList(CoordinateList):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of coordinate_list class.

    """
    def __init__(self):
        """Constructor.

        """
        super(VerticalCoordinateList, self).__init__()

        self.form = None                                  # str
        self.properties = []                              # grids.GridProperty
        self.type = None                                  # str


class ArcTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of arc_type_enum enum.
    """

    pass


class DiscretizationEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of discretization_enum enum.
    """

    pass


class FeatureTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of feature_type_enum enum.
    """

    pass


class GeometryTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of geometry_type_enum enum.
    """

    pass


class GridNodePositionEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of grid_node_position_enum enum.
    """

    pass


class GridTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of grid_type_enum enum.
    """

    pass


class HorizontalCsEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of horizontal_cs_enum enum.
    """

    pass


class RefinementTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of refinement_type_enum enum.
    """

    pass


class VerticalCsEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of vertical_cs_enum enum.
    """

    pass


