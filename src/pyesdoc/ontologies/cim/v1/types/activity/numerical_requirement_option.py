"""
.. module:: cim.v1.types.activity.numerical_requirement_option.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-07-10 16:12:40.222978.

"""

# Module imports.
import datetime
import types
import uuid



class NumericalRequirementOption(object):
    """A concrete class within the cim v1 type system.

    A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that "parent" requirement would have three "child" RequirmentOptions (each of one with the XOR optionRelationship).
    """

    def __init__(self):
        """Constructor"""
        super(NumericalRequirementOption, self).__init__()
        self.relationship = str()                    # type = str
        self.requirement = None                      # type = activity.NumericalRequirement


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
        append(d, 'relationship', self.relationship, False, True, False)
        append(d, 'requirement', self.requirement, False, False, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm
from pyesdoc.ontologies.cim.v1.types.activity.numerical_requirement import NumericalRequirement

