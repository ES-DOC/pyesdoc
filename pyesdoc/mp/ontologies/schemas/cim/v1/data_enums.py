"""
.. module:: data_enums.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 data package enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def data_hierarchy_type():
    """Enumerates the level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject.

    """
    return {
        'type' : 'enum',
        'is_open' : True,
        'members' : [],
    }


def data_status_type():
    """Enumerates status of a data object.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('complete', 'This DataObject is complete.'),
            ('metadataOnly', 'This DataObject is incomplete - it is described in metadata but the actual data has not yet been linked to it.'),
            ('continuouslySupplemented', 'This DataObject\'s actual data is continuously updated.'),
        ],
    }
