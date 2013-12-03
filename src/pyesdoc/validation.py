"""
.. module:: pyesdoc.validation.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document validation functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
from .utils import runtime as rt



def validate(doc):
    """Validates a document.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :returns: A list of validation errors.
    :rtype: list

    """
    # Defensive programming.
    rt.assert_doc('doc', doc)

    # TODO 1. implement a validation algorithm based upon doc type info.
    # TODO 2. allow ontologies to implement custom validators.
    return []


def is_valid(doc):
    """Returns validation status of a document.

    :param doc: A pyesdoc document instance.
    :type doc: object

    :returns: Either True or False depending upon the document's validation state.
    :rtype: bool

    """
    return len(validate(doc)) == 0
