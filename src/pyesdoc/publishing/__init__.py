from .. import utils
from .. import serialization

import requests



# API url option name.
_OPT_API_URL = 'api_url'

# Publishign API endpoint.
_EP_PUBLISHING = 'publishing'


HTTP_RESPONSE_STATUS_200 = 200
HTTP_RESPONSE_STATUS_500 = 500


def _get_api_url(ep):
    """Helper function to return api endpoint url."""
    return utils.get_option(_OPT_API_URL) + '/1/{0}'.format(ep)


def retrieve(uid, version):
    # Construct url.
    url = _get_api_url(_EP_PUBLISHING)
    url += '/{0}/{1}'.format(uid, version)

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

