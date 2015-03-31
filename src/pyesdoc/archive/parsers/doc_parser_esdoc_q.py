# -*- coding: utf-8 -*-
"""
.. module:: handlers_metafor_q.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes Metafor Questionnaire document processing handlers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from ...utils import runtime as rt



# CIM v1 type keys.
_TYPE_KEY_MODEL_COMPONENT = 'cim.1.software.modelcomponent'




def get_parsers():
    """Returns set of document parsers.

    """
    return (
        _set_document_type,
        )





def _is_of_type(doc, type_key):
    """Helper function: returns document type match.

    """
    return doc.type_key.lower() == type_key


def _set_document_type(doc):
    """Sets document type when unassigned.

    """
    if _is_of_type(doc, _TYPE_KEY_MODEL_COMPONENT) and not doc.types:
        doc.type = _TYPE_KEY_MODEL_COMPONENT
        doc.types = [doc.type]
