# -*- coding: utf-8 -*-

"""
.. module:: extender.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes functions for extending documents.

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

# Supported extenders keyed by document type.
SUPPORTED = {}
for o in _ONTOLOGIES:
    for d_type, d_extender in o.SUPPORTED.iteritems():
        SUPPORTED[d_type] = d_extender

# Document extension context information.
_ExtensionContextInfo = namedtuple('ExtensionContextInfo', ['doc', 'meta', 'ext'])


class DocumentExtensionInfo(object):
    """Document extension information injected by extenders.

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


def extend(doc):
    """Invokes a document extender.

    :param doc: pyesdoc document instance.
    :type doc: object

    :returns: Extended document.
    :rtype: object

    """
    # Escape if extending null documents.
    if doc is None:
        return

    # Verify that document type is supported.
    if type(doc) not in _TYPES:
        rt.throw("Unsupported document type: {0}.".format(type(doc)))

    # Initialize document extension information.
    doc.ext = DocumentExtensionInfo()

    # Instantiate extension context.
    ctx = _ExtensionContextInfo(doc, doc.meta, doc.ext)

    # Step 1: invoke default pre-extenders.
    for extender in default.PRE_EXTENDERS:
        extender(ctx)

    # Step 2: invoke type specific extenders.
    if is_extendable(doc):
        for extender in SUPPORTED[doc.type_key.lower()].EXTENDERS:
            extender(ctx)

    # Step 3: invoke default post-extenders.
    for extender in default.POST_EXTENDERS:
        extender(ctx)

    return doc


def is_extendable(doc):
    """Returns flag indicating whether document extension is supported.

    :param doc: pyesdoc document instance or type key.
    :type doc: object | str

    """
    # Defensive programming.
    if not isinstance(doc, str):
        rt.assert_doc('doc', doc, "Invalid document")

    doc_type = doc if isinstance(doc, str) else doc.type_key

    return doc_type.lower() in SUPPORTED
