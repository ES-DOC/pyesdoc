
import os

from pyesdoc.mp.specializations import utils_loader as loader
from pyesdoc.mp.specializations import utils_factory as factory
from pyesdoc.mp.specializations.utils_factory import CACHE



def get_model_specialization(mip_era, topic):
	"""Returns model specializations.

	:param str mip_era: MIP era that model documentation is related to.
	:param str topic: Specialziation topic.

	:result: Topic specializations.
	:rtype: TopicSpecialization

	"""
	load_model_specialization(mip_era, topic)

	return CACHE[_get_cache_key(mip_era, topic)]


def load_model_specialization(mip_era, topic):
	"""Loads model specializations into memory.

	"""
	if _get_cache_key(mip_era, topic) in CACHE:
		return

	mip_era = unicode(mip_era).strip().lower()
	topic = unicode(topic).strip().lower()
	dpath = os.path.join(os.path.dirname(__file__), mip_era)
	modules = loader.get_modules(dpath, topic)
	factory.get_specialization(modules)


def get_property_specialization(specialization_id):
	"""Returns property specializations.

	:param str specialization_id: Specialziation identifier.

	:result: Property specialization.
	:rtype: PropertySpecialization

	"""
	if len(specialization_id) == 0:
		return

	# Ensure topic is loaded.
	parts = specialization_id.split('.')
	load_model_specialization(parts[0], parts[1])

	return CACHE[specialization_id]


def _get_cache_key(mip_era, topic):
	"""Returns model specialization cache key.

	"""
	mip_era = unicode(mip_era).strip().lower()
	topic = unicode(topic).strip().lower()

	return "{}.{}".format(mip_era, topic)
