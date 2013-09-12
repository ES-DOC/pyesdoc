import requests

from .. import utils
from .. import serialization



# API url option name.
_OPT_API_URL = 'api_url'

# Publishing API endpoint.
_EP_PUBLISHING = 'publishing'

# HTTP response codes.
HTTP_RESPONSE_STATUS_200 = 200
HTTP_RESPONSE_STATUS_500 = 500

# Latest document version label.
ESDOC_DOC_VERSION_LATEST = 'latest'

# All document versions label.
ESDOC_DOC_VERSION_ALL = 'all'


def _get_api_url(ep):
    """Helper function to return api endpoint url."""
    return utils.get_option(_OPT_API_URL) + '/1/{0}'.format(ep)


def retrieve(uid, version):
    """Retrieves a document from remote repository.

    :param uid: Document unique identifier.
    :type uid: str or uuid.UUID

    :param version: Document unique identifier.
    :type version: str or uuid.UUID

    :returns: A document from remote repository.
    :rtype: object or None

    """
    # Construct url.
    url = _get_api_url(_EP_PUBLISHING)
    url += '/{0}'.format(uid)
    if version is not None:
        url += '/{0}'.format(version)

    # Issue HTTP GET.
    r = requests.get(url)

    # Inspect status code:
    # ... success
    if r.status_code == HTTP_RESPONSE_STATUS_200:
        if len(r.text):
            return serialization.decode(r.json(),
                                        serialization.ESDOC_ENCODING_DICT)

    # ... failure.
    elif r.status_code == HTTP_RESPONSE_STATUS_500:
        raise utils.PYESDOC_Exception(r.text)

    return None


def publish(doc):
    """Publishes a document to remote repository.

    :param doc: Document being published.
    :type doc: object

    :returns: Updated document.
    :rtype: object

    """
    # Increment version.
    doc.doc_info.version += 1

    # Invoke HTTP operation.
    r = requests.post(_get_api_url(_EP_PUBLISHING),
                      data=serialization.encode(doc, serialization.ESDOC_ENCODING_JSON))

    # Inspect status code:
    # ... success
    if r.status_code == HTTP_RESPONSE_STATUS_200:
        print 'Publish sucess'

    # ... failure.
    elif r.status_code == HTTP_RESPONSE_STATUS_500:
        print 'Publish error'
#        raise utils.PYESDOC_Exception(r.text)


def unpublish(uid, version):
    """Unpublishes a document from remote repository.

    :param doc: Document being unpublished.
    :type doc: object

    """
    # Construct url.
    url = _get_api_url(_EP_PUBLISHING)
    url += '/{0}/{1}'.format(uid, version)
    
    # Invoke HTTP operation.
    r = requests.delete(url)

    # Inspect status code:
    # ... success
    if r.status_code == HTTP_RESPONSE_STATUS_200:
        print 'Unpublish sucess'

    # ... failure.
    elif r.status_code == HTTP_RESPONSE_STATUS_500:
        print 'Unpublish error'
#        raise utils.PYESDOC_Exception(r.text)