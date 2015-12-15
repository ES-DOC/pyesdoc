# -*- coding: utf-8 -*-

"""
.. module:: test_type_cim_v1_software_statistical_model_component.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Tests a cim.v1.StatisticalModelComponent instance.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
import arrow

import pyesdoc.ontologies.cim as cim
import test_utils as tu



# Test type.
DOC_TYPE = cim.v1.StatisticalModelComponent

# Test type display name.
DOC_TYPE_DISPLAY_NAME = "Model"

# Test document type.
DOC_TYPE_KEY = DOC_TYPE.type_key

# Test representation file.
DOC_FILE = 'cim.1.software.StatisticalModelComponent.xml-metafor-cim-v1'

# Test document uid.
DOC_UID = '4b29d25e-2968-11e0-8517-00163e9152a5'

# Test document version.
DOC_VERSION = '9'

# Test document creation date.
DOC_DATE = arrow.get('2013-03-22 17:54:48.178304').datetime

# Test document project.
DOC_PROJECT = "CMIP5"

# Test document project.
DOC_INSTITUTE = "MOHC"

# Test document author.
DOC_AUTHOR = "Metafor Questionnaire"


def assert_doc(doc, meta, ext):
    """Asserts a document.

    :param object doc: Document being tested.
    :param object meta: Document meta information.
    :param object ext: Document extension information.

    """
    return
        
    assert doc.meta.author.individual_name == 'Metafor Questionnaire'
    assert doc.meta.author.role == 'documentAuthor'
    assert len(doc.meta.genealogy.relationships) == 1
    r = doc.meta.genealogy.relationships[0]
    assert r.direction == 'toTarget'
    assert r.target.reference.name == 'IPSLCM4_v2'
    assert r.type == 'previousVersionOf'

    assert len(doc.types ) == 1
    assert len(doc.sub_components) == 0
    assert len(doc.citations) == 1
    assert len(doc.dependencies) == 0
    assert len(doc.deployments) == 0
    assert len(doc.funding_sources) == 0
    assert len(doc.properties) == 1
    assert len(doc.responsible_parties) == 4

    assert doc.composition is None
    assert doc.coupling_framework is ''
    assert doc.description.startswith('IPSL-CM5A-LR is the low resolution')
    assert doc.is_embedded == False
    assert doc.grid is None
    assert doc.language is None
    assert doc.license is None
    assert doc.long_name == "IPSL-CM5A-LR;atmosphere:LMDZ5A(95x96L39);ocean:NEMOv3.2 (OPA-LIM-PISCES,149x182L31)"
    assert doc.previous_version == unicode()
    assert doc.release_date == arrow.get('2010', 'YYYY').datetime
    assert doc.short_name == 'IPSL-CM5A-LR'
    assert doc.types[0] == 'downscaling'

    p = doc.properties[0]
    assert len(p.sub_properties) == 4
    assert p.intent == None
    assert p.is_represented == True
    assert p.long_name == None
    assert p.short_name == 'Sea Ice Key Properties'
    assert len(p.values) == 0

    p = p.sub_properties[0]
    assert len(p.sub_properties) == 0
    assert p.intent == None
    assert p.is_represented == True
    assert p.long_name == 'BasicApproximations'
    assert p.short_name == 'BasicApproximations'
    assert len(p.values) == 1
    assert p.values[0] == '2-level + visco-plastic rheology'


def update_doc(doc):
    """Update a document prior to republishing.

    :param object doc: Document being republished.

    """
    pass


def assert_doc_updates(doc):
    """Asserts a document after being updated.

    :param object doc: Document being tested.

    """
    pass