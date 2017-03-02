
import os

from pyesdoc.mp.specializations import utils_loader as loader
from pyesdoc.mp.specializations import utils_factory as factory
from pyesdoc.mp.specializations.utils_factory import CACHE


def get_model_specialization(mip_era, scope):
	"""Returns model specializations.

	"""
	mip_era = unicode(mip_era).strip().lower()
	scope = unicode(scope).strip().lower()
	cache_key = "{}.{}".format(mip_era, scope)
	if cache_key not in CACHE:
		dpath = os.path.join(os.path.dirname(__file__), mip_era)
		modules = loader.get_modules(dpath, scope)
		factory.get_specialization(modules)

	return CACHE[cache_key]


def get_property_specialization(prop_id):
	return CACHE[prop_id]

