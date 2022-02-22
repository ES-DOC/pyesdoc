# -*- coding: utf-8 -*-

"""
.. module:: shared_classes.py
   :synopsis: Set of CIM v2 ontology type definitions
   which are used to describe attributes of many of
   the other classes.

"""


def text_blob():
    """Provides a text class which supports plaintext, html, and friends
    (or will do)."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{}", ("content",)),
        "properties": [
            ("content", "str", "1.1", "Raw content (including markup)."),
            (
                "encoding",
                "shared.text_blob_encoding",
                "1.1",
                "Content encoding.",
            ),
        ],
    }


def citation():
    """An academic reference to published work."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": True,
        "pstr": ("{}", ("title",)),
        "properties": [
            (
                "abstract",
                "str",
                "0.1",
                "Abstract providing high level reference overview.",
            ),
            ("authors", "str", "0.N", "The Authors of the work."),
            ("bibtex", "str", "0.1", "A BibTeX reference for the work."),
            (
                "citation_detail",
                "str",
                "0.1",
                "A complete citation string as would appear in a "
                "bibliography.",
            ),
            (
                "collective_title",
                "str",
                "0.1",
                "Citation collective title, i.e. with all authors declared.",
            ),
            (
                "context",
                "str",
                "0.1",
                "Brief text description of why this resource is being cited.",
            ),
            ("doi", "str", "0.1", "Digital Object Identifier, if it exists."),
            ("title", "str", "0.1", "The title of the work."),
            ("type", "str", "0.1", "Citation type."),
            ("year", "int", "0.1", "Year of publication."),
            (
                "url",
                "shared.online_resource",
                "0.1",
                "Location of electronic version.",
            ),
        ],
    }


def extra_attribute():
    """An extra attribute with key and value needed to encode further
    information not in the CIM domain model or specialisation.

    Typical use case: in parsing data and encoding attributes found in
    data.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{}:{}", ("key", "value")),
        "properties": [
            ("doc", "str", "0.1", "Documentation associated with this key."),
            ("key", "str", "1.1", "Name of attribute."),
            ("type", "str", "0.1", "If a non-string type, provide type."),
            ("value", "str", "1.1", "Value associated with key."),
        ],
    }


def nil_reason():
    """Provides an enumeration of possible reasons why a property has
    not been defined Based on GML nilReason as discussed here:
    https://www.seegrid.csiro.au/wiki/AppSchemas/NilValues."""
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("nil:inapplicable", "There is no value"),
            (
                "nil:missing",
                "The correct value is not available. Furthermore, a correct "
                "value may not exist",
            ),
            ("nil:template", "The value will be available later"),
            (
                "nil:unknown",
                "The correct value is not known at this time. However, a "
                "correct value probably exists",
            ),
            ("nil:withheld", "The value is not divulged"),
        ],
    }


def online_resource():
    """A minimal approximation of ISO19115 CI_ONLINERESOURCE, provides a
    link and details of how to use that link."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{}", ("linkage",)),
        "properties": [
            (
                "description",
                "str",
                "0.1",
                "Detail of how to access the resource.",
            ),
            ("linkage", "str", "1.1", "A URL."),
            ("name", "str", "1.1", "Name of online resource."),
            ("protocol", "str", "0.1", "Protocol to use at the linkage."),
        ],
    }


def party():
    """Implements minimal material for an ISO19115-1 (2014) compliant
    party.

    For our purposes this is a much better animal than the previous
    responsibleParty which munged roles together with people. Note we
    have collapsed CI_Contact, CI_Individual and CI_Organisation as well
    as the abstract CI_Party.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{}", ("name",)),
        "is_document": True,
        "properties": [
            ("address", "str", "0.1", "Institutional address."),
            ("email", "str", "0.1", "Email address."),
            ("name", "str", "0.1", "Name of person or organisation."),
            ("orcid_id", "str", "0.1", "Orcid ID if available."),
            (
                "is_organisation",
                "bool",
                "0.1",
                "True if an organisation not a person.",
            ),
            (
                "url",
                "shared.online_resource",
                "0.1",
                "URL of person or institution.",
            ),
        ],
    }


def quality_review():
    """Assertions as to the completeness and quality of a document.

    Not to be confused with assertions as to the quality of the resource
    described by the document (as covered by the iso.quality_report). A
    future version of this ontology may rename this class.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": True,
        "pstr": (
            "{}: {}",
            (
                "target_document",
                "quality_status",
            ),
        ),
        "properties": [
            ("date", "str", "1.1", "Date upon which review was made."),
            (
                "metadata_reviewer",
                "linked_to(shared.party)",
                "1.1",
                "Party who made the metadata quality assessment.",
            ),
            (
                "quality_description",
                "str",
                "1.1",
                "Assessment of quality of target document.",
            ),
            (
                "quality_status",
                "shared.quality_status",
                "0.1",
                "Status from a controlled vocabulary.",
            ),
            (
                "target_document",
                "shared.doc_reference",
                "1.1",
                "This is the document about which quality is asserted.",
            ),
        ],
    }


def quality_status():
    """Assertion as to the review status of document."""
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            ("incomplete", "Currently being worked on"),
            ("finalised", "Author has completed document, prior to review"),
            ("under_review", "Document is being reviewed"),
            (
                "reviewed",
                "Document has been formally reviewed and assessed as "
                "complete and accurate",
            ),
        ],
    }


def responsibility():
    """Implements the ISO19115-1 (2014) CI_Responsibility (which
    replaces responsibleParty).

    Combines a person and their role in doing something.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "pstr": ("{}:{}", ("role", "parties")),
        "properties": [
            (
                "parties",
                "linked_to(shared.party)",
                "1.N",
                "Parties delivering responsibility.",
            ),
            (
                "role",
                "shared.role_code",
                "1.1",
                "Role that the party plays or played.",
            ),
            (
                "when",
                "time.time_period",
                "0.1",
                "Period when role was active, if no longer.",
            ),
        ],
    }


def role_code():
    """Responsibility role codes: roles that a party may play in
    delivering a responsibility.

    This is an extension and modification of CI_RoleCode from ISO19115.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [
            (
                "Principal Investigator",
                "Key party responsible for the existence of the resource",
            ),
            (
                "originator",
                "Original source for the resource if obtained from elsewhere",
            ),
            ("author", "Party who created (or co-created) resource"),
            ("collaborator", "Contributor to the production of the resource"),
            ("publisher", "Party who published the resource"),
            ("owner", "Party with legal ownership of the resource"),
            (
                "processor",
                "Party who has taken part in the workflow that resulted in "
                "this resource",
            ),
            ("distributor", "Party who distributes the resource"),
            (
                "sponsor",
                "Party who has invested in the production of the resource",
            ),
            ("user", "Party who uses the resource"),
            (
                "point of contact",
                "Party who can be contacted for acquiring knowledge about or "
                "acquisition of the resource",
            ),
            ("resource provider", "Party that supplies the resource"),
            (
                "custodian",
                "Party that accepts accountability and responsibility for the "
                "source resource",
            ),
            (
                "metadata_reviewer",
                "Party who carried out an independent review of (this) "
                "documentation",
            ),
            ("metadata_author", "Party who created (this) documentation"),
        ],
    }


def text_blob_encoding():
    """Types of text understood by the CIM notebook.

    Currently only plaintext, but we expect safe HTML to be supported as
    soon as practicable.

    """
    return {
        "type": "enum",
        "is_open": False,
        "members": [("ascii", "Normal plain text")],
    }


def numeric():
    """A number which comes with a unit, potentially from a controlled
    vocabulary of units.

    #FIXME: Need to work on the relationship between unit_source and base_unit.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": False,
        "pstr": ("{}{}", ("value", "units")),
        "properties": [
            ("value", "float", "1.1", "Numerical value of number"),
            ("units", "str", "1.1", "Associated Units"),
            ("unit_enumeration", "str", "0.1", "Internal CIM vocabulary"),
            (
                "unit_source",
                "shared.online_resource",
                "0.1",
                "External vocabulary source",
            ),
            ("base_unit", "str", "0.1", "type of unit in external vocabulary"),
        ],
        "constraints": [
            ("mutually_exclusive", ("unit_enumeration", "unit_source"), "0.1"),
        ],
    }
