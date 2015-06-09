# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_misc_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.misc package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-05 15:44:25.800707.

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

        self.simulation = None                            # activity.SimulationRun
        self.simulation_reference = None                  # shared.DocReference
        self.experiment_reference = None                  # shared.DocReference
        self.model = None                                 # software.ModelComponent
        self.ensembles = []                               # activity.Ensemble
        self.grids = []                                   # grids.GridSpec
        self.model_reference = None                       # shared.DocReference
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.ensembles_references = []                    # shared.DocReference
        self.data = []                                    # data.DataObject
        self.platform_reference = None                    # shared.DocReference
        self.experiment = None                            # activity.NumericalExperiment
        self.data_references = []                         # shared.DocReference
        self.platform = None                              # shared.Platform
        self.grids_references = []                        # shared.DocReference


