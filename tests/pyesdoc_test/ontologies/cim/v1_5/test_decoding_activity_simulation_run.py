"""
A set of cim related unit tests.
"""

# Module imports.
import datetime
from dateutil import parser as dateutil_parser
import unittest
import uuid

from pyesdoc.ontologies.cim.v1_5.types import (
    ClosedDateRange,
    PerpetualPeriod,
    SimulationRun as TYPE
    )
from pyesdoc_test.test_utils import *



# Target schema being tested.
SCHEMA = 'cim'

# Target schema version being tested.
SCHEMA_VERSION = '1.5'

# Test representation file.
FILE = 'activity.simulation_run.xml'


class TestDecodeSimulationRun(unittest.TestCase):
    """A decoding from xml unit test.

    """
    def test_open_xml(self):
        xml = get_test_file(SCHEMA, SCHEMA_VERSION, FILE)
        assert xml is not None


    def test_decode_obj_from_xml(self):
        obj = decode_obj_from_xml(SCHEMA, SCHEMA_VERSION, FILE, TYPE)

        assert_cim(obj, '5e45202c-2b2a-11e1-a1f2-00163e9152a5', '2', '2012-02-24 16:26:48.499198')

        assert obj.cim_info.author.individual_name == 'Metafor Questionnaire'
        assert len(obj.cim_info.external_ids) == 1
        assert obj.cim_info.external_ids[0].is_open == True
        assert obj.cim_info.external_ids[0].value == 'MOHC_HadGEM2-ES_6.3 abrupt4xCO2'
        assert len(obj.cim_info.external_ids[0].standards) == 1
        assert obj.cim_info.external_ids[0].standards[0].name == 'QN_DRS'
        assert obj.cim_info.external_ids[0].standards[0].description.startswith('The QN_DRS value')
        
        assert obj.long_name == '6.3  Gregory-style diagnosis of slow climate system responses'
        assert obj.short_name == 'abrupt4xCO2'
        assert obj.description.startswith('Imposes an instantaneous')

        assert obj.authors == 'M Webb, J. Williams, T. Andrews, A. Bodas-Salcedo, Y Tsushima, J Hughes, C Jones'
        
        assert obj.calendar is not None
        assert isinstance(obj.calendar, PerpetualPeriod) == True

        assert len(obj.conformances) == 3
        assert obj.conformances[0].is_conformant == True
        assert obj.conformances[0].type == 'via inputs'
        assert obj.conformances[0].description.startswith('Main element (r1i1p1)')
        assert obj.conformances[0].frequency is None
        assert len(obj.conformances[0].requirements_references) == 1
        assert obj.conformances[0].requirements_references[0].id == uuid.UUID('a0d3a554-d3a5-11df-837f-00163e9152a5')
        assert obj.conformances[0].requirements_references[0].name == 'ic.006'
        assert obj.conformances[0].requirements_references[0].type == 'NumericalRequirement'
        assert obj.conformances[0].requirements_references[0].version == '1'
        assert obj.conformances[0].requirements_references[0].description == 'Reference to a NumericalRequirement called ic.006 in a experiment called 6.3 abrupt4xCO2'
        
        assert obj.control_simulation is None
        assert obj.control_simulation_reference is not None
        assert obj.control_simulation_reference.id == uuid.UUID('354ed4ec-e346-11df-9343-00163e9152a5')
        assert obj.control_simulation_reference.name == 'piControl'
        assert obj.control_simulation_reference.type == 'simulation'
        assert obj.control_simulation_reference.version == '4'
        assert obj.control_simulation_reference.description == 'branch date 1859-12-01'

        assert len(obj.deployments) == 1
        assert obj.deployments[0].description.startswith('The resources(deployment) on which this simulation ran')
        assert obj.deployments[0].platform == None
        assert obj.deployments[0].platform_reference is not None
        assert obj.deployments[0].platform_reference.id == uuid.UUID('b765775a-e2ac-11df-9efb-00163e9152a5')
        assert obj.deployments[0].platform_reference.name == 'IBM Power 6'
        assert obj.deployments[0].platform_reference.type == 'platform'
        assert obj.deployments[0].platform_reference.version == '1'
        assert obj.deployments[0].platform_reference.description == 'Reference to a platform called IBM Power 6'

        assert isinstance(obj.date_range, ClosedDateRange)
        assert obj.date_range.duration == 'P150Y'
        assert obj.date_range.start == dateutil_parser.parse('1859-12-01 00:00:00Z')

        assert len(obj.inputs) == 34
        
        assert len(obj.inputs[0].connections) == 1
        assert len(obj.inputs[0].connections[0].sources) == 1
        assert obj.inputs[0].connections[0].sources[0].data_source_reference is not None
        assert obj.inputs[0].connections[0].sources[0].data_source_reference.id == uuid.UUID('a31d55c4-4bc0-11e0-a872-00163e9152a5')
        assert obj.inputs[0].connections[0].target.data_source_reference is not None
        assert obj.inputs[0].connections[0].target.data_source_reference.id == uuid.UUID('317f51b8-e2b3-11df-bf17-00163e9152a5')

        assert len(obj.inputs[0].sources) == 1
        assert obj.inputs[0].sources[0].data_source_reference is not None
        assert obj.inputs[0].sources[0].data_source_reference.id == uuid.UUID('a31d55c4-4bc0-11e0-a872-00163e9152a5')
        assert obj.inputs[0].sources[0].data_source_reference.name == 'well_mixed_gas_CO2'
        assert obj.inputs[0].sources[0].data_source_reference.type == 'dataObject'
        assert obj.inputs[0].sources[0].data_source_reference.version == '1'
        assert obj.inputs[0].sources[0].data_source_reference.description == 'Reference to a dataObject called well_mixed_gas_CO2'

        assert obj.inputs[0].target.data_source_reference is not None
        assert obj.inputs[0].target.data_source_reference.id == uuid.UUID('317f51b8-e2b3-11df-bf17-00163e9152a5')
        assert obj.inputs[0].target.data_source_reference.name == 'Atmosphere'
        assert obj.inputs[0].target.data_source_reference.type == 'modelComponent'
        assert obj.inputs[0].target.data_source_reference.version == '1'
        assert obj.inputs[0].target.data_source_reference.description == 'Reference to a modelComponent called Atmosphere'

        assert obj.inputs[0].description.startswith('An instantaneous quadrupling')
        assert obj.inputs[0].is_fully_specified == True
        assert obj.inputs[0].purpose == 'boundaryCondition'
        assert obj.inputs[0].type == 'File'
        
        assert obj.inputs[0].time_profile.is_variable_rate == False
        assert obj.inputs[0].time_profile.rate == 30
        assert obj.inputs[0].time_profile.units == 'minutes'
        
        assert obj.inputs[0].time_transformation is not None
        assert obj.inputs[0].time_transformation.mapping_type == 'TimeInterpolation'

        assert len(obj.inputs[33].spatial_regriddings) == 1
        assert obj.inputs[33].spatial_regriddings[0].standard_method == 'conservative'

        assert obj.model == None
        assert obj.model_reference is not None
        assert obj.model_reference.id == uuid.UUID('309f6a26-e2b3-11df-bf17-00163e9152a5')
        assert obj.model_reference.name == 'HadGEM2-ES'
        assert obj.model_reference.type == 'modelComponent'
        assert obj.model_reference.version == '2'
        assert obj.model_reference.description == 'Reference to a modelComponent called HadGEM2-ES'

        assert len(obj.projects) == 1
        assert obj.projects[0] == 'CMIP5'

        assert len(obj.responsible_parties) == 4
        rp = obj.responsible_parties[0]
        assert rp.abbreviation == 'Mark Webb'
        assert rp.contact_info.email == 'mark.webb@metoffice.gov.uk'
        assert rp.individual_name == 'Mark Webb'
        assert rp.role == 'contact'

        assert len(obj.supports_references) == 1
        assert obj.supports_references[0].id == uuid.UUID('a0d3a554-d3a5-11df-837f-00163e9152a5')
        assert obj.supports_references[0].name == 'abrupt4xCO2'
        assert obj.supports_references[0].type == 'experiment'
        assert obj.supports_references[0].version == '1'
        assert obj.supports_references[0].description == 'Reference to an Experiment called abrupt4xCO2 with experimentNumber 6.3'



    def test_representation_dict(self):
        d = decode_dict_from_xml(SCHEMA, SCHEMA_VERSION, FILE, TYPE)
        assert d is not None
        assert isinstance(d, dict) == True

        # TODO







