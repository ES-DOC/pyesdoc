# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_activity_simulation_run.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.SimulationRun instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.SimulationRun

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Simulation"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key

# Test representation file.
DOC_FILE = 'cim.1.activity.SimulationRun.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = 'e4155a28-268e-11e1-9a0e-00163e9152a5'

# Test document version.
DOC_VERSION = '2'

# Test document creation date.
DOC_DATE = arrow.get('2012-04-23 14:59:06.767729').datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_meta_info(meta):
    """Asserts a document's meta-information.

    :param object meta: Document meta information.

    """
    tu.assert_iter(meta.external_ids, 2, cim.v1.StandardName)
    id = meta.external_ids[0]
    tu.assert_bool(id.is_open, True)
    tu.assert_iter(id.standards, 1, cim.v1.Standard)
    tu.assert_str(id.value, "MOHC_HadGEM2-A_amip_r1i1p1_1978")
    std = id.standards[0]
    tu.assert_str(std.description, "The QN_DRS value allows", True)
    tu.assert_str(std.name, "QN_DRS")


def assert_extension_info(ext):
    """Asserts a document's extension information.

    :param object ext: Document extension information.

    """
    tu.assert_str(ext.display_name, "amip")
    tu.assert_str(ext.description, "Main amip ensemble simulations", True)
    tu.assert_str(ext.full_display_name, "CMIP5 Simulation : MOHC - amip")
    tu.assert_int(ext.summary_fields, 2)
    tu.assert_str(ext.summary_fields[0], "amip")
    tu.assert_str(ext.summary_fields[1], "3.3 AMIP and AMIP Ensemble", True)


def _assert_doc_core(doc, is_update):
    """Assert core information."""
    tu.assert_str(doc.authors, "C. Jones, J. Hughes", True)
    tu.assert_object(doc.date_range, cim.v1.ClosedDateRange)
    tu.assert_str(doc.date_range.duration, "P30Y")
    tu.assert_date(doc.date_range.start, "1978-12-01 00:00:00+00:00")
    tu.assert_str(doc.description, "Main amip ensemble simulations", True)
    tu.assert_str(doc.long_name, "3.3 AMIP and AMIP Ensemble", True)
    tu.assert_iter(doc.projects, 1, str)
    tu.assert_str(doc.projects[0], "CMIP5")
    tu.assert_iter(doc.responsible_parties, 4, cim.v1.ResponsibleParty)
    tu.assert_str(doc.short_name, "amip")
    tu.assert_object(doc.spinup_date_range, cim.v1.ClosedDateRange)
    tu.assert_str(doc.spinup_date_range.duration, "P30Y")
    tu.assert_date(doc.spinup_date_range.start, "1978-12-01 00:00:00+00:00")


def _assert_doc_conformances(doc, is_update):
    """Assert simulation conformances."""
    tu.assert_iter(doc.conformances, 13, cim.v1.Conformance)

    c = doc.conformances[0]
    tu.assert_str(c.type, "standard config")
    tu.assert_iter(c.requirements_references, 1, cim.v1.DocReference)
    ref = c.requirements_references[0]
    tu.assert_str(ref.description, "Reference to a NumericalRequirement", True)
    tu.assert_uuid(ref.id, "9fa513fc-d3a5-11df-837f-00163e9152a5")
    tu.assert_str(ref.name, "ic.003")
    tu.assert_str(ref.type, "NumericalRequirement")
    tu.assert_int(ref.version, 1)

    c = doc.conformances[7]
    tu.assert_str(c.description, "Prescribed land use", True)
    tu.assert_bool(c.is_conformant, True)
    tu.assert_str(c.type, "via inputs")


def _assert_doc_deployments(doc, is_update):
    """Assert simulation deployments."""
    tu.assert_iter(doc.deployments, 1, cim.v1.Deployment)

    dep = doc.deployments[0]
    tu.assert_str(dep.description, "The resources(deployment) on which", True)
    tu.assert_object(dep.platform_reference, cim.v1.DocReference)
    ref = dep.platform_reference
    tu.assert_str(ref.description, "Reference to a platform", True)
    tu.assert_uuid(ref.id, "b765775a-e2ac-11df-9efb-00163e9152a5")
    tu.assert_str(ref.name, "IBM Power 6")
    tu.assert_str(ref.type, "platform")
    tu.assert_int(ref.version, 1)


def _assert_doc_inputs(doc, is_update):
    """Assert simulation inputs."""
    tu.assert_iter(doc.inputs, 56, cim.v1.Coupling)


def _assert_doc_references(doc, is_update):
    """Assert simulation references."""
    # Model reference.
    tu.assert_object(doc.model_reference, cim.v1.DocReference)
    ref = doc.model_reference
    tu.assert_str(ref.description, "Reference to a modelComponent", True)
    tu.assert_uuid(ref.id, "7a2b64cc-03ca-11e1-a36a-00163e9152a5")
    tu.assert_str(ref.name, "HadGEM2-A")
    tu.assert_str(ref.type, "modelComponent")
    tu.assert_int(ref.version, 1)

    # Experiment reference.
    tu.assert_iter(doc.supports_references, 1, cim.v1.DocReference)
    ref = doc.supports_references[0]
    tu.assert_str(ref.description, "Reference to an Experiment", True)
    tu.assert_uuid(ref.id, "9fa513fc-d3a5-11df-837f-00163e9152a5")
    tu.assert_str(ref.name, "amip")
    tu.assert_str(ref.type, "experiment")
    tu.assert_int(ref.version, 1)


def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_core,
        _assert_doc_conformances,
        _assert_doc_deployments,
        _assert_doc_inputs,
        _assert_doc_references,
        ):
        assertor(doc, is_update)


def assert_doc1(doc, meta, ext):
    """Asserts a document.

    :param object doc: Document being tested.
    :param object meta: Document meta information.
    :param object ext: Document extension information.

    """
    assert len(doc.meta.external_ids) == 1
    assert doc.meta.external_ids[0].is_open == True
    assert doc.meta.external_ids[0].value == 'MOHC_HadGEM2-ES_6.3 abrupt4xCO2'
    assert len(doc.meta.external_ids[0].standards) == 1
    assert doc.meta.external_ids[0].standards[0].name == 'QN_DRS'
    assert doc.meta.external_ids[0].standards[0].description.startswith('The QN_DRS value')

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
    assert doc.conformances[0].frequency in [None, '']
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
    assert doc.date_range.start == arrow.get('1859-12-01 00:00:00Z').datetime

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
    assert rp.email == 'mark.webb@metoffice.gov.uk'
    assert rp.individual_name == 'Mark Webb'
    assert rp.role == 'contact'

    assert len(doc.supports_references) == 1
    assert doc.supports_references[0].id == uuid.UUID('a0d3a554-d3a5-11df-837f-00163e9152a5')
    assert doc.supports_references[0].name == 'abrupt4xCO2'
    assert doc.supports_references[0].type == 'experiment'
    assert doc.supports_references[0].version == '1'
    assert doc.supports_references[0].description == 'Reference to an Experiment called abrupt4xCO2 with experimentNumber 6.3'


def update_doc(doc):
    """Update a document prior to republishing.

    :param object doc: Document being republished.

    """
    pass


def assert_doc_updates(doc):
    """Asserts a document after being updated.

    :param object doc: Document being tested.

    """
    pass