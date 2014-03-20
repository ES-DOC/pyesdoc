# Module imports.
from . import cim, default
from .. utils import runtime as rt


# Supported ontologies.
_ontologies = [cim]


# Supported parsers keyed by document type.
supported = reduce(lambda x, o: dict(x.items() + o.supported.items()), _ontologies, {})

def parse(doc):
	"""Invokes a document parser.

    :param doc: pyesdoc document instance.
    :type doc: object

    :returns: Parsed document.
    :rtype: object

	"""	
	# Defensive programming.
	rt.assert_doc('doc', doc, "Cannot parse a null document")

	# Escape if already parsed.
	if hasattr(doc, "_parsed") and doc._parsed:
		return

	# Perform default pre-parsing.
	default.pre_parse(doc)

	# Perform type specific parsing.
	if is_parseable(doc):
		supported[doc.type_key.lower()](doc)

	# Perform default post-parsing.
	default.post_parse(doc)

	# Flag as parsed.
	doc._parsed = True


def is_parseable(doc):
	"""Returns a flag indicating whether document parsing is supported.

    :param doc: pyesdoc document instance or type key.
    :type doc: object | str

	"""
	# Defensive programming.
	if not isinstance(doc, str):
		rt.assert_doc('doc', doc, "Invalid document")

	doc_type = doc if isinstance(doc, str) else doc.type_key

	return doc_type.lower() in supported
