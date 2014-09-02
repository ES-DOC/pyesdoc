"""
.. module:: docs.py
   :platform: Unix
   :synopsis: Data access operations across docs domain space.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import sqlalchemy as sa

from . core import (
    delete_by_type,
    delete_by_id,
    delete_by_facet,
    get_by_id,
    get_by_facet,
    get_by_name,
    sort
    )
from .. import (
    models,
    session
    )
from .. models import (
    Document,
    DocumentDRS,
    DocumentExternalID,
    DocumentLanguage,
    DocumentOntology,
    DocumentSummary,
    Institute,
    Project
)



# Module exports.
__all__ = [
    'delete_all_documents',
    'delete_document',
    'delete_document_drs',
    'delete_document_external_ids',
    'delete_document_summaries',
    'get_document',
    'get_document_by_drs_keys',
    'get_document_by_name',
    'get_document_by_type',
    'get_document_counts',
    'get_doc_descriptions',
    'get_document_drs',
    'get_document_external_id',
    'get_document_external_ids',
    'get_document_summaries',
    'get_document_summary',
    'get_document_type_count',
    'get_documents_by_external_id',
    'get_project_document_type_counts',
    'get_summary_eperiment_set',
    'get_summary_model_set',
]



def get_document(project_id,
                 uid,
                 version=models.DOCUMENT_VERSION_LATEST):
    """Returns a Document instance by it's project, UID & version.

    :param project_id: ID of a Project instance.
    :type project_id: int

    :param uid: Document unique identifier.
    :type uid: str

    :param version: Document version.
    :type version: str

    :returns: First matching document.
    :rtype: db.models.Document

    """
    q = session.query(Document)

    if project_id is not None:
        q = q.filter(Document.Project_ID==project_id)
    q = q.filter(Document.UID==unicode(uid))
    if version is None or version in models.DOCUMENT_VERSIONS:
        q = q.order_by(Document.Version.desc())
    else:
        q = q.filter(Document.Version==int(version))

    return q.all() if version == models.DOCUMENT_VERSION_ALL else q.first()


def get_document_by_name(project_id,
                         type,
                         name,
                         institute_id=None,
                         latest_only=True):
    """Retrieves a single document by it's name.

    :param project_id: ID of a Project instance.
    :type project_id: int

    :param type: Document type.
    :type type: str

    :param name: Document name.
    :type name: str

    :param institute_id: ID of an Institute instance.
    :type institute_id: int

    :param latest_only: Project with which document is associated.
    :type latest_only: boolean

    :returns: First matching document.
    :rtype: db.models.Document

    """
    q = session.query(Document)

    q = q.filter(Document.Project_ID==project_id)
    q = q.filter(sa.func.upper(Document.Type)==type.upper())
    q = q.filter(sa.func.upper(Document.Name)==name.upper())
    if institute_id is not None:
        q = q.filter(Document.Institute_ID==institute_id)
    if latest_only == True:
        q = q.filter(Document.IsLatest==True)

    return q.first()


def get_document_by_type(project_id,
                         type,
                         latest_only=True):
    """Retrieves documents by type.

    :param project_id: ID of a Project instance.
    :type project_id: int

    :param type: Document type.
    :type type: str

    :param latest_only: Flag indicating whether to return only the latest documents.
    :type latest_only: boolean

    :returns: Matching documents.
    :rtype: list

    """
    q = session.query(Document)

    q = q.filter(Document.Project_ID==project_id)
    q = q.filter(sa.func.upper(Document.Type)==type.upper())
    if latest_only == True:
        q = q.filter(Document.IsLatest==True)

    return q.all()


def get_document_by_drs_keys(project_id,
                             key_01=None,
                             key_02=None,
                             key_03=None,
                             key_04=None,
                             key_05=None,
                             key_06=None,
                             key_07=None,
                             key_08=None,
                             latest_only = True):
    """Retrieves a single document by it's drs keys.

    :param project_id: ID of a Project instance.
    :type project_id: int

    :param key_01: DRS key 1.
    :type key_01: str

    :param key_02: DRS key 2.
    :type key_02: str

    :param key_03: DRS key 3.
    :type key_03: str

    :param key_04: DRS key 4.
    :type key_04: str

    :param key_05: DRS key 5.
    :type key_05: str

    :param key_06: DRS key 6.
    :type key_06: str

    :param key_07: DRS key 7.
    :type key_07: str

    :param key_08: DRS key 8.
    :type key_08: str

    :param latest_only: Flag indicating whether only the latest document is to be returned.
    :type latest_only: boolean

    :returns: First matching document.
    :rtype: db.models.Document

    """
    q = session.query(Document).join(DocumentDRS)

    q = q.filter(Document.Project_ID==project_id)
    if key_01 is not None:
        q = q.filter(DocumentDRS.Key_01==key_01.upper())
    if key_02 is not None:
        q = q.filter(DocumentDRS.Key_02==key_02.upper())
    if key_03 is not None:
        q = q.filter(DocumentDRS.Key_03==key_03.upper())
    if key_04 is not None:
        q = q.filter(DocumentDRS.Key_04==key_04.upper())
    if key_05 is not None:
        q = q.filter(DocumentDRS.Key_05==key_05.upper())
    if key_06 is not None:
        q = q.filter(DocumentDRS.Key_06==key_06.upper())
    if key_07 is not None:
        q = q.filter(DocumentDRS.Key_07==key_07.upper())
    if key_08 is not None:
        q = q.filter(DocumentDRS.Key_08==key_08.upper())
    if latest_only == True:
        q = q.filter(Document.IsLatest==True)

    return q.first()


def get_documents_by_external_id(project_id, external_id):
    """Retrieves a list of documents with a matching external ID.

    :param project_id: ID of a Project instance.
    :type project_id: int

    :param external_id: External ID to be resolved to a document.
    :type external_id: str

    :returns: List of Document instances with matching external ID.
    :rtype: list

    """
    q = session.query(Document).join(DocumentExternalID)

    q = q.filter(Document.Project_ID==project_id)
    q = q.filter(DocumentExternalID.ExternalID.like('%' + external_id.upper() + '%'))

    return q.all()


def get_document_drs(project_id, document_id, path):
    """Returns a DocumentDRS instance with matching document & drs path.

    :param project_id: ID of a Project instance.
    :type project_id: int

    :param document_id: ID of a Document instance.
    :type document_id: int

    :param path: DRS path.
    :type path: str

    :returns: First DocumentDRS instance with matching document & drs path.
    :rtype: db.models.DocumentDRS

    """
    q = session.query(DocumentDRS)

    q = q.filter(DocumentDRS.Project_ID==project_id)
    q = q.filter(DocumentDRS.Document_ID==document_id)
    q = q.filter(DocumentDRS.Path==path.upper())

    return q.first()


def get_document_external_id(project_id, document_id, external_id):
    """Returns a DocumentExternalID instance with matching document & external id.

    :param project_id: ID of a Project instance.
    :type project_id: int

    :param document_id: ID of a Document instance.
    :type document_id: int

    :param external_id: An external ID.
    :type external_id: str

    :returns: First DocumentExternalID instance with matching document & external id.
    :rtype: db.models.DocumentExternalID

    """
    q = session.query(DocumentExternalID)

    q = q.filter(DocumentExternalID.Project_ID==project_id)
    q = q.filter(DocumentExternalID.Document_ID==document_id)
    q = q.filter(DocumentExternalID.ExternalID==external_id)

    return q.first()


def get_document_external_ids(document_id, project_id=None):
    """Returns a DocumentExternalID instance with matching document & external id.

    :param document_id: ID of a Document instance.
    :type document_id: int

    :param project_id: ID of a Project instance.
    :type project_id: int or None

    :param external_id: An external ID.
    :type external_id: str

    :returns: First DocumentExternalID instance with matching document & external id.
    :rtype: db.models.DocumentExternalID

    """
    q = session.query(DocumentExternalID)

    q = q.filter(DocumentExternalID.Document_ID==document_id)
    if project_id is not None:
        q = q.filter(DocumentExternalID.Project_ID==project_id)

    return q.all()


def get_document_summary(document_id, language_id):
    """Returns a DocumentSummary instance with matching document & language.

    :param document_id: ID of a Document instance.
    :type document_id: int

    :param language_id: ID of a DocumentLanguage instance.
    :type language_id: int

    :returns: First DocumentSummary instance with matching document & language.
    :rtype: db.models.DocumentSummary

    """
    q = session.query(DocumentSummary)

    q = q.filter(DocumentSummary.Document_ID==document_id)
    q = q.filter(DocumentSummary.Language_ID==language_id)

    return q.first()


def get_document_summaries(
    project_id,
    type,
    version,
    language_id,
    institute_id=None,
    model=None,
    experiment=None):
    """Returns a list of DocumentSummary instance with matching criteria.

    :param int project_id: ID of a Project instance.
    :param str type: Document type.
    :param str version: Document version (latest | all).
    :param int language_id: ID of a DocumentLanguage instance.
    :param int institute_id: ID of an Institute instance.

    :returns: First DocumentSummary instance with matching document & language.
    :rtype: db.models.DocumentSummary

    """
    # Format params.
    version = version.lower()
    type = type.upper()
    if model:
        model = model.upper()
    if experiment:
        experiment = experiment.upper()

    # Set query.
    q = session.query(DocumentSummary).join(Document)

    # Set mandatory params.
    q = q.filter(Document.Project_ID==project_id)
    q = q.filter(DocumentSummary.Language_ID==language_id)
    if type != models.DOCUMENT_TYPE_ALL:
        q = q.filter(sa.func.upper(Document.Type)==type)
    if version == models.DOCUMENT_VERSION_LATEST:
        q = q.filter(Document.IsLatest==True)
    if experiment is not None:
        q = q.filter(sa.func.upper(DocumentSummary.Experiment)==experiment)
    if institute_id is not None:
        q = q.filter(Document.Institute_ID==institute_id)
    if model is not None:
        q = q.filter(sa.func.upper(DocumentSummary.Model)==model)

    # Apply query limit.
    q = q.limit(session.QUERY_LIMIT)

    return sort(DocumentSummary, q.all())


def _delete_document_relation(document_id, type):
    """Deletes all document relations of passed type.

    :param document_id: ID of a Document instance.
    :type document_id: int

    :param type: Type of relation.
    :type type: class

    """
    delete_by_facet(type, type.Document_ID==document_id)


def delete_document_summaries(document_id):
    """Deletes a list of DocumentSummary instances filtered by their Document ID.

    :param document_id: ID of a Document instance.
    :type document_id: int

    """
    _delete_document_relation(document_id, DocumentSummary)


def delete_document_external_ids(document_id):
    """Deletes a list of DocumentExternalID instances filtered by their Document ID.

    :param document_id: ID of a Document instance.
    :type document_id: int

    """
    _delete_document_relation(document_id, DocumentExternalID)


def delete_document_drs(document_id):
    """Deletes a list of DocumentDRS instances filtered by their Document ID.

    :param document_id: ID of a Document instance.
    :type document_id: int

    """
    _delete_document_relation(document_id, DocumentDRS)


def delete_document(document_id):
    """Deletes a document.

    :param document_id: ID of a Document instance.
    :type document_id: int

    """
    delete_document_drs(document_id)
    delete_document_external_ids(document_id)
    delete_document_representations(document_id)
    delete_document_summaries(document_id)
    delete_by_id(Document, document_id)


def delete_all_documents():
    """Deletes all documents.

    """
    delete_by_type(Document, delete_document)


def get_project_document_type_counts():
    """Returns document type counts grouped by project.

    :returns: List of counts over a project's document types.
    :rtype: list

    """
    q = session.query(sa.func.count(Document.Type),
                      Document.Project_ID,
                      Document.Type)

    q = q.group_by(Document.Project_ID)
    q = q.group_by(Document.Type)

    return q.all()


def get_document_counts():
    """Returns document counts.

    :returns: List of counts over document types.
    :rtype: list

    """
    q = session.query(sa.func.count(Document.Institute_ID),
                      Project.Name,
                      Institute.Name,
                      Document.Type)
    q = q.join(Project)
    q = q.join(Institute)

    q = q.group_by(Project.ID)
    q = q.group_by(Institute.ID)
    q = q.group_by(Document.Type)

    q = q.order_by(Document.Type.desc())

    return q.all()


def get_document_type_count(project_id, type):
    """Returns count over a project's document type.

    :param type: Document type.
    :type type: str

    :param project_id: ID of a Project instance.
    :type project_id: int

    :returns: List of counts over a project's document types.
    :rtype: list

    """
    q = session.query(sa.func.count(Document.Type))

    q = q.filter(Document.Project_ID==project_id)
    q = q.filter(sa.func.upper(Document.Type)==type.upper())
    q = q.group_by(Document.Type)

    counts = q.all()

    return 0 if not len(counts) else counts[0][0]


def get_doc_descriptions(project_id, language_id, type):
    """Returns document descriptions.

    :param project_id: ID of a Project instance.
    :type project_id: int

    :param language_id: ID of a DocumentLanguage instance.
    :type language_id: int

    :param type: Type of Document instance.
    :type type: str

    :returns: Dictionary of project document desciptions.
    :rtype: dict

    """
    q = session.query(Document.Name, DocumentSummary.Description)
    q = q.join(DocumentSummary)

    q = q.filter(Document.IsLatest==True)
    q = q.filter(Document.Project_ID==project_id)
    q = q.filter(Document.Type==type)
    q = q.filter(DocumentSummary.Language_ID==language_id)

    return q.all()


def _get_summary_fieldset(field):
    """Returns set of unique document summary field values."""
    q = session.query(Document.Project_ID, field)
    q = q.join(DocumentSummary)
    q = q.filter(field!='None')
    q = q.distinct()

    return q.all()


def get_summary_model_set():
    """Returns set of unique document summary model names."""
    return _get_summary_fieldset(DocumentSummary.Model)


def get_summary_eperiment_set():
    """Returns set of unique document summary experiment names."""
    return _get_summary_fieldset(DocumentSummary.Experiment)
