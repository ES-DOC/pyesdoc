# -*- coding: utf-8 -*-
"""
.. module:: content_parser_cmip5_metafor_q.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes CMIP5 Metafor Questionnaire content parsers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc import exceptions



# CIM v1.4 schema .
CIM_V1_4 = 'http://www.metaforclimate.eu/cim/1.4"'

# CIM v1 xsd reference.
CIM_V1_XSD = 'http://www.purl.org/org/esmetadata/cim/1.5/schemas/cim.xsd'

# CIM v1 schema reference.
CIM_V1_SCHEMA = 'http://www.purl.org/org/esmetadata/cim/1.5/schemas'


def _reject_obsolete(content):
    """Rejects obsolete documents.

    """
    if content.find(CIM_V1_4) != -1:
        raise exceptions.ObsoleteException("cim schema = 1.4")


def _correct_schema_reference(content):
    """Corrects schema reference.

    """
    return content.replace(CIM_V1_XSD, CIM_V1_SCHEMA)


# Set of content parsers.
PARSERS = (
	_reject_obsolete,
	_correct_schema_reference
	)
