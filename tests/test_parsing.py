import nose

import pyesdoc
import test_utils as tu
import test_types as tt



def test_custom_parser_count():
    tu.assert_collection(pyesdoc.parsers.supported, length=7)


def test_is_custom_parseable():
    for dt in pyesdoc.ontologies.get_types():
        if dt.type_key.lower() in pyesdoc.parsers.supported:
            assert pyesdoc.is_parseable(dt.type_key)
        else:
            assert pyesdoc.is_parseable(dt.type_key) == False


def _test_parsing(tm):
    tu.get_doc(tm)


def test_all():
    for tm in tt.MODULES:
        desc = "test_standard_parse.{0}".format(tm.__name__.split(".")[-1])
        _test_parsing.description = desc
        yield _test_parsing, tm


def test_parsing_cim_v1_activity_ensemble():
    doc = tu.get_doc(tt.test_type_cim_v1_activity_ensemble)
    # TODO assert parsed attributes

def test_parsing_cim_v1_activity_numerical_experiment():
    doc = tu.get_doc(tt.test_type_cim_v1_activity_numerical_experiment)
    # TODO assert parsed attributes

def test_parsing_cim_v1_activity_simulation_run():
    doc = tu.get_doc(tt.test_type_cim_v1_activity_simulation_run)
    # TODO assert parsed attributes
    
def test_parsing_cim_v1_data_data_object():
    doc = tu.get_doc(tt.test_type_cim_v1_data_data_object)
    # TODO assert parsed attributes
    
def test_parsing_cim_v1_grids_gridspec():
    doc = tu.get_doc(tt.test_type_cim_v1_grids_gridspec)
    # TODO assert parsed attributes
    
def test_parsing_cim_v1_misc_document_set():
    # TODO
    pass

def test_parsing_cim_v1_quality_cim_quality():
    doc = tu.get_doc(tt.test_type_cim_v1_quality_cim_quality)
    # TODO assert parsed attributes
    
def test_parsing_cim_v1_shared_platform():
    doc = tu.get_doc(tt.test_type_cim_v1_shared_platform)
    # TODO assert parsed attributes
    
def test_parsing_cim_v1_software_model_component():
    doc = tu.get_doc(tt.test_type_cim_v1_software_model_component)
    # TODO assert parsed attributes

    # tu.assert_collection(doc._component_tree, 25)
    # for c in doc._component_tree:
    #     tu.assert_collection(c._property_tree)

def test_parsing_cim_v1_software_statistical_model_component():
    # TODO
    pass
