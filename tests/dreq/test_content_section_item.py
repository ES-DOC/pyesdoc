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
    """dreq-tests: content-section-item: verify section item types.

    """
    for section in dreq.content:
        for item in section:
            assert isinstance(item, dreq.ContentSectionItem)


def test_required():
    """dreq-tests: content-section-item: verify required section items.

    """
    for section in dreq.content:
        for item in section:
        	for attribute in section.cfg.required_attributes:
    			assert hasattr(item, attribute.name)


def test_value_type():
    """dreq-tests: content-section-item: verify value type.

    """
    for section in dreq.content:
        for item in section:
            for attribute in section.cfg.scalar_attributes:
                if hasattr(item, attribute.name):
                    assert type(getattr(item, attribute.name)) == attribute.type_python
