"""
.. module:: json.decoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Decodes a document from a JSON text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc._codecs.dictionary import decoder as dict_decoder
from pyesdoc.utils import convertor



def decode(as_json):
    """Decodes a document from a UTF-8 encoded json text blob.

    :param as_json: Document json representation.
    :returns: A pyesdoc document instance.

    """
    # Convert to dictionary.
    as_dict = convertor.json_to_dict(as_json)

    # Decode from dictionary.
    return dict_decoder.decode(as_dict)
