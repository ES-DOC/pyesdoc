import nose

import pyesdoc
from . import (
    test_utils as tu,
    test_type_cim_v1_activity_ensemble,
    test_type_cim_v1_activity_numerical_experiment,
    test_type_cim_v1_activity_simulation_run,
    test_type_cim_v1_data_data_object,
    test_type_cim_v1_grids_gridspec,
    test_type_cim_v1_quality_cim_quality,
    test_type_cim_v1_shared_platform,
    test_type_cim_v1_software_model_component,
    test_type_cim_v1_software_statistical_model_component
    )



# Set of type test modules.
_test_modules = (
    test_type_cim_v1_activity_ensemble,
    test_type_cim_v1_activity_numerical_experiment,
    test_type_cim_v1_activity_simulation_run,
    test_type_cim_v1_data_data_object,
    test_type_cim_v1_grids_gridspec,
    test_type_cim_v1_quality_cim_quality,
    test_type_cim_v1_shared_platform,
    test_type_cim_v1_software_model_component,
    # test_type_cim_v1_software_statistical_model_component,
)


def _assert_doc(tm, doc):
    assert isinstance(doc, tm.DOC_TYPE), "Decoded type mismatch"
    tu.assert_pyesdoc_obj(doc, tm.DOC_UID, tm.DOC_VERSION, tm.DOC_DATE)
    tm.assert_doc(doc)


def _create_doc(tm):
    """Creates a test document."""
    doc = tu.decode_from_xml_metafor_cim_v1(tm.DOC_FILE, tm.DOC_TYPE)
    doc.doc_info.project = 'cmip5'
    doc.doc_info.source = 'testing'
    _assert_doc(tm, doc)

    return doc


def _parse_doc(tm):
    doc = _create_doc(tm)
    pyesdoc.parse(doc)

    return doc


def test_parser_count():
    tu.assert_collection(pyesdoc.parsers.supported, 1)


def test_is_parseable():
    for doc_type in pyesdoc.parsers.supported.keys():
        assert pyesdoc.is_parseable(doc_type)


def test_parsers():
    for tm in _test_modules:
        _parse_doc(tm)


def test_parser_cim_v1_software_model_component():
    doc = _parse_doc(test_type_cim_v1_software_model_component)

    tu.assert_collection(doc._component_tree, 25)
    for c in doc._component_tree:
        tu.assert_collection(c._property_tree)
