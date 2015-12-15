# -*- coding: utf-8 -*-

"""
.. module:: test_types.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Set of document types to be tested.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
# Module imports.
import test_type_cim_v1_activity_ensemble_1
import test_type_cim_v1_activity_ensemble_2
import test_type_cim_v1_activity_numerical_experiment
import test_type_cim_v1_activity_simulation_run
import test_type_cim_v1_data_data_object_1
import test_type_cim_v1_data_data_object_2
import test_type_cim_v1_grids_gridspec
import test_type_cim_v1_misc_document_set
import test_type_cim_v1_quality_cim_quality
import test_type_cim_v1_shared_platform
import test_type_cim_v1_software_model_component_1
import test_type_cim_v1_software_model_component_2
import test_type_cim_v1_software_statistical_model_component


# Set of test modules.
MODULES = (
    test_type_cim_v1_activity_ensemble_1,
    test_type_cim_v1_activity_ensemble_2,
    test_type_cim_v1_activity_numerical_experiment,
    test_type_cim_v1_activity_simulation_run,
    test_type_cim_v1_data_data_object_1,
    test_type_cim_v1_data_data_object_2,
    test_type_cim_v1_grids_gridspec,
    test_type_cim_v1_misc_document_set,
    test_type_cim_v1_quality_cim_quality,
    test_type_cim_v1_shared_platform,
    test_type_cim_v1_software_model_component_1,
    test_type_cim_v1_software_model_component_2,
    # test_type_cim_v1_software_statistical_model_component,
)


# Set of stateful test module fields.
STATE_FIELDS = (
    "DOC_TYPE",
    "DOC_TYPE_KEY",
    "DOC_FILE",
    "DOC_UID",
    "DOC_VERSION",
    "DOC_DATE",
    "DOC_PROJECT",
    "DOC_INSTITUTE",
    "DOC_AUTHOR"
    )


# Initial state of test modules.
INITIAL_STATE = {mod:{} for mod in MODULES}
for mod in MODULES:
    for field in STATE_FIELDS:
        INITIAL_STATE[mod][field] = getattr(mod, field)


def reset_all():
    """Resets all module state prior to usage.

    """
    for mod in MODULES:
        reset(mod)


def reset(mod):
    """Resets module state prior to usage.

    :param module mod: Test module.

    """
    assert mod in MODULES
    assert mod in INITIAL_STATE
    for field in STATE_FIELDS:
        setattr(mod, field, INITIAL_STATE[mod][field])
