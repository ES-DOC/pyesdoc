"""
.. module:: doc_parser_esdoc_q.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: ES-DOC questionniare docuemnt parser.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def _set_institute(doc):
    """Set default institute name."""
    if doc.meta.institute is None:
        doc.meta.institute = "--"


# Set of document parsers.
PARSERS = (
    _set_institute,
    )
