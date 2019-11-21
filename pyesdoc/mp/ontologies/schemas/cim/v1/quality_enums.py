"""
.. module:: quality_enums.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 quality package enum definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def cim_feature_type():
    """Creates and returns instance of cim_feature_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('file', None),
            ('diagnostic', None),
        ],
    }


def cim_result_type():
    """Creates and returns instance of cim_result_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('plot', None),
            ('document', None),
            ('logfile', None),
        ],
    }


def cim_scope_code_type():
    """This would cover quality issues with the CIM itself.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('dataset', None),
            ('software', None),
            ('service', None),
            ('model', None),
            ('modelComponent', None),
            ('simulation', None),
            ('experiment', None),
            ('numericalRequirement', None),
            ('ensemble', None),
            ('file', None),
        ],
    }


def quality_issue_type():
    """Creates and returns instance of quality_issue_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('metadata', None),
            ('data_format', None),
            ('data_content', None),
            ('data_indexing', None),
            ('science', None),
        ],
    }


def quality_severity_type():
    """Creates and returns instance of quality_severity_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('cosmetic', None),
            ('minor', None),
            ('major', None),
        ],
    }


def quality_status_type():
    """Creates and returns instance of quality_status_type enum.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ('reported', None),
            ('confirmed', None),
            ('partially_resolved', None),
            ('resolved', None),
        ],
    }
