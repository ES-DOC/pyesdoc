"""
.. module:: cim.v1.types.quality.evaluation.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.245195.

"""

# Module imports.
import datetime
import types
import uuid



class Evaluation(object):
    """A concrete class within the cim v1 type system.

    
    """

    def __init__(self):
        """Constructor"""
        super(Evaluation, self).__init__()
        self.date = datetime.datetime.now()          # type = datetime.datetime
        self.description = str()                     # type = str
        self.did_pass = bool()                       # type = bool
        self.explanation = str()                     # type = str
        self.specification = str()                   # type = str
        self.specification_hyperlink = str()         # type = str
        self.title = str()                           # type = str
        self.type = str()                            # type = str
        self.type_hyperlink = str()                  # type = str


    def as_dict(self):
        """Returns a deep dictionary representation.

        """
        def append(d, key, value, is_iterative, is_primitive, is_enum):
            if value is None:
                if is_iterative:
                    value = []
            elif is_primitive == False and is_enum == False:
                if is_iterative:
                    value = map(lambda i : i.as_dict(), value)
                else:
                    value = value.as_dict()
            d[key] = value

        # Populate a deep dictionary.
        d = dict()
        append(d, 'date', self.date, False, True, False)
        append(d, 'description', self.description, False, True, False)
        append(d, 'did_pass', self.did_pass, False, True, False)
        append(d, 'explanation', self.explanation, False, True, False)
        append(d, 'specification', self.specification, False, True, False)
        append(d, 'specification_hyperlink', self.specification_hyperlink, False, True, False)
        append(d, 'title', self.title, False, True, False)
        append(d, 'type', self.type, False, True, False)
        append(d, 'type_hyperlink', self.type_hyperlink, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

