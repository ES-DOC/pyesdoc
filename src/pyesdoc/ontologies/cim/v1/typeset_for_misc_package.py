# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_misc_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.misc package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:33:18.153885.

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

        self.grids_references = []                        # shared.DocReference
        self.simulation_reference = None                  # shared.DocReference
        self.experiment = None                            # activity.NumericalExperiment
        self.model_reference = None                       # shared.DocReference
        self.model = None                                 # software.ModelComponent
        self.simulation = None                            # activity.SimulationRun
        self.data_references = []                         # shared.DocReference
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.experiment_reference = None                  # shared.DocReference
        self.ensembles = []                               # activity.Ensemble
        self.platform = None                              # shared.Platform
        self.grids = []                                   # grids.GridSpec
        self.platform_reference = None                    # shared.DocReference
        self.ensembles_references = []                    # shared.DocReference
        self.data = []                                    # data.DataObject


