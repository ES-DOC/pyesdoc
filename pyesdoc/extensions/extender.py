# -*- coding: utf-8 -*-

"""
.. module:: extender.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes functions for extending documents.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import pyesdoc
from pyesdoc.extensions import cim
from pyesdoc.extensions import default
from pyesdoc.utils import runtime as rt
from pyesdoc.ontologies import get_types



# Set of extenders mapped by ontology.
_ONTOLOGIES = {cim}

# Set of ontology types.
_TYPES = get_types()

# Supported extenders keyed by document type.
SUPPORTED = {}
for o in _ONTOLOGIES:
    for doc_type, doc_extender in o.SUPPORTED.iteritems():
        SUPPORTED[doc_type] = doc_extender


class _ExtensionContextInfo(object):
    """Document extension context information.

    """
    def __init__(self, doc, meta, ext):
        """Instance constructor.

        """
        self.doc = doc
        self.meta = meta
        self.ext = ext


class DocumentExtensionInfo(object):
    """Document extension information injected by extenders.

    """
    def __init__(self):
        """Instance constructor.

        """
        self.children = []
        self.css_class = str()
        self.description = str()
        self.display_name = str()
        self.encodings = []
        self.full_display_name = str()
        self.language = str()
        self.summary_fields = []
        self.type = str()
        self.viewer_url = str()


def extend(doc):
    """Invokes a document extender.

    :param doc: pyesdoc document instance.
    :type doc: object

    :returns: Extended document.
    :rtype: object

    """
    # Escape if extending null documents or already extended.
    if doc is None or hasattr(doc, 'ext'):
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
        mod = SUPPORTED[doc.type_key.lower()]
        # Step 2.1  Unpack child documents.
        try:
            mod.unpack_children(ctx)
        except AttributeError:
            pass

        # Step 2.2 Extend child documents (i.e. bottom up recursive extension).
        for child in ctx.ext.children:
            extend(child)

        # Step 2.3 Invoke extension callbacks.
        for extender in mod.get_extenders():
            try:
                extender(ctx)
            except Exception as err:
                raise pyesdoc.ExtendingException(err, extender)

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
    doc_type = doc_type.lower()

    return doc_type in SUPPORTED
