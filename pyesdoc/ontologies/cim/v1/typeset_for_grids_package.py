"""
.. module:: cim.v1.typeset_for_grids_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.grids package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class CoordinateList(object):
    """A concrete class within the cim v1 type system.

    The CoordList type may be used to specify a list of coordinates, typically for the purpose of defining coordinates along the X, Y or Z axes. The length of the coordinate list is given by the attribute of that name. This may be used by software to allocate memory in advance of storing the coordinate values. The hasConstantOffset attribute may be used to indicate that the coordinate list consists of values with constant offset (spacing). In this case only the first coordinate value and the offset (spacing) value need to be specified; however, the length attribute must still define the final as-built size of the coordinate list.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(CoordinateList, self).__init__()

        self.has_constant_offset = None                   # bool (0.1)
        self.length = None                                # int (0.1)
        self.uom = None                                   # unicode (0.1)


class GridExtent(object):
    """A concrete class within the cim v1 type system.

    DataType for recording the geographic extent of a gridMosaic or gridTile.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(GridExtent, self).__init__()

        self.maximum_latitude = None                      # unicode (1.1)
        self.maximum_longitude = None                     # unicode (1.1)
        self.minimum_latitude = None                      # unicode (1.1)
        self.minimum_longitude = None                     # unicode (1.1)
        self.units = None                                 # unicode (0.1)


class GridMosaic(object):
    """A concrete class within the cim v1 type system.

    The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(GridMosaic, self).__init__()

        self.citations = []                               # shared.Citation (0.N)
        self.description = None                           # unicode (0.1)
        self.extent = None                                # grids.GridExtent (0.1)
        self.has_congruent_tiles = None                   # bool (0.1)
        self.id = None                                    # unicode (1.1)
        self.is_leaf = None                               # bool (1.1)
        self.long_name = None                             # unicode (0.1)
        self.mnemonic = None                              # unicode (0.1)
        self.mosaic_count = None                          # int (0.1)
        self.mosaics = []                                 # grids.GridMosaic (0.N)
        self.short_name = None                            # unicode (1.1)
        self.tile_count = None                            # int (0.1)
        self.tiles = []                                   # grids.GridTile (0.N)
        self.type = None                                  # unicode (1.1)


class GridProperty(shared.Property):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of grid_property class.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(GridProperty, self).__init__()



class GridSpec(object):
    """A concrete class within the cim v1 type system.

    This is a container class for GridSpec objects. A GridSpec object can contain one or more esmModelGrid objects, and one or more esmExchangeGrid objects. These objects may be serialised to one or possibly several files according to taste. Since GridSpec is sub-typed from GML's AbstractGeometryType it can, and should, be identified using a gml:id attribute.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(GridSpec, self).__init__()

        self.esm_exchange_grids = []                      # grids.GridMosaic (0.N)
        self.esm_model_grids = []                         # grids.GridMosaic (0.N)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)


class GridTile(object):
    """A concrete class within the cim v1 type system.

    The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(GridTile, self).__init__()

        self.area = None                                  # unicode (0.1)
        self.cell_array = None                            # unicode (0.1)
        self.cell_ref_array = None                        # unicode (0.1)
        self.coord_file = None                            # unicode (0.1)
        self.coordinate_pole = None                       # unicode (0.1)
        self.description = None                           # unicode (0.1)
        self.discretization_type = None                   # grids.DiscretizationEnum (0.1)
        self.extent = None                                # grids.GridExtent (0.1)
        self.geometry_type = None                         # grids.GeometryTypeEnum (0.1)
        self.grid_north_pole = None                       # unicode (0.1)
        self.horizontal_crs = None                        # unicode (0.1)
        self.horizontal_resolution = None                 # grids.GridTileResolutionType (0.1)
        self.id = None                                    # unicode (0.1)
        self.is_conformal = None                          # bool (0.1)
        self.is_regular = None                            # bool (0.1)
        self.is_terrain_following = None                  # bool (0.1)
        self.is_uniform = None                            # bool (0.1)
        self.long_name = None                             # unicode (0.1)
        self.mnemonic = None                              # unicode (0.1)
        self.nx = None                                    # int (0.1)
        self.ny = None                                    # int (0.1)
        self.nz = None                                    # int (0.1)
        self.refinement_scheme = None                     # grids.RefinementTypeEnum (0.1)
        self.short_name = None                            # unicode (0.1)
        self.simple_grid_geom = None                      # grids.SimpleGridGeometry (0.1)
        self.vertical_crs = None                          # unicode (0.1)
        self.vertical_resolution = None                   # grids.GridTileResolutionType (0.1)
        self.zcoords = None                               # grids.VerticalCoordinateList (0.1)


class GridTileResolutionType(object):
    """A concrete class within the cim v1 type system.

    Provides a description and set of named properties for the horizontal or vertical resolution.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(GridTileResolutionType, self).__init__()

        self.description = None                           # unicode (0.1)
        self.properties = []                              # grids.GridProperty (0.N)


class SimpleGridGeometry(object):
    """A concrete class within the cim v1 type system.

    SimpleGridGeometry:This property may be used to define the coordinates of the nodes or cells making up a simple (i.e. uniform or regular) grid tile. More details are provided in the description of the SimpleGridGeometry data type.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SimpleGridGeometry, self).__init__()

        self.dim_order = None                             # unicode (0.1)
        self.is_mesh = None                               # bool (0.1)
        self.num_dims = None                              # int (1.1)
        self.xcoords = None                               # grids.CoordinateList (1.1)
        self.ycoords = None                               # grids.CoordinateList (1.1)
        self.zcoords = None                               # grids.CoordinateList (0.1)


class VerticalCoordinateList(CoordinateList):
    """A concrete class within the cim v1 type system.

    There are some specific attributes that are associated with vertical coordinates.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(VerticalCoordinateList, self).__init__()

        self.form = None                                  # unicode (0.1)
        self.properties = []                              # grids.GridProperty (0.N)
        self.type = None                                  # unicode (0.1)


class ArcTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of arc_type_enum enum.
    """
    is_open = False
    members = [
        "geodesic",
        "great_circle",
        "small_circle",
        "complex"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None"
        ]


class DiscretizationEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of discretization_enum enum.
    """
    is_open = False
    members = [
        "logically_rectangular",
        "structured_triangular",
        "unstructured_triangular",
        "pixel-based_catchment",
        "unstructured_polygonal",
        "spherical_harmonics",
        "other"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None"
        ]


class FeatureTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of feature_type_enum enum.
    """
    is_open = False
    members = [
        "point",
        "edge"
        ]
    descriptions = [
        "None",
        "None"
        ]


class GeometryTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of geometry_type_enum enum.
    """
    is_open = False
    members = [
        "ellipsoid",
        "plane",
        "sphere"
        ]
    descriptions = [
        "None",
        "None",
        "None"
        ]


class GridNodePositionEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of grid_node_position_enum enum.
    """
    is_open = False
    members = [
        "centre",
        "plane",
        "sphere"
        ]
    descriptions = [
        "None",
        "None",
        "None"
        ]


class GridTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of grid_type_enum enum.
    """
    is_open = False
    members = [
        "cubed_sphere",
        "displaced_pole",
        "icosahedral_geodesic",
        "reduced_gaussian",
        "regular_lat_lon",
        "spectral_gaussian",
        "tripolar",
        "yin_yang",
        "composite",
        "other"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None",
        "None"
        ]


class HorizontalCsEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of horizontal_cs_enum enum.
    """
    is_open = False
    members = [
        "cartesian",
        "ellipsoidal",
        "polar",
        "spherical"
        ]
    descriptions = [
        "None",
        "None",
        "None",
        "None"
        ]


class RefinementTypeEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of refinement_type_enum enum.
    """
    is_open = False
    members = [
        "none",
        "integer",
        "rational"
        ]
    descriptions = [
        "Tile boundaries have no refinement when the grid lines meeting at the tile boundary are continuous.",
        "The refinement is integer when grid lines from the coarser grid are continuous on the finer grid, but not vice versa.",
        "The refinement is rational when the adjacent or overlapping grid tiles have grid line counts that are coprime (i.e. no common factor other than 1)."
        ]


class VerticalCsEnum(object):
    """An enumeration within the cim v1 type system.

    Creates and returns instance of vertical_cs_enum enum.
    """
    is_open = False
    members = [
        "mass-based",
        "space-based"
        ]
    descriptions = [
        "None",
        "None"
        ]


