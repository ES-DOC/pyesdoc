# Module imports.
from . import (
	activity_numerical_experiment,
	data_data_object,
	grids_grid_spec,
	misc_document_set,
	software_model_component,
	quality_cimquality,
	)



# Module exports.
__all__ = ['parsers']



# Supported parsers keyed by document type.
supported = {
	"cim.1.activity.numericalexperiment": activity_numerical_experiment.parse,
	"cim.1.data.dataobject": data_data_object.parse,
	"cim.1.grids.gridspec": grids_grid_spec.parse,
	"cim.1.misc.documentset": misc_document_set.parse,
	"cim.1.software.modelcomponent": software_model_component.parse,
	"cim.1.software.statisticalmodelcomponent": software_model_component.parse,
	"cim.1.quality.cimquality": quality_cimquality.parse,
}
