"""
.. module:: test_decoding_cim_v1_5_0_grids_gridspec.py
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests a cim v1.5.0 grids gridspec document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import nose
import uuid

from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
_TEST_TYPE = cim.v1.GridSpec

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/grids.grid_spec.xml'


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_decode_from_xml_metafor_cim_v1():
    obj = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(obj, '9cef52e4-e2af-11df-bf17-00163e9152a5', '1', '2012-03-01 13:08:34.746335')

    assert len(obj.esm_model_grids) == 1
    assert len(obj.esm_exchange_grids) == 0

    assert obj.esm_model_grids[0].description.startswith('Specification of the ocean grid configuration')
    assert obj.esm_model_grids[0].long_name == 'Met Office Unified Model 360-column 40-level Ocean Grid System'
    assert obj.esm_model_grids[0].short_name == 'UM N180L40 OCN Grid System'

    assert len(obj.esm_model_grids[0].citations) == 2
    assert obj.esm_model_grids[0].citations[0].title == 'Johns_2005'
    assert obj.esm_model_grids[0].citations[0].collective_title.startswith('Johns T.C., et al. (2005).')

    assert obj.esm_model_grids[0].extent is None
    assert obj.esm_model_grids[0].has_congruent_tiles == False
    assert obj.esm_model_grids[0].id == ''
    assert obj.esm_model_grids[0].is_leaf == True
    assert obj.esm_model_grids[0].mosaic_count == 0
    assert obj.esm_model_grids[0].tile_count == 1
    assert obj.esm_model_grids[0].type == 'regular_lat_lon'

    assert len(obj.esm_model_grids[0].tiles) == 1
    assert obj.esm_model_grids[0].tiles[0].description.startswith('Horizontal properties: Between the poles')
    assert obj.esm_model_grids[0].tiles[0].extent is not None
    assert obj.esm_model_grids[0].tiles[0].extent.minimum_latitude == '-90'
    assert obj.esm_model_grids[0].tiles[0].extent.maximum_latitude == '90'
    assert obj.esm_model_grids[0].tiles[0].extent.minimum_longitude == '0'
    assert obj.esm_model_grids[0].tiles[0].extent.maximum_longitude == '360'
    assert obj.esm_model_grids[0].tiles[0].extent.units is None
    assert obj.esm_model_grids[0].tiles[0].mnemonic == 'N180'
    assert obj.esm_model_grids[0].tiles[0].horizontal_resolution is not None
    assert obj.esm_model_grids[0].tiles[0].horizontal_resolution.description.startswith('1 deg by 1 deg')
    assert len(obj.esm_model_grids[0].tiles[0].horizontal_resolution.properties) == 2
    assert obj.esm_model_grids[0].tiles[0].horizontal_resolution.properties[0].name == 'NumberOfLatitudinalGridCells'
    assert obj.esm_model_grids[0].tiles[0].horizontal_resolution.properties[0].value == '216'
    assert obj.esm_model_grids[0].tiles[0].vertical_resolution is not None
    assert len(obj.esm_model_grids[0].tiles[0].vertical_resolution.properties) == 4
    assert obj.esm_model_grids[0].tiles[0].vertical_resolution.properties[0].name == 'NumberOfLevelsInUpper100m'
    assert obj.esm_model_grids[0].tiles[0].vertical_resolution.properties[0].value == '10'

    assert obj.esm_model_grids[0].tiles[0].zcoords is not None
    assert obj.esm_model_grids[0].tiles[0].zcoords.type == 'space-based'
    assert obj.esm_model_grids[0].tiles[0].zcoords.form == 'depth'



@nose.tools.raises(NotImplementedError)
def test_encode_xml_metafor_cim_v1():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.encode_to_xml_metafor_cim_v1(doc)


def test_decode_dict():
    doc1 = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    as_dict = tu.encode_to_dict(doc1)

    doc = tu.decode_from_dict(as_dict)


def test_encode_dict():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    d = tu.encode_to_dict(doc)


def test_decode_json():
    doc1 = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    as_json = tu.encode_to_json(doc1)

    doc = tu.decode_from_json(as_json)


def test_encode_json():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.encode_to_json(doc)


@nose.tools.raises(NotImplementedError)
def test_decode_xml():
    doc1 = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    as_xml = tu.encode_to_xml(doc1)

    doc = tu.decode_from_xml(as_xml)


def test_encode_xml():
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.encode_to_xml(doc)

