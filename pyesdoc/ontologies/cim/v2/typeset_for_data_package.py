"""
.. module:: cim.v2.typeset_for_data_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared



class Dataset(object):
    """A concrete class within the cim v2 type system.

    Dataset discovery information.

    This may be further enhanced for ISO (or any other) compliance via
    the extra attributes or project specific sub-classing.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Dataset, self).__init__()

        self.availability = []                            # shared.OnlineResource (0.N)
        self.citations = []                               # shared.Citation (0.N)
        self.contains = []                                # data.VariableCollection (0.N)
        self.description = None                           # unicode (0.1)
        self.further_attributes = []                      # shared.ExtraAttribute (0.N)
        self.keywords = []                                # unicode (0.N)
        self.lineage = None                               # iso.Lineage (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (1.1)
        self.progress = None                              # iso.MdProgressCode (0.1)
        self.related_to_dataset = []                      # shared.FormalAssociation (0.N)
        self.responsible_parties = []                     # shared.Responsibility (0.N)
        self.type = []                                    # data.DatasetType (1.N)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class VariableCollection(object):
    """A concrete class within the cim v2 type system.

    A collection of variables within the scope of a code or process
    element.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(VariableCollection, self).__init__()

        self.collection_name = None                       # unicode (0.1)
        self.geometry = None                              # iso.MdCellgeometryCode (0.1)
        self.variables = []                               # unicode (1.N)


class DatasetType(object):
    """An enumeration within the cim v2 type system.

    Classifier of dataset type, to inform discovery metadata.

    Informed by Bedia et al,
    https://doi.org/10.1016/j.envsoft.2019.07.005, but adjusted for more
    generality.
    """
    is_open = False
    members = [
        "reanalysis",
        "analysis",
        "forecast",
        "hindcast",
        "projection",
        "representation",
        "observation",
        "dump",
        "modified",
        "unphysical",
        "downscaled"
        ]
    descriptions = [
        "Hindcast which includes observations via data assimilation",
        "Product of manipulation of multiple input datasets",
        "Representation of a future real time predicted from a specific initial condition ",
        "Representation of a past real time predicted from a specific initial condition",
        "Representation a possible future given initial conditions and assumptions",
        "Simulation of a particular object or process",
        "Constructed from observations or measurements alone",
        "Raw computer output intended for re-use within or by originating software",
        "Modified representation of another dataset (e.g. regridded)",
        "Not intended for comparison with the real world (e.g. as part of a sensitivity study)",
        "Dataset was downscaled by embedded simulation within driving data at larger scale"
        ]


