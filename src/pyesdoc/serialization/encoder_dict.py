"""
.. module:: encoder_dict.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Dictionary encoder from document.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
from .. import ontologies



# Set of ontology types.
_TYPES = ontologies.get_types()


def _is_encodable(obj):
    """Returns flag indicating whether an object is encodable or not."""
    return type(obj) in _TYPES


def _encode(doc):
    """Encodes an object to a deep dictionary."""
    result = {
        'ontology_type_key' : type(doc).type_key
    }

    # Iterate document dictionary key/value pairs.
    for k, v in doc.__dict__.items():
        # Omit private members.
        if k[0]  == "_" or k[0:2]  == "__":
            continue

        # Test for iterability.
        try:
            iter(v)
        # ... non-iterables
        except TypeError:
            result[k] = _encode(v) if _is_encodable(v) else v
        # ... iterables
        else:
            # ... strings / unicodes
            if type(v) in (str, unicode,):
                result[k] = v
            # ... mapped
            else:
                result[k] = map(lambda i : _encode(i) if _is_encodable(i) else i, v)

    return result


def encode(doc):
    """Encodes a document to a dictionary.

    :param doc: Document being encoded.
    :type doc: object.

    :returns: A dictionary representation of a document.
    :rtype: dict

    """
    return _encode(doc)