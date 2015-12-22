# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_misc_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.misc package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class DocumentSet(object):
    """A concrete class within the cim v1 type system.

    Represents a bundled set of documents.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocumentSet, self).__init__()

        self.data = []                                    # data.DataObject
        self.ensembles = []                               # activity.Ensemble
        self.experiment = None                            # activity.NumericalExperiment
        self.grids = []                                   # grids.GridSpec
        self.link_to_data = []                            # shared.DocReference
        self.link_to_ensembles = []                       # shared.DocReference
        self.link_to_experiment = None                    # shared.DocReference
        self.link_to_grids = []                           # shared.DocReference
        self.link_to_model = None                         # shared.DocReference
        self.link_to_platform = None                      # shared.DocReference
        self.link_to_simulation = None                    # shared.DocReference
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.model = None                                 # software.ModelComponent
        self.platform = None                              # shared.Platform
        self.simulation = None                            # activity.SimulationRun


