"""
.. module:: xml_metafor_cim_v1.encoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encodes a document as a Metafor cim v1 XML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""

def encode(doc):
    """Encodes a document.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An encoded document representation.
    :rtype: unicode

    """
    raise NotImplementedError("Metafor XML endoing does not require an encoder.")
