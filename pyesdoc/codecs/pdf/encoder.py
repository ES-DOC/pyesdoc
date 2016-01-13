# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.pdf.encoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encodes a document as a PDF text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import pyesdoc
from pyesdoc import ontologies
from pyesdoc.codecs.pdf import encoders
from pyesdoc.codecs.pdf import encoder_utils as u



# Map of supported document types to PDF encoder types.
_PAGE_FACTORIES = {
    ontologies.cim.v2.NumericalExperiment: encoders.cim.v2.NumericalExperiment
}


def encode(doc):
    """Encodes a document.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An encoded document representation.
    :rtype: unicode

    """
    if type(doc) not in _PAGE_FACTORIES:
        raise ValueError("PDF encoding unsupported for documents of type {}.".format(type(doc)))

    # Ensure archive is initialized.
    pyesdoc.archive.init()

    # Ensure document is extended.
    pyesdoc.extend(doc)

    # Initialise PDF output.
    u.story = []
    u.set_frontis(doc)

    # Set document page factory & emit pages.
    page_factory = _PAGE_FACTORIES[type(doc)]
    page_factory(doc)

    return u.get_content()
