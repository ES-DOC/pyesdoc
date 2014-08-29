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



# Data to be inserted into db.
_DATA = u'''cim.1 | 1'''



def _get_data():
    """Yields rows to be uploaded to db."""
    for row in [l.split('|') for l in _DATA.splitlines()]:
        for i in range(len(row)):
            row[i] = row[i].strip()
        yield row


def execute():
    """Initializes collection of document ontologies.

    """
    for row in _get_data():
        # Create.
        i = models.DocumentOntology()
        i.Name = row[0]
        i.Version = row[1]

        # Persist.
        session.insert(i)
