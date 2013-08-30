"""
.. module:: test_decoding_cim_v1_8_1_software_statistical_model_component.py
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests a cim v1.8.1 software statistical model component document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import nose
import uuid

from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
_TEST_TYPE = cim.v1.StatisticalModelComponent

# Test representation file.
_TEST_FILE = 'cim/v1_8_1/software.statisticalModelComponent.xml'



def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_decode_from_xml_metafor_cim_v1():
    obj = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(obj, '4b29d25e-2968-11e0-8517-00163e9152a5', '9', '2013-03-22 17:54:48.178304')

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
    assert d['cim_info']['id'] == uuid.UUID('4b29d25e-2968-11e0-8517-00163e9152a5')


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
