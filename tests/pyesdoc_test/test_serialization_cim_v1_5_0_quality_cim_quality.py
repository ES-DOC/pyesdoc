"""
.. module:: test_decoding_cim_v1_5_0_quality_cim_quality.py
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests a cim v1.5.0 quality quality document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import nose
import uuid

from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
_TEST_TYPE = cim.v1.CimQuality

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/quality.cim_quality.xml'


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_decode_from_xml_metafor_cim_v1():
    obj = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(obj, 'c1debb66-2737-11e2-bc06-0010185b3f28', '2', '2012-11-05T09:51:25')

    tu.assert_collection(obj.reports, 1)
    r1 = obj.reports[0]
    tu.assert_date(r1.date, '2011-05-01 12:00:00')

    tu.assert_object(r1.evaluator)
    tu.assert_string(r1.evaluator.individual_name, 'stockhause@dkrz.de')
    tu.assert_string(r1.evaluator.role, 'pointofContact')

    tu.assert_object(r1.measure)
    tu.assert_string(r1.measure.identification, 'cmip5-qc-2d')
    tu.assert_string(r1.measure.description, 'WDCC Conformance', True)
    tu.assert_string(r1.measure.name, 'CMIP5 Quality Control Data Level 2')

    tu.assert_object(r1.evaluation)
    tu.assert_date(r1.evaluation.date, '2012-11-05')
    tu.assert_string(r1.evaluation.description, 'evaluationMethodType=indirect', True)

    tu.assert_string(r1.evaluation.type, 'QC Level 2 Results')
    tu.assert_string(r1.evaluation.type_hyperlink, 'http://cera-www.dkrz.de/WDCC/CMIP5/QCResult.jsp?experiment=cmip5/output1/NCC/NorESM1-ME/rcp45')
    tu.assert_string(r1.evaluation.specification, 'The CMIP5/AR5 Model Data Quality Control')
    tu.assert_string(r1.evaluation.specification_hyperlink, 'http://cmip5qc.wdc-climate.de')


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
    tu.assert_uuid(d['cim_info']['id'], 'c1debb66-2737-11e2-bc06-0010185b3f28')
    tu.assert_string(d['cim_info']['version'], '2')
    tu.assert_date(d['cim_info']['create_date'], '2012-11-05T09:51:25')


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

