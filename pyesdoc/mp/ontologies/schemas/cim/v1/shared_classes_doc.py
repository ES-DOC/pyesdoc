"""
.. module:: shared_classes_doc.py
   :synopsis: Set of CIM v1 ontology type definitions.

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
            ('author', 'shared.responsible_party', '0.1',
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
        ],
        'decodings': [
            ('author', 'child::cim:documentAuthor'),
            ('create_date', 'child::cim:documentCreationDate'),
            ('external_ids', 'child::cim:externalID'),
            ('genealogy', 'child::cim:documentGenealogy'),
            ('id', 'child::cim:documentID'),
            ('update_date', 'child::cim:documentCreationDate'),
            ('version', 'child::cim:documentVersion'),
            ('version', 'self::cim:numericalExperiment/@documentVersion')
        ]
    }


def doc_reference():
    """A reference to another cim entity.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('changes', 'shared.change', '0.N',
                "An optional description of how the item being referenced has been modified.  This is particularly useful for dealing with Ensembles (a set of simulations where something about each simulation has changed) or Conformances."),
            ('canonical_name', 'str', '0.1',
                "Canonical name given to document."),
            ('constraint_vocabulary', 'str', '0.1',
                "A constraint vocabulary for the relationship."),
            ('context', 'str', '0.1',
                "Information about remote record in context of reference."),
            ('description', 'str', '0.1',
                "Detail of how to access the resource."),
            ('external_id', 'str', '0.1',
                "External identifier of remote resource, if known."),
            ('id', 'str', '0.1',
                "Identifier of remote resource, if known."),
            ('institute', 'str', '0.1',
                "Canonical institute name of referenced document."),
            ('linkage', 'str', '1.1',
                "A URL."),
            ('name', 'str', '1.1',
                "A user friendly name given to document."),
            ('protocol', 'str', '0.1',
                "Protocol to use at the linkage."),
            ('relationship', 'str', '0.1',
                "Predicate - relationship of the object target as seen from the subject resource."),
            ('type', 'str', '1.1',
                "The type of remote document."),
            ('url', 'str', '0.1',
                "The URL of the remote document."),
            ('version', 'int', '0.1',
                "The version of the remote document.")
        ],
        'decodings': [
            ('changes', 'child::cim:change'),
            ('description', 'child::cim:description'),
            ('external_id', 'child::cim:externalID'),
            ('id', 'child::cim:id'),
            ('name', 'child::cim:name'),
            ('type', 'child::cim:type'),
            ('version', 'child::cim:version'),
        ]
    }
