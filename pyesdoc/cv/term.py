# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.term.py
   :copyright: Copyright "December 01, 2014", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: A vocabulary term.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import uuid

import arrow

import pyesdoc.cv
from pyesdoc.cv import constants
from pyesdoc.cv import _term_validator as validator



class Term(object):
    """A vocabulary term.

    """
    def __init__(self, domain, kind, name, status=None):
        """Instance constructor.

        """
        # Meta attributes.
        self.create_date = arrow.utcnow().datetime
        self.domain = domain
        self.idx = None
        self.kind = kind
        self.status = status or constants.GOVERNANCE_STATUS_PENDING
        self.uid = unicode(uuid.uuid4())

        # Name related attributes.
        self.name = name
        self.alternative_name = None
        self.aliases = []

        # UI related.
        self.labels = {}

        # Relationship attributes.
        self.associations = set()
        self.parent = None

        # Other attributes.
        self.description = None
        self.url = None
        self.alternative_url = None

        # Path to term file on local file system.
        self.io_path = None


    def __repr__(self):
        """Instance representation.

        """
        return u"{0} -> {1} -> [{2}]".format(self.namespace, self.name, self.status).lower()


    @property
    def all_names(self):
        """Returns all names associated witht the term.

        """
        result = [self.name, self.alternative_name] + self.aliases
        result = [t for t in result if t is not None and len(t) > 0]

        return set(result)


    @property
    def depth(self):
        """Returns hierarchical depth.

        """
        return len(self.ancestors)


    @property
    def errors(self):
        """Returns set of term validation errors.

        """
        return pyesdoc.cv.validate(self)


    @property
    def is_cached(self):
        """Returns flag indicating whether the term is cached or not.

        """
        return self.partition.is_cached(self)


    @property
    def is_valid(self):
        """Returns flag indicating whether the term is valid or not.

        """
        return validator.is_valid(self)


    @property
    def is_written(self):
        """Returns flag indicating whether the term is written to file system or not.

        """
        return self.partition.is_written(self)


    @property
    def errors(self):
        """Returns set of term validation errors.

        """
        return validator.validate(self)


    @property
    def namespace(self):
        """Returns full namespace of the term set.

        """
        return ":".join([self.domain, self.kind])


    @property
    def partition(self):
        """Returns associated partition.

        """
        return pyesdoc.cv.get_partition(self.domain)


    @property
    def sort_key(self):
        """Gets the term's sort key

        """
        return u"{0}::{1}".format(self.namespace, self.name).lower()


    def as_dict(self):
        """Returns dictionary representation of term.

        """
        return pyesdoc.cv.encode(self, constants.ENCODING_DICT)


    def as_json(self):
        """Returns json representation of term.

        """
        return pyesdoc.cv.encode(self, constants.ENCODING_JSON)


    def add_alias(self, new_alias):
        """Marks as accepted.

        """
        # Escape if alias is null.
        if new_alias is None:
            return

        # Format new alias.
        new_alias = unicode(new_alias).strip()

        # Escape if alias is zero length.
        if len(new_alias) == 0:
            return

        # Escape if already aliased.
        for alias in self.aliases:
            if alias == new_alias:
                return

        # Update alias set.
        self.aliases = sorted(self.aliases + [new_alias])

        # Save term.
        self.partition.save(self)


    def accept(self):
        """Marks as accepted.

        """
        self.partition.accept(self)


    def reject(self):
        """Marks as rejected.

        """
        self.partition.reject(self)


    def save(self):
        """Saves term to persistant state stores.

        """
        self.partition.save(self)


    def deprecate(self):
        """Marks as deprecated.

        """
        self.partition.deprecate(self)


    def destroy(self):
        """Destroys term from all persistant state stores.

        """
        self.partition.destroy(self)


    def show_errors(self):
        """Displays list of validation errors.

        """
        for err in self.errors:
            print err


    def set_label(self, name, language=constants.DEFAULT_LANGUAGE):
        """Sets a user interface label.

        """
        self.labels[language] = name


    def get_label(self, language=constants.DEFAULT_LANGUAGE):
        """Gets a user interface label.

        """
        try:
            return self.labels[language]
        except KeyError:
            return self.name


    def ancestors(self):
        """Gets a term's set of ancestors.

        """
        result = []
        ancestor = self.parent
        while ancestor:
            result.append(ancestor)
            ancestor = ancestor.parent

        return reversed(result)


    def associate(self, term):
        """Appends an associated term to managed collection.

        :param pyesdoc.cv.Term term: Associated term to be added.

        """
        self.associations.add(term)

