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


def _create_doc(tm):
    """Creates a document from a cmip5 file emitted by Metafor cmip5 questionnaire."""
    doc = tu.decode_from_xml_metafor_cim_v1(tm.DOC_FILE, tm.DOC_TYPE)
    doc.doc_info.project = 'cmip5'
    doc.doc_info.source = 'testing'

    return doc


def _test_open_file(tm):
    assert tu.get_test_file(tm.DOC_FILE) is not None

    
def _test_serialization(tm, encoding):
    doc = _create_doc(tm)
    tu.assert_pyesdoc_obj(doc, tm.DOC_UID, tm.DOC_VERSION, tm.DOC_DATE)
    tm.assert_doc(doc)
    repr = tu.encode(doc, encoding)
    doc = tu.decode(repr, encoding)
    assert isinstance(doc, tm.DOC_TYPE), "Decoded type mismatch"
    tm.assert_doc(doc)

        
def test():
    for tm in _test_modules:
        _test_open_file.description = "{0}.test_open_file".format(tm.__name__)
        yield _test_open_file, tm        
        for encoding in pyesdoc.ESDOC_ENCODINGS:
            _test_serialization.description = "{0}.test_serialize.{1}".format(tm.__name__, encoding)
            yield _test_serialization, tm, encoding


