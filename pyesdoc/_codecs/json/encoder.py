"""
.. module:: json.encoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encodes a document as a JSON text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc._codecs.dictionary import encoder as dict_encoder
from pyesdoc.utils import convert



def encode(doc):
    """Encodes a document.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An encoded document representation.
    :rtype: unicode

    """
    return convert.dict_to_json(
      dict_encoder.encode(doc),
      convert.str_to_camel_case
      )
