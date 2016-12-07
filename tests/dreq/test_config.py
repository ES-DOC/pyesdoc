# -*- coding: utf-8 -*-

"""
.. module:: test_config.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests data request configuration wrapper.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import dreq


def test_is_loaded():
    """dreq-tests: config: verify config is loaded into memory.

    """
    assert isinstance(dreq.config, dreq.ConfigWrapper)
    assert len(dreq.config) == len(dreq.config.tables) == 24
