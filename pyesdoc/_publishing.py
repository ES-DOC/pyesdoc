"""
.. module:: pyesdoc._publishing.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document publishing functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime
import urllib
import uuid

import requests

from pyesdoc import constants
from pyesdoc import _api_proxy as proxy
from pyesdoc._extensions import extend
from pyesdoc._serialization import decode
from pyesdoc._serialization import encode
from pyesdoc._validation import is_valid


# Set of target endpoints.
_EP_CREATE = "/2/document/create"
_EP_RETRIEVE = "/2/document/retrieve"
_EP_UPDATE = "/2/document/update"
_EP_DELETE = "/2/document/delete"


def retrieve(uid, version=constants.DOC_VERSION_LATEST):
    """Retrieves a document from web service.

    :param str|uuid.UUID uid: Document unique identifier.
    :param str|int version: Document version.

    :returns: A document from remote repository.
    :rtype: object | None

    """
    # Validate inputs.
    if not isinstance(uid, uuid.UUID):
        try:
            uid = uuid.UUID(uid)
        except ValueError:
            _throw_invalid_doc_id()
    if version != constants.DOC_VERSION_LATEST and \
       not isinstance(version, int):
        _throw_invalid_doc_version()

    # Invoke web-service.
    endpoint = _get_doc_endpoint(_EP_RETRIEVE, uid, version, constants.ENCODING_JSON)
    response = proxy.invoke(requests.get, endpoint)
    proxy.parse_response(response, error_on_404=False)

    # Process web-service response.
    if response.text:
        return extend(decode(response.json(), constants.ENCODING_DICT))


def publish(doc):
    """Publishes a document to web service.

    :param doc: Document being published.
    :type doc: object

    :returns: Updated document.
    :rtype: object

    """
    # Validate inputs.
    if doc is None:
        raise TypeError("Cannot publish null documents.")
    if not is_valid(doc):
        raise ValueError("Cannot publish invalid documents.")

    # Increment version / update date.
    doc.meta.version = doc.meta.version + 1
    doc.meta.update_date = datetime.datetime.now()

    # Invoke web-service.
    endpoint = _EP_UPDATE if doc.meta.version > 1 else _EP_CREATE
    payload = encode(doc, constants.ENCODING_JSON)
    verb = requests.put if doc.meta.version > 1 else requests.post
    response = proxy.invoke(verb, endpoint, data=payload)

    # Process web-service response.
    proxy.parse_response(response)


def unpublish(uid, version=constants.DOC_VERSION_ALL):
    """Unpublishes a document from web service.

    :param str|uuid.UUID uid: Document unique identifier.
    :param str|int version: Document version.

    """
    # Validate inputs.
    if not isinstance(uid, uuid.UUID):
        try:
            uid = uuid.UUID(uid)
        except ValueError:
            _throw_invalid_doc_id()
    if not version == constants.DOC_VERSION_ALL and \
       not version == constants.DOC_VERSION_LATEST and \
       not isinstance(version, int):
        _throw_invalid_doc_version()

    # Invoke web-service.
    endpoint = _get_doc_endpoint(_EP_DELETE, uid, version)
    response = proxy.invoke(requests.delete, endpoint)

    # Process web-service response.
    proxy.parse_response(response)


def _throw_invalid_doc_id():
    """Throws an error.

    """
    raise TypeError("Invalid document uid (must be an instance of uuid.UUID).")


def _throw_invalid_doc_version():
    """Throws an error.

    """
    raise TypeError("Invalid document version (must be either 'all', 'latest' or an integer.")


def _get_doc_endpoint(endpoint, uid, version, encoding=None):
    """Returns a document instance endpoint url.

    """
    params = {
        "document_id": uid,
        "document_version": version
    }
    if encoding:
        params["encoding"] = encoding

    return "{}?{}".format(endpoint, urllib.urlencode(params))
