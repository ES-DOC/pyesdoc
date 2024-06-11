# -*- coding: utf-8 -*-
"""
.. module:: cim.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim package initializer.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using pyesdoc @ 2013-04-17 13:14:13.903808.

"""
from . import v1
from . import v2



# Map of document types to display names.
DISPLAY_NAMES = {
    v1.activity.NumericalExperiment: "Experiment",
    v1.activity.SimulationRun: "Simulation",
    v1.data.DataObject: "Data Object",
    v1.grids.GridSpec: "Grid Spec",
    v1.misc.DocumentSet: "Simulation",
    v1.quality.CimQuality: "Dataset QC",
    v1.software.ModelComponent: "Model",
    v2.designing.NumericalExperiment: "Experiment",
    v2.designing.Project: "Sub MIP"
}

# Map of document types to sort keys.
SORT_KEYS = {
    v1.activity.Ensemble: "BC",
    v1.activity.NumericalExperiment: "AB",
    v1.activity.SimulationRun: "AC",
    v1.data.DataObject: "CA",
    v1.grids.GridSpec: "BB",
    v1.misc.DocumentSet: "AC",
    v1.quality.CimQuality: "CB",
    v1.shared.Platform: "BA",
    v1.software.ModelComponent: "AA",
    v2.designing.NumericalExperiment: "AB",
    v2.designing.Project: "AA"
}
