"""
.. module:: pyesdoc.serialization.decoder_json.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Exposes functions for decoding document instances from json representations.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>

"""

# Module imports.
import json


def decode(ctx):
    """Decodes a pyesdoc document from a json representation.

    :param ctx: Serialization context info.
    :type ctx: namedtuple

    """    
    # TODO 1. From dictionary representation get type info.
    # TODO 2. Instantiate type.
    # TODO 3. Hydrate type.
    ctx.instance = json.loads(ctx.representation)
