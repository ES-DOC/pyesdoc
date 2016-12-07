# -*- coding: utf-8 -*-

"""
.. module:: test_config_table.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests data request configuration tables.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import dreq


# Set of table properties mapped from <table> xml attributes.
_TABLE_PROPERTIES = {
    'description',
    'label',
    'uid',
    'id',
    'item_label_mode',
    'level',
    'max_occurs',
    'is_lab_unique'
    }


def test_type():
    """dreq-tests: config-table: verify table types.

    """
    for table in dreq.config:
        assert isinstance(table, dreq.ConfigTable)


def test_properties():
    """dreq-tests: config-table: verify table properties.

    """
    for table in dreq.config:
        for name in _TABLE_PROPERTIES:
            assert hasattr(table, name)


def test_property_pythonic_label():
    """dreq-tests: config-table: verify each table has an injected label_pythonic property.

    """
    for table in dreq.config:
        try:
            assert table.label_pythonic == dreq.LABEL_MAP[table.label]
        except KeyError:
            assert table.label_pythonic == table.label


def test_direct_reference():
    """dreq-tests: config-table: verify access to specific tables.

    """
    assert dreq.config.CMORvar is not None
    assert dreq.config.experiment is not None
    assert dreq.config.exptgroup is not None
    assert dreq.config.grids is not None
    assert dreq.config.mip is not None
    assert dreq.config.modelConfig is not None
    assert dreq.config.objective is not None
    assert dreq.config.objectiveLink is not None
    assert dreq.config.remarks is not None
    assert dreq.config.requestItem is not None
    assert dreq.config.requestLink is not None
    assert dreq.config.requestVar is not None
    assert dreq.config.requestVarGroup is not None
    assert dreq.config.spatialShape is not None
    assert dreq.config.standardname is not None
    assert dreq.config.structure is not None
    assert dreq.config.tableSection is not None
    assert dreq.config.temporalShape is not None
    assert dreq.config.timeSlice is not None
    assert dreq.config.var is not None
    assert dreq.config.varChoice is not None
    assert dreq.config.varChoiceLinkC is not None
    assert dreq.config.varChoiceLinkR is not None


def test_direct_reference_pythonic_label():
    """dreq-tests: config-table: verify access to specific tables via it's pythonic label.

    """
    assert dreq.config.cmor_variable == dreq.config.CMORvar
    assert dreq.config.experiment_group == dreq.config.exptgroup
    assert dreq.config.model_config == dreq.config.modelConfig
    assert dreq.config.objective_link == dreq.config.objectiveLink
    assert dreq.config.request_item == dreq.config.requestItem
    assert dreq.config.request_link == dreq.config.requestLink
    assert dreq.config.request_variable == dreq.config.requestVar
    assert dreq.config.request_variable_group == dreq.config.requestVarGroup
    assert dreq.config.spatial_shape == dreq.config.spatialShape
    assert dreq.config.standard_name == dreq.config.standardname
    assert dreq.config.table_section == dreq.config.tableSection
    assert dreq.config.temporal_shape == dreq.config.temporalShape
    assert dreq.config.time_slice == dreq.config.timeSlice
    assert dreq.config.var_choice == dreq.config.varChoice
    assert dreq.config.var_choice_link_c == dreq.config.varChoiceLinkC
    assert dreq.config.var_choice_link_r == dreq.config.varChoiceLinkR
