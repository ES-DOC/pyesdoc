# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.io_manager.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encpasulates domain model class instance I/O functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import glob
import json
import os

from pyesdoc.cv import validation
from pyesdoc.cv import constants
from pyesdoc.cv.model import Authority
from pyesdoc.cv.codecs import to_json
from pyesdoc.cv.codecs import from_json


_HOME = "/Users/macg/dev/esdoc/repos/esdoc-cv"

_SEPARATOR = "__"

# Manifest file name.
_MANIFEST = "MANIFEST"


def write(dpath, authority):
    """Writes a CV instance to file system.

    :param str dpath: Path to directory to which the CV will be written.
    :param pyesdoc.cv.Authority authority: Authority class instance to be written to file-system.

    """
    # Validate inputs.
    if not os.path.isdir(dpath):
        raise OSError("Invalid directory.")
    if not isinstance(authority, Authority):
        raise NotImplementedError("Invalid authority: unknown type")
    if not validation.is_valid(authority):
        raise ValueError("Invalid authority: has validation errors")

    # Write authority manifest.
    with open(os.path.join(dpath, _MANIFEST), "w") as fstream:
        fstream.write(to_json(authority))

    # Write terms.
    for scope in authority.scopes:
        for collection in scope.collections:
            for term in collection.terms:
                _write_term(dpath, term)


def _write_term(dpath, term):
    """Writes a term to the file system.

    """
    dpath = _get_term_dpath(dpath, term)
    fname = "{}.json".format(term.name)
    with open(os.path.join(dpath, fname), "w") as fstream:
        fstream.write(to_json(term))
    if term.data:
        _write_term_data(dpath, term)


def _write_term_data(dpath, term):
    """Writes a term's data to the file system.

    """
    fname = "{}.json.data".format(term.name)
    with open(os.path.join(dpath, fname), "w") as fstream:
        fstream.write(json.dumps(term.data, indent=4, sort_keys=True))


def _get_term_dpath(dpath, term):
    """Returns directory path to which term files will be written.

    """
    dpath = os.path.join(dpath, term.scope.name)
    dpath = os.path.join(dpath, term.collection.name)
    dpath = os.path.join(dpath, term.status)
    try:
        os.makedirs(dpath)
    except OSError:
        pass

    return dpath


def read(dpath):
    """Reads a CV hierarchy from file system.

    :param str dpath: Path to directory to which a CV hierarchy has been written.

    """
    if not os.path.isdir(dpath):
        raise OSError("Invalid directory.")
    if not os.path.isfile(os.path.join(dpath, _MANIFEST)):
        raise OSError("Invalid MANIFEST.")

    # Read authority from manifest.
    with open(os.path.join(dpath, _MANIFEST), "r") as fstream:
        authority = from_json(fstream.read())

    # Read terms.
    for scope in authority.scopes:
        for collection in scope.collections:
            collection.terms = []
            for status in constants.GOVERNANCE_STATUS_SET:
                collection.terms += _read_terms(dpath, scope, collection, status)

    # Set inter-concept hierachy.
    terms = {}
    for scope in authority.scopes:
        scope.authority = authority
        for collection in scope.collections:
            collection.scope = scope
            for term in collection.terms:
                term.collection = collection
                terms[term.uid] = term

    # Set inter-term hierarchies.
    for term in terms.values():
        if term.parent in terms:
            term.parent = terms[term.parent]

    # Set intra-term hierarchies.
    for term in [i for i in terms.values() if i.associations]:
        term.associations = [terms[i] if i in terms else i for i in term.associations]

    return authority


def _read_terms(dpath, scope, collection, status):
    """Reads terms from file system.

    """
    def _read(fpath):
        with open(fpath, "r") as fstream:
            return from_json(fstream.read())

    # Set term directory path.
    dpath = os.path.join(dpath, scope.name)
    dpath = os.path.join(dpath, collection.name)
    dpath = os.path.join(dpath, status)
    dpath = os.path.join(dpath, "*")

    return [_read(i) for i in glob.iglob(dpath)]
