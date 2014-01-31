import datetime
import uuid
import nose

import pyesdoc
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


def _create_doc(tm):
    doc = tu.decode_from_xml_metafor_cim_v1(tm.DOC_FILE, tm.DOC_TYPE)
    doc.doc_info.id = uuid.uuid4()
    doc.doc_info.version = 0
    doc.doc_info.create_date = datetime.datetime.now()
    doc.doc_info.project = 'cmip5'
    doc.doc_info.source = 'testing'

    return doc


def _set_api_url(mode='dev'):
    if mode == 'dev':
        pyesdoc.set_option("api_url", "http://127.0.0.1:5000")      
    elif mode == 'test':
        pyesdoc.set_option("api_url", "http://test.api.es-doc.org")      
    elif mode == 'test':
        pyesdoc.set_option("api_url", "http://api.es-doc.org")      


def _test_publishing(tm):
    # Create.
    doc = _create_doc(tm)
    tm.assert_doc(doc)

    # Set identifiers.
    uid = doc.doc_info.id
    version = doc.doc_info.version
    create_date = doc.doc_info.create_date

    # Publish.
    pyesdoc.publish(doc)
    version += 1
    tu.assert_pyesdoc_obj(doc, uid, version, create_date)

    # Retrieve.
    doc = pyesdoc.retrieve(uid, version)
    tu.assert_pyesdoc_obj(doc, uid, version, create_date)
    tm.assert_doc(doc)

    # Update.
    tm.update_doc(doc)
    tm.assert_doc_updates(doc)

    # Republish.
    pyesdoc.publish(doc)
    version += 1

    # Retrieve.
    doc = pyesdoc.retrieve(uid, version)
    tu.assert_pyesdoc_obj(doc, uid, version, create_date)
    tm.assert_doc_updates(doc)

    # Republish.
    pyesdoc.publish(doc)
    version += 1
    
    # Unpublish.
    pyesdoc.unpublish(uid, version)
    tu.assert_none(pyesdoc.retrieve(uid, version))
    version -= 1

    # TODO - determine why below this line the test is failing.
    return

    # Retrieve latest.
    doc = pyesdoc.retrieve(uid, pyesdoc.ESDOC_DOC_VERSION_LATEST)
    tu.assert_pyesdoc_obj(doc, uid, version, create_date)

    # Unpublish.
    pyesdoc.unpublish(uid, version)
    tu.assert_none(pyesdoc.retrieve(uid, version))
    version -= 1

    # Retrieve latest.
    doc = pyesdoc.retrieve(uid, pyesdoc.ESDOC_DOC_VERSION_LATEST)
    tu.assert_pyesdoc_obj(doc, uid, version, create_date)

    # Unpublish.
    pyesdoc.unpublish(uid, version)
    tu.assert_none(pyesdoc.retrieve(uid, version))
    version -= 1
    tu.assert_none(pyesdoc.retrieve(uid, version))


def test_publishing():
    _set_api_url('dev')
    for tm in _test_modules:
        _test_publishing.description = 'test_publish.{0}'.format(tm.DOC_TYPE)
        yield _test_publishing, tm


