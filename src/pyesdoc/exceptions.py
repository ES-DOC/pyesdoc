
class ObsoleteDocumentException(Exception):
	"""Raised when an obsolete documents is being processed."""
	def __init__(self, message):
		Exception.__init__(self, "WARNING :: obsolete document 123 :: {0}".format(message))


class DocumentDecodingException(Exception):
	"""Raised when document decoding fails."""
	def __init__(self):
		Exception.__init__(self, "Document decoding failed.")
