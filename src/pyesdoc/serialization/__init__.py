"""
.. module:: pyesdoc.serialization.__init__.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package initialisor.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from collections import namedtuple

from pyesdoc.utils.ontologies import is_supported as is_supported_ontology
from pyesdoc.serialization.decoder_json import decode as json_decoder
from pyesdoc.serialization.decoder_xml import decode as xml_decoder
from pyesdoc.serialization.encoder_json import encode as json_encoder
from pyesdoc.serialization.encoder_xml import encode as xml_encoder
from pyesdoc.utils.exception import PYESDOC_Exception



class _ContextInfo(object):
    """Contextual information passed around during serialization operations.

    """
    def __init__(self,
                 schema_name,
                 schema_version,
                 encoding,
                 type=None,
                 representation=None,
                 instance=None):
        self.schema_name = str(schema_name).upper()
        self.schema_version = str(schema_version).upper()
        self.encoding = str(encoding).lower()
        self.type = type
        self.representation = representation
        self.instance = instance


# Set of supported ESDOC encodings.
ESDOC_ENCODING_JSON = 'json'
ESDOC_ENCODING_XML = 'xml'

# Set of decoders.
_decoders = {
    ESDOC_ENCODING_JSON : json_decoder,
    ESDOC_ENCODING_XML : xml_decoder,
}

# Set of encoders.
_encoders = {
    ESDOC_ENCODING_JSON : json_encoder,
    ESDOC_ENCODING_XML : xml_encoder,
}



def decode(representation, schema_name, schema_version, encoding):
    """Decodes a pyesdoc document representation.

    :param representation: A document representation (e.g. utf-8).
    :type representation: str

    :param schema_name: A document schema (e.g. CIM).
    :type schema_name: str

    :param schema_version: A document schema version (e.g. v1).
    :type schema_version: str

    :param encoding: A document encoding (e.g. json).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    if representation is None:
        raise PYESDOC_Exception('Document instances cannot be decoded from null objects.')
    if not is_supported_ontology(schema_name, schema_version):
        msg = "Ontology {0} v{1} is unsupported."
        raise PYESDOC_Exception(msg.format(schema_name, schema_version))
    if not encoding in _decoders:
        raise PYESDOC_Exception("{0} decoding unsupported.".format(encoding))

    ctx = _ContextInfo(schema_name, schema_version, encoding, representation=representation)
    _decoders[encoding](ctx)

    return ctx.instance


def encode(instance, schema_name, schema_version, encoding):
    """Encodes a pyesdoc document instance.

    :param instance: pyesdoc document instance.
    :type instance: object

    :param schema_name: A document schema (e.g. CIM).
    :type schema_name: str

    :param schema_version: A document schema version (e.g. v1).
    :type schema_version: str
    
    :param encoding: A document encoding (e.g. json).
    :type encoding: str

    :returns: A pyesdoc document instance.
    :rtype: object

    """
    # Defensive programming.
    if instance is None:
        raise PYESDOC_Exception('Cannot encode null objects.')
    if not is_supported_ontology(schema_name, schema_version):
        msg = "Schema {0} v{1} (encoding {2}) is unsupported."
        raise PYESDOC_Exception(msg.format(schema_name, schema_version, encoding))
    if not encoding in _encoders:
        raise PYESDOC_Exception("{0} encoding unsupported.".format(encoding))

    ctx = _ContextInfo(schema_name, schema_version, encoding, instance=instance)
    _encoders[encoding](ctx)

    return ctx.representation
