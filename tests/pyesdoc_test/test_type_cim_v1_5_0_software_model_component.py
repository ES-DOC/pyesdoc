import uuid

from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test document type.
DOC_TYPE = cim.v1.ModelComponent

# Test document metafor cim v1 xml file.
DOC_FILE = 'cim/v1_5_0/software.model_component.xml'

# Test document uid.
DOC_UID = '7a2b64cc-03ca-11e1-a36a-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = '2012-01-31 12:34:51.361018'


def assert_doc(doc):
    assert isinstance(doc.doc_info, cim.v1.DocInfo)
    assert doc.doc_info.author.individual_name == 'Metafor Questionnaire'
    assert doc.doc_info.author.role == 'documentAuthor'
    assert len(doc.doc_info.genealogy.relationships) == 1
    r = doc.doc_info.genealogy.relationships[0]
    assert r.description.startswith('The HadGEM2-A model')
    assert r.direction == 'toTarget'
    assert r.type == 'previousVersionOf'
    assert r.target.reference.name == 'HadGEM1'

    assert doc.activity is None
    assert doc.timing is None
    assert doc.type == 'model'
    assert len(doc.types ) == 1
    t = doc.types[0]
    assert t == 'model'
    assert len(doc.sub_components) == 4
    cc = doc.sub_components[0]
    assert len(cc.sub_components) == 3
    assert len(cc.properties) == 4
    assert len(cc.responsible_parties) == 4
    assert cc.short_name == 'Aerosols'
    assert len(cc.types) == 2    
    assert cc.doc_info.id == uuid.UUID('7a44cb24-03ca-11e1-a36a-00163e9152a5')
    cp = cc.properties[0]
    assert len(cp.sub_properties) == 6
    assert cp.is_represented == True
    assert cp.long_name == 'Aerosols'
    assert cp.short_name == 'Aerosol Key Properties'
    assert cp.intent == 'interactive'
    assert len(cp.values) == 0
    cp = cp.sub_properties[0]
    assert len(cp.sub_properties) == 0
    assert cp.intent is None
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


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass