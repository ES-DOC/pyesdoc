"""
.. module:: cim.v1.types.quality.report.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-06-21 14:34:23.270627.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1.types.quality.evaluation import Evaluation
from pyesdoc.ontologies.cim.v1.types.shared.responsible_party import ResponsibleParty
from pyesdoc.ontologies.cim.v1.types.quality.measure import Measure


class Report(object):
    """A concrete class within the cim v1 type system.

    
    """

    def __init__(self):
        """Constructor"""
        super(Report, self).__init__()
        self.date = datetime.datetime.now()          # type = datetime.datetime
        self.evaluation = None                       # type = quality.Evaluation
        self.evaluator = None                        # type = shared.ResponsibleParty
        self.measure = None                          # type = quality.Measure


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
        append(d, 'evaluation', self.evaluation, False, False, False)
        append(d, 'evaluator', self.evaluator, False, False, False)
        append(d, 'measure', self.measure, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

