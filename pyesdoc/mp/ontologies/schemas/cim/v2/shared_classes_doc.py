"""
.. module:: shared_classes_doc.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""

def doc_meta_info():
    """Encapsulates document meta information used by es-doc machinery. Will not normally be
    populated by humans. May duplicate information held in 'visible' metadata.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('author', 'shared.party', '0.1',
                "Author of the metadata in the parent document."),
            ('create_date', 'datetime', '1.1',
                "Date upon which the instance was created."),
            ('drs_keys', 'str', '0.N',
                "DRS related keys to support correlation of documents with datasets."),
            ('drs_path', 'str', '0.1',
                "DRS related path to support documents with datasets."),
            ('external_ids', 'str', '0.N',
                "Set of identifiers used to reference the document by external parties."),
            ('id', 'str', '1.1',
                "Universal document identifier (must be a valid UUID)."),
            ('institute', 'str', '0.1',
                "Name of institute with which instance is associated."),
            ('project', 'str', '0.1',
                "Name of project with which instance is associated."),
            ('sort_key', 'str', '0.1',
                "Document sort key."),
            ('source', 'str', '1.1',
                "Name of application that created the instance."),
            ('source_key', 'str', '0.1',
                "Key of application that created the instance."),
            ('sub_projects', 'str', '0.N',
                "Set of sub-projects with which instance is associated."),
            ('type', 'str', '1.1',
                "Document ontology type key."),
            ('type_display_name', 'str', '0.1',
                "Document type display name."),
            ('type_sort_key', 'str', '0.1',
                "Document type sort key."),
            ('update_date', 'datetime', '0.1',
                "Date upon which the instance was last updated."),
            ('version', 'int', '1.1',
                "Document version identifier.")
        ]
    }


def doc_reference():
    """A reference to another cim entity.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{}', ('canonical_name',)),
        'properties': [
            ('canonical_name', 'str', '0.1',
                "Canonical name given to document."),
            ('id', 'str', '0.1',
                "Identifier of remote resource, if known."),
            ('name', 'str', '0.1',
                "A user friendly name given to document."),
            ('type', 'str', '0.1',
                "The type of remote document."),
            ('version', 'int', '0.1',
                "The version of the remote document."),

            ('relationship', 'str', '0.1',
                "Relationship of the object target as seen from the subject resource."),
            ('further_info', 'str', '0.1',
                "A further piece of information used in ad-hoc contexts."),

            # TODO verify whether really needed
            ('context', 'str', '0.1',
                "Information about remote record in context of reference."),
            ('constraint_vocabulary', 'str', '0.1',
                "A constraint vocabulary for the relationship."),
            ('description', 'str', '0.1',
                "Detail of how to access the resource."),
            ('external_id', 'str', '0.1',
                "External identifier of remote resource, if known."),
            ('institute', 'str', '0.1',
                "Canonical institute name of referenced document."),
            ('linkage', 'str', '0.1',
                "A URL."),
            ('protocol', 'str', '0.1',
                "Protocol to use at the linkage."),
            ('url', 'str', '0.1',
                "The URL of the remote document.")
        ]
    }
