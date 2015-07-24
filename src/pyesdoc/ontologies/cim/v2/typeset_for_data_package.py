# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_data_package.py

   :copyright: @2015 Earth System Documentation (http://es-doc.org)
   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.data package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using esdoc_mp @ 2015-07-24 23:58:29.529542.

"""
import abc
import datetime
import uuid

import typeset_for_data_package as data
import typeset_for_shared_package as shared



class VariableCollection(object):
    """A concrete class within the cim v2 type system.

    A collection of variables within the scope of a code or process element

    """
    def __init__(self):
        """Constructor.

        """
        super(VariableCollection, self).__init__()

        self.collection_name = None                       # str
        self.variables = []                               # str


class Dataset(object):
    """A concrete class within the cim v2 type system.

    Dataset discovery information

    """
    def __init__(self):
        """Constructor.

        """
        super(Dataset, self).__init__()

        self.meta = shared.Meta()                         # shared.Meta
        self.description = None                           # str
        self.availability = []                            # shared.OnlineResource
        self.produced_by = None                           # activity.Simulation
        self.dataset_author = []                          # shared.Party
        self.drs_datasets = []                            # drs.DrsPublicationDataset
        self.name = None                                  # str
        self.references = []                              # shared.Citation
        self.related_to_dataset = []                      # data.RelatedData


class RelatedData(shared.CimLink):
    """A concrete class within the cim v2 type system.

    A related dataset and a controlled relationship

    """
    def __init__(self):
        """Constructor.

        """
        super(RelatedData, self).__init__()

        self.relationship = None                          # data.DataAssociationTypes
        self.other_dataset = None                         # data.Dataset


class DataAssociationTypes(object):
    """An enumeration within the cim v2 type system.

    Set of possible dataset associations.
    Selected from, and extended from,  ISO19115 (2014) DS_AssociationTypeCode
    """

    pass


