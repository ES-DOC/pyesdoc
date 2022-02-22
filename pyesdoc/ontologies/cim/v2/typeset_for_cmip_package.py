"""
.. module:: cim.v2.typeset_for_cmip_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.cmip package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_activity_package as activity
import typeset_for_data_package as data
import typeset_for_shared_package as shared



class CmipDataset(data.Dataset):
    """A concrete class within the cim v2 type system.

    A CMIP dataset.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(CmipDataset, self).__init__()

        self.drs_location = []                            # drs.DrsPublicationDataset (0.N)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.originating_simulation = None                # activity.Simulation (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class CmipSimulation(activity.Simulation):
    """A concrete class within the cim v2 type system.

    A CMIP simulation.

    In most CMIP cases this should be auto-generated from output dataset
    file headers.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(CmipSimulation, self).__init__()

        self.forcing_index = None                         # int (1.1)
        self.initialization_index = None                  # int (1.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.physics_index = None                         # int (1.1)
        self.realization_index = None                     # int (1.1)
        self.variant_info = None                          # unicode (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "({}/{}/{}{}{}{})".format(self.used, self.ran_for_experiments, self.realization_index, self.initialization_index, self.physics_index, self.forcing_index)


