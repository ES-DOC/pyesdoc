"""
A set of cim related unit tests.
"""

# Module imports.
import datetime
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pyesdoc.ontologies.cim.v1.types import (
    Citation,
    DataObject as TYPE,
    DataProperty
    )
from pyesdoc_test.test_utils import *



# Target schema being tested.
SCHEMA = 'cim'

# Target schema version being tested.
SCHEMA_VERSION = '1'

# Test representation file.
FILE = '1.5/data.data_object.xml'


class TestDecodeDataObject(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        xml = get_test_file(SCHEMA, SCHEMA_VERSION, FILE)
        assert xml is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(SCHEMA, SCHEMA_VERSION, FILE, TYPE)

        assert_cim(obj, '834151a4-978d-4627-954e-285916bb907a', '1', '2011-09-28T16:08:41')

        assert obj.acronym == 'HADGEM2_20C3M_1_D0_hus700'
        assert obj.child_object == []
        for i in range(1):
            c = obj.citations[i]
            assert c is not None
            assert isinstance(c, Citation)
            assert c.title.startswith(str(i + 1) + ' - ')
            assert c.date == dateutil_parser.parse('2009-02-11')
        assert len(obj.content) == 1
        assert obj.content[0].aggregation == 'sum'
        assert obj.content[0].frequency == 'Other'
        assert obj.content[0].topic.name == 'specific_humidity'
        assert obj.content[0].topic.description.find('specific" means per unit mass') >= 0
        assert obj.content[0].topic.unit == 'm s-1'
        for i in range(1):
            dp = obj.data_property[i]
            assert isinstance(dp, DataProperty)
            assert dp.name == 'TestProperty' + str(i + 1)
            assert dp.value == str(i + 1)
        assert obj.data_status == 'complete'
        assert obj.description.startswith('This dataset represents daily output: instantaneous daily')
        assert obj.distribution.access == 'OnlineFileHTTP'
        assert obj.distribution.format == 'NetCDF'
        assert obj.distribution.responsible_party.individual_name == 'Met Office (HC)'
        assert obj.distribution.responsible_party.organisation_name == 'Hadley Centre'
        assert obj.distribution.responsible_party.role == 'distributor'
        assert obj.extent.geographical.east == float(360)
        assert obj.extent.geographical.south == float(-90)
        assert obj.extent.geographical.west == float(0)
        assert obj.extent.geographical.north == float(90)
        assert obj.extent.temporal.begin == dateutil_parser.parse('1859-12-1')
        assert obj.extent.temporal.end == dateutil_parser.parse('1999-12-30')
        assert obj.extent.temporal.time_interval.factor == int(-1)
        assert obj.extent.temporal.time_interval.radix == int(50430)
        assert obj.extent.temporal.time_interval.unit == 'day'
        # TODO set type correctly
        # assert obj.geometry_model is None
        assert obj.hierarchy_level.name == 'experiment'
        assert obj.hierarchy_level.value == 'HADGEM2_20C3M_1_D0_hus700'
        assert obj.hierarchy_level.is_open == True
        assert obj.keyword == 'Test keyword'
        assert obj.parent_object is None
        assert obj.parent_object_reference is None
        assert obj.purpose == 'test'
        assert len(obj.restriction) == 0
        # TODO set type correctly
        # assert obj.source_simulation is None
        assert len(obj.storage) == 0


    def test_representation_dict(self):
        d = decode_dict_from_xml(SCHEMA, SCHEMA_VERSION, FILE, TYPE)

        assert d is not None
        assert isinstance(d, dict) == True

        assert d['cim_info']['id'] == uuid.UUID('834151a4-978d-4627-954e-285916bb907a')

        assert d['acronym'] == 'HADGEM2_20C3M_1_D0_hus700'
        assert len(d['content']) == 1
        assert d['extent']['temporal']['begin'] == dateutil_parser.parse('1859-12-1')






