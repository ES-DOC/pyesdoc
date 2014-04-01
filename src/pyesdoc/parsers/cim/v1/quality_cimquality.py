"""
.. module:: quality_cim_quality.py
   :platform: Unix, Windows
   :synopsis: Parses a cim.v1.quality.cim_quality document.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
def _set_display_name(doc):
    """Sets document display name."""
    if len(doc.reports) and doc.reports[0].measure is not None:
        doc._display_name = doc.reports[0].measure.name


def _set_type_display_name(doc):
    """Sets document type display name."""
    doc._type_display_name = doc.doc_info.type_display_name = "QC Record"


def _set_summary_fields(doc):
    """Sets document summary fields."""
    if len(doc.doc_info.external_ids):
        doc._summary_fields += (
            doc.doc_info.external_ids[0].value, 
        )


def parse(doc):
    for parser in (
        _set_display_name, 
        _set_type_display_name, 
        _set_summary_fields):
        parser(doc)
