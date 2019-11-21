"""
.. module:: cim.v1.typeset_for_misc_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v1.misc package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

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
        """Instance constructor.

        """
        super(DocumentSet, self).__init__()

        self.data = []                                    # data.DataObject (0.N)
        self.ensembles = []                               # activity.Ensemble (0.N)
        self.experiment = None                            # activity.NumericalExperiment (0.1)
        self.grids = []                                   # grids.GridSpec (0.N)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.model = None                                 # software.ModelComponent (0.1)
        self.platform = None                              # shared.Platform (0.1)
        self.simulation = None                            # activity.SimulationRun (0.1)


