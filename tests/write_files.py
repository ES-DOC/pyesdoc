import pyesdoc
import pyesdoc.ontologies.cim as cim
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


# Output folder.
OP = '/Users/markmorgan/Development/sourcetree/esdoc/esdoc-py-client/tests/pyesdoc_test/files'


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
    test_type_cim_v1_software_statistical_model_component,
)


def _get_file_name(type, encoding):
    path = OP
    path += '/'
    path += encoding
    path += '/'
    path += type.type_key
    path += '.'
    if encoding == pyesdoc.METAFOR_CIM_XML_ENCODING:
        path += pyesdoc.ESDOC_ENCODING_XML
    else:
        path += encoding

    return path


def _write_file(doc, encoding):
    with open(_get_file_name(doc.__class__, encoding), 'w') as f:
        f.write(pyesdoc.encode(doc, encoding))

    
for tm in _test_modules:
    doc = tu.decode_from_xml_metafor_cim_v1(tm.DOC_FILE, tm.DOC_TYPE)
    for encoding in (pyesdoc.ESDOC_ENCODING_XML, pyesdoc.ESDOC_ENCODING_JSON):
        _write_file(doc, encoding)
