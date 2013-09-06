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

import pyesdoc
import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
_TEST_TYPE = cim.v1.StatisticalModelComponent

# Test representation file.
_TEST_FILE = 'cim/v1_8_1/software.statisticalModelComponent.xml'



def _assert_doc(doc):
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(doc, '4b29d25e-2968-11e0-8517-00163e9152a5', '9', '2013-03-22 17:54:48.178304')

    assert doc.cim_info.author.individual_name == 'Metafor Questionnaire'
    assert doc.cim_info.author.role == 'documentAuthor'
    assert len(doc.cim_info.genealogy.relationships) == 1
    r = doc.cim_info.genealogy.relationships[0]
    assert r.direction == 'toTarget'
    assert r.target.reference.name == 'IPSLCM4_v2'
    assert r.type == 'previousVersionOf'

    assert len(doc.types ) == 1
    assert len(doc.children) == 0
    assert len(doc.citations) == 1
    assert len(doc.dependencies) == 0
    assert len(doc.deployments) == 0
    assert len(doc.funding_sources) == 0
    assert len(doc.properties) == 1
    assert len(doc.responsible_parties) == 4

    assert doc.composition is None
    assert doc.coupling_framework is ''
    assert doc.description.startswith('IPSL-CM5A-LR is the low resolution')
    assert doc.is_embedded == False
    assert doc.grid is None
    assert doc.language is None
    assert doc.license is None
    assert doc.long_name == "IPSL-CM5A-LR;atmosphere:LMDZ5A(95x96L39);ocean:NEMOv3.2 (OPA-LIM-PISCES,149x182L31)"
    assert doc.previous_version == str()
    assert doc.release_date == dateutil_parser.parse('2010')
    assert doc.short_name == 'IPSL-CM5A-LR'
    assert doc.types[0] == 'downscaling'

    p = doc.properties[0]
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


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_serialize():
    for encoding in pyesdoc.ESDOC_ENCODINGS:
        tu.serialize.description = "{0}.test_serialize.{1}".format(__name__, encoding)
        yield tu.serialize, encoding, _TEST_FILE, _TEST_TYPE, _assert_doc
