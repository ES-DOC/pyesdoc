"""
A set of cim related unit tests.
"""

# Module imports.
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pyesdoc.ontologies.cim.v1.types import ModelComponent as TYPE
from pyesdoc_test.test_utils import *



# Target schema being tested.
_SCHEMA_NAME = 'cim'

# Target schema version being tested.
_SCHEMA_VERSION = '1'

# Test representation file.
_TEST_FILE = '/v1_5_0/files/software.model_component.xml'


class TestDecodeCIM_v1_5_0_ModelComponent(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        assert get_test_file(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE) is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)

        assert_cim(obj, '7a2b64cc-03ca-11e1-a36a-00163e9152a5', '1', '2012-01-31 12:34:51.361018')

        assert obj.cim_info.author.individual_name == 'Metafor Questionnaire'
        assert obj.cim_info.author.role == 'documentAuthor'
        assert len(obj.cim_info.genealogy.relationships) == 1
        r = obj.cim_info.genealogy.relationships[0]
        assert r.description.startswith('The HadGEM2-A model')
        assert r.direction == 'toTarget'
        assert r.target.reference.name == 'HadGEM1'
        assert r.type == 'previousVersionOf'

        assert obj.activity is None
        assert obj.timing is None
        assert len(obj.types ) == 1
        t = obj.types[0]
        assert t == 'model'
        assert len(obj.children) == 4
        cc = obj.children[0]
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
        assert len(obj.citations) == 2
        c = obj.citations[0]
        assert c.collective_title.startswith('Bellouin')
        assert c.location.startswith("http://www.metoffice.gov.uk/publications/HCTN/HCTN_73.pdf")
        assert c.title.startswith('Bellouin')
        c = obj.citations[1]
        assert c.collective_title.startswith('Collins')
        assert c.location.startswith("http://www.metoffice.gov.uk/publications/HCTN/HCTN_74.pdf")
        assert c.title.startswith('Collins')
        assert obj.language is None
        assert obj.properties == []
        assert obj.composition is None
        assert obj.coupling_framework is ''
        assert obj.dependencies == []
        assert obj.deployments == []
        assert obj.description.startswith('The HadGEM2-A model')
        assert obj.funding_sources == []
        assert obj.grid is None
        assert obj.is_embedded == False
        assert obj.license is None
        assert obj.long_name == 'Hadley Global Environment Model 2 - Atmosphere'
        # TODO default for uri's = None ?
        assert obj.online_resource == str()
        assert obj.parent is None
        # TODO default for str's = None ?
        assert obj.previous_version == str()
        assert obj.release_date == dateutil_parser.parse('2009')
        assert len(obj.responsible_parties) == 4
        rp = obj.responsible_parties[0]
        assert rp.abbreviation == 'Chris Jones'
        assert rp.contact_info.address.startswith('Met Office Hadley Centre')
        assert rp.contact_info.email is None
        assert rp.contact_info.url.startswith('http://www.metoffice.gov.uk/research/our-scientists/climate-chemistry-ecosystems/chris-jones')
        assert rp.individual_name == 'Chris Jones'
        assert rp.role == 'PI'
        rp = obj.responsible_parties[2]
        assert rp.abbreviation == 'Gill Martin'
        assert rp.contact_info.address.startswith('Met Office Hadley Centre')
        assert rp.contact_info.email == 'mark.webb@metoffice.gov.uk'
        assert rp.contact_info.url.startswith('http://www.metoffice.gov.uk/research/people/gill-martin')
        assert rp.individual_name == 'Gill Martin'
        assert rp.role == 'contact'
        assert obj.short_name == 'HadGEM2-A'


    def test_representation_dict(self):
        d = decode_dict_from_xml(_SCHEMA_NAME, _SCHEMA_VERSION, _TEST_FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True
        
        assert d['cim_info']['id'] == uuid.UUID('7a2b64cc-03ca-11e1-a36a-00163e9152a5')

        assert d['short_name'] == 'HadGEM2-A'
        assert len(d['types']) == 1
        assert len(d['children']) == 4
        cc = d['children'][0]
        assert len(cc['children']) == 3
        assert cc['short_name'] == 'Aerosols'
        assert cc['cim_info']['id'] == uuid.UUID('7a44cb24-03ca-11e1-a36a-00163e9152a5')
        cp = cc['properties'][0]
        assert len(cp['children']) == 6
        assert cp['intent'] == 'interactive'
        assert cp['short_name'] == 'Aerosol Key Properties'









