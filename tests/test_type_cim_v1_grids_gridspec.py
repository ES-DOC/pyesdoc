# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_grids_gridspec.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.GridSpec instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.GridSpec

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Grid Spec"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key

# Test representation file.
DOC_FILE = 'cim.1.grids.GridSpec.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = '56259768-e2b1-11df-aab5-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = arrow.get('2012-04-23 14:59:07.384733').datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_extension_info(ext):
    """Asserts a document's extension information.

    :param object ext: Document extension information.

    """
    tu.assert_str(ext.display_name, "UM N96L38 ATM Grid System")
    tu.assert_str(ext.description, "Met Office Unified Model", True)
    tu.assert_str(ext.full_display_name, "CMIP5 Grid Spec : MOHC - UM N96L38 ATM Grid System")
    tu.assert_int(ext.summary_fields, 2)
    tu.assert_str(ext.summary_fields[0], "UM N96L38 ATM Grid System")
    tu.assert_str(ext.summary_fields[1], "Met Office Unified Model", True)


def _assert_doc_core(doc, is_update):
    """Assert core information."""
    tu.assert_iter(doc.esm_model_grids, 1, cim.v1.GridMosaic)
    g = doc.esm_model_grids[0]
    tu.assert_iter(g.citations, 2, cim.v1.Citation)
    tu.assert_str(g.description, "Specification of the atmosphere", True)
    tu.assert_bool(g.is_leaf, True)
    tu.assert_str(g.long_name, "Met Office Unified Model 192", True)
    tu.assert_str(g.short_name, "UM N96L38 ATM Grid System")
    tu.assert_str(g.type, "regular_lat_lon")


def _assert_doc_tile(doc, is_update):
    """Assert tile information."""
    g = doc.esm_model_grids[0]
    tu.assert_int(g.tile_count, 1)
    tu.assert_iter(g.tiles, 1, cim.v1.GridTile)
    tu.assert_object(g.tiles[0], cim.v1.GridTile)
    t = g.tiles[0]
    tu.assert_str(t.description, "Horizontal properties: The N96", True)
    tu.assert_str(t.discretization_type, "logically_rectangular")
    tu.assert_str(t.mnemonic, "N96")


def _assert_doc_tile_extent(doc, is_update):
    """Assert tile extent information."""
    t = doc.esm_model_grids[0].tiles[0]
    tu.assert_object(t.extent, cim.v1.GridExtent)
    e = t.extent
    tu.assert_int(e.maximum_latitude, 90)
    tu.assert_int(e.minimum_latitude, -90)
    tu.assert_int(e.minimum_longitude, 0)
    tu.assert_int(e.maximum_longitude, 360, int)


def _assert_doc_tile_horizontal_resolution(doc, is_update):
    """Assert tile horizontal resolution."""
    t = doc.esm_model_grids[0].tiles[0]
    tu.assert_object(t.horizontal_resolution, cim.v1.GridTileResolutionType)
    hr = t.horizontal_resolution
    tu.assert_str(hr.description, "1.875 degrees in longitude", True)
    tu.assert_iter(hr.properties, 2, cim.v1.GridProperty)
    p = hr.properties[0]
    tu.assert_str(p.name, "NumberOfLatitudinalGridCells")
    tu.assert_str(p.value, "145")


def _assert_doc_tile_vertical_resolution(doc, is_update):
    """Assert tile vertical resolution."""
    t = doc.esm_model_grids[0].tiles[0]
    tu.assert_object(t.vertical_resolution, cim.v1.GridTileResolutionType)
    vr = t.vertical_resolution
    tu.assert_iter(vr.properties, 4, cim.v1.GridProperty)
    p = vr.properties[0]
    tu.assert_str(p.name, "TopModelLevel")
    tu.assert_str(p.value, "39254.8")


def _assert_doc_tile_zcoords(doc, is_update):
    """Assert tile zcoords information."""
    t = doc.esm_model_grids[0].tiles[0]
    tu.assert_object(t.zcoords, cim.v1.VerticalCoordinateList)
    z = t.zcoords
    tu.assert_str(z.form, "hybrid height")
    tu.assert_str(z.type, "hybrid")
    tu.assert_iter(z.properties, 1, cim.v1.GridProperty)


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_core,
        _assert_doc_tile,
        _assert_doc_tile_extent,
        _assert_doc_tile_horizontal_resolution,
        _assert_doc_tile_vertical_resolution,
        _assert_doc_tile_zcoords
        ):
        assertor(doc, is_update)


def update_doc(doc):
    """Update a document prior to republishing.

    :param object doc: Document being republished.

    """
    pass


def assert_doc_updates(doc):
    """Asserts a document after being updated.

    :param object doc: Document being tested.

    """
    pass