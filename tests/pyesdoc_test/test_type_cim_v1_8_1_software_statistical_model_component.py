from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
DOC_TYPE = cim.v1.StatisticalModelComponent

# Test representation file.
DOC_FILE = 'cim/v1_8_1/software.statisticalModelComponent.xml'

# Test document uid.
DOC_UID = '4b29d25e-2968-11e0-8517-00163e9152a5'

# Test document version.
DOC_VERSION = '9'

# Test document creation date.
DOC_DATE = '2013-03-22 17:54:48.178304'



def assert_doc(doc):
    assert doc.doc_info.author.individual_name == 'Metafor Questionnaire'
    assert doc.doc_info.author.role == 'documentAuthor'
    assert len(doc.doc_info.genealogy.relationships) == 1
    r = doc.doc_info.genealogy.relationships[0]
    assert r.direction == 'toTarget'
    assert r.target.reference.name == 'IPSLCM4_v2'
    assert r.type == 'previousVersionOf'

    assert len(doc.types ) == 1
    assert len(doc.sub_components) == 0
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
    assert len(p.sub_properties) == 4
    assert p.intent == None
    assert p.is_represented == True
    assert p.long_name == None
    assert p.short_name == 'Sea Ice Key Properties'
    assert len(p.values) == 0

    p = p.sub_properties[0]
    assert len(p.sub_properties) == 0
    assert p.intent == None
    assert p.is_represented == True
    assert p.long_name == 'BasicApproximations'
    assert p.short_name == 'BasicApproximations'
    assert len(p.values) == 1
    assert p.values[0] == '2-level + visco-plastic rheology'


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass