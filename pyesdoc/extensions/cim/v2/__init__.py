# -*- coding: utf-8 -*-

from pyesdoc.extensions.cim.v2 import designing_numerical_experiment



# Module exports.
__all__ = ['SUPPORTED']



# Supported extenders keyed by document type.
SUPPORTED = {
	"cim.2.designing.numericalexperiment": designing_numerical_experiment,
}
