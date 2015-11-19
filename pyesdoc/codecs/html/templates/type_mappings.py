# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.codecs.html.encoder.py

   :copyright: @2013 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Encodes a document as an HTML text blob.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>

"""
from pyesdoc.ontologies import cim



# Mapping of doucment type to template.
TEMPLATE_TYPE_MAPPINGS = {
    # CIM v1 templates.
    cim.v1.activity.Ensemble: "cim_1/activity_ensemble.html",
    cim.v1.activity.NumericalExperiment: "cim_1/activity_numerical_experiment.html",
    cim.v1.activity.SimulationRun: "cim_1/activity_simulation_run.html",
    cim.v1.data.DataObject: "cim_1/data_data_object.html",
    cim.v1.grids.GridSpec: "cim_1/grids_grid_spec.html",
    cim.v1.shared.Platform: "cim_1/shared_platform.html",
    cim.v1.software.ModelComponent: "cim_1/software_model_component.html",
    cim.v1.quality.CimQuality: "cim_1/quality_cimquality.html",
    # CIM v2 templates.
    # cim.v2.activity.Project: "cim_2/activity_project.html",
    # cim.v2.activity.NumericalExperiment: "cim_2/activity_numerical_experiment.html"
}
