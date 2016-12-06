# -*- coding: utf-8 -*-
"""
.. module:: cim.__init__.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The cim package initializer.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using pyesdoc @ 2013-04-17 13:14:13.903808.

"""
import v1
import v2



# Map of document types to display names.
DISPLAY_NAMES = {
    v1.activity.NumericalExperiment: u"Experiment",
    v1.activity.SimulationRun: u"Simulation",
    v1.data.DataObject: u"Data Object",
    v1.grids.GridSpec: u"Grid Spec",
    v1.misc.DocumentSet: u"Simulation",
    v1.quality.CimQuality: u"Dataset QC",
    v1.software.ModelComponent: u"Model",
    v2.designing.NumericalExperiment: u"Experiment",
    v2.designing.Project: u"Sub MIP"
}

# Map of document types to sort keys.
SORT_KEYS = {
    v1.activity.Ensemble: u"BC",
    v1.activity.NumericalExperiment: u"AB",
    v1.activity.SimulationRun: u"AC",
    v1.data.DataObject: u"CA",
    v1.grids.GridSpec: u"BB",
    v1.misc.DocumentSet: u"AC",
    v1.quality.CimQuality: u"CB",
    v1.shared.Platform: u"BA",
    v1.software.ModelComponent: u"AA",
    v2.designing.NumericalExperiment: u"AB",
    v2.designing.Project: u"AA"
}
