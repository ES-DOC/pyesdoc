# -*- coding: utf-8 -*-
"""
.. module:: pyesdoc.archive.parsing.__init__.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes a document parser that 'corrects' either content
   or decoded documents prior to further processing.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.archive.parsing import content_parser
from pyesdoc.archive.parsing import doc_parser



# Set of parsers mapped by type.
_PARSERS = {
    'content': content_parser,
    'document': doc_parser
}


def parse(target, encoding, project, source, target_type='document'):
    """Performs a parse over the target.

    :param target: Object to be parsed.
    :param encoding: Original encoding of target.
    :param str project: Name of a supported project (e.g. cmip6).
    :param str source: Name of a document source (e.g. esdoc-q).
    :param target_type: Type of object to be parsed.

    :returns: Parsed target.
    :rtype: object

    """
    if target_type not in _PARSERS:
        raise KeyError("Parsing target type not supported.")

    return _PARSERS[target_type].parse(encoding, project, source, target)
