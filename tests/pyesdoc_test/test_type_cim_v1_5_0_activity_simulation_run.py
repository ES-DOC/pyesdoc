import uuid

from dateutil import parser as dateutil_parser

import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



# Test type.
DOC_TYPE = cim.v1.SimulationRun

# Test representation file.
DOC_FILE = 'cim/v1_5_0/activity.simulation_run.xml'

# Test document uid.
DOC_UID = '5e45202c-2b2a-11e1-a1f2-00163e9152a5'

# Test document version.
DOC_VERSION = '2'

# Test document creation date.
DOC_DATE = '2012-02-24 16:26:48.499198'


def assert_doc(doc):
    assert doc.doc_info.author.individual_name == 'Metafor Questionnaire'
    assert len(doc.doc_info.external_ids) == 1
    assert doc.doc_info.external_ids[0].is_open == True
    assert doc.doc_info.external_ids[0].value == 'MOHC_HadGEM2-ES_6.3 abrupt4xCO2'
    assert len(doc.doc_info.external_ids[0].standards) == 1
    assert doc.doc_info.external_ids[0].standards[0].name == 'QN_DRS'
    assert doc.doc_info.external_ids[0].standards[0].description.startswith('The QN_DRS value')

    assert doc.long_name == '6.3  Gregory-style diagnosis of slow climate system responses'
    assert doc.short_name == 'abrupt4xCO2'
    assert doc.description.startswith('Imposes an instantaneous')

    assert doc.authors == 'M Webb, J. Williams, T. Andrews, A. Bodas-Salcedo, Y Tsushima, J Hughes, C Jones'

    assert doc.calendar is not None
    assert isinstance(doc.calendar, cim.v1.PerpetualPeriod) == True

    assert len(doc.conformances) == 3
    assert doc.conformances[0].is_conformant == True
    assert doc.conformances[0].type == 'via inputs'
    assert doc.conformances[0].description.startswith('Main element (r1i1p1)')
    assert doc.conformances[0].frequency is None
    assert len(doc.conformances[0].requirements_references) == 1
    assert doc.conformances[0].requirements_references[0].id == uuid.UUID('a0d3a554-d3a5-11df-837f-00163e9152a5')
    assert doc.conformances[0].requirements_references[0].name == 'ic.006'
    assert doc.conformances[0].requirements_references[0].type == 'NumericalRequirement'
    assert doc.conformances[0].requirements_references[0].version == '1'
    assert doc.conformances[0].requirements_references[0].description == 'Reference to a NumericalRequirement called ic.006 in a experiment called 6.3 abrupt4xCO2'

    assert doc.control_simulation is None
    assert doc.control_simulation_reference is not None
    assert doc.control_simulation_reference.id == uuid.UUID('354ed4ec-e346-11df-9343-00163e9152a5')
    assert doc.control_simulation_reference.name == 'piControl'
    assert doc.control_simulation_reference.type == 'simulation'
    assert doc.control_simulation_reference.version == '4'
    assert doc.control_simulation_reference.description == 'branch date 1859-12-01'

    assert len(doc.deployments) == 1
    assert doc.deployments[0].description.startswith('The resources(deployment) on which this simulation ran')
    assert doc.deployments[0].platform == None
    assert doc.deployments[0].platform_reference is not None
    assert doc.deployments[0].platform_reference.id == uuid.UUID('b765775a-e2ac-11df-9efb-00163e9152a5')
    assert doc.deployments[0].platform_reference.name == 'IBM Power 6'
    assert doc.deployments[0].platform_reference.type == 'platform'
    assert doc.deployments[0].platform_reference.version == '1'
    assert doc.deployments[0].platform_reference.description == 'Reference to a platform called IBM Power 6'

    assert isinstance(doc.date_range, cim.v1.ClosedDateRange)
    assert doc.date_range.duration == 'P150Y'
    assert doc.date_range.start == dateutil_parser.parse('1859-12-01 00:00:00Z')

    assert len(doc.inputs) == 34

    assert len(doc.inputs[0].connections) == 1
    assert len(doc.inputs[0].connections[0].sources) == 1
    assert doc.inputs[0].connections[0].sources[0].data_source_reference is not None
    assert doc.inputs[0].connections[0].sources[0].data_source_reference.id == uuid.UUID('a31d55c4-4bc0-11e0-a872-00163e9152a5')
    assert doc.inputs[0].connections[0].target.data_source_reference is not None
    assert doc.inputs[0].connections[0].target.data_source_reference.id == uuid.UUID('317f51b8-e2b3-11df-bf17-00163e9152a5')

    assert len(doc.inputs[0].sources) == 1
    assert doc.inputs[0].sources[0].data_source_reference is not None
    assert doc.inputs[0].sources[0].data_source_reference.id == uuid.UUID('a31d55c4-4bc0-11e0-a872-00163e9152a5')
    assert doc.inputs[0].sources[0].data_source_reference.name == 'well_mixed_gas_CO2'
    assert doc.inputs[0].sources[0].data_source_reference.type == 'dataObject'
    assert doc.inputs[0].sources[0].data_source_reference.version == '1'
    assert doc.inputs[0].sources[0].data_source_reference.description == 'Reference to a dataObject called well_mixed_gas_CO2'

    assert doc.inputs[0].target.data_source_reference is not None
    assert doc.inputs[0].target.data_source_reference.id == uuid.UUID('317f51b8-e2b3-11df-bf17-00163e9152a5')
    assert doc.inputs[0].target.data_source_reference.name == 'Atmosphere'
    assert doc.inputs[0].target.data_source_reference.type == 'modelComponent'
    assert doc.inputs[0].target.data_source_reference.version == '1'
    assert doc.inputs[0].target.data_source_reference.description == 'Reference to a modelComponent called Atmosphere'

    assert doc.inputs[0].description.startswith('An instantaneous quadrupling')
    assert doc.inputs[0].is_fully_specified == True
    assert doc.inputs[0].purpose == 'boundaryCondition'
    assert doc.inputs[0].type == 'File'

    assert doc.inputs[0].time_profile.is_variable_rate == False
    assert doc.inputs[0].time_profile.rate == 30
    assert doc.inputs[0].time_profile.units == 'minutes'

    assert doc.inputs[0].time_transformation is not None
    assert doc.inputs[0].time_transformation.mapping_type == 'TimeInterpolation'

    assert len(doc.inputs[33].spatial_regriddings) == 1
    assert doc.inputs[33].spatial_regriddings[0].standard_method == 'conservative'

    assert doc.model == None
    assert doc.model_reference is not None
    assert doc.model_reference.id == uuid.UUID('309f6a26-e2b3-11df-bf17-00163e9152a5')
    assert doc.model_reference.name == 'HadGEM2-ES'
    assert doc.model_reference.type == 'modelComponent'
    assert doc.model_reference.version == '2'
    assert doc.model_reference.description == 'Reference to a modelComponent called HadGEM2-ES'

    assert len(doc.projects) == 1
    assert doc.projects[0] == 'CMIP5'

    assert len(doc.responsible_parties) == 4
    rp = doc.responsible_parties[0]
    assert rp.abbreviation == 'Mark Webb'
    assert rp.contact_info.email == 'mark.webb@metoffice.gov.uk'
    assert rp.individual_name == 'Mark Webb'
    assert rp.role == 'contact'

    assert len(doc.supports_references) == 1
    assert doc.supports_references[0].id == uuid.UUID('a0d3a554-d3a5-11df-837f-00163e9152a5')
    assert doc.supports_references[0].name == 'abrupt4xCO2'
    assert doc.supports_references[0].type == 'experiment'
    assert doc.supports_references[0].version == '1'
    assert doc.supports_references[0].description == 'Reference to an Experiment called abrupt4xCO2 with experimentNumber 6.3'


def update_doc(doc):
    pass


def assert_doc_updates(doc):
    pass