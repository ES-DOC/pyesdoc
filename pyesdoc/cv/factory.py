# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.cv.factory.py
   :copyright: Copyright "December 01, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates creation of domain model class instances.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>

"""
import arrow
import re
import uuid

from pyesdoc.cv import constants
from pyesdoc.cv import validation as v
from pyesdoc.cv.exceptions import ValidationError
from pyesdoc.cv.model import Term
from pyesdoc.cv.model import Authority
from pyesdoc.cv.model import Collection
from pyesdoc.cv.model import Scope



def create_authority(name, description, url):
	"""Instantiates, initialises & returns a term authority.

	"""
	# Validate inputs.
	v.validate_authority_name(name)
	v.validate_authority_description(description)
	v.validate_authority_url(url)

	# Format inputs.
	name = unicode(name).strip()
	description = unicode(description).strip()
	url = unicode(url).strip()

	# Instantiate.
	i = Authority()
	i.description = description
	i.label = name
	i.name = name.lower()
	i.url = url

	# Raise validation exception (if appropriate).
	if not i.is_valid:
		raise ValidationError(i.errors)

	return i


def create_scope(authority, name, description, url):
	"""Instantiates, initialises & returns a term scope.

	"""
	# Validate inputs.
	v.validate(authority)
	v.validate_scope_name(name)
	v.validate_scope_description(description)
	v.validate_scope_url(url)

	# Format inputs.
	name = unicode(name).strip()
	description = unicode(description).strip()
	url = unicode(url).strip()

	# Instantiate.
	i = Scope()
	i.authority = authority
	i.description = description
	i.label = name
	i.name = name.lower()
	i.uid = uuid.uuid4()
	i.url = url

	# Append to parent & set idx.
	authority.scopes.append(i)
	i.idx = len(authority.scopes)

	# Raise validation exception (if appropriate).
	if not i.is_valid:
		raise ValidationError(i.errors)

	return i


def create_collection(scope, name, description):
	"""Instantiates, initialises & returns a term collection.

	"""
	# Validate inputs.
	v.validate(scope)
	v.validate_collection_name(name)
	v.validate_collection_description(description)

	# Format inputs.
	name = unicode(name).strip()
	description = unicode(description).strip()

	# Instantiate.
	i = Collection()
	i.create_date = arrow.utcnow().datetime
	i.description = description
	i.label = name
	i.name = name.lower()
	i.scope = scope
	i.uid = uuid.uuid4()

	# Append to parent & set idx.
	scope.collections.append(i)
	i.idx = len(scope.collections)

	# Raise validation exception (if appropriate).
	if not i.is_valid:
		raise ValidationError(i.errors)

	return i


def create_term(collection, name):
	"""Instantiates, initialises & returns a term.

	"""
	# Validate inputs.
	v.validate(collection)
	v.validate_term_name(name)

	# Format inputs.
	name = unicode(name).strip()

	# Instantiate.
	i = Term()
	i.collection = collection
	i.create_date = arrow.utcnow().datetime
	i.labels[constants.DEFAULT_LANGUAGE] = name
	i.name = name.lower()
	i.status = constants.GOVERNANCE_STATUS_PENDING
	i.uid = uuid.uuid4()

	# Append to parent & set idx.
	collection.terms.append(i)
	i.idx = len(collection.terms)

	# Raise validation exception (if appropriate).
	if not i.is_valid:
		raise ValidationError(i.errors)

	return i
