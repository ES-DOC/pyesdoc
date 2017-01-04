
import os

from pyesdoc.mp.specializations import utils_loader as loader
from pyesdoc.mp.specializations import utils_factory as factory
from pyesdoc.mp.specializations.utils_factory import CACHE


def get_model_realm_specialization(mip_era, realm):
	"""Returns model realm specializations.

	"""
	mip_era = unicode(mip_era).strip().lower()
	realm = unicode(realm).strip().lower()
	cache_key = "{}.{}".format(mip_era, realm)
	if cache_key not in CACHE:
		dpath = os.path.join(os.path.dirname(__file__), mip_era)
		specs = loader.get_realm_specializations(dpath, realm)
		factory.create_realm_specialization(specs)

	return CACHE[cache_key]


def get_property_specialization(prop_id):
	return CACHE[prop_id]

