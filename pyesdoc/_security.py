"""
.. module:: security.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Wraps security related functions.

.. moduleauthor:: Mark A. Conway-Greenslade


"""
import base64
import json
import os

import requests



# GitHub API - credentials.
_GH_API_CREDENTIALS = ('esdoc-system-user', os.getenv('ESDOC_GITHUB_ACCESS_TOKEN'))

# GitHub API - teams.
_GH_API_TEAMS = "https://api.github.com/teams"

# GitHub API - user.
_GH_API_USER = "https://api.github.com/user"

# Map of recognized teams and their GitHub identifiers.
_GH_TEAMS = {
    'cdf2cim-publication': 2375689,
    'documentation-publication': 2375693,
    'errata-publication': 2375691,

    'cmip5-bcc': 2567241,
    'cmip5-bnu': 2567242,
    'cmip5-cccma': 2567243,
    'cmip5-cmcc': 2567244,
    'cmip5-cnrm-cerfacs': 2567245,
    'cmip5-csiro': 2567246,
    'cmip5-csiro-bom': 2567247,
    'cmip5-csiro-qccce': 2567248,
    'cmip5-doe-cola-cmmap-gmu': 2567249,
    'cmip5-fio': 2567250,
    'cmip5-ichec': 2567251,
    'cmip5-inm': 2567252,
    'cmip5-ipsl': 2567253,
    'cmip5-lasg-cess': 2567254,
    'cmip5-lasg-iap': 2567255,
    'cmip5-miroc': 2567256,
    'cmip5-mohc': 2567257,
    'cmip5-mpi-m': 2567258,
    'cmip5-mri': 2567259,
    'cmip5-nasa-giss': 2567260,
    'cmip5-nasa-gmao': 2567261,
    'cmip5-ncar': 2567262,
    'cmip5-ncc': 2567263,
    'cmip5-nicam': 2567264,
    'cmip5-nimr-kma': 2567265,
    'cmip5-noaa-gfdl': 2567266,
    'cmip5-nsf-doe-ncar': 2567267,
    'cmip5-unsw': 2567268,

    'cmip6-awi': 2567269,
    'cmip6-bcc': 2567270,
    'cmip6-bnu': 2567271,
    'cmip6-cams': 2567272,
    'cmip6-cas': 2567273,
    'cmip6-cccma': 2567274,
    'cmip6-cccr-iitm': 2567275,
    'cmip6-cmcc': 2567276,
    'cmip6-cnrm-cerfacs': 2567277,
    'cmip6-csir-csiro': 2567278,
    'cmip6-csiro-bom': 2567279,
    'cmip6-ec-earth-consortium': 2567280,
    'cmip6-fio-ronm': 2567281,
    'cmip6-hammoz-consortium': 2567282,
    'cmip6-inm': 2567283,
    'cmip6-inpe': 2567284,
    'cmip6-ipsl': 2567285,
    'cmip6-messy-consortium': 2567286,
    'cmip6-miroc': 2567287,
    'cmip6-mohc': 2567288,
    'cmip6-mpi-m': 2567289,
    'cmip6-mri': 2567290,
    'cmip6-nasa-giss': 2567291,
    'cmip6-ncar': 2567292,
    'cmip6-ncc': 2567293,
    'cmip6-nerc': 2567294,
    'cmip6-nims-kma': 2567295,
    'cmip6-niwa': 2567296,
    'cmip6-noaa-gfdl': 2567297,
    'cmip6-nuist': 2567298,
    'cmip6-pcmdi': 2567299,
    'cmip6-snu': 2567300,
    'cmip6-thu': 2567301,

    'cordex-auth-lhtee': 2567302,
    'cordex-auth-met': 2567303,
    'cordex-awi': 2567304,
    'cordex-bccr': 2567305,
    'cordex-cccma': 2567306,
    'cordex-chmi': 2567307,
    'cordex-clmcom': 2567308,
    'cordex-cnrm': 2567309,
    'cordex-crp-gl': 2567310,
    'cordex-cuni': 2567311,
    'cordex-dhmz': 2567312,
    'cordex-dmi': 2567313,
    'cordex-enea': 2567314,
    'cordex-gerics': 2567315,
    'cordex-hms': 2567316,
    'cordex-ictp': 2567317,
    'cordex-idl': 2567318,
    'cordex-iitm': 2567319,
    'cordex-ipsl-ineris': 2567320,
    'cordex-knmi': 2567321,
    'cordex-mgo': 2567322,
    'cordex-miub': 2567323,
    'cordex-mohc': 2567324,
    'cordex-mpi-csc': 2567325,
    'cordex-nuim': 2567326,
    'cordex-rmib-ugent': 2567327,
    'cordex-smhi': 2567328,
    'cordex-ucan': 2567329,
    'cordex-uclm': 2567330,
    'cordex-uhoh': 2567331,
    'cordex-ulg': 2567332,
    'cordex-uqam': 2567333
}

# Request authentication error HTTP response code.
_HTTP_UNAUTHENTICATED_ERROR = 401

# Request authorization error HTTP response code.
_HTTP_UNAUTHORIZED_ERROR = 403


class AuthenticationError(Exception):
    """Raised when an authentication assertion fails.

    """
    def __init__(self, msg=None):
        """Instance constructor.

        """
        err = "AUTHENTICATION FAILED"
        if msg is not None:
           err = "{} : {}".format(err, msg) 
        super(AuthenticationError, self).__init__(err)
        self.response_code = _HTTP_UNAUTHENTICATED_ERROR


class AuthorizationError(Exception):
    """Raised when an authorization assertion fails.

    """
    def __init__(self, msg=None):
        """Instance constructor.

        """
        err = "AUTHORIZATION FAILED"
        if msg is not None:
           err = "{} : {}".format(err, msg) 
        super(AuthorizationError, self).__init__(err)
        self.response_code = _HTTP_UNAUTHORIZED_ERROR


def authenticate_user(credentials):
    """Authenticates user credentials request against GitHub user api.

    :param tuple credentials: 2 member tuple (GitHub username, GitHub access token)

    :returns: GitHub username
    :rtype: str

    """
    # Unpack credentials.
    user_id, _ = credentials

    # Invoke GitHub API.
    r = requests.get(_GH_API_USER, auth=credentials)

    # Assert access token is valid (status_code = 200).
    if r.status_code != 200:
        raise AuthenticationError("GitHub user authentication with access token failed")

    # Assert user has granted application read:org permissions.
    if 'admin:org' not in r.headers['X-OAuth-Scopes'] and \
       'read:org' not in r.headers['X-OAuth-Scopes']:
        raise AuthenticationError("Access token must have either admin:org or read:org scope enabled")

    # Assert user id matches access token.
    if json.loads(r.text)['login'] != user_id:
        raise AuthenticationError("Github User ID is not matched with access token")

    return user_id


def authorize_user(team_id, user_id):
    """Verifies a user is a member of a team.

    :param str team_id: GitHub team identifier.
    :param str user_id: GitHub user login.

    """
    # Validate inputs.
    assert team_id in _GH_TEAMS, "Invalid team identifier {}".format(team_id)

    # Invoke GitHub API.
    url = '{}/{}/memberships/{}'.format(_GH_API_TEAMS, _GH_TEAMS[team_id], user_id)
    r = requests.get(url, auth=_GH_API_CREDENTIALS)

    # Assert user is a team member.
    if r.status_code != 200:
        raise AuthorizationError()


def strip_credentials(credentials):
    """Strips passed credentials from HTTP header.

    :param str credentials: Base64 encoded, ':' delimited credentials.

    :returns: Stripped credentials.
    :rtype: tuple

    """
    # Strip out HTTP Basic authorization header prefix.
    credentials = credentials.replace('Basic ', '')

    # Decode (b64).
    try:
        credentials = base64.b64decode(credentials)
    except TypeError:
        raise AuthenticationError()

    # Extract.
    credentials = credentials.split(':')
    if len(credentials) != 2:
        raise AuthenticationError()

    # Decode (utf-8).
    credentials = [i.decode('utf-8') for i in credentials]

    return tuple(credentials)
