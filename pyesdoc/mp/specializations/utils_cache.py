"""
.. module:: utils_cache.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates access to specialization cache.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

from utils_loader import get_modules



# Map of specializations by id.
_CACHE = dict()


def set_specialization(spec):
    """Place specialization in cache.

    """
    _CACHE[spec.id.lower()] = spec


def get_topic_specialization(mip_era, topic):
	"""Returns topic specializations.

	:param str mip_era: MIP era that model documentation is related to.
	:param str topic: Specialization topic.

	:result: Topic specializations.
	:rtype: TopicSpecialization

	"""
	# JIT load.
	_set_topic_specialization(mip_era, topic)

	return _CACHE[_get_topic_cache_key(mip_era, topic)]


def get_property_specialization(specialization_id):
	"""Returns property specializations.

	:param str specialization_id: Specialziation identifier.

	:result: Property specialization.
	:rtype: PropertySpecialization

	"""
	if len(specialization_id) == 0:
		return

	# JIT load.
	parts = specialization_id.split('.')
	_set_topic_specialization(parts[0], parts[1])

	return _CACHE[specialization_id.lower()]


def _set_topic_specialization(mip_era, topic):
	"""Loads topic specializations into memory.

	"""
	if _get_topic_cache_key(mip_era, topic) in _CACHE:
		return

	# JIT to avoid circular dependencies.
	from utils_factory import create_specializations

	mip_era = mip_era.strip().lower()
	topic = topic.strip().lower()
	dpath = os.path.join(os.path.dirname(__file__), mip_era)
	modules = get_modules(dpath, topic)
	create_specializations(modules)


def _get_topic_cache_key(mip_era, topic):
	"""Returns topic specialization cache key.

	"""
	mip_era = mip_era.strip().lower()
	topic = topic.strip().lower()

	return "{}.{}".format(mip_era, topic)
