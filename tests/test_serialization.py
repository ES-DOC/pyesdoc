import pyesdoc
from . import (
    test_utils as tu,
    test_type_cim_v1_activity_ensemble,
    test_type_cim_v1_activity_numerical_experiment,
    test_type_cim_v1_activity_simulation_run,
    test_type_cim_v1_data_data_object,
    test_type_cim_v1_grids_gridspec,
    test_type_cim_v1_misc_document_set,
    test_type_cim_v1_quality_cim_quality,
    test_type_cim_v1_shared_platform,
    test_type_cim_v1_software_model_component,
    test_type_cim_v1_software_statistical_model_component
    )



# Set of type test modules.
_test_modules = (
    # test_type_cim_v1_activity_ensemble,
    # test_type_cim_v1_activity_numerical_experiment,
    # test_type_cim_v1_activity_simulation_run,
    # test_type_cim_v1_data_data_object,
    # test_type_cim_v1_grids_gridspec,
    test_type_cim_v1_misc_document_set,    
    # test_type_cim_v1_quality_cim_quality,
    # test_type_cim_v1_shared_platform,
    # test_type_cim_v1_software_model_component,
    # test_type_cim_v1_software_statistical_model_component,
)

def _assert_doc(tm, doc):
    assert isinstance(doc, tm.DOC_TYPE), "Decoded type mismatch"
    tu.assert_pyesdoc_obj(doc, tm.DOC_UID, tm.DOC_VERSION, tm.DOC_DATE)
    tm.assert_doc(doc)


def _create_doc(tm):
    """Creates a document from a cmip5 file emitted by Metafor cmip5 questionnaire."""
    doc = tu.decode_from_xml_metafor_cim_v1(tm.DOC_FILE, tm.DOC_TYPE)
    doc.doc_info.project = 'cmip5'
    doc.doc_info.source = 'testing'
    _assert_doc(tm, doc)

    return doc


def _test_open_file(tm):
    assert tu.get_test_file(tm.DOC_FILE) is not None

    
def _test_serialization(tm, encoding):
    doc_1 = _create_doc(tm)
    repr_1 = tu.encode(doc_1, encoding)
    doc_2 = tu.decode(repr_1, encoding)
    # assert tu.encode(doc_2, encoding) == repr_1
    _assert_doc(tm, doc_2)

        
def _test_serialization_html(tm, encoding):
    doc = _create_doc(tm)
    html = tu.encode(doc, encoding)


def test():
    for tm in _test_modules:
        _test_open_file.description = "{0}.test_open_file".format(tm.__name__)
        yield _test_open_file, tm        
        for encoding in pyesdoc.ESDOC_ENCODINGS:
            f = _test_serialization_html if encoding == pyesdoc.ESDOC_ENCODING_HTML else _test_serialization
            f.description = "{0}.test_serialize.{1}".format(tm.__name__, encoding)
            yield f, tm, encoding


