# Module imports.
from . import cim, default
from .. utils import runtime as rt


# Supported ontologies.
_ontologies = [cim]


# Supported parsers keyed by document type.
supported = reduce(lambda x, o: dict(x.items() + o.supported.items()), _ontologies, {})


# Map of document type display names.
_type_display_names = {
	"cim.1.activity.numericalexperiment" : "Experiment",
	"cim.1.data.dataobject" : "Data",
	"cim.1.grids.gridspec" : "Grid",
	"cim.1.software.modelcomponent" : "Model",
	"cim.1.quality.cimquality" : "QC Record",
}


def _parse(doc):
	# Set type display name.
	doc_type = doc.type_key.lower()
	if doc_type in _type_display_names:
		doc.doc_info.type_display_name = _type_display_names[doc_type]
	else:
		doc.doc_info.type_display_name = doc.doc_info.type


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
	if hasattr(doc, "_parsed"):
		return

	# Perform default parsing.
	default.parse(doc)

	if is_parseable(doc):
		supported[doc.type_key.lower()](doc)
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
