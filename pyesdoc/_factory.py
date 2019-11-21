"""
.. module:: pyesdoc._factory.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document creation functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime
import uuid

from pyesdoc import exceptions
from pyesdoc import ontologies



def create(
    typeof,
    project=None,
    sub_projects=None,
    institute=None,
    source=None,
    author=None,
    uid=None,
    version=0
    ):
    """Creates a document.

    :param class typeof: Ontology type, e.g. cim.1.software.ModelComponent.
    :param str project: Project wih which instance is associated.
    :param list|str sub_projects: Sub-project(s) with which instance is associated.
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
    if sub_projects:
        if isinstance(sub_projects, (str, unicode)):
            sub_projects = [sub_projects]
        sub_projects = [unicode(i).lower() for i in sub_projects]

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
        doc.meta.institute = institute or None
        doc.meta.project = project or None
        doc.meta.sub_projects = sub_projects or []
        doc.meta.source = source or None
        doc.meta.type = typeof.type_key

    return doc
