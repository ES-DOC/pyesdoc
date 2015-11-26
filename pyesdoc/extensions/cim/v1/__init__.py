# -*- coding: utf-8 -*-

from pyesdoc.extensions.cim.v1 import activity_ensemble
from pyesdoc.extensions.cim.v1 import activity_numerical_experiment
from pyesdoc.extensions.cim.v1 import activity_simulation_run
from pyesdoc.extensions.cim.v1 import data_data_object
from pyesdoc.extensions.cim.v1 import grids_grid_spec
from pyesdoc.extensions.cim.v1 import misc_document_set
from pyesdoc.extensions.cim.v1 import software_model_component
from pyesdoc.extensions.cim.v1 import quality_cimquality



# Module exports.
__all__ = ['SUPPORTED']



# Supported extenders keyed by document type.
SUPPORTED = {
	"cim.1.activity.ensemble": activity_ensemble,
	"cim.1.activity.numericalexperiment": activity_numerical_experiment,
	"cim.1.activity.simulationrun": activity_simulation_run,
	"cim.1.data.dataobject": data_data_object,
	"cim.1.grids.gridspec": grids_grid_spec,
	"cim.1.misc.documentset": misc_document_set,
	"cim.1.software.modelcomponent": software_model_component,
	"cim.1.software.statisticalmodelcomponent": software_model_component,
	"cim.1.quality.cimquality": quality_cimquality,
}
