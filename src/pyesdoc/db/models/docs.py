"""
.. module:: docs.py
   :copyright: Copyright "Jun 29, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: ES-DOC API db models - docs domain partition.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
# Module imports.
import datetime
import uuid

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    Text,
    Unicode,
    UniqueConstraint
    )
from sqlalchemy.orm import relationship

from . utils import (
    create_fk,
    Entity,
    EntityConvertor
    )


# Module exports.
__all__ = [
    'Document',
    'DocumentDRS',
    'DocumentExternalID',
    'DocumentSummary',
    'DOCUMENT_VERSIONS',
    'DOCUMENT_VERSION_LATEST',
    'DOCUMENT_VERSION_ALL'
]



# Domain model partition.
_DOMAIN_PARTITION = 'docs'

# Default drs split.
_DRS_SPLIT = '/'

# Document version related constants.
DOCUMENT_VERSION_ALL = '*'
DOCUMENT_VERSION_LATEST = 'latest'
DOCUMENT_VERSIONS = [DOCUMENT_VERSION_ALL, DOCUMENT_VERSION_LATEST]


class Document(Entity):
    """A document ingested into the ES-DOC API repository.

    """
    # SQLAlchemy directives.
    __tablename__ = 'tblDocument'
    __table_args__ = (
        UniqueConstraint('Project_ID' ,'UID', 'Version'),
        {'schema' : _DOMAIN_PARTITION}
    )

    # Foreign keys.
    Project_ID = create_fk('vocab.tblProject.ID', required=True)
    Institute_ID = create_fk('vocab.tblInstitute.ID')

    # Relationships.
    ExternalIDs = relationship("DocumentExternalID", backref="Document")
    Summaries = relationship("DocumentSummary", backref="Document", lazy='joined')

    # Field set.
    Source_Key =  Column(Unicode(255), nullable=True)
    Type =  Column(Unicode(255), nullable=False)
    Name =  Column(Unicode(255), nullable=False)
    UID = Column(Unicode(63), nullable=False, default=uuid.uuid4())
    Version = Column(Integer, nullable=False, default=1)
    IngestDate =  Column(DateTime, default=datetime.datetime.now())

    IsLatest = Column(Boolean, nullable=False, default=False)

    def __init__(self):
        """Constructor.

        """
        super(Document, self).__init__()
        self.children = []
        self.as_obj = None


    @property
    def summary(self):
        """Gets top summary from associated collection.

        """
        if self.Summaries is not None or len(self.Summaries) > 0:
            return self.Summaries[0]
        else:
            return None


    @classmethod
    def get_default_sort_key(cls):
        """Gets default sort key.

        """
        return lambda instance: instance.UID + str(instance.Version)


class DocumentDRS(Entity):
    """Encapsulates information required to resolve a document from DRS (directory reference syntax) info.

    """
    # SQLAlchemy directives.
    __tablename__ = 'tblDocumentDRS'
    __table_args__ = (
        UniqueConstraint('Project_ID' ,'Document_ID', 'Path'),
        {'schema' : _DOMAIN_PARTITION}
    )

    # Foreign keys.
    Project_ID = create_fk('vocab.tblProject.ID', required=True)
    Document_ID = create_fk('docs.tblDocument.ID', required=True)

    # Field set.
    Path = Column(Unicode(511))
    Key_01 = Column(Unicode(63))
    Key_02 = Column(Unicode(63))
    Key_03 = Column(Unicode(63))
    Key_04 = Column(Unicode(63))
    Key_05 = Column(Unicode(63))
    Key_06 = Column(Unicode(63))
    Key_07 = Column(Unicode(63))
    Key_08 = Column(Unicode(63))


    def clone(self):
        """Returns a cloned instance.

        """
        result = DocumentDRS()

        result.Document_ID = self.Document_ID
        result.Key_01 = self.Key_01
        result.Key_02 = self.Key_02
        result.Key_03 = self.Key_03
        result.Key_04 = self.Key_04
        result.Key_05 = self.Key_05
        result.Key_06 = self.Key_06
        result.Key_07 = self.Key_07
        result.Key_08 = self.Key_08
        result.Path = self.Path
        result.Project_ID = self.Project_ID

        return result


    def reset_path(self):
        """Resets drs path based upon value of keys.

        """
        path = ''
        for i in range(8):
            key = getattr(self, "Key_0" + str(i + 1))
            if key is not None:
                if i > 0:
                    path += _DRS_SPLIT
                path += key.upper()
        self.Path = path


    @classmethod
    def get_default_sort_key(cls):
        """
        Gets default sort key.
        """
        return lambda instance: instance.Path


class DocumentExternalID(Entity):
    """The external id of a cim document.

    """
    # SQLAlchemy directives.
    __tablename__ = 'tblDocumentExternalID'
    __table_args__ = (
        UniqueConstraint('Project_ID' ,'Document_ID', 'ExternalID'),
        {'schema' : _DOMAIN_PARTITION}
    )

    # Foreign keys.
    Project_ID = create_fk('vocab.tblProject.ID', required=True)
    Document_ID = create_fk('docs.tblDocument.ID', required=True)

    # Field set.
    ExternalID = Column(Unicode(255), nullable=False)


class DocumentSummary(Entity):
    """Encapsulates document summary information.

    """
    # SQLAlchemy directives.
    __tablename__ = 'tblDocumentSummary'
    __table_args__ = (
        UniqueConstraint('Document_ID' ,'Language_ID'),
        {'schema' : _DOMAIN_PARTITION}
    )

    # Foreign keys.
    Document_ID = create_fk('docs.tblDocument.ID', required=True)
    Language_ID = create_fk('vocab.tblDocumentLanguage.ID', required=True)

    # Field set.
    ShortName = Column(Unicode(1023))
    LongName = Column(Unicode(1023))
    Description = Column(Unicode(1023))
    Field_01 = Column(Unicode(1023))
    Field_02 = Column(Unicode(1023))
    Field_03 = Column(Unicode(1023))
    Field_04 = Column(Unicode(1023))
    Field_05 = Column(Unicode(1023))
    Field_06 = Column(Unicode(1023))
    Field_07 = Column(Unicode(1023))
    Field_08 = Column(Unicode(1023))
    Model = Column(Unicode(1023))
    Experiment = Column(Unicode(1023))


    def format_dict(self, as_dict, key_formatter=None, json_formatting=False):
        """Formats a dictionary representation.

        """
        as_dict['document'] = \
            EntityConvertor.to_dict(self.Document, key_formatter, json_formatting)


    @classmethod
    def get_default_sort_key(cls):
        """
        Gets default sort key.
        """
        return lambda instance: instance.ShortName

