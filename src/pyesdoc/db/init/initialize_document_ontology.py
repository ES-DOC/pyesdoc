"""
.. module:: initialize_document_ontology.py
   :platform: Unix
   :synopsis: Initializes collection of supported document ontologies.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# -*- coding: iso-8859-15 -*-

# Module imports.
from .. import (
    models, 
    session
    )
from ...utils import runtime as rt



_DATA = u'''cim.1 | 1'''


def execute():
    """Initializes collection of document ontologies.

    """
    for row in get_rows(_DATA):
        # Create.
        i = models.DocumentOntology()
        i.Name = row[0]
        i.Version = row[1]

        # Persist.
        session.insert(i)
