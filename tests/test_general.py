import inspect

import nose.tools

import pyesdoc
import pyesdoc.ontologies.cim as cim
from . import test_utils as tu



# Test ontology constants.
_CIM = 'cim'
_CIM_V1 = '1'
_CIM_PACKAGE = 'software'
_CIM_TYPE = 'modelComponent'

# Test constants.
_INSTITUTE = 'TEST'
_PROJECT = 'TEST'

# Test representation file.
DOC_FILE = 'cim/v1_5_0/software.model_component.xml'


def _create_doc(o=_CIM, v=_CIM_V1, p=_CIM_PACKAGE, t=_CIM_TYPE):
    return pyesdoc.create(".".join([o, v, p, t]), _INSTITUTE, _PROJECT)


def _assert_doc(doc, type=None):
    tu.assert_object(doc, type)
    if hasattr(doc, 'doc_info'):
        tu.assert_string(doc.doc_info.institute, _INSTITUTE.lower())
        tu.assert_string(doc.doc_info.language, pyesdoc.ESDOC_DEFAULT_LANGUAGE)
        tu.assert_string(doc.doc_info.project, _PROJECT.lower())


def test_version():
    tu.assert_string(pyesdoc.__version__, "0.9.0.2")


def test_create_01():
    doc = _create_doc()
    _assert_doc(doc, cim.v1.ModelComponent)


def test_create_02():
    for o, v, p, t in pyesdoc.list_types():
        doc = _create_doc(o, v, p, t)
        _assert_doc(doc)
        tu.assert_string(doc.__class__.type_key, "{0}.{1}.{2}.{3}".format(o, v, p, t))


def test_create_03():
    for type in pyesdoc.get_types():
        doc = pyesdoc.create(type, _INSTITUTE, _PROJECT)
        _assert_doc(doc, type)


def test_import_01():
    assert inspect.ismodule(pyesdoc)
    assert inspect.ismodule(pyesdoc.ontologies.cim)


def test_import_02():
    import pyesdoc.ontologies.cim
    import pyesdoc.ontologies.cim.v1
    import pyesdoc.ontologies.cim.v1.decoder_for_activity_package
    import pyesdoc.ontologies.cim.v1.decoder_for_data_package
    import pyesdoc.ontologies.cim.v1.decoder_for_grids_package
    import pyesdoc.ontologies.cim.v1.decoder_for_quality_package
    import pyesdoc.ontologies.cim.v1.decoder_for_shared_package
    import pyesdoc.ontologies.cim.v1.decoder_for_software_package


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
    tu.assert_integer(len(types), 103)

    # supported - cim v1
    types = pyesdoc.list_types(_CIM, _CIM_V1)
    tu.assert_integer(len(types), 103)

    # unsupported
    types = pyesdoc.list_types('x', 'x')
    tu.assert_integer(len(types), 0)


@nose.tools.raises(NotImplementedError)
def test_validate():
    raise NotImplementedError("TODO test validate")


def test_set_option_01():
    api_url = 'http://es-doc.org'
    api_url_old = pyesdoc.get_option('api_url')
    pyesdoc.set_option('api_url', api_url)
    tu.assert_string(api_url, pyesdoc.get_option('api_url'))
    pyesdoc.set_option('api_url', api_url_old)
    

@nose.tools.raises(pyesdoc.PYESDOC_Exception)
def test_set_option_02():
    pyesdoc.set_option('xxx', 'xxx')
