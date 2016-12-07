# -*- coding: utf-8 -*-

"""
.. module:: test_content_section.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Tests data request content sections.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import dreq



# Set of section properties mapped from <section> xml attributes.
_SECTION_PROPERTIES = {
    'id',
    'label',
    'title',
    'uid',
    'use_class',
    }


def test_type():
    """dreq-tests: content-section: verify section types.

    """
    for section in dreq.content:
        assert isinstance(section, dreq.ContentSection)


def test_properties():
    """dreq-tests: content-section: verify section properties.

    """
    for section in dreq.content:
        for name in _SECTION_PROPERTIES:
            assert hasattr(section, name), name


def test_property_pythonic_label():
    """dreq-tests: content-section: verify each section has an injected label_pythonic property.

    """
    for section in dreq.content:
		try:
			assert section.label_pythonic == dreq.LABEL_MAP[section.label]
		except KeyError:
			assert section.label_pythonic == section.label


def test_direct_reference():
    """dreq-tests: content-section: verify direct access to specific section.

    """
    assert dreq.content.CMORvar is not None
    assert dreq.content.experiment is not None
    assert dreq.content.exptgroup is not None
    assert dreq.content.grids is not None
    assert dreq.content.mip is not None
    assert dreq.content.modelConfig is not None
    assert dreq.content.objective is not None
    assert dreq.content.objectiveLink is not None
    assert dreq.content.remarks is not None
    assert dreq.content.requestItem is not None
    assert dreq.content.requestLink is not None
    assert dreq.content.requestVar is not None
    assert dreq.content.requestVarGroup is not None
    assert dreq.content.spatialShape is not None
    assert dreq.content.standardname is not None
    assert dreq.content.structure is not None
    assert dreq.content.tableSection is not None
    assert dreq.content.temporalShape is not None
    assert dreq.content.timeSlice is not None
    assert dreq.content.var is not None
    assert dreq.content.varChoice is not None
    assert dreq.content.varChoiceLinkC is not None
    assert dreq.content.varChoiceLinkR is not None


def test_direct_reference_pythonic_label():
    """dreq-tests: content-section: verify access to specific sections via it's pythonic label.

    """
    assert dreq.content.cmor_variable == dreq.content.CMORvar
    assert dreq.content.experiment_group == dreq.content.exptgroup
    assert dreq.content.model_config == dreq.content.modelConfig
    assert dreq.content.objective_link == dreq.content.objectiveLink
    assert dreq.content.request_item == dreq.content.requestItem
    assert dreq.content.request_link == dreq.content.requestLink
    assert dreq.content.request_variable == dreq.content.requestVar
    assert dreq.content.request_variable_group == dreq.content.requestVarGroup
    assert dreq.content.spatial_shape == dreq.content.spatialShape
    assert dreq.content.standard_name == dreq.content.standardname
    assert dreq.content.table_section == dreq.content.tableSection
    assert dreq.content.temporal_shape == dreq.content.temporalShape
    assert dreq.content.time_slice == dreq.content.timeSlice
    assert dreq.content.var_choice == dreq.content.varChoice
    assert dreq.content.var_choice_link_c == dreq.content.varChoiceLinkC
    assert dreq.content.var_choice_link_r == dreq.content.varChoiceLinkR
