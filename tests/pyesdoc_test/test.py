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
_CIM_V1 = '1'
_CIM_PACKAGE = 'software'
_CIM_TYPE = 'modelComponent'

# Test representation file.
_TEST_FILE = 'cim/v1_5_0/software.model_component.xml'



def test_import():
    assert inspect.ismodule(pyesdoc)
    

def _test_decode(encoding, type):
    as_xml_metafor = tu.get_test_file(_TEST_FILE, 'xml')
    doc1 = pyesdoc.decode(as_xml_metafor, pyesdoc.METAFOR_CIM_XML_ENCODING)
    tu.assert_object(doc1, type)

    as_dict = pyesdoc.encode(doc1, encoding)
    doc2 = pyesdoc.decode(as_dict, encoding)
    tu.assert_object(doc2, type)


def test_decode_dict():
    _test_decode(pyesdoc.ESDOC_ENCODING_DICT,
                 pyesdoc.ontologies.cim.v1.typeset.ModelComponent)


def test_decode_json():
    _test_decode(pyesdoc.ESDOC_ENCODING_JSON,
                 pyesdoc.ontologies.cim.v1.typeset.ModelComponent)


@nose.tools.raises(NotImplementedError)
def test_decode_xml():
    _test_decode(pyesdoc.ESDOC_ENCODING_XML,
                 pyesdoc.ontologies.cim.v1.typeset.ModelComponent)


@nose.tools.raises(NotImplementedError)
def test_decode_xml_metafor_cim_v1():
    _test_decode(pyesdoc.METAFOR_CIM_XML_ENCODING,
                 pyesdoc.ontologies.cim.v1.typeset.ModelComponent)


def _test_encode(encoding, type):
    doc = pyesdoc.create(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    repr = pyesdoc.encode(doc, encoding)
    tu.assert_object(repr, type)
    

def test_encode_dict():
    _test_encode(pyesdoc.ESDOC_ENCODING_DICT, dict)


def test_encode_json():
    _test_encode(pyesdoc.ESDOC_ENCODING_JSON, str)


def test_encode_xml():
    _test_encode(pyesdoc.ESDOC_ENCODING_XML, str)


@nose.tools.raises(NotImplementedError)
def test_encode_xml_metafor_cim_v1():
    _test_encode(pyesdoc.METAFOR_CIM_XML_ENCODING, str)


def test_encode():
    doc = pyesdoc.create(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    as_dict = pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_DICT)
    tu.assert_object(as_dict, dict)
    as_json = pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_JSON)
    tu.assert_object(as_json, str)
    as_xml = pyesdoc.encode(doc, pyesdoc.ESDOC_ENCODING_XML)
    tu.assert_object(as_xml, str)


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
    tu.assert_integer(len(types), 102)

    # supported - cim v1
    types = pyesdoc.list_types(_CIM, _CIM_V1)
    tu.assert_integer(len(types), 102)

    # unsupported
    types = pyesdoc.list_types('x', 'x')
    tu.assert_integer(len(types), 0)


def test_is_supported_ontology():
    # supported
    assert pyesdoc.is_supported(_CIM, _CIM_V1)

    # unsupported
    assert not pyesdoc.is_supported('x', _CIM_V1)
    assert not pyesdoc.is_supported(_CIM, 'x')


def test_is_supported_type():
    # supported
    assert pyesdoc.is_supported(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)

    # unsupported
    assert not pyesdoc.is_supported('x', _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, 'x', _CIM_PACKAGE, _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, _CIM_V1, 'x', _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, _CIM_V1, _CIM_PACKAGE, 'x')


def test_create():
    instance = pyesdoc.create(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    tu.assert_object(instance, pyesdoc.ontologies.cim.v1.typeset.ModelComponent)    

    for o, v, p, t in pyesdoc.list_types():
        instance = pyesdoc.create(o, v, p, t)
        tu.assert_object(instance)
        tu.assert_string(instance.type_key.lower(),
                         "{0}.{1}.{2}.{3}".format(o, v, p, t).lower())


@nose.tools.raises(NotImplementedError)
def test_validate():
    raise NotImplementedError("TODO test validate")


@nose.tools.raises(NotImplementedError)
def test_is_valid():
    raise NotImplementedError("TODO test is_valid")


    