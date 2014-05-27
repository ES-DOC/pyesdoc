# Module imports.
from . import (
	activity_ensemble,
	activity_numerical_experiment,
	activity_simulation_run,
	data_data_object,
	grids_grid_spec,
	misc_document_set,
	shared_platform,
	software_model_component,
	quality_cimquality,
	)



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
	"cim.1.shared.platform": shared_platform,
	"cim.1.software.modelcomponent": software_model_component,
	"cim.1.software.statisticalmodelcomponent": software_model_component,
	"cim.1.quality.cimquality": quality_cimquality,
}
