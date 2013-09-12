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
DOC_FILE = 'cim/v1_5_0/software.model_component.xml'



def test_create_01():
    doc = pyesdoc.create(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    tu.assert_object(doc, pyesdoc.ontologies.cim.v1.typeset.ModelComponent)
    tu.assert_string(doc.doc_info.language, pyesdoc.ESDOC_DEFAULT_LANGUAGE)


def test_create_02():
    for o, v, p, t in pyesdoc.list_types():
        doc = pyesdoc.create(o, v, p, t)
        tu.assert_object(doc)
        if hasattr(doc, 'doc_info'):
            tu.assert_string(doc.doc_info.language, pyesdoc.ESDOC_DEFAULT_LANGUAGE)
        tu.assert_string(doc.__class__.type_key, "{0}.{1}.{2}.{3}".format(o, v, p, t))


def test_import():
    assert inspect.ismodule(pyesdoc)


def test_is_supported_ontology():
    # supported
    assert pyesdoc.is_supported(_CIM, _CIM_V1)

    # unsupported
    assert not pyesdoc.is_supported('x', _CIM_V1)
    assert not pyesdoc.is_supported(_CIM, 'x')


def test_is_supported_type_01():
    # supported
    assert pyesdoc.is_supported(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    for o, v, p, t in pyesdoc.list_types():
        assert pyesdoc.is_supported(o, v, p, t)


def test_is_supported_type_02():
    # unsupported
    assert not pyesdoc.is_supported('x', _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, 'x', _CIM_PACKAGE, _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, _CIM_V1, 'x', _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, _CIM_V1, _CIM_PACKAGE, 'x')


@nose.tools.raises(NotImplementedError)
def test_is_valid():
    raise NotImplementedError("TODO test is_valid")


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


def test_set_institute():
    doc = pyesdoc.create(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    tu.assert_string(doc.doc_info.institute, '')
    pyesdoc.set_institute(doc, "TEST")
    tu.assert_string(doc.doc_info.institute, "TEST".lower())


def test_set_project():
    doc = pyesdoc.create(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    tu.assert_string(doc.doc_info.project, '')
    pyesdoc.set_project(doc, "TEST")
    tu.assert_string(doc.doc_info.project, "TEST".lower())


@nose.tools.raises(NotImplementedError)
def test_validate():
    raise NotImplementedError("TODO test validate")


