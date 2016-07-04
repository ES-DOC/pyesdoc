# -*- coding: utf-8 -*-
from pyesdoc.extensions.cim.v2 import designing_numerical_experiment
from pyesdoc.extensions.cim.v2 import designing_project


# Module exports.
__all__ = ['SUPPORTED']



# Supported extenders keyed by document type.
SUPPORTED = {
	"cim.2.designing.numericalexperiment": designing_numerical_experiment,
	"cim.2.designing.project": designing_project,
}
