# -*- coding: utf-8 -*-

"""
.. module:: test_serialization_non_ascii.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Executes pyesdoc non-ascii document content tests.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import pyesdoc
import pyesdoc.ontologies.cim as cim

import test_utils as tu
import test_types as tt



# Create test model component.
_MODEL = pyesdoc.create(cim.v1.ModelComponent, "cmip5", "mohc")
_MODEL.long_name = "Atmosphere"
_MODEL.short_name = "Atmosphere"
_MODEL.type = "model"


def _get_description(text_type):
    """Returns model description with non-ascii characters."""
    if text_type == str:
        return ("{AS PARENT with differences as indicated}\r\n"
            "The horizontal resolution is 0.44\xc2\xb0 x 0.44\xc2\xb0, which gives "
            "a minimum resolution of ~50 km at the Equator of the rotated "
            "grid. Due to its fine resolution, the model requires a timestep "
            "of 5 minutes to maintain numerical stability."
            )
    elif text_type == unicode:
        return (u"{AS PARENT with differences as indicated}\r\n"
            u"The horizontal resolution is 0.44\xb0 x 0.44\xb0, which gives "
            u"a minimum resolution of ~50 km at the Equator of the rotated "
            u"grid. Due to its fine resolution, the model requires a timestep "
            u"of 5 minutes to maintain numerical stability."
            ).encode('utf-8')


def _do_test(encoding):
    """Executes a serialization test."""
    for desc in (_get_description(t) for t in (str, unicode)):
        _MODEL.description = desc
        representation = pyesdoc.encode(_MODEL, encoding)
        tu.assert_object(representation, str)
        as_doc = pyesdoc.decode(representation, encoding)
        tu.assert_object(as_doc, cim.v1.ModelComponent)


def _test_xml_serialization():
    """Test xml serialization of a document containing non-ascii characters."""
    _do_test(pyesdoc.ENCODING_XML)


def _test_json_serialization():
    """Test json serialization of a document containing non-ascii characters."""
    _do_test(pyesdoc.ENCODING_JSON)


def test():
    """Test serialization of documents containing non-ascii characters."""
    for func in (
        _test_xml_serialization,
        _test_json_serialization,
        ):
        tu.init(func, func.__doc__[5:])
        yield func
