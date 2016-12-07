# -*- coding: utf-8 -*-

"""
.. module:: test_content_section_item.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests data request content section items.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import dreq



def test_type():
    """dreq-tests: config-table-attribute: verify table attribute types.

    """
    for table in dreq.config:
        for attribute in table:
            assert isinstance(attribute, dreq.ConfigTableAttribute)

