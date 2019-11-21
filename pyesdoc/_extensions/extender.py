"""
.. module:: extender.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes functions for extending documents.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc import exceptions
from pyesdoc._extensions import cim
from pyesdoc._extensions import default
from pyesdoc.ontologies import type_info
from pyesdoc.utils import runtime



# Supported extenders keyed by document type.
SUPPORTED = {}
for o in {cim.v1, cim.v2}:
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
        self.css_class = unicode()
        self.description = unicode()
        self.display_name = unicode()
        self.full_display_name = unicode()
        self.summary_fields = []
        self.type = unicode()
        self.viewer_url = unicode()


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
    if type(doc) not in type_info.TYPES:
        raise TypeError("Unsupported document type: {0}.".format(type(doc)))

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
                raise exceptions.ExtendingException(err, extender)

    # Step 3: invoke default post-extenders.
    for extender in default.POST_EXTENDERS:
        extender(ctx)

    return doc


def is_extendable(doc):
    """Returns flag indicating whether a document is extensible or not.

    :param doc: pyesdoc document instance or type key.
    :type doc: object | str

    :returns: A flag indicating whether a document is extensible or not.
    :rtype: boolean

    """
    if not isinstance(doc, str):
        runtime.assert_doc(doc)

    doc_type = doc if isinstance(doc, str) else doc.type_key
    doc_type = doc_type.lower()

    return doc_type in SUPPORTED
