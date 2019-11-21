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

import typeset_for_activity_package as activity
import typeset_for_shared_package as shared



class Dataset(object):
    """A concrete class within the cim v2 type system.

    Dataset discovery information.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Dataset, self).__init__()

        self.availability = []                            # shared.OnlineResource (0.N)
        self.citations = []                               # shared.Citation (0.N)
        self.description = None                           # unicode (0.1)
        self.drs_datasets = []                            # drs.DrsPublicationDataset (0.N)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (1.1)
        self.produced_by = None                           # data.Simulation (0.1)
        self.related_to_dataset = []                      # shared.OnlineResource (0.N)
        self.responsible_parties = []                     # shared.Responsibility (0.N)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class InputDataset(object):
    """A concrete class within the cim v2 type system.

    An input dataset is used as within another component (such as a
model). It comprises an original, source dataset plus any
modifications requirted to use it in the relevant component.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(InputDataset, self).__init__()

        self.modifications_applied = None                 # unicode (0.1)
        self.original_data = None                         # data.Dataset (1.1)


class Simulation(activity.Activity):
    """A concrete class within the cim v2 type system.

    Simulation class provides the integrating link about what models
    were run and wny.  In many cases this should be auto-generated
    from output file headers.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Simulation, self).__init__()

        self.calendar = None                              # time.Calendar (0.1)
        self.end_time = None                              # time.DateTime (0.1)
        self.extra_attributes = []                        # shared.ExtraAttribute (0.N)
        self.forcing_index = None                         # int (0.1)
        self.further_info_url = None                      # unicode (0.1)
        self.initialization_index = None                  # int (0.1)
        self.insitution = None                            # shared.Party (0.1)
        self.parent_simulation = None                     # activity.ParentSimulation (0.1)
        self.part_of_project = []                         # designing.Project (1.N)
        self.physics_index = None                         # int (0.1)
        self.primary_ensemble = None                      # activity.Ensemble (0.1)
        self.ran_for_experiments = []                     # designing.NumericalExperiment (1.N)
        self.realization_index = None                     # int (0.1)
        self.start_time = None                            # time.DateTime (0.1)
        self.sub_experiment = None                        # designing.NumericalExperiment (0.1)
        self.used = None                                  # science.Model (1.1)
        self.variant_info = None                          # unicode (0.1)


class VariableCollection(object):
    """A concrete class within the cim v2 type system.

    A collection of variables within the scope of a code or process element.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(VariableCollection, self).__init__()

        self.collection_name = None                       # unicode (0.1)
        self.variables = []                               # unicode (1.N)


class Downscaling(Simulation):
    """A concrete class within the cim v2 type system.

    Defines a downscaling activity.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Downscaling, self).__init__()

        self.downscaled_from = None                       # data.Simulation (1.1)


class DataAssociationTypes(object):
    """An enumeration within the cim v2 type system.

    Set of possible dataset associations.

    Selected from, and extended from,  ISO19115 (2014) DS_AssociationTypeCode.
    """
    is_open = False
    members = [
        "revisonOf",
        "partOf",
        "isComposedOf"
        ]
    descriptions = [
        "This dataset was revised from the target",
        "This dataset forms part of the target",
        "This dataset is composed from the target"
        ]


