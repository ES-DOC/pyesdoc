"""
.. module:: pyesdoc.drq.content.cache.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: An internal cache of decoded objects.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import collections


# Simple map of drq object uid's to drq object.
DATA = collections.OrderedDict()



def add(instance):
	"""Adds an instance to the cache.

	"""
	DATA[instance.uid] = instance
