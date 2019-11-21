"""
.. module:: shared_enums_doc.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 shared package document related enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def doc_relationship_direction_type():
    """Creates and returns instance of relationship_direction_type enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('toTarget', None),
            ('fromTarget', None),
        ],
    }


def doc_relationship_type():
    """Creates and returns instance of document_relationship_type enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('similarTo', None),
            ('other', None),
            ('laterVersionOf', None),
            ('previousVersionOf', None),
            ('fixedVersionOf', None),
        ],
    }


def doc_status_type():
    """Status of cim document.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('complete', None),
            ('incomplete', None),
            ('in-progress', None),
        ],
    }


def doc_type():
    """Creates and returns instance of doc_type enum.

    """
    return {
        'type' : 'enum',
        'is_open' : False,
        'members' : [
            ('downscalingSimulation', None),
            ('statisticalModelComponent', None),
            ('simulationRun', None),
            ('assimilation', None),
            ('simulationComposite', None),
            ('numericalExperiment', None),
            ('dataProcessing', None),
            ('ensemble', None),
            ('dataObject', None),
            ('gridSpec', None),
            ('cimQuality', None),
            ('platform', None),
            ('processorComponent', None),
            ('modelComponent', None),
        ],
    }



