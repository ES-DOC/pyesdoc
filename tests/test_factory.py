# -*- coding: utf-8 -*-

"""
.. module:: test_general.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc general tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import pyesdoc
from pyesdoc.ontologies import cim
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
        tu.assert_str(doc.meta.source, _INSTITUTE.lower())
        if typeof is not None:
            tu.assert_str(doc.meta.type, typeof.type_key)


def _test_create_01():
    """Test creating documents - 1."""
    doc = _create_doc()

    _assert_doc(doc, cim.v1.ModelComponent)


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


def test():
    """Runs set of factory unit tests."""
    for func in (
        _test_create_01,
        _test_create_02,
        _test_create_03,
        ):
        tu.init(func, func.__doc__[5:])
        yield func