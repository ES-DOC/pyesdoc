# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.typeset_for_misc_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.misc package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-06-01 16:50:10.361806.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class DocumentSet(object):
    """A concrete class within the cim v1 type system.

    Creates and returns instance of document_set class.

    """
    def __init__(self):
        """Constructor.

        """
        super(DocumentSet, self).__init__()

        self.data = []                                    # data.DataObject
        self.data_references = []                         # shared.DocReference
        self.ensembles = []                               # activity.Ensemble
        self.ensembles_references = []                    # shared.DocReference
        self.experiment = None                            # activity.NumericalExperiment
        self.experiment_reference = None                  # shared.DocReference
        self.grids = []                                   # grids.GridSpec
        self.grids_references = []                        # shared.DocReference
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo
        self.model = None                                 # software.ModelComponent
        self.model_reference = None                       # shared.DocReference
        self.platform = None                              # shared.Platform
        self.platform_reference = None                    # shared.DocReference
        self.simulation = None                            # activity.SimulationRun
        self.simulation_reference = None                  # shared.DocReference


