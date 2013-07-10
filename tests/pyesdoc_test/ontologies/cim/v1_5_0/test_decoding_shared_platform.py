"""
A set of cim related unit tests.
"""

# Module imports.
import datetime
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pyesdoc.ontologies.cim.v1.types import Platform as TYPE
from pyesdoc_test.test_utils import *



# Target schema being tested.
_SCHEMA_NAME = 'cim'

# Target schema version being tested.
_SCHEMA_VERSION = '1'

# Test representation file.
_TEST_FILE = '/v1_5_0/files/shared.platform.xml'


class TestDecodeCIM_v1_5_0_Platform(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        assert get_test_file(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE) is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)
        
        assert_cim(obj, 'b765775a-e2ac-11df-9efb-00163e9152a5', '1', '2012-03-01 13:55:56.232228')

        assert obj.description is None
        assert obj.long_name == 'Machine IBM Power 6 and compiler Other'
        assert obj.short_name == 'IBM Power 6_Other'

        assert len(obj.contacts) == 1
        assert obj.contacts[0].abbreviation == 'MOHC'
        assert obj.contacts[0].organisation_name == 'UK Met Office Hadley Centre'
        assert obj.contacts[0].role == 'contact'
        
        assert len(obj.units) == 1
        assert obj.units[0].machine is not None
        assert obj.units[0].machine.cores_per_processor == 32
        assert obj.units[0].machine.description is None
        assert obj.units[0].machine.interconnect == 'Infiniband'
        assert obj.units[0].machine.name == 'IBM Power 6'
        assert len(obj.units[0].machine.libraries) == 0
        assert obj.units[0].machine.location is None
        assert obj.units[0].machine.maximum_processors == 2
        assert obj.units[0].machine.operating_system == 'AIX'
        assert obj.units[0].machine.system == 'Parallel'
        assert obj.units[0].machine.type is None
        assert obj.units[0].machine.vendor == 'IBM'
        assert obj.units[0].machine.processor_type == 'Other'
        assert len(obj.units[0].compilers) == 1
        assert obj.units[0].compilers[0].environment_variables is None
        assert obj.units[0].compilers[0].language is None
        assert obj.units[0].compilers[0].name == 'Other'
        assert obj.units[0].compilers[0].options is None
        assert obj.units[0].compilers[0].type is None
        assert obj.units[0].compilers[0].version == '12.1.0.0'


    def test_representation_dict(self):
        d = decode_dict_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True

        # TODO
        






