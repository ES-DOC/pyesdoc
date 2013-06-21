"""
A set of cim related unit tests.
"""

# Module imports.
import datetime
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pyesdoc.ontologies.cim.v1.types import GridSpec as TYPE
from pyesdoc_test.test_utils import *



# Target schema being tested.
_SCHEMA_NAME = 'cim'

# Target schema version being tested.
_SCHEMA_VERSION = '1'

# Test representation file.
_TEST_FILE = '1.5/grids.grid_spec.xml'


class TestDecodeGridSpec(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        assert get_test_file(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE) is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)

        assert_cim(obj, '9cef52e4-e2af-11df-bf17-00163e9152a5', '1', '2012-03-01 13:08:34.746335')

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

        
        
    def test_representation_dict(self):
        d = decode_dict_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True

        # TODO






