"""
.. module:: exceptions.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Package exceptions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import inspect



class LibraryBaseException(Exception):
    """Default library exception class.

    """

    def __init__(self, msg):
        """Contructor.

        :param msg: Exception message.
        :type msg: str

        """
        self.message = msg() if inspect.isfunction(msg) else unicode(msg)


    def __str__(self):
        """Returns a string representation.

        """
        return u"ES-DOC PY-CLIENT EXCEPTION : {0}".format(repr(self.message))


class ObsoleteException(LibraryBaseException):
    """Raised when an obsolete documents is being processed.

    """
    def __init__(self, message):
        """Instance constructor.

        """
        super(ObsoleteException, self).__init__("WARNING :: obsolete document :: {0}".format(message))


class DecodingException(LibraryBaseException):
    """Raised when document decoding fails.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DecodingException, self).__init__("Document decoding failed.")


class EncodingException(LibraryBaseException):
    """Raised when document encoding fails.

    """
    def __init__(self, encoding, doc, error):
        """Instance constructor.

        """
        super(EncodingException, self).__init__("Document {} encoding failed :: Doc Type = {} :: Error = {}".format(encoding.upper(), type(doc), error))


class ExtendingException(LibraryBaseException):
    """Exception raised when document extension fails.

    """
    def __init__(self, err, extender=None):
        """Instance constructor.

        """
        if extender is not None:
            err = "Document extension failed: {0} :: {1}".format(extender, err)
        else:
            err = "Document extension failed: {}".format(err)
        super(ExtendingException, self).__init__(err)


class InvalidDocumentTypeException(LibraryBaseException):
    """Exception raised when an invalid document type is declared.

    """
    def __init__(self, doc_type):
        """Instance constructor.

        """
        err = "Document type [{}] is unsupported.".format(doc_type)
        super(InvalidDocumentTypeException, self).__init__(err)


class LoadingException(LibraryBaseException):
    """Exception raised when document loading fails.

    """
    def __init__(self, err):
        """Instance constructor.

        """
        err = "Document loading failed: {}".format(err)
        super(LoadingException, self).__init__(err)


class ParsingException(LibraryBaseException):
    """Exception raised when document parsing fails.

    """
    def __init__(self, err):
        """Instance constructor.

        """
        err = "Document parsing failed: {}".format(err)
        super(ParsingException, self).__init__(err)


class WebServiceException(LibraryBaseException):
    """Exception raised when a web service operation fails.

    """
    def __init__(self, err):
        """Instance constructor.

        """
        err = "Web service invocation failed: {}".format(err)
        super(ParsingException, self).__init__(err)

