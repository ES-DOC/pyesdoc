"""
.. module:: cim.v1.decoder_for_grids_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
from decoder_xml_utils import set_attributes
from decoder_for_shared_package import *
import typeset



def decode_coordinate_list(xml, nsmap):
    """Decodes an instance of the following type: coordinate list.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.CoordinateList

    """
    decodings = [
        ('has_constant_offset', False, 'bool', '@hasConstantOffset'),
        ('length', False, 'int', '@length'),
        ('uom', False, 'unicode', '@uom'),
    ]

    return set_attributes(typeset.grids.CoordinateList(), xml, nsmap, decodings)


def decode_grid_extent(xml, nsmap):
    """Decodes an instance of the following type: grid extent.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridExtent

    """
    decodings = [
        ('maximum_latitude', False, 'unicode', 'child::cim:latMax'),
        ('maximum_longitude', False, 'unicode', 'child::cim:lonMax'),
        ('minimum_latitude', False, 'unicode', 'child::cim:latMin'),
        ('minimum_longitude', False, 'unicode', 'child::cim:lonMin'),
        ('units', False, 'unicode', 'child::cim:units'),
    ]

    return set_attributes(typeset.grids.GridExtent(), xml, nsmap, decodings)


def decode_grid_mosaic(xml, nsmap):
    """Decodes an instance of the following type: grid mosaic.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridMosaic

    """
    decodings = [
        ('citations', True, decode_citation, 'child::cim:citationList/cim:citation'),
        ('description', False, 'unicode', 'child::cim:description'),
        ('has_congruent_tiles', False, 'bool', '@congruentTiles'),
        ('id', False, 'unicode', '@id'),
        ('is_leaf', False, 'bool', '@isLeaf'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('mnemonic', False, 'unicode', 'child::cim:mnemonic'),
        ('mosaic_count', False, 'int', '@numMosaics'),
        ('mosaics', True, decode_grid_mosaic, 'child::cim:gridMosaic'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('tile_count', False, 'int', '@numTiles'),
        ('tiles', True, decode_grid_tile, 'child::cim:gridTile'),
        ('type', False, 'unicode', '@gridType'),
    ]

    return set_attributes(typeset.grids.GridMosaic(), xml, nsmap, decodings)


def decode_grid_property(xml, nsmap):
    """Decodes an instance of the following type: grid property.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridProperty

    """
    decodings = [
        ('name', False, 'unicode', 'child::cim:name'),
        ('value', False, 'unicode', 'child::cim:value'),
    ]

    return set_attributes(typeset.grids.GridProperty(), xml, nsmap, decodings)


def decode_grid_spec(xml, nsmap):
    """Decodes an instance of the following type: grid spec.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridSpec

    """
    decodings = [
        ('esm_exchange_grids', True, decode_grid_mosaic, 'child::cim:esmExchangeGrid'),
        ('esm_model_grids', True, decode_grid_mosaic, 'child::cim:esmModelGrid'),
        ('meta', False, decode_doc_meta_info, 'self::cim:gridSpec'),
    ]

    return set_attributes(typeset.grids.GridSpec(), xml, nsmap, decodings)


def decode_grid_tile(xml, nsmap):
    """Decodes an instance of the following type: grid tile.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridTile

    """
    decodings = [
        ('description', False, 'unicode', 'child::cim:description'),
        ('discretization_type', False, 'unicode', '@discretizationType'),
        ('extent', False, decode_grid_extent, 'child::cim:extent'),
        ('geometry_type', False, 'unicode', '@geometryType'),
        ('horizontal_resolution', False, decode_grid_tile_resolution_type, 'child::cim:horizontalResolution'),
        ('id', False, 'unicode', '@id'),
        ('is_conformal', False, 'bool', '@isConformal'),
        ('is_regular', False, 'bool', '@isRegular'),
        ('is_terrain_following', False, 'bool', '@isTerrainFollowing'),
        ('is_uniform', False, 'bool', '@isUniform'),
        ('long_name', False, 'unicode', 'child::cim:longName'),
        ('mnemonic', False, 'unicode', 'child::cim:mnemonic'),
        ('nx', False, 'int', '@nx'),
        ('ny', False, 'int', '@ny'),
        ('nz', False, 'int', '@nz'),
        ('refinement_scheme', False, 'unicode', '@refinementScheme'),
        ('short_name', False, 'unicode', 'child::cim:shortName'),
        ('vertical_resolution', False, decode_grid_tile_resolution_type, 'child::cim:verticalResolution'),
        ('zcoords', False, decode_vertical_coordinate_list, 'child::cim:zcoords'),
    ]

    return set_attributes(typeset.grids.GridTile(), xml, nsmap, decodings)


def decode_grid_tile_resolution_type(xml, nsmap):
    """Decodes an instance of the following type: grid tile resolution type.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridTileResolutionType

    """
    decodings = [
        ('description', False, 'unicode', '@description'),
        ('properties', True, decode_grid_property, 'child::cim:property'),
    ]

    return set_attributes(typeset.grids.GridTileResolutionType(), xml, nsmap, decodings)


def decode_simple_grid_geometry(xml, nsmap):
    """Decodes an instance of the following type: simple grid geometry.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.SimpleGridGeometry

    """
    decodings = [
    ]

    return set_attributes(typeset.grids.SimpleGridGeometry(), xml, nsmap, decodings)


def decode_vertical_coordinate_list(xml, nsmap):
    """Decodes an instance of the following type: vertical coordinate list.

    :param lxml.etree xml: XML from which type is to be decoded.
    :param dict nsmap: XML namespace mappings.

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.VerticalCoordinateList

    """
    decodings = [
        ('form', False, 'unicode', '@coordinateForm'),
        ('has_constant_offset', False, 'bool', '@hasConstantOffset'),
        ('length', False, 'int', '@length'),
        ('properties', True, decode_grid_property, 'child::cim:property'),
        ('type', False, 'unicode', '@coordinateType'),
        ('uom', False, 'unicode', '@uom'),
    ]

    return set_attributes(typeset.grids.VerticalCoordinateList(), xml, nsmap, decodings)


