# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.decoder_for_grids_package.py

   :copyright: @2014 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A set of cim 1 decoders.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2014-05-06 19:21:26.910477.

"""

# Module imports.
from decoder_xml_utils import set_attributes
from decoder_for_shared_package import *
import typeset



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
        ('maximum_latitude', False, 'str', 'child::cim:latMax'),
        ('maximum_longitude', False, 'str', 'child::cim:lonMax'),
        ('minimum_latitude', False, 'str', 'child::cim:latMin'),
        ('minimum_longitude', False, 'str', 'child::cim:lonMin'),
        ('units', False, 'str', 'child::cim:units'),
    ]

    return set_attributes(typeset.grids.GridExtent(), xml, nsmap, decodings)


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
        ('citations', True, decode_citation, 'child::cim:citationList/cim:citation'),
        ('description', False, 'str', 'child::cim:description'),
        ('has_congruent_tiles', False, 'bool', '@congruentTiles'),
        ('id', False, 'str', '@id'),
        ('is_leaf', False, 'bool', '@isLeaf'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('mnemonic', False, 'str', 'child::cim:mnemonic'),
        ('mosaic_count', False, 'int', '@numMosaics'),
        ('mosaics', True, decode_grid_mosaic, 'child::cim:gridMosaic'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('tile_count', False, 'int', '@numTiles'),
        ('tiles', True, decode_grid_tile, 'child::cim:gridTile'),
        ('type', False, 'str', '@gridType'),
    ]

    return set_attributes(typeset.grids.GridMosaic(), xml, nsmap, decodings)


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
        ('esm_exchange_grids', True, decode_grid_mosaic, 'child::cim:esmExchangeGrid'),
        ('esm_model_grids', True, decode_grid_mosaic, 'child::cim:esmModelGrid'),
        ('meta', False, decode_doc_meta_info, 'self::cim:gridSpec'),
    ]

    return set_attributes(typeset.grids.GridSpec(), xml, nsmap, decodings)


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
        ('description', False, 'str', 'child::cim:description'),
        ('discretization_type', False, 'str', '@discretizationType'),
        ('extent', False, decode_grid_extent, 'child::cim:extent'),
        ('geometry_type', False, 'str', '@geometryType'),
        ('horizontal_resolution', False, decode_grid_tile_resolution_type, 'child::cim:horizontalResolution'),
        ('id', False, 'str', '@id'),
        ('is_conformal', False, 'bool', '@isConformal'),
        ('is_regular', False, 'bool', '@isRegular'),
        ('is_terrain_following', False, 'bool', '@isTerrainFollowing'),
        ('is_uniform', False, 'bool', '@isUniform'),
        ('long_name', False, 'str', 'child::cim:longName'),
        ('mnemonic', False, 'str', 'child::cim:mnemonic'),
        ('nx', False, 'int', '@nx'),
        ('ny', False, 'int', '@ny'),
        ('nz', False, 'int', '@nz'),
        ('refinement_scheme', False, 'str', '@refinementScheme'),
        ('short_name', False, 'str', 'child::cim:shortName'),
        ('vertical_resolution', False, decode_grid_tile_resolution_type, 'child::cim:verticalResolution'),
        ('zcoords', False, decode_vertical_coordinate_list, 'child::cim:zcoords'),
    ]

    return set_attributes(typeset.grids.GridTile(), xml, nsmap, decodings)


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
        ('form', False, 'str', '@coordinateForm'),
        ('has_constant_offset', False, 'bool', '@hasConstantOffset'),
        ('length', False, 'int', '@length'),
        ('properties', True, decode_grid_property, 'child::cim:property'),
        ('type', False, 'str', '@coordinateType'),
        ('uom', False, 'str', '@uom'),
    ]

    return set_attributes(typeset.grids.VerticalCoordinateList(), xml, nsmap, decodings)


