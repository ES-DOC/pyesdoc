# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_data_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

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
        self.description = None                           # unicode (0.1)
        self.drs_datasets = []                            # drs.DrsPublicationDataset (0.N)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.name = None                                  # unicode (1.1)
        self.produced_by = None                           # data.Simulation (0.1)
        self.references = []                              # shared.Reference (0.N)
        self.related_to_dataset = []                      # shared.OnlineResource (0.N)
        self.responsible_parties = []                     # shared.Responsibility (0.N)


class Simulation(activity.Activity):
    """A concrete class within the cim v2 type system.

    Simulation class provides the integrating link about what models were run and wny.
    In many cases this should be auto-generated from output file headers.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Simulation, self).__init__()

        self.activity_id = None                           # unicode (0.1)
        self.branch_method = None                         # unicode (0.1)
        self.branch_time_in_child = None                  # float (0.1)
        self.branch_time_in_parent = None                 # float (0.1)
        self.calendar = None                              # time.Calendar (0.1)
        self.comment = None                               # unicode (0.1)
        self.contact = None                               # unicode (0.1)
        self.conventions = None                           # unicode (0.1)
        self.data_specs_version = None                    # unicode (0.1)
        self.ensemble_identifier = None                   # unicode (1.1)
        self.experiment_id = None                         # unicode (0.1)
        self.experisment = None                           # unicode (0.1)
        self.extra_attributes = []                        # shared.ExtraAttribute (0.N)
        self.forcing_index = None                         # int (0.1)
        self.frequency = None                             # unicode (0.1)
        self.further_info_url = None                      # unicode (0.1)
        self.grid = None                                  # unicode (0.1)
        self.grid_label = None                            # unicode (0.1)
        self.grid_resolution = None                       # unicode (0.1)
        self.initialization_index = None                  # int (0.1)
        self.insitution = None                            # unicode (0.1)
        self.institution_id = None                        # unicode (0.1)
        self.mip_era = None                               # unicode (0.1)
        self.parent_activity_id = None                    # unicode (0.1)
        self.parent_experiment_id = None                  # unicode (0.1)
        self.parent_mip_era = None                        # unicode (0.1)
        self.parent_simulation = None                     # activity.ParentSimulation (0.1)
        self.parent_source_id = None                      # unicode (0.1)
        self.parent_sub_experiment_id = None              # unicode (0.1)
        self.parent_time_units = None                     # unicode (0.1)
        self.parent_variant_label = None                  # unicode (0.1)
        self.part_of_project = []                         # designing.Project (1.N)
        self.physics_index = None                         # int (0.1)
        self.primary_ensemble = None                      # activity.Ensemble (0.1)
        self.product = None                               # unicode (0.1)
        self.ran_for_experiments = []                     # designing.NumericalExperiment (1.N)
        self.realization_index = None                     # int (0.1)
        self.realm = None                                 # unicode (0.1)
        self.references = None                            # unicode (0.1)
        self.source = None                                # unicode (0.1)
        self.source_id = None                             # unicode (0.1)
        self.source_type = None                           # unicode (0.1)
        self.sub_eperiment = None                         # unicode (0.1)
        self.sub_eperiment_id = None                      # unicode (0.1)
        self.table_id = None                              # unicode (0.1)
        self.used = None                                  # science.Model (1.1)
        self.variant_info = None                          # unicode (0.1)
        self.variant_label = None                         # unicode (0.1)


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
        "isComposedOf",
        "partOf",
        "revisonOf"
        ]


