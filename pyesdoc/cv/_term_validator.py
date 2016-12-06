# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv._validation.py
   :copyright: Copyright "December 01, 2014", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package validation functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime
import uuid

from pyesdoc.cv import constants
from pyesdoc.cv.exceptions import ValidationError



# Set of illigal name characters.
# TODO move to regex.
_ILLEGAL_NAME_CHARACTERS = set(["/", "&"])


def _validate_term_alternative_name(term):
    """Validates a term's name.

    """
    if term.alternative_name:
        _validate_unicode(term.alternative_name, "alternative_name")
        for char in _ILLEGAL_NAME_CHARACTERS:
            if term.alternative_name.find(char) > -1:
                raise ValidationError('alternative name is invalid')


def _validate_term_create_date(term):
    """Validates a term's creation date.

    """
    if term.create_date is None:
        raise ValidationError('create date is undefined')
    if not isinstance(term.create_date, datetime.datetime):
        raise ValidationError("create date is invalid")


def _validate_term_domain(term):
    """Validates a termset's domain.

    """
    _validate_unicode(term.domain, "domain")


def _validate_term_description(term):
    """Validates a termset's description.

    """
    if term.description is not None:
        _validate_unicode(term.description, "description")


def _validate_term_id(term):
    """Validates a term's unique identifier.

    """
    if term.idx is None:
        raise ValidationError('id is undefined')

    if not isinstance(term.idx, int):
        try:
            term.idx = int(term.idx)
        except ValueError:
            raise ValidationError("idx must be a positive integer")

    if term.idx < 0:
        raise ValidationError("idx must be a positive integer")


def _validate_termset_kind(term):
    """Validates a termset's typeof.

    """
    _validate_unicode(term.kind, "kind")
    for char in _ILLEGAL_NAME_CHARACTERS:
        if term.kind.find(char) > -1:
            raise ValidationError('kind is invalid')


def _validate_term_name(term):
    """Validates a term's name.

    """
    _validate_unicode(term.name, "name")
    for char in _ILLEGAL_NAME_CHARACTERS:
        if term.name.find(char) > -1:
            raise ValidationError('name is invalid')


def _validate_term_status(term):
    """Validates a term's governance status.

    """
    if term.status not in constants.GOVERNANCE_STATUS_SET:
        msg = "governance status is invalid - valid states = {}"
        msg = msg.format(" | ".join(sorted(constants.GOVERNANCE_STATUS_SET)))
        raise ValidationError('governance status is invalid - valid states = {}'.format(msg))


def _validate_term_uid(term):
    """Validates a term's unique identifier.

    """
    if term.uid is None:
        raise ValidationError('unique identifier is undefined')

    if not isinstance(term.uid, uuid.UUID):
        try:
            term.uid = uuid.UUID(term.uid)
        except ValueError:
            raise ValidationError("unique identifier is invalid")


def _validate_term_url(term):
    """Validates a term's url.

    """
    if term.url is not None:
        _validate_unicode(term.url, "url")


def _validate_unicode(target, msg_prefix):
    """Validates a unique identifer.

    """
    if target is None:
        raise ValidationError("{} is undefined".format(msg_prefix))
    elif not isinstance(target, unicode):
        raise ValidationError("{} is not a unicode".format(msg_prefix))
    elif not len(target.strip()):
        raise ValidationError("{} is zero length".format(msg_prefix))


# Map of types to validators.
_VALIDATORS = {
    _validate_term_alternative_name,
    _validate_term_create_date,
    _validate_term_description,
    _validate_term_domain,
    _validate_termset_kind,
    _validate_term_id,
    _validate_term_name,
    _validate_term_status,
    _validate_term_uid,
    _validate_term_url
}


def validate(term):
    """Validates a term.

    :param pyesdoc.cv.Term term: A term.

    :returns: Collection of term validation errors.
    :rtype: list

    """
    result = []
    for validator in _VALIDATORS:
        try:
            validator(term)
        except ValidationError as err:
            result.append(err.message)

    return result


def is_valid(term):
    """Returns flag indicating whether a term is valid or not.

    :param pyesdoc.cv.Term term: A term.

    :returns: A flag indicating whether a term is valid or not.
    :rtype: bool

    """
    return len(validate(term)) == 0
