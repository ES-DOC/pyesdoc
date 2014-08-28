"""
.. module:: initialize_document_encoding.py
   :platform: Unix
   :synopsis: Initializes collection of supported document encodings.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# -*- coding: iso-8859-15 -*-

# Module imports.
from .. import (
    models,
    session
    )
from ... import constants


def execute():
    """Initializes collection of supported document encodings.

    """
    for encoding in (constants.ESDOC_ENCODINGS + constants.ESDOC_ENCODINGS_CUSTOM):
        # Create.
        i = models.DocumentEncoding()
        i.Encoding = encoding

        # Persist.
        session.insert(i)
