# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_sofware_model_component.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.ModelComponent instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test document type.
DOC_TYPE = cim.v1.ModelComponent

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Model"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key

# Test representation file.
DOC_FILE = 'cim.1.software.ModelComponent-1.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = '7a2b64cc-03ca-11e1-a36a-00163e9152a5'

# Test document version.
DOC_VERSION = '1'

# Test document creation date.
DOC_DATE = arrow.get('2012-04-23 14:59:06.258353').datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_meta_info(meta):
    """Asserts a document's meta-information.

    :param object meta: Document meta information.

    """
    tu.assert_iter(meta.genealogy.relationships, 1, cim.v1.DocRelationship)

    r = meta.genealogy.relationships[0]
    tu.assert_str(r.description, "The HadGEM2-A model", True)
    tu.assert_str(r.direction, "toTarget")
    tu.assert_str(r.type, "previousVersionOf")
    tu.assert_str(r.target.reference.name, "HadGEM1")


def assert_extension_info(ext):
    """Asserts a document's extension information.

    :param object ext: Document extension information.

    """
    tu.assert_str(ext.display_name, "HadGEM2-A")
    tu.assert_str(ext.description, "The HadGEM2-A model", True)
    tu.assert_str(ext.full_display_name, "CMIP5 Model : MOHC - HadGEM2-A")
    tu.assert_int(ext.summary_fields, 2)
    tu.assert_str(ext.summary_fields[0], "HadGEM2-A")
    tu.assert_str(ext.summary_fields[1], "Hadley Global Environment Model 2 - Atmosphere")


def _assert_doc_core(doc, is_update):
    """Assert core information."""
    tu.assert_str(doc.description, "The HadGEM2-A model", True)
    if not is_update:
        tu.assert_str(doc.long_name, "Hadley Global Environment Model 2 - Atmosphere")
    tu.assert_date(doc.release_date, "2009")
    tu.assert_str(doc.short_name, "HadGEM2-A")
    tu.assert_str(doc.type, "model")
    tu.assert_int(doc.types, 2)
    tu.assert_str(doc.types[1], "model")


def _assert_doc_citations(doc, is_update):
    """Assert citations."""
    tu.assert_int(doc.citations, 2)

    c = doc.citations[0]
    tu.assert_str(c.collective_title, "Bellouin N., O. Boucher", True)
    tu.assert_str(c.location, "http://www.metoffice.gov.uk/publications/HCTN/HCTN_73.pdf")
    tu.assert_str(c.title, "Bellouin et al. 2007")
    tu.assert_str(c.type, "Online Other")


def _assert_doc_responsible_parties(doc, is_update):
    """Assert responsible parties."""
    tu.assert_int(doc.responsible_parties, 4)

    rp = doc.responsible_parties[0]
    tu.assert_str(rp.abbreviation, "Chris Jones")
    tu.assert_str(rp.address, "Met Office Hadley Centre", True)
    tu.assert_str(rp.email, "chris.jones@metoffice.gov.uk")
    tu.assert_str(rp.individual_name, "Chris Jones")
    tu.assert_str(rp.role, "PI")
    tu.assert_str(rp.url, r"http://www.metoffice.gov.uk/research/our-scientists/climate-chemistry-ecosystems/chris-jones", True)

    rp = doc.responsible_parties[1]
    tu.assert_str(rp.organisation_name, "UK Met Office Hadley Centre")


def _assert_doc_sub_components(doc, is_update):
    """Assert sub-components."""
    tu.assert_int(doc.sub_components, 4)

    sc = doc.sub_components[0]
    tu.assert_int(sc.citations, 1)
    tu.assert_str(sc.description, "The model includes interactive schemes", True)
    tu.assert_uuid(sc.meta.id, "7a44cb24-03ca-11e1-a36a-00163e9152a5")
    tu.assert_int(sc.meta.version, 1)
    tu.assert_date(sc.meta.create_date, "2012-04-23 14:59:04.757315")
    tu.assert_str(sc.long_name, "Aerosols")
    tu.assert_int(sc.properties, 4)
    tu.assert_int(sc.responsible_parties, 4)
    tu.assert_int(sc.sub_components, 3)
    tu.assert_str(sc.short_name, "Aerosols")
    tu.assert_str(sc.type, "Aerosols")
    tu.assert_int(sc.types, 3)

    # Property.
    p = sc.properties[0]
    tu.assert_bool(p.is_represented, True)
    tu.assert_str(p.long_name, "Aerosols")
    tu.assert_str(p.short_name, "Aerosol Key Properties")
    tu.assert_int(p.sub_properties, 6)

    p = sc.properties[2]
    tu.assert_int(p.standard_names, 1)
    tu.assert_str(p.standard_names[0], "tendency_of_atmosphere", True)
    tu.assert_str(p.units, "kg/m2/s")

    # Sub-property.
    p = sc.properties[0].sub_properties[0]
    tu.assert_str(p.short_name, "AerosolSchemeScope")
    tu.assert_str(p.long_name, "AerosolSchemeScope")
    tu.assert_int(p.values, 1)
    tu.assert_str(p.values[0], "Whole atmosphere")



def assert_doc(doc, is_update=False):
    """Asserts a document.

    :param object doc: Document being tested.
    :param bool is_update: Flag indicating whether document has been updated.

    """
    for assertor in (
        _assert_doc_core,
        _assert_doc_citations,
        _assert_doc_responsible_parties,
        _assert_doc_sub_components
        ):
        assertor(doc, is_update)


def update_doc(doc):
    """Update a document prior to republishing.

    :param object doc: Document being republished.

    """
    doc.long_name = "X"


def assert_doc_updates(doc):
    """Asserts a document after being updated.

    :param object doc: Document being tested.

    """
    tu.assert_str(doc.long_name, "X")


def assert_doc_extensions(doc):
    """Asserts a document after being extended.

    :param object doc: Document being tested.

    """
    pass
