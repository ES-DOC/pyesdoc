# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.json.encoder.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encodes a term to JSON.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.cv.codecs.dictionary import encoder as dict_encoder
from pyesdoc.cv.utils import convert



def encode(term):
    """Converts input dictionary to json.

    :param pyesdoc.cv.Term term: Term to be written to file system.

    :returns: JSON encoded string.
    :rtype: str

    """
    # Convert to dictionary.
    as_dict = dict_encoder.encode(term)

    # Return JSON.
    return convert.dict_to_json(as_dict)
