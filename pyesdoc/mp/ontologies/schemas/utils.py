"""
.. module:: pyesdoc.mp.schema.utils
   :platform: Unix, Windows
   :synopsis: Ontology schema utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.mp.ontologies.schemas import cim



def get_schema(name, version):
    """Returns a supported ontology schema module.

    :param str name: Schema name.
    :param str version: Schema version.

    :returns: An ontology schema.
    :rtype: module

    """
    if name == 'cim':
        if version == '1':
            return cim.v1
        if version == '2':
            return cim.v2

    raise KeyError("Ontology schema not found: {} :: v{}".format(name, version))


def parse_type(typeof):
    """Parses a type declaration.

    """
    if typeof.startswith('linked_to'):
        parts = [i.strip() for i in typeof[10:-1].split(",")]
        try:
            return parts[0], parts[1]
        except IndexError:
            return parts[0], None
    else:
        return typeof, None
