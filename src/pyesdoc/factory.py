"""
.. module:: pyesdoc.factory.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document creation functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import datetime
import uuid

from . import constants, ontologies
from . utils import runtime as rt



def _assert_type(typeof):
    """Asserts that the passed type is a supported pyesdoc document type reference."""
    if isinstance(typeof, str):
        o, v, p, t = typeof.split('.')
        if not ontologies.is_supported(o, v, p, t):
            rt.throw("Type {0}.v{1}.{2} is unsupported.".format(o, v, p, t))
    elif typeof not in ontologies.get_types():
        rt.throw("Type {0} is unsupported.".format(typeof))


def create(typeof,
           project,
           institute,
           language=constants.ESDOC_DEFAULT_LANGUAGE,
           source=None):
    """Creates a document.

    :param typeof: Ontology type, e.g. cim.1.software.ModelComponent.
    :type typeof: str | class
    :param str project: Project wih which instance is associated.
    :param str institute: Institute wih which instance is associated.
    :param str source: Source application with which instance is associated.

    :returns: A pyesdoc document instance.
    :rtype: pyesdoc object

    """
    # Defensive programming.
    _assert_type(typeof)
    rt.assert_var('institute', institute, str)
    rt.assert_var('project', project, str)
    rt.assert_var('language', language, str)
    if source is not None:
        rt.assert_var('source', source, str)

    # Format params.
    institute = str(institute).lower()
    language = str(language).lower()
    project = str(project).lower()
    source = source if source is not None else institute

    # Create document.
    doc = None
    if isinstance(typeof, str):
        ontology, version, package, type_ = typeof.split('.')
        doc = ontologies.create(ontology, version, package, type_)
    else:
        doc = typeof()

    # Assign document meta info.
    if doc is not None and hasattr(doc, 'meta'):
        doc.meta.id = uuid.uuid4()
        doc.meta.version = 0
        doc.meta.create_date = datetime.datetime.now()
        doc.meta.institute = institute
        doc.meta.language = language
        doc.meta.project = project
        doc.meta.type = doc.__class__.type_key
        doc.meta.source = source

    return doc
