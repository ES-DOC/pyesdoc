# -*- coding: utf-8 -*-

"""
.. module:: test_content.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests data request content wrapper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import dreq


def test_is_loaded():
    """dreq-tests: content: verify content is loaded into memory.

    """
    assert isinstance(dreq.content, dreq.ContentWrapper)
    assert len(dreq.content) == len(dreq.content.sections) == 24
