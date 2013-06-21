"""
A set of cim related unit tests.
"""

# Module imports.
import datetime
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pyesdoc.ontologies.cim.v1.types import CimQuality as TYPE
from pyesdoc_test.test_utils import *



# Target schema being tested.
_SCHEMA_NAME = 'cim'

# Target schema version being tested.
_SCHEMA_VERSION = '1'

# Test representation file.
_TEST_FILE = '1.5/quality.cim_quality.xml'


class TestDecodeCimQuality(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        assert get_test_file(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE) is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)
    
        assert_cim(obj, 'c1debb66-2737-11e2-bc06-0010185b3f28', '2', '2012-11-05T09:51:25')

        assert_collection(obj.reports, 1)
        r1 = obj.reports[0]
        assert_date(r1.date, '2011-05-01 12:00:00')
        
        assert_object(r1.evaluator)
        assert_string(r1.evaluator.individual_name, 'stockhause@dkrz.de')
        assert_string(r1.evaluator.role, 'pointofContact')

        assert_object(r1.measure)
        assert_string(r1.measure.identification, 'cmip5-qc-2d')
        assert_string(r1.measure.description, 'WDCC Conformance', True)
        assert_string(r1.measure.name, 'CMIP5 Quality Control Data Level 2')

        assert_object(r1.evaluation)
        assert_date(r1.evaluation.date, '2012-11-05')
        assert_string(r1.evaluation.description, 'evaluationMethodType=indirect', True)

        assert_string(r1.evaluation.type, 'QC Level 2 Results')
        assert_string(r1.evaluation.type_hyperlink, 'http://cera-www.dkrz.de/WDCC/CMIP5/QCResult.jsp?experiment=cmip5/output1/NCC/NorESM1-ME/rcp45')
        assert_string(r1.evaluation.specification, 'The CMIP5/AR5 Model Data Quality Control')
        assert_string(r1.evaluation.specification_hyperlink, 'http://cmip5qc.wdc-climate.de')


    def test_representation_dict(self):
        d = decode_dict_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)

        assert_object(d, dict)
        assert_uuid(d['cim_info']['id'], 'c1debb66-2737-11e2-bc06-0010185b3f28')
        assert_string(d['cim_info']['version'], '2')
        assert_date(d['cim_info']['create_date'], '2012-11-05T09:51:25')






