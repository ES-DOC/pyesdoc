# -*- coding: utf-8 -*-
from pyesdoc._extensions.cim.v2 import designing_numerical_experiment
from pyesdoc._extensions.cim.v2 import designing_project
from pyesdoc._extensions.cim.v2 import science_model



# Supported extenders keyed by document type.
SUPPORTED = {
	"cim.2.designing.numericalexperiment": designing_numerical_experiment,
	"cim.2.designing.project": designing_project,
	"cim.2.science.model": science_model
}
