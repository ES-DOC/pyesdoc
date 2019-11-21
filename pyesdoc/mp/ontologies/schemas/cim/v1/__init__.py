"""
.. module:: cim.v1.__init__.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: CIM v1 ontology schema.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

from . import activity_classes
from . import activity_enums
from . import data_classes
from . import data_enums
from . import grids_classes
from . import grids_enums
from . import misc_classes
from . import quality_classes
from . import quality_enums
from . import shared_classes
from . import shared_classes_doc
from . import shared_classes_time
from . import shared_enums
from . import software_classes
from . import software_enums


# Ontology name.
NAME = 'cim'

# Ontology version.
VERSION = '1'

# Ontology doc string.
DOC = 'Metafor CIM ontology schema - version 1'




def activity():
    """Types that describe context against which climate models are run.

    """
    return {
        activity_classes,
        activity_enums
    }


def data():
    """Types that describe output that climate models emit.

    """
    return {
        data_classes,
        data_enums
    }


def grids():
    """Types that describe the grids that climate models plot.

    """
    return {
        grids_classes,
        grids_enums
    }


def misc():
    """Miscellaneous types.

    """
    return {
        misc_classes
    }


def quality():
    """Types that describe the quailty of output that climate models emit.

    """
    return {
        quality_classes,
        quality_enums
    }


def shared():
    """Shared types that might be imported from other packages within the ontology.

    """
    return {
        shared_classes,
        shared_classes_doc,
        shared_classes_time,
        shared_enums
    }


def software():
    """Types that describe the climate models software.

    """
    return {
        software_classes,
        software_enums
    }
