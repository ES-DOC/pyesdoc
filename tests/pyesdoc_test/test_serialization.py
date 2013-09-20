import pyesdoc
import pyesdoc_test.test_utils as tu
import test_type_cim_v1_5_0_activity_ensemble
import test_type_cim_v1_5_0_activity_numerical_experiment
import test_type_cim_v1_5_0_activity_simulation_run
import test_type_cim_v1_5_0_data_data_object
import test_type_cim_v1_5_0_grids_gridspec
import test_type_cim_v1_5_0_quality_cim_quality
import test_type_cim_v1_5_0_shared_platform
import test_type_cim_v1_5_0_software_model_component
import test_type_cim_v1_8_1_activity_numerical_experiment
import test_type_cim_v1_8_1_software_statistical_model_component


# Set of type test modules.
_test_modules = (
    test_type_cim_v1_5_0_activity_ensemble,
    test_type_cim_v1_5_0_activity_numerical_experiment,
    test_type_cim_v1_5_0_activity_simulation_run,
    test_type_cim_v1_5_0_data_data_object,
    test_type_cim_v1_5_0_grids_gridspec,
    test_type_cim_v1_5_0_quality_cim_quality,
    test_type_cim_v1_5_0_shared_platform,
    test_type_cim_v1_5_0_software_model_component,
    test_type_cim_v1_8_1_activity_numerical_experiment,
    test_type_cim_v1_8_1_software_statistical_model_component,
)

_test_modules = (
    test_type_cim_v1_5_0_software_model_component,
)


def _create_doc(tm):
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
    if encoding not in (pyesdoc.ESDOC_ENCODING_XML):
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


