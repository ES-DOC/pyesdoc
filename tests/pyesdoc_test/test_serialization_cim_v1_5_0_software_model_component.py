"""
.. module:: test_decoding_cim_v1_5_0_software_model_component.py
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests a cim v1.5.0 software model component document.

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
_TEST_TYPE = cim.v1.ModelComponent

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/software.model_component.xml'


def _assert_doc(doc):
    doc = tu.decode_from_xml_metafor_cim_v1(_TEST_FILE, _TEST_TYPE)

    tu.assert_pyesdoc_obj(doc, '7a2b64cc-03ca-11e1-a36a-00163e9152a5', '1', '2012-01-31 12:34:51.361018')

    assert isinstance(doc.cim_info, cim.v1.CimInfo)
    assert doc.cim_info.author.individual_name == 'Metafor Questionnaire'
    assert doc.cim_info.author.role == 'documentAuthor'
    assert len(doc.cim_info.genealogy.relationships) == 1
    r = doc.cim_info.genealogy.relationships[0]
    assert r.description.startswith('The HadGEM2-A model')
    assert r.direction == 'toTarget'
    assert r.target.reference.name == 'HadGEM1'
    assert r.type == 'previousVersionOf'

    assert doc.activity is None
    assert doc.timing is None
    assert len(doc.types ) == 1
    t = doc.types[0]
    assert t == 'model'
    assert len(doc.children) == 4
    cc = doc.children[0]
    assert len(cc.children) == 3
    assert len(cc.properties) == 4
    assert len(cc.responsible_parties) == 4
    assert cc.short_name == 'Aerosols'
    assert len(cc.types) == 2
    assert cc.cim_info.id == uuid.UUID('7a44cb24-03ca-11e1-a36a-00163e9152a5')
    cp = cc.properties[0]
    assert len(cp.children) == 6
    assert cp.intent == 'interactive'
    assert cp.is_represented == True
    assert cp.long_name == 'Aerosols'
    assert cp.short_name == 'Aerosol Key Properties'
    assert len(cp.values) == 0
    cp = cp.children[0]
    assert len(cp.children) == 0
    assert cp.intent == None
    assert cp.is_represented == True
    assert cp.long_name == 'AerosolSchemeScope'
    assert cp.short_name == 'AerosolSchemeScope'
    assert len(cp.values) >= 1
    assert cp.values[0] == 'whole atmosphere'
    cp = cc.properties[1]
    assert cp.description.startswith('Emissions of aerosols')
    assert cp.units == 'kg/m2/s'
    assert len(cp.standard_names) == 2
    sn = cp.standard_names[0]
    assert sn == 'biomass_burning_carbon_flux'
    sn = cp.standard_names[1]
    assert sn == 'carbon_flux'
    assert len(doc.citations) == 2
    c = doc.citations[0]
    assert c.collective_title.startswith('Bellouin')
    assert c.location.startswith("http://www.metoffice.gov.uk/publications/HCTN/HCTN_73.pdf")
    assert c.title.startswith('Bellouin')
    c = doc.citations[1]
    assert c.collective_title.startswith('Collins')
    assert c.location.startswith("http://www.metoffice.gov.uk/publications/HCTN/HCTN_74.pdf")
    assert c.title.startswith('Collins')
    assert doc.language is None
    assert doc.properties == []
    assert doc.composition is None
    assert doc.coupling_framework is ''
    assert doc.dependencies == []
    assert doc.deployments == []
    assert doc.description.startswith('The HadGEM2-A model')
    assert doc.funding_sources == []
    assert doc.grid is None
    assert doc.is_embedded == False
    assert doc.license is None
    assert doc.long_name == 'Hadley Global Environment Model 2 - Atmosphere'
    # TODO default for uri's = None ?
    assert doc.online_resource == str()
    assert doc.parent is None
    # TODO default for str's = None ?
    assert doc.previous_version == str()
    assert doc.release_date == dateutil_parser.parse('2009')
    assert len(doc.responsible_parties) == 4
    rp = doc.responsible_parties[0]
    assert rp.abbreviation == 'Chris Jones'
    assert rp.contact_info.address.startswith('Met Office Hadley Centre')
    assert rp.contact_info.email is None
    assert rp.contact_info.url.startswith('http://www.metoffice.gov.uk/research/our-scientists/climate-chemistry-ecosystems/chris-jones')
    assert rp.individual_name == 'Chris Jones'
    assert rp.role == 'PI'
    rp = doc.responsible_parties[2]
    assert rp.abbreviation == 'Gill Martin'
    assert rp.contact_info.address.startswith('Met Office Hadley Centre')
    assert rp.contact_info.email == 'mark.webb@metoffice.gov.uk'
    assert rp.contact_info.url.startswith('http://www.metoffice.gov.uk/research/people/gill-martin')
    assert rp.individual_name == 'Gill Martin'
    assert rp.role == 'contact'
    assert doc.short_name == 'HadGEM2-A'


def test_open_test_file():
    assert tu.get_test_file(_TEST_FILE) is not None


def test_serialize():    
    for encoding in pyesdoc.ESDOC_ENCODINGS:
        tu.serialize.description = "{0}.test_serialize.{1}".format(__name__, encoding)
        yield tu.serialize, encoding, _TEST_FILE, _TEST_TYPE, _assert_doc
