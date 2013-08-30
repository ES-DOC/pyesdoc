"""
.. module:: TODO - write module name
   :copyright: Copyright "Aug 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: TODO - write synopsis

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import inspect

import nose.tools

import pyesdoc
import pyesdoc_test.test_utils as tu


# Test ontology constants.
_CIM = 'cim'
_CIM_1 = '1'
_CIM_TYPE = 'modelComponent'

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/software.model_component.xml'



def test_import():
    assert inspect.ismodule(pyesdoc)
    

def test_decode():
    representation = tu.get_test_file(_TEST_FILE, 'xml')
    document = pyesdoc.decode(representation, _CIM, _CIM_1, 'xml')
    tu.assert_object(document, pyesdoc.ontologies.cim.v1.typeset.ModelComponent)


def test_encode():
    document = pyesdoc.create(_CIM, _CIM_1, _CIM_TYPE)
    tu.assert_object(document, pyesdoc.ontologies.cim.v1.typeset.ModelComponent)    


@nose.tools.raises(NotImplementedError)
def test_publish():
    raise NotImplementedError("TODO test publish")


@nose.tools.raises(NotImplementedError)
def test_unpublish():
    raise NotImplementedError("TODO test unpublish")


@nose.tools.raises(NotImplementedError)
def test_retrieve():
    raise NotImplementedError("TODO test retrieve")

def test_list_types():
    # supported - all
    types = pyesdoc.list_types()
    tu.assert_integer(len(types), 14)

    # supported - cim v1
    types = pyesdoc.list_types(_CIM, _CIM_1)
    tu.assert_integer(len(types), 14)

    # unsupported
    types = pyesdoc.list_types('x', 'x')
    tu.assert_integer(len(types), 0)


def test_is_supported_ontology():
    # supported
    assert pyesdoc.is_supported_ontology(_CIM, _CIM_1)

    # unsupported
    assert not pyesdoc.is_supported_ontology('x', _CIM_1)
    assert not pyesdoc.is_supported_ontology(_CIM, 'x')


def test_is_supported_type():
    # supported
    assert pyesdoc.is_supported_type(_CIM, _CIM_1, _CIM_TYPE)

    # unsupported
    assert not pyesdoc.is_supported_type('x', '1', 'x')
    assert not pyesdoc.is_supported_type(_CIM, 'x', 'x')
    assert not pyesdoc.is_supported_type(_CIM, _CIM_1, 'x')


def test_create():
    for ontology_name, ontology_version, type_name, type  in pyesdoc.list_types():
        instance = pyesdoc.create(ontology_name, ontology_version, type_name)
        # supported
        if type is not None:
            tu.assert_object(instance, type)
        # unsupported
        else:
            tu.assert_none(instance)


@nose.tools.raises(NotImplementedError)
def test_validate():
    raise NotImplementedError("TODO test validate")


@nose.tools.raises(NotImplementedError)
def test_is_valid():
    raise NotImplementedError("TODO test is_valid")


    