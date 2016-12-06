"""
.. module:: pyesdoc.mp.generate.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: pyesdoc.mp code generator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from . import exceptions
from pyesdoc.mp.ontologies.core import create_ontology as get_ontology
from pyesdoc.mp.ontologies.schemas import get_schema
from pyesdoc.mp.ontologies.schemas import validate
from pyesdoc.mp.ontologies.generators import generate

