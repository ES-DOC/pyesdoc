"""
.. module:: cim.v1_5.types.shared.cim_info.py

   :copyright: @2013 Earth System Documentation (http://esdocumentation.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: A concrete class within the cim v1.5 type system.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@esdocumentation.org>
.. note:: Code generated using esdoc_mp @ 2013-04-17 17:20:28.691697.

"""

# Module imports.
import datetime
import types
import uuid

from pyesdoc.ontologies.cim.v1_5.types.shared.responsible_party import ResponsibleParty
from pyesdoc.ontologies.cim.v1_5.types.shared.standard_name import StandardName
from pyesdoc.ontologies.cim.v1_5.types.shared.cim_genealogy import CimGenealogy
from pyesdoc.ontologies.cim.v1_5.types.shared.document_status_type import DocumentStatusType
from pyesdoc.ontologies.cim.v1_5.types.shared.cim_type_info import CimTypeInfo


class CimInfo(object):
    """A concrete class within the cim v1.5 type system.

    Encapsulates common cim information.
    """

    def __init__(self):
        """Constructor"""
        super(CimInfo, self).__init__()
        self.author = None                           # type = shared.ResponsibleParty
        self.create_date = datetime.datetime.now()   # type = datetime.datetime
        self.external_ids = []                       # type = shared.StandardName
        self.genealogy = None                        # type = shared.CimGenealogy
        self.id = uuid.uuid4()                       # type = uuid.UUID
        self.language = str()                        # type = str
        self.metadata_id = str()                     # type = str
        self.metadata_version = str()                # type = str
        self.project = str()                         # type = str
        self.source = str()                          # type = str
        self.status = ''                             # type = shared.DocumentStatusType
        self.type_info = None                        # type = shared.CimTypeInfo
        self.version = str()                         # type = str


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
        append(d, 'author', self.author, False, False, False)
        append(d, 'create_date', self.create_date, False, True, False)
        append(d, 'external_ids', self.external_ids, True, False, False)
        append(d, 'genealogy', self.genealogy, False, False, False)
        append(d, 'id', self.id, False, True, False)
        append(d, 'language', self.language, False, True, False)
        append(d, 'metadata_id', self.metadata_id, False, True, False)
        append(d, 'metadata_version', self.metadata_version, False, True, False)
        append(d, 'project', self.project, False, True, False)
        append(d, 'source', self.source, False, True, False)
        append(d, 'status', self.status, False, False, True)
        append(d, 'type_info', self.type_info, False, False, False)
        append(d, 'version', self.version, False, True, False)
        return d


# Circular reference imports.
# N.B. - see http://effbot.org/zone/import-confusion.htm

