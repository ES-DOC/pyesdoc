# -*- coding: utf-8 -*-

"""
.. module:: exceptions.py
   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package exceptions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
class ObsoleteDocumentException(Exception):
	"""Raised when an obsolete documents is being processed."""
	def __init__(self, message):
		Exception.__init__(self, "WARNING :: obsolete document :: {0}".format(message))


class DocumentDecodingException(Exception):
	"""Raised when document decoding fails."""
	def __init__(self):
		Exception.__init__(self, "Document decoding failed.")
