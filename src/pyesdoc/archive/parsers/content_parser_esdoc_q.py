"""
.. module:: content_parser_esdoc_q.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes ES-DOC Questionnaire content parsers.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

def _correct_property_values(content):
    """Removes erroneous property values."""
    return content.replace('(+: (DEFAULT: ), 1)', '1')


# Set of content parsers.
PARSERS = (
	_correct_property_values,
	)
