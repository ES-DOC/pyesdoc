"""
.. module:: pyesdoc.serialization.decoder_json.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes functions for decoding document instances from json representations.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
try:
    import simplejson as json
except ImportError:
    import json


def decode(representation, schema):
    """Decodes a pyesdoc document from a json representation.

    :param representation: A document json representation.
    :type representation: str

    :param schema: A document schema (e.g. CIM v1).
    :type schema: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    as_dict = json.loads(representation)
    
    # TODO 1. From dictionary representation get type info.
    # TODO 2. Instantiate type.
    # TODO 3. Hydrate type.

    return as_dict


