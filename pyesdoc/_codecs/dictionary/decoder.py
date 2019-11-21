"""
.. module:: dictionary.decoder.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Decodes a document from a python dictionary.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc import ontologies
from pyesdoc.utils import convert



def _create_doc(obj, doc_type):
    """Creates & returns a document to be hydrated from a dictionary.

    """
    try:
        obj['meta']
    # ... only DocMetaInfo objects do not have a meta section.
    except KeyError:
        doc_type = ontologies.get_type_from_key('cim.2.shared.DocMetaInfo')
    else:
        if ontologies.get_type_key(doc_type) != obj['meta']['type']:
            doc_type = ontologies.get_type_from_key(obj['meta']['type'])
    finally:
        if doc_type is None:
            raise ValueError('Target decoding type is unrecognized')

    return doc_type(), ontologies.get_decoder_info(doc_type)


def _decode_simple(value, target_type, is_iterable):
    """Decodes a simple value.

    """
    if is_iterable:
        return [convert.text_to_typed_value(i, target_type) for i in value]
    return convert.text_to_typed_value(value, target_type)


def _decode(value, doc_type, is_iterable):
    """Decodes a dictionary.

    """
    def _do(obj):
        # Create doc.
        doc, doc_type_info = _create_doc(obj, doc_type)

        # Set doc attributes:
        for _name, _type, _is_iterable in doc_type_info:
            # ... skip placeholders;
            if _name not in obj:
                continue

            # ... set incoming value;
            _val = obj[_name]

            # ... nulls;
            if _val is None:
                setattr(doc, _name, [] if _is_iterable else None)

            # ... complex types;
            elif _type in ontologies.get_types():
                setattr(doc, _name, _decode(_val, _type, _is_iterable))

            # ... simple types;
            else:
                setattr(doc, _name, _decode_simple(_val, _type, _is_iterable))

        return doc

    return _do(value) if not is_iterable else [_do(i) for i in value]


def decode(as_dict):
    """Decodes a document from a dictionary.

    :param dict as_dict: A document in dictionary format.

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Format keys.
    as_dict = convert.dict_keys(as_dict, convert.str_to_underscore_case)

    # Get document type key.
    try:
        doc_type_key = as_dict['meta']['type']
    except KeyError:
        raise KeyError('Document pyesdoc type key is invalid.')

    # Get document type.
    doc_type = ontologies.get_type_from_key(doc_type_key)
    if doc_type is None:
        raise ValueError('Document pyesdoc type key is invalid.')

    return _decode(as_dict, doc_type, False)
