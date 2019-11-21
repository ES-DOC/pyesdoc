"""
.. module:: shared_classes_time.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 shared package time related class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def calendar():
    """Describes a method of calculating a span of dates.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('description', 'str', '0.1'),
            ('length', 'int', '0.1'),
            ('range', 'shared.date_range', '0.1'),
        ],
        'doc_strings': {
            'description': 'Describes the finer details of the calendar, in case they are not-obvious.  For example, if an experiment has changing conditions within it (ie: 1% CO2 increase until 2100, then hold fixed for the remaining period of the  experment)',
        },
        'decodings': [
            ('description', 'child::cim:description'),
            ('length', 'child::cim:length'),
            ('range', 'child::cim:range/cim:closedDateRange', 'shared.closed_date_range'),
            ('range', 'child::cim:range/cim:openDateRange', 'shared.open_date_range'),
        ]
    }


def closed_date_range():
    """A date range with specified start and end points.

    """
    return {
        'type': 'class',
        'base': 'shared.date_range',
        'is_abstract': False,
        'properties': [
            ('end', 'datetime', '0.1'),
            ('start', 'datetime', '1.1'),
        ],
        'doc_strings': {
            'end': 'End date is optional becuase the length of a ClosedDateRange can be calculated from the StartDate plus the Duration element.',
        },
        'decodings': [
            ('end', 'child::cim:endDate'),
            ('start', 'child::cim:startDate'),
        ]
    }


def daily_360():
    """Creates and returns instance of daily_360 class.

    """
    return {
        'type': 'class',
        'base': 'shared.calendar',
        'is_abstract': False
    }


def date_range():
    """Creates and returns instance of date_range class.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('duration', 'str', '0.1'),
        ],
        'decodings': [
            ('duration', 'child::cim:duration'),
        ]
    }


def open_date_range():
    """A date range without a specified start and/or end point.

    """
    return {
        'type': 'class',
        'base': 'shared.date_range',
        'is_abstract': False,
        'properties': [
            ('end', 'datetime', '0.1'),
            ('start', 'datetime', '0.1'),
        ],
        'decodings': [
            ('end', 'child::cim:endDate'),
            ('start', 'child::cim:startDate'),
        ]
    }


def perpetual_period():
    """Creates and returns instance of perpetual_period class.

    """
    return {
        'type': 'class',
        'base': 'shared.calendar',
        'is_abstract': False
    }


def real_calendar():
    """Creates and returns instance of real_calendar class.

    """
    return {
        'type': 'class',
        'base': 'shared.calendar',
        'is_abstract': False
    }
