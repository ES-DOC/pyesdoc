# -*- coding: utf-8 -*-

"""
.. module:: utils.py
   :copyright: Copyright "Feb 7, 2013", Earth System Documentation
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Exposes extension utility functions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

class DocumentExtensionInfo(object):
    """Document extension information injected by extenders.

    """
    def __init__(self):
        """Constructor.

        """
        self.description = str()
        self.display_name = str()
        self.encodings = []
        self.full_display_name = str()
        self.language = str()
        self.summary_fields = []
        self.type = str()
        self.type_display_name = str()

