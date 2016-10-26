# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.factory.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document creation functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections
import datetime
import uuid

from pyesdoc import constants
from pyesdoc import exceptions
from pyesdoc import ontologies



def create(
    typeof,
    project=None,
    institute=None,
    source=None,
    author=None,
    uid=None,
    version=0
    ):
    """Creates a document.

    :param class typeof: Ontology type, e.g. cim.1.software.ModelComponent.
    :param str project: Project wih which instance is associated.
    :param str institute: Institute wih which instance is associated.
    :param str source: Source application with which instance is associated.
    :param str author: Author wih which instance is associated.
    :param uuid.UUID uid: Document unique identifier.

    :returns: A pyesdoc document instance.
    :rtype: pyesdoc object

    """
    # Validate document type.
    if typeof not in ontologies.type_info.TYPES:
        raise exceptions.InvalidDocumentTypeException(typeof)

    # Set defaults.
    if not uid:
        uid = uuid.uuid4()

    # Reformat.
    if institute:
        institute = unicode(institute).lower()
    if project:
        project = unicode(project).lower()
    if source:
        source = unicode(source).lower()
    elif institute:
        source = institute
    elif project:
        source = project
    uid = unicode(uid)

    # Verify uid.
    try:
        uuid.UUID(uid)
    except ValueError:
        raise ValueError("Document identifiers must be UUID's.")

    # Instantiate & initialize meta info (if necessary).
    doc = typeof()
    if hasattr(doc, 'meta'):
        doc.meta.author = author
        doc.meta.id = uid
        doc.meta.version = version
        doc.meta.create_date = datetime.datetime.now()
        if institute:
            doc.meta.institute = institute
        if project:
            doc.meta.project = project
        if source:
            doc.meta.source = source
        doc.meta.type = typeof.type_key

    return doc


def create_notebook_output(obj):
    """Returns output for an IPython notebook.

    """
    doc = collections.OrderedDict()
    for k in sorted(obj.keys()):
        doc[k] = obj[k]

    return doc
