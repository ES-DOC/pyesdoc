"""
.. module:: grids_grid_spec.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.grids.grid_spec document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""

def _set_display_name(doc):
    """Sets document display name."""
    if len(doc.esm_model_grids):
        doc._display_name = doc.esm_model_grids[0].short_name
    elif len(doc.esm_exchange_grids):
        doc._display_name = doc.esm_exchange_grids[0].short_name


def _set_type_display_name(doc):
    """Sets document type display name."""
    doc._type_display_name = doc.doc_info.type_display_name = "Grid Spec"


def _set_summary_fields(doc):
    """Sets document summary fields."""
    if len(doc.esm_model_grids):
    	doc._summary_fields += (
            doc.esm_model_grids[0].short_name,
            doc.esm_model_grids[0].long_name
        )
    elif len(doc.esm_exchange_grids):
    	doc._summary_fields += (
            doc.esm_exchange_grids[0].short_name,
            doc.esm_exchange_grids[0].long_name
        )


def parse(doc):
	for parser in (
		_set_display_name, 
		_set_type_display_name, 
		_set_summary_fields):
		parser(doc)