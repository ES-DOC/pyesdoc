"""
.. module:: cim.v1.types.grids.grid_tile.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-14 19:01:08.061348.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.grids.discretization_enum import DiscretizationEnum
from pyesdoc.ontologies.cim.v1.types.grids.grid_extent import GridExtent
from pyesdoc.ontologies.cim.v1.types.grids.geometry_type_enum import GeometryTypeEnum
from pyesdoc.ontologies.cim.v1.types.grids.grid_tile_resolution_type import GridTileResolutionType
from pyesdoc.ontologies.cim.v1.types.grids.refinement_type_enum import RefinementTypeEnum
from pyesdoc.ontologies.cim.v1.types.grids.vertical_coordinate_list import VerticalCoordinateList


class GridTile(object):
    """A concrete class within the cim v1 type system.

    The GridTile class is used to model an individual grid tile contained within a grid mosaic. A GridTile consists of an array of grid cells which may be defined in one of four ways: 1) for simple grids, by use of the SimpleGridGeometry data type; 2) by defining an array of GridCell objects; 3) by specifying an array of references to externally defined GridCell objects; or 4) by specifying a URI to a remote data file containing the grid cell definitions.  For all but the simplest grid tiles, it is envisaged that method 4 above will be the most frequently used option. However, it should be remembered that the CIM is primarily concerned with encoding climate model metadata. Specifying the coordinates of individual grid tiles and cells will most likely not be required as part of such metadata descriptions.  A GridTile object is associated with a geodetic or projected CRS via the horizontalCRS property, and with a vertical CRS via the verticalCRS property.
    """

    def __init__(self):
        """Constructor"""
        super(GridTile, self).__init__()
        self.area = str()                            # type = str
        self.cell_array = str()                      # type = str
        self.cell_ref_array = str()                  # type = str
        self.coord_file = str()                      # type = str
        self.coordinate_pole = str()                 # type = str
        self.description = str()                     # type = str
        self.discretization_type = ''                # type = grids.DiscretizationEnum
        self.extent = None                           # type = grids.GridExtent
        self.geometry_type = ''                      # type = grids.GeometryTypeEnum
        self.grid_north_pole = str()                 # type = str
        self.horizontal_crs = str()                  # type = str
        self.horizontal_resolution = None            # type = grids.GridTileResolutionType
        self.id = str()                              # type = str
        self.is_conformal = bool()                   # type = bool
        self.is_regular = bool()                     # type = bool
        self.is_terrain_following = bool()           # type = bool
        self.is_uniform = bool()                     # type = bool
        self.long_name = str()                       # type = str
        self.mnemonic = str()                        # type = str
        self.nx = int()                              # type = int
        self.ny = int()                              # type = int
        self.nz = int()                              # type = int
        self.refinement_scheme = ''                  # type = grids.RefinementTypeEnum
        self.short_name = str()                      # type = str
        self.simple_grid_geom = str()                # type = str
        self.vertical_crs = str()                    # type = str
        self.vertical_resolution = None              # type = grids.GridTileResolutionType
        self.zcoords = None                          # type = grids.VerticalCoordinateList


    def as_dict(self):
        """Returns a deep dictionary representation.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'area', self.area, False, True, False)
        append(d, 'cell_array', self.cell_array, False, True, False)
        append(d, 'cell_ref_array', self.cell_ref_array, False, True, False)
        append(d, 'coord_file', self.coord_file, False, True, False)
        append(d, 'coordinate_pole', self.coordinate_pole, False, True, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'discretization_type', self.discretization_type, False, False, True)
        append(d, 'extent', self.extent, False, False, False)
        append(d, 'geometry_type', self.geometry_type, False, False, True)
        append(d, 'grid_north_pole', self.grid_north_pole, False, True, False)
        append(d, 'horizontal_crs', self.horizontal_crs, False, True, False)
        append(d, 'horizontal_resolution', self.horizontal_resolution, False, False, False)
        append(d, 'id', self.id, False, True, False)
        append(d, 'is_conformal', self.is_conformal, False, True, False)
        append(d, 'is_regular', self.is_regular, False, True, False)
        append(d, 'is_terrain_following', self.is_terrain_following, False, True, False)
        append(d, 'is_uniform', self.is_uniform, False, True, False)
        append(d, 'long_name', self.long_name, False, True, False)
        append(d, 'mnemonic', self.mnemonic, False, True, False)
        append(d, 'nx', self.nx, False, True, False)
        append(d, 'ny', self.ny, False, True, False)
        append(d, 'nz', self.nz, False, True, False)
        append(d, 'refinement_scheme', self.refinement_scheme, False, False, True)
        append(d, 'short_name', self.short_name, False, True, False)
        append(d, 'simple_grid_geom', self.simple_grid_geom, False, True, False)
        append(d, 'vertical_crs', self.vertical_crs, False, True, False)
        append(d, 'vertical_resolution', self.vertical_resolution, False, False, False)
        append(d, 'zcoords', self.zcoords, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

