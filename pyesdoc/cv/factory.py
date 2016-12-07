import arrow
import re
import uuid

from pyesdoc.cv import constants
from pyesdoc.cv.term import Term
from pyesdoc.cv.term_authority import TermAuthority
from pyesdoc.cv.term_collection import TermCollection
from pyesdoc.cv.term_scope import TermScope



def create_authority(name, description, homepage):
	"""Instantiates, initialises & returns a term authority.

	"""
	assert isinstance(name, (str, unicode)) and len(name)
	assert isinstance(description, (str, unicode)) and len(description)
	assert isinstance(homepage, (str, unicode)) and len(homepage)

	name = unicode(name).strip()
	description = unicode(description).strip()
	homepage = unicode(homepage).strip()

	i = TermAuthority()
	i.description = description
	i.homepage = homepage
	i.label = name
	i.name = name.lower()

	return i


def create_scope(authority, name, description, homepage):
	"""Instantiates, initialises & returns a term scope.

	"""
	assert isinstance(authority, TermAuthority)
	assert isinstance(name, (str, unicode)) and len(name)
	assert isinstance(description, (str, unicode)) and len(description)
	assert isinstance(homepage, (str, unicode)) and len(homepage)

	name = unicode(name).strip()
	description = unicode(description).strip()
	homepage = unicode(homepage).strip()

	i = TermScope()
	i.authority = authority
	i.description = description
	i.homepage = homepage
	i.label = name
	i.name = name.lower()
	i.uid = uuid.uuid4()

	authority.scopes.append(i)
	i.idx = unicode(len(authority.scopes))

	return i


def create_collection(scope, name, description):
	"""Instantiates, initialises & returns a term collection.

	"""
	assert isinstance(scope, TermScope)
	assert isinstance(name, (str, unicode)) and len(name)
	assert isinstance(description, (str, unicode)) and len(description)

	name = unicode(name).strip()
	description = unicode(description).strip()

	i = TermCollection()
	i.create_date = arrow.utcnow().datetime
	i.description = description
	i.label = name
	i.name = name.lower()
	i.scope = scope
	i.uid = uuid.uuid4()

	scope.collections.append(i)
	i.idx = u"{}.{}".format(scope.idx, len(scope.collections))

	return i


def create_term(collection, name, description=None):
	"""Instantiates, initialises & returns a term.

	"""
	assert isinstance(collection, TermCollection)
	assert isinstance(name, (str, unicode)) and len(name)
	if description is not None:
		assert isinstance(description, (str, unicode)) and len(description)

	name = unicode(name).strip()
	if description is not None:
		description = unicode(description).strip()

	i = Term()
	i.collection = collection
	i.create_date = arrow.utcnow().datetime
	if description is not None:
		i.description = description
	i.labels[constants.DEFAULT_LANGUAGE] = name
	i.name = name.lower()
	i.status = constants.GOVERNANCE_STATUS_PENDING
	i.uid = uuid.uuid4()

	collection.terms.append(i)
	i.idx = u"{}.{}".format(collection.idx, len(collection.terms))

	return i
