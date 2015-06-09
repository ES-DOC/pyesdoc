# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.decoder_for_grids_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 15:44:25.775858.

"""
from decoder_xml_utils import set_attributes
from decoder_for_shared_package import *
import typeset



def decode_grid_spec(xml, nsmap):
    """Decodes an instance of the following type: grid spec.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridSpec

    """
    decodings = [
        ('esm_model_grids', True, decode_grid_mosaic, 'child::cim:esmModelGrid'),
        ('meta', False, decode_doc_meta_info, 'self::cim:gridSpec'),
        ('esm_exchange_grids', True, decode_grid_mosaic, 'child::cim:esmExchangeGrid'),
    ]

    return set_attributes(typeset.grids.GridSpec(), xml, nsmap, decodings)


def decode_coordinate_list(xml, nsmap):
    """Decodes an instance of the following type: coordinate list.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.CoordinateList

    """
    decodings = [
        ('has_constant_offset', False, 'bool', '@hasConstantOffset'),
        ('length', False, 'int', '@length'),
        ('uom', False, 'str', '@uom'),
    ]

    return set_attributes(typeset.grids.CoordinateList(), xml, nsmap, decodings)


def decode_vertical_coordinate_list(xml, nsmap):
    """Decodes an instance of the following type: vertical coordinate list.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.VerticalCoordinateList

    """
    decodings = [
        ('length', False, 'int', '@length'),
        ('form', False, 'str', '@coordinateForm'),
        ('has_constant_offset', False, 'bool', '@hasConstantOffset'),
        ('type', False, 'str', '@coordinateType'),
        ('properties', True, decode_grid_property, 'child::cim:property'),
        ('uom', False, 'str', '@uom'),
    ]

    return set_attributes(typeset.grids.VerticalCoordinateList(), xml, nsmap, decodings)


def decode_grid_tile_resolution_type(xml, nsmap):
    """Decodes an instance of the following type: grid tile resolution type.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridTileResolutionType

    """
    decodings = [
        ('description', False, 'str', '@description'),
        ('properties', True, decode_grid_property, 'child::cim:property'),
    ]

    return set_attributes(typeset.grids.GridTileResolutionType(), xml, nsmap, decodings)


def decode_grid_tile(xml, nsmap):
    """Decodes an instance of the following type: grid tile.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridTile

    """
    decodings = [
        ('mnemonic', False, 'str', 'child::cim:mnemonic'),
        ('horizontal_resolution', False, decode_grid_tile_resolution_type, 'child::cim:horizontalResolution'),
        ('zcoords', False, decode_vertical_coordinate_list, 'child::cim:zcoords'),
        ('nx', False, 'int', '@nx'),
        ('discretization_type', False, 'str', '@discretizationType'),
        ('ny', False, 'int', '@ny'),
        ('is_conformal', False, 'bool', '@isConformal'),
        ('is_terrain_following', False, 'bool', '@isTerrainFollowing'),
        ('nz', False, 'int', '@nz'),
        ('refinement_scheme', False, 'str', '@refinementScheme'),
        ('description', False, 'str', 'child::cim:description'),
        ('id', False, 'str', '@id'),
        ('is_regular', False, 'bool', '@isRegular'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('is_uniform', False, 'bool', '@isUniform'),
        ('extent', False, decode_grid_extent, 'child::cim:extent'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('geometry_type', False, 'str', '@geometryType'),
        ('vertical_resolution', False, decode_grid_tile_resolution_type, 'child::cim:verticalResolution'),
    ]

    return set_attributes(typeset.grids.GridTile(), xml, nsmap, decodings)


def decode_grid_property(xml, nsmap):
    """Decodes an instance of the following type: grid property.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridProperty

    """
    decodings = [
        ('name', False, 'str', 'child::cim:name'),
        ('value', False, 'str', 'child::cim:value'),
    ]

    return set_attributes(typeset.grids.GridProperty(), xml, nsmap, decodings)


def decode_grid_mosaic(xml, nsmap):
    """Decodes an instance of the following type: grid mosaic.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridMosaic

    """
    decodings = [
        ('is_leaf', False, 'bool', '@isLeaf'),
        ('description', False, 'str', 'child::cim:description'),
        ('has_congruent_tiles', False, 'bool', '@congruentTiles'),
        ('tile_count', False, 'int', '@numTiles'),
        ('type', False, 'str', '@gridType'),
        ('tiles', True, decode_grid_tile, 'child::cim:gridTile'),
        ('mnemonic', False, 'str', 'child::cim:mnemonic'),
        ('citations', True, decode_citation, 'child::cim:citationList/cim:citation'),
        ('id', False, 'str', '@id'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('mosaic_count', False, 'int', '@numMosaics'),
        ('mosaics', True, decode_grid_mosaic, 'child::cim:gridMosaic'),
    ]

    return set_attributes(typeset.grids.GridMosaic(), xml, nsmap, decodings)


def decode_grid_extent(xml, nsmap):
    """Decodes an instance of the following type: grid extent.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.GridExtent

    """
    decodings = [
        ('maximum_longitude', False, 'str', 'child::cim:lonMax'),
        ('minimum_longitude', False, 'str', 'child::cim:lonMin'),
        ('minimum_latitude', False, 'str', 'child::cim:latMin'),
        ('units', False, 'str', 'child::cim:units'),
        ('maximum_latitude', False, 'str', 'child::cim:latMax'),
    ]

    return set_attributes(typeset.grids.GridExtent(), xml, nsmap, decodings)


def decode_simple_grid_geometry(xml, nsmap):
    """Decodes an instance of the following type: simple grid geometry.

    :param xml: XML from which type is to be decoded.
    :type xml: lxml.etree

    :param nsmap: XML namespace mappings.
    :type nsmap: dict

    :returns: A decoded type instance.
    :rtype: cim.v1.typeset.grids.SimpleGridGeometry

    """
    decodings = [
    ]

    return set_attributes(typeset.grids.SimpleGridGeometry(), xml, nsmap, decodings)


