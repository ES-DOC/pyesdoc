"""
.. module:: TODO - write module name
   :copyright: Copyright "Sep 4, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: TODO - write synopsis

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
import uuid

import pyesdoc
import pyesdoc.ontologies.cim as cim
import pyesdoc_test.test_utils as tu



_TEST_DOC_UID = '309f6a26-e2b3-11df-bf17-00163e9152a5'
_TEST_DOC_UUID = uuid.UUID(_TEST_DOC_UID)
_TEST_DOC_VERSION = 3
_TEST_DOC_DATE = '2013-01-02 16:45:04.068790'
_TEST_DOC_TYPE = cim.v1.ModelComponent


def _assert_test_doc(doc):
    tu.assert_pyesdoc_obj(doc, _TEST_DOC_UID, _TEST_DOC_VERSION, _TEST_DOC_DATE)
    

def _retrieve(uid, version, type, err_type=None):
    doc = None
    try:
        doc = pyesdoc.retrieve(uid, version)
        if type is not None:
            tu.assert_object(doc, type)
        else:
            tu.assert_none(doc)
    except BaseException as e:
        if not isinstance(e, err_type):
            raise e
    if doc is not None:
        _assert_test_doc(doc)

        

def test_retrieve():        
    yield _retrieve, _TEST_DOC_UID, _TEST_DOC_VERSION, _TEST_DOC_TYPE
    yield _retrieve, _TEST_DOC_UUID, _TEST_DOC_VERSION, _TEST_DOC_TYPE
    yield _retrieve, _TEST_DOC_UID, '3', _TEST_DOC_TYPE
    yield _retrieve, _TEST_DOC_UID, 999, None
    yield _retrieve, 'XXXX', _TEST_DOC_VERSION, None, ValueError
    yield _retrieve, _TEST_DOC_UID, 'XXX', None, ValueError


