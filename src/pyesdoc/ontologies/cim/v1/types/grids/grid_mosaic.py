"""
.. module:: cim.v1.types.grids.grid_mosaic.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.239090.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.shared.citation import Citation
from pyesdoc.ontologies.cim.v1.types.grids.grid_extent import GridExtent
from pyesdoc.ontologies.cim.v1.types.grids.grid_tile import GridTile


class GridMosaic(object):
    """A concrete class within the cim v1 type system.

    The GridMosaic class is used to define the geometry properties of an earth system model grid or an exchange grid. Such a grid definition may then be referenced by any number of earth system models. A GridMosaic object consists either of 1 or more child GridMosaics, or one or more child GridTiles, but not both. In the latter case the isLeaf property should be set to true, indicating that the mosaic is a leaf mosaic.
    """

    def __init__(self):
        """Constructor"""
        super(GridMosaic, self).__init__()
        self.citations = []                          # type = shared.Citation
        self.description = str()                     # type = str
        self.extent = None                           # type = grids.GridExtent
        self.has_congruent_tiles = bool()            # type = bool
        self.id = str()                              # type = str
        self.is_leaf = bool()                        # type = bool
        self.long_name = str()                       # type = str
        self.mnemonic = str()                        # type = str
        self.mosaic_count = int()                    # type = int
        self.mosaics = []                            # type = grids.GridMosaic
        self.short_name = str()                      # type = str
        self.tile_count = int()                      # type = int
        self.tiles = []                              # type = grids.GridTile
        self.type = str()                            # type = str


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
        append(d, 'citations', self.citations, True, False, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'extent', self.extent, False, False, False)
        append(d, 'has_congruent_tiles', self.has_congruent_tiles, False, True, False)
        append(d, 'id', self.id, False, True, False)
        append(d, 'is_leaf', self.is_leaf, False, True, False)
        append(d, 'long_name', self.long_name, False, True, False)
        append(d, 'mnemonic', self.mnemonic, False, True, False)
        append(d, 'mosaic_count', self.mosaic_count, False, True, False)
        append(d, 'mosaics', self.mosaics, True, False, False)
        append(d, 'short_name', self.short_name, False, True, False)
        append(d, 'tile_count', self.tile_count, False, True, False)
        append(d, 'tiles', self.tiles, True, False, False)
        append(d, 'type', self.type, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

