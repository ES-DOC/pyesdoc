"""
A set of cim related unit tests.
"""

# Module imports.
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pyesdoc.ontologies.cim.v1.types import StatisticalModelComponent as TYPE
from pyesdoc_test.test_utils import *



# Target schema being tested.
_SCHEMA_NAME = 'cim'

# Target schema version being tested.
_SCHEMA_VERSION = '1'

# Test representation file.
_TEST_FILE = '1.8.1/software.statisticalModelComponent.xml'



class TestDecodeStatisticalModelComponent(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        assert get_test_file(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE) is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)

        assert_cim(obj, '4b29d25e-2968-11e0-8517-00163e9152a5', '9', '2013-03-22 17:54:48.178304')

        assert obj.cim_info.author.individual_name == 'Metafor Questionnaire'
        assert obj.cim_info.author.role == 'documentAuthor'
        assert len(obj.cim_info.genealogy.relationships) == 1
        r = obj.cim_info.genealogy.relationships[0]
        assert r.direction == 'toTarget'
        assert r.target.reference.name == 'IPSLCM4_v2'
        assert r.type == 'previousVersionOf'

        assert len(obj.types ) == 1
        assert len(obj.children) == 0
        assert len(obj.citations) == 1
        assert len(obj.dependencies) == 0
        assert len(obj.deployments) == 0
        assert len(obj.funding_sources) == 0
        assert len(obj.properties) == 1
        assert len(obj.responsible_parties) == 4

        assert obj.composition is None
        assert obj.coupling_framework is ''
        assert obj.description.startswith('IPSL-CM5A-LR is the low resolution')
        assert obj.is_embedded == False
        assert obj.grid is None
        assert obj.language is None
        assert obj.license is None
        assert obj.long_name == "IPSL-CM5A-LR;atmosphere:LMDZ5A(95x96L39);ocean:NEMOv3.2 (OPA-LIM-PISCES,149x182L31)"
        assert obj.previous_version == str()
        assert obj.release_date == dateutil_parser.parse('2010')
        assert obj.short_name == 'IPSL-CM5A-LR'        
        assert obj.types[0] == 'downscaling'

        p = obj.properties[0]
        assert len(p.children) == 4
        assert p.intent == None
        assert p.is_represented == True
        assert p.long_name == None
        assert p.short_name == 'Sea Ice Key Properties'
        assert len(p.values) == 0

        p = p.children[0]
        assert len(p.children) == 0
        assert p.intent == None
        assert p.is_represented == True
        assert p.long_name == 'BasicApproximations'
        assert p.short_name == 'BasicApproximations'
        assert len(p.values) == 1
        assert p.values[0] == '2-level + visco-plastic rheology'        


    def test_representation_dict(self):
        d = decode_dict_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True
        
        assert d['cim_info']['id'] == uuid.UUID('4b29d25e-2968-11e0-8517-00163e9152a5')










