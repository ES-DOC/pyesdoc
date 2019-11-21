"""
.. module:: pyesdoc._api_proxy.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Proxies documentaiton web-service calls.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os
import urllib

import requests

from pyesdoc import exceptions



# HTTP response codes.
HTTP_RESPONSE_STATUS_200 = 200
HTTP_RESPONSE_STATUS_404 = 404
HTTP_RESPONSE_STATUS_500 = 500

# Web service base url.
_BASE_URL = os.getenv("ESDOC_API", r"https://api.es-doc.org")



def invoke(verb, endpoint, params=None, data=None):
    """Invokes endpoint.

    """
    # Set endpoint url.
    url = "{}{}".format(_BASE_URL, endpoint)
    if params is not None:
    	url += "?{}".format(urllib.urlencode(params))

    # Set request headers.
    headers = None if not data else {'content-type': 'application/json'}

    # Make remote call.
    try:
        return verb(url, data=data, headers=headers)
    except requests.ConnectionError:
        _throw_connection_error()
    except requests.HTTPError:
        _throw_http_error()
    except requests.Timeout:
        _throw_timeout_error()


def parse_response(resp, error_on_404=True):
    """Parses response returned from API.

    """
    if resp.status_code == HTTP_RESPONSE_STATUS_404:
        if error_on_404:
            _throw_not_found_error()
    elif resp.status_code == HTTP_RESPONSE_STATUS_500:
        _throw_server_error(resp)
    elif resp.status_code != HTTP_RESPONSE_STATUS_200:
        _throw_uncontrolled_server_error(resp)


def _throw_connection_error():
    """Throws an error.

    """
    raise exceptions.WebServiceException("Could not connect to remote API server.")


def _throw_not_found_error():
    """Throws an error.

    """
    raise exceptions.WebServiceException("Could not find remote resource.")


def _throw_http_error():
    """Throws an error.

    """
    raise exceptions.WebServiceException("Invalid HTTP response from remote API server.")


def _throw_timeout_error():
    """Throws an error.

    """
    raise exceptions.WebServiceException("Remote API server connection timed out.")


def _throw_server_error(resp):
    """Throws an error.

    """
    raise exceptions.WebServiceException("A server side failure has occurred: {0}".format(resp.text))


def _throw_uncontrolled_server_error(resp):
    """Throws an unknown server error.

    """
    raise exceptions.WebServiceException("An uncontrolled server side failure has occurred: {0}".format(resp.text))
