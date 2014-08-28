"""
.. module:: accessors.py
   :copyright: Copyright "Jun 12, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Cache accessor functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
from . import core
from .. import models



def get_doc_encoding(item_id=None):
    """Returns either all document encodings or first document encoding with matching name.

    :param item_id: Document encoding identifier.
    :type item_id: str | int

    :returns: Either a document encoding list or an instance.
    :rtype: list | models.DocumentEncoding

    """
    return core.get(models.DocumentEncoding, item_id)


def get_doc_language(item_id=None):
    """Returns either all document languages or first document language with matching name.

    :param item_id: Document language identifier.
    :type item_id: str | int

    :returns: Either a document language list or an instance.
    :rtype: list | models.DocumentLanguage

    """
    return core.get(models.DocumentLanguage, item_id)


def get_doc_ontology(name=None, version=None):
    """Returns either all document ontologies or first document ontology with matching name.

    :param str name: Document ontology name.
    :param str version: Document ontology version.

    :returns: Either list of all ontologies or first matching ontology.
    :rtype: list or models.DocumentOntology

    """
    if name is None:
        return core.get(models.DocumentOntology)

    if version is not None:
        name += "."
        name += str(version)

    for ontology in core.get(models.DocumentOntology):
        if ontology.Name.upper() == name.upper():
            return ontology

    return None


def get_doc_type(item_id=None):
    """Returns either all document types or first document type with matching name.

    :param item_id: Document type identifier.
    :type item_id: str | int

    :returns: Either a document type list or an instance.
    :rtype: list | models.DocumentType

    """
    return core.get(models.DocumentType, item_id)


def get_institute(item_id=None):
    """Returns either all institutes or first institute with matching name.

    :param item_id: Institute identifier.
    :type item_id: str | int

    :returns: Either an institute list or an instance.
    :rtype: list | models.Institute

    """
    return core.get(models.Institute, item_id)


def get_institute_id(item_id):
    """Returns ID of first institute with matching name.

    :param item_id: Institute identifier.
    :type item_id: str | int

    :returns: An institute instance identifier or None.
    :rtype: None | int

    """
    return core.get_id(models.Institute, item_id)


def get_project(item_id=None):
    """Returns either all projects or first project with matching name.

    :param item_id: Project identifier.
    :type item_id: str | int

    :returns: Either a project list or an instance.
    :rtype: list | models.Project

    """
    return core.get(models.Project, item_id)


def get_project_id(item_id):
    """Returns ID of first project with matching name.

    :param item_id: Project identifier.
    :type item_id: str | int

    :returns: A project instance identifier or None.
    :rtype: None | int

    """
    return core.get_id(models.Project, item_id)
