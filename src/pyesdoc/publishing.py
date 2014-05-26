"""
.. module:: pyesdoc.publishing.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document publishing functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import uuid

import requests

from . import constants, options
from . serialization import encode, decode
from . extensions import extend
from . utils import runtime as rt
from . validation import is_valid



# API url option name.
_OPT_API_URL = 'api_url'

# Publishing API endpoint.
_EP_PUBLISHING = 'publishing'

# HTTP response codes.
HTTP_RESPONSE_STATUS_200 = 200
HTTP_RESPONSE_STATUS_404 = 404
HTTP_RESPONSE_STATUS_500 = 500


def _assert_doc(doc, msg):
    """Asserts document instance."""
    if doc is None:
        rt.throw(msg if msg is not None else "Document instance is null.")


def _throw_invalid_doc_id():
    """Throws an error."""
    rt.throw("Invalid document uid (must be an instance of uuid.UUID).")


def _throw_invalid_doc_version():
    """Throws an error."""
    rt.throw("Invalid document version (must be either \
             'all', 'latest' or an integer.")


def _throw_connection_error():
    """Throws an error."""
    rt.throw("Could not connect to remote API server.")


def _throw_http_error():
    """Throws an error."""
    rt.throw("Invalid HTTP response from remote API server.")


def _throw_timeout_error():
    """Throws an error."""
    rt.throw("Remote API server connection timed out.")


def _throw_server_error():
    """Throws an error."""
    rt.throw("A server side failure has occurred.")


def _invoke(operation, url, data=None):
    """Invokes a publishing endpoint operation."""
    try:
        if data is not None:
            return operation(url, data=data)
        else:
            return operation(url)
    except requests.ConnectionError:
        _throw_connection_error()
    except requests.HTTPError:
        _throw_http_error()
    except requests.Timeout:
        _throw_timeout_error()


def _get_api_url(endpoint):
    """Helper function to return api endpoint url."""
    return options.get(_OPT_API_URL) + '/1/{0}'.format(endpoint)


def _get_doc_url(uid, version=None, encoding=None):
    """Returns a document instance endpoint url."""
    url = _get_api_url(_EP_PUBLISHING)
    url += '/{0}'.format(uid)
    if version is not None:
        url += '/{0}'.format(version)
    if encoding is not None:
        url += '.{0}'.format(encoding)

    return url


def exists(uid, version=None):
    """Determines whether a document already exists within remote repository.

    :param uid: Document unique identifier.
    :type uid: str | uuid.UUID

    :returns: Flag indicating whether document already exists.
    :rtype: bool

    """
    # Defensive programming.
    if not isinstance(uid, uuid.UUID):
        _throw_invalid_doc_id()
    if version is not None and not isinstance(version, int):
        _throw_invalid_doc_version()

    # Issue HTTP HEAD.
    url = _get_doc_url(uid, version)
    resp = _invoke(requests.head, url)

    # Process HTTP response code.
    # 200 - return true;
    if resp.status_code == HTTP_RESPONSE_STATUS_200:
        return True

    # 404 - return false;
    elif resp.status_code == HTTP_RESPONSE_STATUS_404:
        return False

    # 500 - raise error.
    elif resp.status_code == HTTP_RESPONSE_STATUS_500:
        rt.throw("Document retrieval server side failure")


def retrieve(uid, version=constants.ESDOC_DOC_VERSION_LATEST):
    """Retrieves a document from remote repository.

    :param uid: Document unique identifier.
    :type uid: str or uuid.UUID

    :param version: Document unique identifier.
    :type version: str or uuid.UUID

    :returns: A document from remote repository.
    :rtype: object, list or None

    """
    # Defensive programming.
    if not isinstance(uid, uuid.UUID):
        _throw_invalid_doc_id()
    if version != constants.ESDOC_DOC_VERSION_LATEST and \
       not isinstance(version, int):
        _throw_invalid_doc_version()

    # Issue HTTP GET.
    url = _get_doc_url(uid, version, constants.ESDOC_ENCODING_JSON)
    resp = _invoke(requests.get, url)

    # Process HTTP response code:
    # 200 - return decoded/extended document;
    if resp.status_code == HTTP_RESPONSE_STATUS_200 and len(resp.text):
        return extend(decode(resp.json(), constants.ESDOC_ENCODING_DICT))

    # 404 - raise error;
    elif resp.status_code == HTTP_RESPONSE_STATUS_404:
        rt.throw("Document Not Found :: {0}-v{1}".format(uid, version))

    # 500 - raise error.
    elif resp.status_code == HTTP_RESPONSE_STATUS_500:
        rt.throw("Document retrieval server side failure")


def publish(doc):
    """Publishes a document to remote repository.

    :param doc: Document being published.
    :type doc: object

    :returns: Updated document.
    :rtype: object

    """
    # Defensive programming.
    if doc is None:
        rt.throw("Cannot publish null documents.")
    if not is_valid(doc):
        rt.throw("Cannot publish invalid documents.")

    # Increment version.
    doc.meta.version += 1

    # Set HTTP operation parameters.
    url = _get_api_url(_EP_PUBLISHING)
    data = encode(doc, constants.ESDOC_ENCODING_JSON)

    # Invoke HTTP operation.
    resp = _invoke(requests.post, url, data)

    # Process HTTP response code:
    # 500 - raise error.
    if resp.status_code == HTTP_RESPONSE_STATUS_500:
        _throw_server_error()


def unpublish(uid, version=constants.ESDOC_DOC_VERSION_ALL):
    """Unpublishes a document from remote repository.

    :param doc: Document being unpublished.
    :type doc: object

    """
    # Defensive programming.
    if not isinstance(uid, uuid.UUID):
        _throw_invalid_doc_id()
    if not version == constants.ESDOC_DOC_VERSION_ALL and \
       not version == constants.ESDOC_DOC_VERSION_LATEST and \
       not isinstance(version, int):
        _throw_invalid_doc_version()

    # Invoke HTTP operation.
    url = _get_doc_url(uid, version)
    resp = _invoke(requests.delete, url)

    # Process HTTP response code:
    # 500 - raise error.
    if resp.status_code == HTTP_RESPONSE_STATUS_500:
        _throw_server_error()
