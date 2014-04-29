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



def _assert_type(type):
    """Asserts that the passed type is a supported pyesdoc document type reference."""
    if isinstance(type, str):
        o, v, p, t = type.split('.')
        if not ontologies.is_supported(o, v, p, t):
            rt.throw("Type {0}.v{1}.{2} is unsupported.".format(o, v, p, t))
    elif type not in ontologies.get_types():
        rt.throw("Type {0} is unsupported.".format(type))


def create(type, project, institute, language=constants.ESDOC_DEFAULT_LANGUAGE):
    """Creates a document.

    :param type: Ontology type, e.g. cim.1.software.ModelComponent.
    :type type: str

    :param project: Project wih which instance is associated.
    :type project: str

    :param institute: Institute wih which instance is associated.
    :type institute: str

    :returns: A pyesdoc document instance.
    :rtype: pyesdoc object

    """
    # Defensive programming.
    _assert_type(type)
    rt.assert_var('institute', institute, str)
    rt.assert_var('project', project, str)
    rt.assert_var('language', language, str)

    # Create document.
    doc = None
    if isinstance(type, str):
        o, v, p, t = type.split('.')
        doc = ontologies.create(o, v, p, t)
    else:
        doc = type()
        
    # Assign document meta info.
    if doc is not None and hasattr(doc, 'meta'):
        doc.meta.id = uuid.uuid4()
        doc.meta.version = 0
        doc.meta.create_date = datetime.datetime.now()
        doc.meta.institute = str(institute).lower()
        doc.meta.language = str(language).lower()
        doc.meta.project = str(project).lower()

    return doc
