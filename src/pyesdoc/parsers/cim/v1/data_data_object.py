"""
.. module:: data_data_object.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.data.data_object document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
def _set_display_name(doc):
    """Sets document display name."""
    doc._display_name = doc.acronym


def _set_type_display_name(doc):
    """Sets document type display name."""
    doc._type_display_name = doc.doc_info.type_display_name = "Data Object"


def _set_summary_fields(doc):
    """Sets document summary fields."""
    doc._summary_fields += (
        doc.acronym,
        doc.description
    )


def parse(doc):
    for parser in (
        _set_display_name, 
        _set_type_display_name, 
        _set_summary_fields):
        parser(doc)
    