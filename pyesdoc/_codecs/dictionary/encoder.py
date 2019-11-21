"""
.. module:: dictionary.encoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Enocdes a document as a python dictionary.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc import ontologies



def _is_pyesdoc_type(obj):
    """Returns flag indicating whether an object is a pyesdoc type.

    """
    return isinstance(obj, ontologies.get_types())


def _is_encodable_attribute(name):
    """Returns flag indicating whether an attribute is encodable.

    """
    if name.startswith("_") or name.startswith("__") or name == "ext":
        return False
    return True


def encode(doc):
    """Encodes a document.

    :param doc: Document being encoded.
    :type doc: object

    :returns: An encoded document representation.
    :rtype: dict

    """
    obj = dict()

    for key, val in doc.__dict__.items():
        # Escape private/magic properties.
        if not _is_encodable_attribute(key):
            continue

        # Process iterables / non-iterables differently.
        try:
            iter(val)

        # Encode non-iterables:
        except TypeError:
            # ... pyesdoc types;
            if _is_pyesdoc_type(val):
                obj[key] = encode(val)
            # ... simple types;
            elif val is not None:
                obj[key] = val

        # Encode iterables:
        else:
            if len(val) > 0:
                # ... string types;
                if isinstance(val, (str, unicode)):
                    obj[key] = val
                # ... collections;
                else:
                    obj[key] = [encode(i) if _is_pyesdoc_type(i) else i for i in val]

    # Inject type info to simplify decoding.
    if doc.__class__.__name__ != "DocMetaInfo":
        if 'meta' not in obj:
            obj['meta'] = {}
        obj['meta']['type'] = type(doc).type_key

    return obj
