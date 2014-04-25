"""
.. module:: test_general.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc general tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import inspect

import nose.tools

import pyesdoc
import pyesdoc.ontologies.cim as cim
import test_utils as tu
import test_types as tt



# Test ontology constants.
_CIM = 'cim'
_CIM_V1 = '1'
_CIM_PACKAGE = 'software'
_CIM_TYPE = 'modelComponent'

# Test constants.
_INSTITUTE = 'TEST'
_PROJECT = 'TEST'


def _create_doc(o=_CIM, v=_CIM_V1, p=_CIM_PACKAGE, t=_CIM_TYPE):
    return pyesdoc.create(".".join([o, v, p, t]), _INSTITUTE, _PROJECT)


def _assert_doc(doc, type=None):
    tu.assert_object(doc, type)
    if hasattr(doc, 'meta'):
        tu.assert_str(doc.meta.institute, _INSTITUTE.lower())
        tu.assert_str(doc.meta.language, pyesdoc.ESDOC_DEFAULT_LANGUAGE)
        tu.assert_str(doc.meta.project, _PROJECT.lower())


def _test_open_file(mod):
    assert tu.get_test_file(mod.DOC_FILE) is not None


def _test_module_setup(mod):
    """Tests that the test document module is correctly setup."""
    tu.assert_bool(mod in tt.MODULES, True)
    tu.assert_bool(mod in tt.INITIAL_STATE, True)
    for field in tt.STATE_FIELDS:
        tu.assert_bool(hasattr(mod, field), True)


def _test_module_reset(mod):
    """Tests that the test document module is correctly reset."""
    pass


def test_version():
    """Test package version."""
    tu.assert_str(pyesdoc.__version__, "0.9.0.3")


def test_module_setup():
    """Tests that the test document modules are correctly setup."""
    for mod in tt.MODULES:
        _test_module_setup.description = "ES-DOC :: Test module setup - {0}".format(mod.__name__.split('.')[1])
        yield _test_module_setup, mod


def test_module_reset():
    """Tests that the test document modules are correctly reset."""
    for mod in tt.MODULES:
        _test_module_reset.description = "ES-DOC :: Test module reset - {0}".format(mod.__name__.split('.')[1])
        yield _test_module_reset, mod


def test_open_files():
    """Test opening test files."""
    for mod in tt.MODULES:
        _test_open_file.description = "{0}.test_open_file".format(mod.__name__)
        assert tu.get_test_file(mod.DOC_FILE) is not None


def test_create_01():
    """Test creating documents - 1."""
    doc = _create_doc()
    _assert_doc(doc, cim.v1.ModelComponent)


def test_create_02():
    """Test creating documents - 2."""
    for o, v, p, t in pyesdoc.list_types():
        doc = _create_doc(o, v, p, t)
        _assert_doc(doc)
        tu.assert_str(doc.__class__.type_key, "{0}.{1}.{2}.{3}".format(o, v, p, t))


def test_create_03():
    """Test creating documents - 3."""
    for type in pyesdoc.get_types():
        doc = pyesdoc.create(type, _INSTITUTE, _PROJECT)
        _assert_doc(doc, type)


def test_import_01():
    """Test importing package - 1."""
    assert inspect.ismodule(pyesdoc)
    assert inspect.ismodule(pyesdoc.ontologies.cim)


def test_import_02():
    """Test importing package - 2."""
    import pyesdoc.ontologies.cim
    import pyesdoc.ontologies.cim.v1
    import pyesdoc.ontologies.cim.v1.decoder_for_activity_package
    import pyesdoc.ontologies.cim.v1.decoder_for_data_package
    import pyesdoc.ontologies.cim.v1.decoder_for_grids_package
    import pyesdoc.ontologies.cim.v1.decoder_for_quality_package
    import pyesdoc.ontologies.cim.v1.decoder_for_shared_package
    import pyesdoc.ontologies.cim.v1.decoder_for_software_package


def test_is_supported_ontology():
    """Test supported ontologies."""
    # supported
    assert pyesdoc.is_supported(_CIM, _CIM_V1)

    # unsupported
    assert not pyesdoc.is_supported('x', _CIM_V1)
    assert not pyesdoc.is_supported(_CIM, 'x')


def test_is_supported_type_01():
    """Test supported ontology types - positive."""
    # supported
    assert pyesdoc.is_supported(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    for o, v, p, t in pyesdoc.list_types():
        assert pyesdoc.is_supported(o, v, p, t)


def test_is_supported_type_02():
    """Test supported ontology types - negative."""
    # unsupported
    assert not pyesdoc.is_supported('x', _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, 'x', _CIM_PACKAGE, _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, _CIM_V1, 'x', _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, _CIM_V1, _CIM_PACKAGE, 'x')


def test_list_types():
    """Test listing of supported types."""
    # supported - all
    types = pyesdoc.list_types()
    tu.assert_int(len(types), 103)

    # supported - cim v1
    types = pyesdoc.list_types(_CIM, _CIM_V1)
    tu.assert_int(len(types), 103)

    # unsupported
    types = pyesdoc.list_types('x', 'x')
    tu.assert_int(len(types), 0)


def test_set_option_01():
    """Test setting package options - positive."""
    api_url = 'http://es-doc.org'
    api_url_old = pyesdoc.get_option('api_url')
    pyesdoc.set_option('api_url', api_url)
    tu.assert_str(api_url, pyesdoc.get_option('api_url'))
    pyesdoc.set_option('api_url', api_url_old)


@nose.tools.raises(pyesdoc.PYESDOC_Exception)
def test_set_option_02():
    """Test setting package options - negative."""
    pyesdoc.set_option('xxx', 'xxx')
