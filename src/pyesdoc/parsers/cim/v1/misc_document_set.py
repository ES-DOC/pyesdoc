"""
.. module:: misc_document_set.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.misc.document_set document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
def _set_doc_info(doc):
    """Sets document identifiers."""
    if doc.simulation:
        doc.doc_info.create_date = doc.simulation.doc_info.create_date
        doc.doc_info.id = doc.simulation.doc_info.id
        doc.doc_info.version = doc.simulation.doc_info.version


def _set_display_name(doc):
    """Sets document display name."""
    pass


def _set_type_display_name(doc):
    """Sets document type display name."""
    pass


def _set_summary_fields(doc):
    """Sets document summary fields."""
    pass


def parse(doc):
    for parser in (
        _set_doc_info,
        _set_display_name, 
        _set_type_display_name, 
        _set_summary_fields):
        parser(doc)
    