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


def _create_doc(ontology=_CIM,
                version=_CIM_V1,
                package=_CIM_PACKAGE,
                typeof=_CIM_TYPE):
    """Creates a test document."""
    type_key = ".".join([ontology, version, package, typeof])

    return pyesdoc.create(type_key, _INSTITUTE, _PROJECT)


def _assert_doc(doc, typeof=None):
    """Perform standard test document assertions."""
    tu.assert_object(doc, typeof)
    if hasattr(doc, 'meta'):
        tu.assert_str(doc.meta.institute, _INSTITUTE.lower())
        tu.assert_str(doc.meta.language, pyesdoc.ESDOC_DEFAULT_LANGUAGE)
        tu.assert_str(doc.meta.project, _PROJECT.lower())


def _test_module_setup(mod):
    """Test that the test document module is correctly setup."""
    tu.assert_bool(mod in tt.MODULES, True)
    tu.assert_bool(mod in tt.INITIAL_STATE, True)
    for field in tt.STATE_FIELDS:
        tu.assert_bool(hasattr(mod, field), True)


def _test_version():
    """Test package version."""
    tu.assert_str(pyesdoc.__version__, "0.9.0.3")


def _test_module_reset(mod):
    """Test that the test document modules are correctly reset."""
    # Assert module state is cached.
    assert mod in tt.INITIAL_STATE

    # Update state.
    for field in tt.STATE_FIELDS:
        setattr(mod, field, "XXX")
        tu.assert_str(getattr(mod, field), "XXX")

    # Reset.
    tt.reset(mod)

    # Assert initial state.
    for field in tt.STATE_FIELDS:
        state = tt.INITIAL_STATE[mod][field]
        assert getattr(mod, field) == state


def _test_module_file_open(mod):
    """Test opening module test files."""
    assert tu.get_test_file(mod.DOC_FILE) is not None


def _test_create_01():
    """Test creating documents - 1."""
    doc = _create_doc()
    _assert_doc(doc, pyesdoc.ontologies.cim.v1.ModelComponent)


def _test_create_02():
    """Test creating documents - 2."""
    for ontology, version, package, typeof in pyesdoc.list_types():
        doc = _create_doc(ontology, version, package, typeof)
        _assert_doc(doc)
        type_key = "{0}.{1}.{2}.{3}".format(ontology, version, package, typeof)
        tu.assert_str(doc.__class__.type_key, type_key)


def _test_create_03():
    """Test creating documents - 3."""
    for doc_type in pyesdoc.get_types():
        doc = pyesdoc.create(doc_type, _INSTITUTE, _PROJECT)
        _assert_doc(doc, doc_type)


def _test_import(mod):
    """Test module import."""
    assert inspect.ismodule(mod)


def test_imports_01():
    """Test importing packages - 1."""
    for mod in (
        pyesdoc,
        pyesdoc.constants,
        pyesdoc.factory,
        pyesdoc.io,
        pyesdoc.ontologies,
        pyesdoc.options,
        pyesdoc.parsing,
        pyesdoc.parsing.default,
        pyesdoc.parsing.parser,
        pyesdoc.publishing,
        pyesdoc.serialization,
        pyesdoc.utils,
        pyesdoc.utils.convert,
        pyesdoc.utils.functional,
        pyesdoc.utils.runtime,
        pyesdoc.validation,
        pyesdoc.validation.graph,
        pyesdoc.validation.validator,
        ):
        tu.init(_test_import, "import module", mod)
        yield _test_import, mod


def test_imports_02():
    """Test importing packages - 2."""
    cim = pyesdoc.ontologies.cim
    for mod in (
        cim,
        cim.v1,
        cim.v1.decoder,
        cim.v1.decoder_for_activity_package,
        cim.v1.decoder_for_data_package,
        cim.v1.decoder_for_grids_package,
        cim.v1.decoder_for_misc_package,
        cim.v1.decoder_for_quality_package,
        cim.v1.decoder_for_shared_package,
        cim.v1.decoder_for_software_package,
        cim.v1.typeset,
        cim.v1.typeset_for_activity_package,
        cim.v1.typeset_for_data_package,
        cim.v1.typeset_for_grids_package,
        cim.v1.typeset_for_misc_package,
        cim.v1.typeset_for_quality_package,
        cim.v1.typeset_for_shared_package,
        cim.v1.typeset_for_software_package,
        cim.v1.typeset_meta,
        ):
        tu.init(_test_import, "import cim module", mod)
        yield _test_import, mod


def _test_is_supported_ontology():
    """Test supported ontologies."""
    # supported
    assert pyesdoc.is_supported(_CIM, _CIM_V1)

    # unsupported
    assert not pyesdoc.is_supported('x', _CIM_V1)
    assert not pyesdoc.is_supported(_CIM, 'x')


def _test_is_supported_type_01():
    """Test supported ontology types - positive."""
    # supported
    assert pyesdoc.is_supported(_CIM, _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    for ontology, version, package, typeof in pyesdoc.list_types():
        assert pyesdoc.is_supported(ontology, version, package, typeof)


def _test_is_supported_type_02():
    """Test supported ontology types - negative."""
    # unsupported
    assert not pyesdoc.is_supported('x', _CIM_V1, _CIM_PACKAGE, _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, 'x', _CIM_PACKAGE, _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, _CIM_V1, 'x', _CIM_TYPE)
    assert not pyesdoc.is_supported(_CIM, _CIM_V1, _CIM_PACKAGE, 'x')


def _test_list_types():
    """Test listing supported types."""
    # supported - all
    types = pyesdoc.list_types()
    tu.assert_int(len(types), 103)

    # supported - cim v1
    types = pyesdoc.list_types(_CIM, _CIM_V1)
    tu.assert_int(len(types), 103)

    # unsupported
    types = pyesdoc.list_types('x', 'x')
    tu.assert_int(len(types), 0)


def _test_set_option_01():
    """Test setting package options - positive."""
    api_url = 'http://es-doc.org'
    api_url_old = pyesdoc.get_option('api_url')
    pyesdoc.set_option('api_url', api_url)
    tu.assert_str(api_url, pyesdoc.get_option('api_url'))
    pyesdoc.set_option('api_url', api_url_old)


@nose.tools.raises(pyesdoc.PYESDOC_Exception)
def _test_set_option_02():
    """Test setting package options - negative."""
    pyesdoc.set_option('xxx', 'xxx')


def test():
    """Runs set of geenral unit tests."""
    for mod in tt.MODULES:
        tu.init(_test_module_file_open, 'open document module test file', mod)
        yield _test_module_file_open, mod

    for mod in tt.MODULES:
        tu.init(_test_module_reset, 'document module reset', mod)
        yield _test_module_reset, mod

    for mod in tt.MODULES:
        tu.init(_test_module_setup, 'document module setup', mod)
        yield _test_module_setup, mod

    for func in (
        _test_version,
        _test_set_option_01,
        _test_set_option_02,
        _test_is_supported_ontology,
        _test_is_supported_type_01,
        _test_is_supported_type_02,
        _test_list_types,
        _test_create_01,
        _test_create_02,
        _test_create_03,
        ):
        tu.init(func, func.__doc__[5:])
        yield func

