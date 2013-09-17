"""
.. module:: pyesdoc.factory.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document creation functions.

.. moduleauthor:: Mark Conway-Greenslade (formerly Morgan) <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import datetime
import uuid

from . import ESDOC_DEFAULT_LANGUAGE
from . import ontologies
from .utils import runtime as rt



def _assert_type(o, v, p, t):
    """Asserts document type."""
    if not ontologies.is_supported(o, v, p, t):
        _raise("Type {0}.v{1}.{2} is unsupported.".format(o, v, p, t))


# Module imports.
def create(ontology_name,
           ontology_version,
           ontology_package,
           ontology_type,
           institute,
           project,
           language=ESDOC_DEFAULT_LANGUAGE):
    """Creates a document.

    :param ontology_name: Ontology name, e.g. cim.
    :type ontology_name: str

    :param ontology_version: Ontology version, e.g. 1.
    :type ontology_version: str

    :param ontology_package: Ontology package, e.g. activity.
    :type ontology_package: str

    :param ontology_type: Ontology type, e.g. Experiment.
    :type ontology_type: str

    :returns: A pyesdoc document instance.
    :rtype: pyesdoc object

    """
    # Defensive programming.
    _assert_type(ontology_name, ontology_version, ontology_package, ontology_type)
    rt.assert_var('institute', institute, str)
    rt.assert_var('project', project, str)
    rt.assert_var('language', language, str)

    # Create document.
    doc = ontologies.create(ontology_name,
                            ontology_version,
                            ontology_package,
                            ontology_type)

    # Auto assign defaults if dealing with a publishable document.
    if doc is not None and hasattr(doc, 'doc_info'):
        doc.doc_info.id = uuid.uuid4()
        doc.doc_info.version = 0
        doc.doc_info.create_date = datetime.datetime.now()
        doc.doc_info.institute = str(institute).lower()
        doc.doc_info.language = str(language).lower()
        doc.doc_info.project = str(project).lower()

    return doc
