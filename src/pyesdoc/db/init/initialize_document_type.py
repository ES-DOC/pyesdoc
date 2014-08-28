"""
.. module:: initialize_document_type.py
   :platform: Unix
   :synopsis: Initializes collection of supported document types.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# -*- coding: iso-8859-15 -*-

# Module imports.
from .. import (
    dao,
    models, 
    session
    )
from ...utils import runtime as rt



def execute():
    """Initializes collection of cim document schema types.

    """
    ontologies = {}

    for type_key in cim_v1.ACTIVE_TYPES:
        # Unpack type info.
        o, v, p, t = type_key.split(".")
        o = o + "." + v

        # Cache.
        if o not in ontologies:
            ontologies[o] = dao.get_doc_ontology(o)

        # Create.
        i = models.DocumentType()
        i.Ontology_ID = ontologies[o].ID
        i.Key = type_key
        i.DisplayName = cim_v1.DISPLAY_NAMES[type_key]
        i.SearchTarget = type_key in cim_v1.SEARCH_TYPES

        # Persist.
        session.insert(i)

