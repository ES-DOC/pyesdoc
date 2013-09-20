"""
.. module:: pyesdoc.publishing.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document publishing functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import uuid

import requests

from . import utils
from . import options
from . import serialization
from . validation import is_valid



# API url option name.
_OPT_API_URL = 'api_url'

# Publishing API endpoint.
_EP_PUBLISHING = 'publishing'

# HTTP response codes.
HTTP_RESPONSE_STATUS_200 = 200
HTTP_RESPONSE_STATUS_404 = 404
HTTP_RESPONSE_STATUS_500 = 500

# Latest document version label.
ESDOC_DOC_VERSION_LATEST = 'latest'

# All document versions label.
ESDOC_DOC_VERSION_ALL = 'all'


def _assert_doc(doc, msg):
    """Asserts document instance."""
    if doc is None:
        _raise(msg if msg is not None else "Document instance is null.")


def _raise(msg):
    """Raise exception."""
    raise utils.PYESDOC_Exception(msg)


def _raise_connection_error():
    _raise("Could not connect to remote API server.")


def _raise_http_error():
    _raise("Invalid HTTP response from remote API server.")


def _raise_timeout_error():
    _raise("Remote API server connection timed out.")


def _invoke(op, url, data=None):
    try:
        if data is not None:
            return op(url, data=data)
        else:
            return op(url)
    except requests.ConnectionError:
        _raise_connection_error()
    except requests.HTTPError:
        _raise_http_error()
    except requests.Timeout:
        _raise_timeout_error()
    

def _get_api_url(ep):
    """Helper function to return api endpoint url."""
    return options.get(_OPT_API_URL) + '/1/{0}'.format(ep)


def retrieve(uid, version):
    """Retrieves a document from remote repository.

    :param uid: Document unique identifier.
    :type uid: str or uuid.UUID

    :param version: Document unique identifier.
    :type version: str or uuid.UUID

    :returns: A document from remote repository.
    :rtype: object or None

    """
    # Defensive programming.
    if not isinstance(uid, uuid.UUID):
        _raise("Invalid document uid (must be an instance of uuid.UUID).")
    if version != ESDOC_DOC_VERSION_LATEST and not isinstance(version, int):
        _raise("Invalid document version (must be either 'latest' or an integer.")

    # Set HTTP operation parameters.
    url = _get_api_url(_EP_PUBLISHING)
    url += '/{0}'.format(uid)
    if version is not None:
        url += '/{0}'.format(version)

    # Issue HTTP GET.
    r = _invoke(requests.get, url)

    # Process HTTP response code.
    if r.status_code == HTTP_RESPONSE_STATUS_200 and len(r.text):
        return serialization.decode(r.json(), serialization.ESDOC_ENCODING_DICT)
    elif r.status_code == HTTP_RESPONSE_STATUS_404:
        _raise("XXXX :: {0}-v{1}".format(uid, version))
    elif r.status_code == HTTP_RESPONSE_STATUS_500:
        _raise("Document retrieval server side failure")


def publish(doc):
    """Publishes a document to remote repository.

    :param doc: Document being published.
    :type doc: object

    :returns: Updated document.
    :rtype: object

    """
    # Defensive programming.
    if doc is None:
        _raise("Cannot publish null documents.")
    if not is_valid(doc):
        _raise("Cannot publish invalid documents.")
        
    # Increment version.
    doc.doc_info.version += 1

    # Set HTTP operation parameters.
    url = _get_api_url(_EP_PUBLISHING)
    data = serialization.encode(doc, serialization.ESDOC_ENCODING_JSON)


    # Invoke HTTP operation.
    r = _invoke(requests.post, url, data)

    # Process HTTP response code.
    if r.status_code == HTTP_RESPONSE_STATUS_500:
        _raise("Document publishing server side failure")


def unpublish(uid, version):
    """Unpublishes a document from remote repository.

    :param doc: Document being unpublished.
    :type doc: object

    """
    # Defensive programming.
    if not isinstance(uid, uuid.UUID):
        _raise("Invalid document uid (must be an instance of uuid.UUID).")
    if not version == ESDOC_DOC_VERSION_ALL and \
       not version == ESDOC_DOC_VERSION_LATEST and \
       not isinstance(version, int):
        _raise("Invalid document version (must be either 'all', 'latest' or an integer.")

    # Set HTTP operation parameters.
    url = _get_api_url(_EP_PUBLISHING)
    url += '/{0}/{1}'.format(uid, version)

    # Invoke HTTP operation.
    r = _invoke(requests.delete, url)

    # Process HTTP response code.
    if r.status_code == HTTP_RESPONSE_STATUS_500:
        _raise("Document unpublishing server side failure")
