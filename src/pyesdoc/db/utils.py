"""
.. module:: db.utils.py
   :copyright: Copyright "Jul 2, 2013", Earth System models.Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Database utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import json
import os

import sqlalchemy
from . import (
    cache,
    dao,
    models,
    session
    )
from ..utils import runtime as rt
from .. import (
    constants, 
    serialization
    )



# Default drs split.
_DRS_SPLIT = '/'


def create(mtype):
    """Creates a type instance and appends to current session.

    :param type: A domain model type.
    :type type: class

    :returns: An instance of passed domain model type.
    :rtype: A sub-class of db.models.Entity

    """
    rt.assert_iter_item(models.SUPPORTED_TYPES, mtype, "Unknown model type.")

    instance = mtype()
    session.insert(instance, auto_commit=False)

    return instance


def create_doc_from_json(doc_json):
    """Creates a document instance from a json blob.

    :param doc_json: A json blob.
    :type doc_json: unicode

    :returns: A document.
    :rtype: db.models.Document

    """
    # Decode document from json.
    doc = serialization.decode(doc_json, constants.ESDOC_ENCODING_JSON)
    if doc is None:
        rt.raise_error("Document could not be deserialized")

    # Derive project.
    project = cache.get_project(doc.meta.project)
    if project is None:
        rt.raise_error("Project {0} is unsupported".format(doc.meta.project))

    # Verify document does not already exist.
    if dao.get_document(project.ID, doc.meta.id, doc.meta.version) is not None:
        rt.raise_error("Document already exists")

    # Derive institute.
    institute = cache.get_institute(doc.meta.institute)

    # Derive language.
    language = cache.get_doc_language(doc.meta.language)
    if language is None:
        rt.raise_error("Language {0} is unsupported".format(doc.meta.language))

    # Derive encoding.
    encoding = cache.get_doc_encoding(constants.ESDOC_ENCODING_JSON)

    # Derive ontology.
    ontology = get_doc_ontology(doc)
    if ontology is None:
        rt.raise_error("Ontology {0} is unsupported".format(doc.__class__.type_key))

    # Create document repository.
    document = create_doc(doc, project, None, institute)

    # Create document summary.
    create_doc_summary(document, language)

    # Create document external ID (i.e. simulation id).
    create_doc_external_ids(document)

    # Persist.
    session.commit()

    # Log.
    rt.log("CREATED DOC :: T={0} ID={1} UID={2} V={3}.".format(
        document.Type, document.ID, document.UID, document.Version))

    return {
        id : document.ID
    }


def update_doc_from_json(doc_json):
    """Updates a document instance from a json blob.

    :param doc_json: A json blob.
    :type doc_json: unicode

    :returns: A document.
    :rtype: db.models.Document

    """
    # Decode document from json.
    doc = serialization.decode(doc_json, constants.ESDOC_ENCODING_JSON)
    if doc is None:
        rt.raise_error("Document could not be deserialized")

    # Derive project.
    project = cache.get_project(doc.meta.project)
    if project is None:
        rt.raise_error("Project {0} is unsupported".format(doc.meta.project))

    # Derive institute.
    institute = cache.get_institute(doc.meta.institute)

    # Derive language.
    language = cache.get_doc_language(doc.meta.language)
    if language is None:
        rt.raise_error("Language {0} is unsupported".format(doc.meta.language))

    # Derive encoding.
    encoding = cache.get_doc_encoding(constants.ESDOC_ENCODING_JSON)

    # Derive ontology.
    ontology = get_doc_ontology(doc)
    if ontology is None:
        rt.raise_error("Ontology {0} is unsupported".format(doc.__class__.type_key))

    # Create document repository.
    document = create_doc(doc, project, None, institute)

    # Create document summary.
    create_doc_summary(document, language)

    # Create document external ID (i.e. simulation id).
    create_doc_external_ids(document)

    # Persist.
    session.commit()

    # Log.
    rt.log("CREATED DOC :: T={0} ID={1} UID={2} V={3}.".format(
        document.Type, document.ID, document.UID, document.Version))

    return {
        id : document.ID
    }


def create_doc(doc, project, institute=None):
    """Creates & returns a models.Document instance.

    :param doc: Document object representation.
    :type doc: object

    :param project: Project with which document is associated.
    :type project: db.models.Project

    :param institute: Institute with which document is associated.
    :type institute: db.models.Institute

    :returns: A document.
    :rtype: db.models.Document

    """
    # Defensive programming.
    rt.assert_doc('doc', doc)
    rt.assert_var('project', project, models.Project)
    rt.assert_optional_var('institute', institute, models.Institute)

    # Instantiate & assign attributes.
    instance = dao.get_document(project.ID,
                                str(doc.meta.id),
                                str(doc.meta.version))
    if instance is None:
        instance = create(models.Document)
        instance.as_obj = doc
        if institute is not None:
            instance.Institute_ID = institute.ID
        instance.Name = get_doc_name(doc)
        instance.Project_ID = project.ID
        instance.Type = doc.type_key
        instance.UID = str(doc.meta.id)
        instance.Version = int(doc.meta.version)
        set_doc_is_latest_flag(instance)

    return instance


def set_doc_is_latest_flag(document):
    """Sets flag indicating whether a document is the latest version or not.

    :param document: models.Document whose is_latest flag is being assigned.
    :type document: db.models.Document

    """
    # Defensive programming.
    rt.assert_var('document', document, models.Document)

    # Get all related documents and update IsLatest flag accordingly.
    all = dao.get_document(document.Project_ID, document.UID, models.DOCUMENT_VERSION_ALL)
    for i in range(len(all)):
        all[i].IsLatest = (i == 0)
        if all[i].Version == document.Version:
            document.IsLatest == all[i].IsLatest


def create_doc_drs(document, keys):
    """Factory method to create and return a models.DocumentDRS instance.

    :param document: A deserialized models.Document instance.
    :type document: db.models.Document

    :param keys: Set of DRS keys.
    :type keys: list

    :returns: A models.DocumentDRS instance.
    :rtype: db.models.DocumentDRS

    """
    # Defensive programming.
    rt.assert_var('document', document, models.Document)
    rt.assert_typed_iter(keys, str)

    # Reformat path.
    path = _DRS_SPLIT.join(keys).upper()

    # Create (only if necessary).
    instance = dao.get_document_drs(document.Project_ID, document.ID, path)
    if instance is None:
        instance = create(models.DocumentDRS)
        instance.Document_ID = document.ID
        instance.Path = path
        instance.Project_ID = document.Project_ID
        for i in range(len(keys)):
            if i > 7:
                break
            elif keys[i] is not None:
                setattr(instance, "Key_0" + str(i + 1), keys[i].upper())

    return instance


def create_doc_external_ids(document, first_only=False):
    """Factory method to create and return a list of models.DocumentExternalID instances.

    :param document: A deserialized models.Document instance.
    :type document: db.models.Document

    :param first_only: Flag indicating whether only the first external id will be returned.
    :type first_only: bool

    :returns: A models.DocumentExternalID instance.
    :rtype: db.models.DocumentExternalID

    """
    # Defensive programming.
    rt.assert_var('document', document, models.Document)
    rt.assert_var('first_only', first_only, bool)
    rt.assert_doc('document.as_obj', document.as_obj)

    for id in document.as_obj.meta.external_ids:
        instance = dao.get_document_external_id(document.Project_ID,
                                                document.ID,
                                                id.value.upper())
        if instance is None:
            instance = create(models.DocumentExternalID)
            instance.Project_ID = document.Project_ID
            instance.Document_ID = document.ID
            instance.ExternalID = id.value.upper()
        if first_only:
            break

    return dao.get_document_external_ids(document.ID, document.Project_ID)


def create_doc_summary(document, language):
    """Factory method to create and return a models.DocumentSummary instance.

    :param document: A deserialized models.Document instance.
    :type document: db.models.Document

    :param language: A models.DocumentLanguage instance.
    :type language: db.models.DocumentLanguage

    :returns: A models.DocumentSummary instance.
    :rtype: db.models.DocumentSummary

    """
    # Defensive programming.
    rt.assert_var('document', document, models.Document)
    rt.assert_var('language', language, models.DocumentLanguage)

    # Create.
    instance = dao.get_document_summary(document.ID, language.ID)
    if instance is None:
        instance = create(models.DocumentSummary)
        instance.Document_ID = document.ID
        instance.Language_ID = language.ID

    # Set attributes derived from document.
    set_doc_summary(document.as_obj, instance)

    # Rebuild collection.
    document.Summaries = [s for s in document.Summaries if s.ID != instance.ID]
    document.Summaries.append(instance)

    return instance


def delete_doc(uid, version):
    """Deletes a document.

    :param uid: Document unique identifier.
    :type uid: str

    :param version: Document version.
    :type version: str

    """
    docs = dao.get_document(None, uid, version)
    if docs is None:
        return

    if not rt.is_iterable(docs):
        docs = [docs]

    for doc in docs:
        dao.delete_document(doc.ID)

    # Persist.
    session.commit()


def _get_doc_meta_info(doc, getters):
    # Defensive programming.
    rt.assert_doc('doc', doc)

    # Assign getter.
    getter = None if doc.type_key not in getters else getters[doc.type_key]

    return None if getter is None else getter(doc)


def get_doc_ontology(doc):
    """Returns document ontology.

    :param doc: Document object representation.
    :type doc: object

    :returns: Document ontology.
    :rtype: models.DocumentOntology

    """
    # Defensive programming.
    rt.assert_doc('doc', doc)

    # Unpack type key.
    ontology, version, package, doc_type = \
        doc.__class__.type_key.split(".")

    return cache.get_doc_ontology(ontology, version)


def set_doc_summary(doc, summary):
    """Sets document summary fields.

    :param doc: Document object representation.
    :type doc: object

    :param summary: Summary whose fields are being assigned.
    :type summary: db.models.DocumentSummary

    """
    # Defensive programming.
    rt.assert_doc('doc', doc)
    rt.assert_var('summary', summary, models.DocumentSummary)

    summary.Description = get_doc_description(doc)
    for i, field in enumerate(get_doc_summary_fields(doc)):
        if i == 0:
            summary.ShortName = str(field)
        elif i == 1:
            summary.LongName = str(field)
        else:
            setattr(summary, 'Field_0' + str(i - 1), str(field))
def write_doc_stats():
    """Writes document stats to file system.

    """
    def map_row(row):
        return {
            "project": row[1],
            "institute": row[2],
            "doc_type": row[3],
            "doc_count": row[0]
        }

    def write_json(counts):
        path = os.path.dirname(os.path.abspath(__file__))
        path = path.replace("lib/repo", "static/json")
        path += "/doc_stats.json"

        with open(path, 'w') as f:
            json.dump(map(map_row, counts), f, encoding="ISO-8859-1")


    def write_jsonp(counts):
        path = os.path.dirname(os.path.abspath(__file__))
        path = path.replace("lib/repo", "static/json")
        path += "/doc_stats.jsonp"

        with open(path, 'w') as f:
            f.write('onESDOC_JSONPLoad(')
            json.dump(map(map_row, counts), f, encoding="ISO-8859-1")
            f.write(');')


    def write_csv(counts):
        path = os.path.dirname(os.path.abspath(__file__))
        path = path.replace("lib/repo", "static/csv")
        path += "/doc_stats.csv"

        with open(path, 'w') as f:
            f.write("Project, Institute, Document Type, Document Count\n")
            for doc_count, project, institute, doc_type in counts:
                f.write("{0}, {1}, {2}, {3}\n".format(project, institute, doc_type, doc_count))

    # Get counts.
    counts = dao.get_document_counts()

    # Write files.
    for f in [write_csv, write_json, write_jsonp]:
        f(counts)


def create_node(type_of,
                field,
                project_id=1,
                sort_text=None):
    """Creates a facet node (if necessary).

    :param str project_id: Project with which facet node is associated.
    :param str type_of: Facet node type.
    :param str field: Facet node field.
    :param bool create: Flag indicating whether to create node if not in db.
    :param str sort_text: Text used in sort scenarios.

    :returns: A facet node.
    :rtype: models.Node

    """
    def get_field_id(fld):
        """Parses a field representation and returns the field id."""
        if isinstance(fld, models.Node):
            return u'n' + unicode(fld.ID)
        elif isinstance(fld, models.NodeField):
            return unicode(fld.ID)
        else:
            return unicode(fld)

    # Parse field.
    if isinstance(field, (models.Node, models.NodeField)):
        field = get_field_id(field)
    elif isinstance(field, (str, unicode)):
        field = get_field_id(create_node_field(field))
    elif isinstance(field, tuple):
        field = u",".join([get_field_id(f) for f in field])
    else:
        raise ValueError("Node field cannot be parsed:: {0} :: {1}".format(type(field), field))

    # Create node.
    node = models.Node()
    node.project_id = project_id
    node.type_of = type_of
    node.field = field

    # Insert.
    try:
        session.insert(node)
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
        node = dao.get_node(project_id, type_of, field)
    else:
        rt.log("INDEXING :: CORE :: created node {0}".format(node))

    # Set sort value (if necessary).
    if sort_text is not None:
        field = unicode(create_node_field(sort_text).ID)
        if node.sort_field != field:
            node.sort_field = field
            session.commit()

    return node


def create_node_fields(text):
    if not isinstance(text, list):
        text = [text]

    return [create_node_field(t) for t in text]


def create_node_field(text):
    # Create.
    field = models.NodeField()
    field.text = text

    # Insert.
    try:
        session.insert(field)
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
        field = dao.get_node_field(text)
    else:
        rt.log("INDEXING :: CORE :: created field {0}".format(field))

    return field


def create_node_value(text):
    """Creates a node value (if necessary).

    :param str text: Facet text.

    :returns: A facet node value.
    :rtype: models.NodeValue

    """
    # Create.
    value = models.NodeValue()
    value.text = text

    # Insert.
    try:
        session.insert(value)
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
        value = dao.get_node_value(text)
    else:
        rt.log("INDEXING :: CORE :: created value {0}".format(value))

    return value


def create_node_combination(type_of, nodeset, project_id=1):
    """Creates a node combination (if necessary).

    :param str type_of: Facet combination type.
    :param str nodeset: Set of nodes acting as a vector.
    :param str project_id: Project with which a facet combination is associated.

    :returns: A facet node combination.
    :rtype: models.NodeCombination

    """
    # Set vector.
    vector = u""
    for index, node in enumerate(nodeset):
        if index > 0:
            vector += u"-"
        vector += unicode(node.ID)

    # Create.
    combo = models.NodeCombination()
    combo.combination = vector
    combo.project_id = project_id
    combo.type_of = type_of

    # Insert.
    try:
        session.insert(combo)
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
        combo = dao.get_node_combination(project_id, type_of, vector)
    else:
        rt.log("INDEXING :: CORE :: created combination {0}".format(combo))

    return combo


def get_node_value_set(project_id):
    """Returns set of facet node values filtered by project.

    :param int project_id: Project with which facet node values are associated.

    :returns: Set of facet node values.
    :rtype: list

    """
    def reduce_value(values, value):
        """The value reducer."""
        return values + [value.ID, value.text]

    return reduce(reduce_value, dao.get_node_value_set(project_id), [])


def get_node_set(project_id):
    """Returns set of facet nodes filtered by project.

    :param int project_id: Project with which facet nodes are associated.

    :returns: Set of facet nodes.
    :rtype: list

    """
    def reduce_node(nodes, node):
        """The node reducer."""
        return nodes + [
            node.ID,
            models.NODE_TYPES.index(node.type_of),
            node.field
            ]

    return reduce(reduce_node, dao.get_node_set(project_id), [])


def get_node_field_set(project_id):
    """Returns set of facet fields filtered by project.

    :param int project_id: Project with which facet nodes are associated.

    :returns: Set of facet fields.
    :rtype: list

    """
    def reduce_field(fields, field):
        """The node reducer."""
        return fields + [
            field.ID,
            field.text
            ]

    return reduce(reduce_field, dao.get_node_field_set(project_id), [])


