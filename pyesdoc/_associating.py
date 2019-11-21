"""
.. module:: pyesdoc._associating.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes document creation functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import uuid

from pyesdoc import exceptions
from pyesdoc import ontologies
from pyesdoc.ontologies import cim



def associate(source, target):
    """Associates a source document with a target document.

    :param object source: Source document.
    :param object target: Target document.

    :returns: Document reference encapsulating the association.
    :rtype: cim.v2.DocReference

    """
    if type(source) not in ontologies.type_info.TYPES:
        raise exceptions.InvalidDocumentTypeException(type(source))
    if type(target) not in ontologies.type_info.TYPES:
        raise exceptions.InvalidDocumentTypeException(type(target))

    association = cim.v2.DocReference()
    association.id = target.meta.id
    association.version = target.meta.version

    return association


def associate_by_id(source, target_id):
    """Associates a source document with target document identifer(s).

    :param object source: Source document.
    :param str target_id: Target document identifier.

    :returns: Document reference encapsulating the association.
    :rtype: cim.v2.DocReference

    """
    if type(source) not in ontologies.type_info.TYPES:
        raise exceptions.InvalidDocumentTypeException(type(source))
    try:
        uuid.UUID(target_id)
    except ValueError:
        raise ValueError("Document id must be uuid compatible")

    association = cim.v2.DocReference()
    association.id = target_id

    return association


def associate_by_id_and_version(source, target_id, target_version):
    """Associates a source document with target document identifer / version.

    :param object source: Source document.
    :param str target_id: Target document identifier.
    :param int target_version: Target document version.

    :returns: Document reference encapsulating the association.
    :rtype: cim.v2.DocReference

    """
    if type(source) not in ontologies.type_info.TYPES:
        raise exceptions.InvalidDocumentTypeException(type(source))
    try:
        uuid.UUID(target_id)
    except ValueError:
        raise ValueError("Document id must be uuid compatible")
    try:
        target_version = int(target_version)
    except ValueError:
        raise ValueError("Document version must be a positive integer")
    else:
        if target_version < 0:
            raise ValueError("Document version must be a positive integer")

    association = cim.v2.DocReference()
    association.id = target_id
    association.version = target_version

    return association


def associate_by_name(source, target_type, target_name):
    """Associates document(s) with another via document name.

    :param object source: Source document.
    :param class target_type: Type of target document.
    :param str target_name: Name of target document.

    :returns: Document reference encapsulating the association.
    :rtype: cim.v2.DocReference

    """
    if type(source) not in ontologies.type_info.TYPES:
        raise exceptions.InvalidDocumentTypeException(type(source))
    if target_type not in ontologies.type_info.TYPES:
        raise exceptions.InvalidDocumentTypeException(target_type)

    association = cim.v2.DocReference()
    association.name = target_name
    association.type = target_type.type_key

    return association
