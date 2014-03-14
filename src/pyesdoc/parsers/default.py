# -*- coding: utf-8 -*-

"""
.. module:: default.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Default document parser.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""

# Map of document type display names.
_doc_type_display_names = {
	"cim.1.activity.numericalexperiment" : "Experiment",
	"cim.1.data.dataobject" : "Data",
	"cim.1.grids.gridspec" : "Grid",
	"cim.1.software.modelcomponent" : "Model",
	"cim.1.quality.cimquality" : "QC Record",
}



def _set_doc_type_display_name(doc):
	"""Sets document type display name."""
	doc_type = doc.type_key.lower()
	if doc_type in _doc_type_display_names:
		doc.doc_info.type_display_name = _doc_type_display_names[doc_type]
	else:
		doc.doc_info.type_display_name = doc.doc_info.type	


# Set of parsers.
_parsers = (_set_doc_type_display_name, )


def parse(doc):
	"""Performs default document parsing.

	:param object doc: A document to be parsed.

	"""
	for parser in _parsers:
		parser(doc)
