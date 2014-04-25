# -*- coding: utf-8 -*-

"""
.. module:: parse.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes functions for parsing documents.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from collections import namedtuple

from . import cim, default
from .. utils import runtime as rt
from .. ontologies import get_types



# Set of ontologies.
_ONTOLOGIES = [cim]

# Set of ontology types.
_TYPES = get_types()

# Supported parsers keyed by document type.
SUPPORTED = {}
for o in _ONTOLOGIES:
    for doc_type, doc_parser in o.SUPPORTED.iteritems():
        SUPPORTED[doc_type] = doc_parser

# Document parsing context information.
_ParsingContextInfo = namedtuple('ParsingContextInfo', ['doc', 'meta', 'ext'])


class DocumentExtensionInfo(object):
    """Document extension information injected by parsers.

    """
    def __init__(self):
        """Constructor.

        """
        self.description = str()
        self.display_name = str()
        self.encodings = []
        self.full_display_name = str()
        self.language = str()
        self.summary_fields = []
        self.type = str()
        self.type_display_name = str()


def parse(doc):
    """Invokes a document parser.

    :param doc: pyesdoc document instance.
    :type doc: object

    :returns: Parsed document.
    :rtype: object

    """
    # Escape is parsing null document.
    if doc is None:
        return

    # Verify that document type is supported.
    if type(doc) not in _TYPES:
        rt.throw("Unsupported document type: {0}.".format(type(doc)))

    # Initialize document extension information.
    doc.ext = DocumentExtensionInfo()

    # Instantiate parsing context.
    ctx = _ParsingContextInfo(doc, doc.meta, doc.ext)

    # Perform default pre-parsing.
    for parser in default.PRE_PARSERS:
        parser(ctx)

    # Perform type specific parsing.
    if is_parseable(doc):
        for parser in SUPPORTED[doc.type_key.lower()].PARSERS:
            parser(ctx)

    # Perform default post-parsing.
    for parser in default.POST_PARSERS:
        parser(ctx)

    return doc


def is_parseable(doc):
    """Returns flag indicating whether document parsing is supported.

    :param doc: pyesdoc document instance or type key.
    :type doc: object | str

    """
    # Defensive programming.
    if not isinstance(doc, str):
        rt.assert_doc('doc', doc, "Invalid document")

    doc_type = doc if isinstance(doc, str) else doc.type_key

    return doc_type.lower() in SUPPORTED
