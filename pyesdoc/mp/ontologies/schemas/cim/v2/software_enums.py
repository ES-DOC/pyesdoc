"""
.. module:: software_enums.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def coupling_framework():
    """The set of terms which define known coupling frameworks.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("OASIS", "The OASIS coupler - prior to OASIS-MCT"),
            ("OASIS3-MCT", "The MCT variant of the OASIS coupler"),
            ("ESMF", "Vanilla Earth System Modelling Framework"),
            ("NUOPC", "National Unified Operational Prediction Capability variant of ESMF"),
            ("Bespoke", "Customised coupler developed for this model"),
            ("Unknown", "It is not known what/if-a coupler is used"),
            ("None", "No coupler is used")
        ]
    }


def programming_language():
    """The set of terms which define programming languages used for earth
    system simulation.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Fortran", "Fortran Programming Language"),
            ("C", "C Programmming Language"),
            ("C++", "C++ Programming Language"),
            ("Python", "Python Programming Language")
        ]
    }
