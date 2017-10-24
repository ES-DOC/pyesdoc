# -*- coding: utf-8 -*-

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
_GH_API_CREDENTIALS = (
    'esdoc-system-user',
     os.getenv('ESDOC_GITHUB_ACCESS_TOKEN')
     )

# GitHub API - teams.
_GH_API_TEAMS = "https://api.github.com/teams"

# GitHub API - user.
_GH_API_USER = "https://api.github.com/user"

# Map of recognized teams and their GitHub identifiers.
_GH_TEAMS = {
    "cdf2cim-publication": 2375689,
    "documentation-publication": 2375693,
    "errata-publication": 2375691,
    "staff-awi": 2508352,
    "staff-bcc": 2508353,
    "staff-bnu": 2508354,
    "staff-cams": 2508355,
    "staff-cccma": 2508356,
    "staff-cccr-iitm": 2508357,
    "staff-cmcc": 2508358,
    "staff-cnrm-cerfacs": 2508359,
    "staff-csir-csiro": 2508360,
    "staff-csiro-bom": 2508361,
    "staff-ec-earth-consortium": 2508362,
    "staff-fio-ronm": 2508363,
    "staff-hammoz-consortium": 2508364,
    "staff-inm": 2508365,
    "staff-inpe": 2508366,
    "staff-ipsl": 2508367,
    "staff-messy-consortium": 2508368,
    "staff-miroc": 2508369,
    "staff-mohc": 2508370,
    "staff-mpi-m": 2508371,
    "staff-mri": 2508372,
    "staff-nasa-giss": 2508373,
    "staff-ncar": 2508374,
    "staff-ncc": 2508375,
    "staff-nerc": 2508376,
    "staff-nims-kma": 2508377,
    "staff-noaa-gfdl": 2508378,
    "staff-nuist": 2508379,
    "staff-pcmdi": 2508380,
    "staff-snu": 2508381,
    "staff-thu": 2508382
}

# Request authentication error HTTP response code.
_HTTP_UNAUTHENTICATED_ERROR = 401

# Request authorization error HTTP response code.
_HTTP_UNAUTHORIZED_ERROR = 403


class AuthenticationError(Exception):
    """Raised when an authentication assertion fails.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(AuthenticationError, self).__init__("AUTHENTICATION FAILED")
        self.response_code = _HTTP_UNAUTHENTICATED_ERROR


class AuthorizationError(Exception):
    """Raised when an authorization assertion fails.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(AuthorizationError, self).__init__("AUTHORIZATION FAILED")
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
        raise AuthenticationError()

    # Assert user has granted application read:org permissions.
    if 'read:org' not in r.headers['X-OAuth-Scopes']:
        raise AuthenticationError()

    # Assert user id matches access token.
    if json.loads(r.text)['login'] != user_id:
        raise AuthenticationError()

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
