# -*- coding: utf-8 -*-

"""
.. module:: pyesdoc.drq._initializer.py
   :copyright: Copyright "February 27, 2016", IPSL
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Encapsulates library initialization.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from pyesdoc.drq.config.initializer import Initializer as ConfigInitializer
from pyesdoc.drq.content.initializer import Initializer as ContentInitializer



class _State(object):
    """Encpasulates mutable module state.

    """
    # Flag indicating whether state has been initialized.
    _is_initialized = False


# List of initializer to be executed.
_INITIALIZERS = [
    ConfigInitializer,
    ContentInitializer
]


def initialize():
    """Initializes library by parsing & loading config & content xml files.

    """
    # Ensure once.
    if _State._is_initialized:
        return

    # Invoke initializers.
    for initializer in _INITIALIZERS:
        initializer()

    # Remember.
    _State._is_initialized = True
