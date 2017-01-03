# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.typeset_for_science_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.science package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid

import typeset_for_shared_package as shared
import typeset_for_software_package as software



class Model(software.ComponentBase):
    """A concrete class within the cim v2 type system.

    A model component: can be executed standalone, and has as
    scientific description available via a link to a science.domain
    document. (A configured model can be understood in terms of a
    simulation, a model, and a configuration.).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Model, self).__init__()

        self.coupled_components = []                      # science.Model (0.N)
        self.coupler = None                               # software.CouplingFramework (0.1)
        self.internal_software_components = []            # software.SoftwareComponent (0.N)
        self.key_properties = None                        # science.Process (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.model_type = None                            # science.ModelTypes (1.1)
        self.realms = []                                  # science.Realm (0.N)


class Topic(object):
    """A concrete class within the cim v2 type system.

    An organized collection of details upon a specific topic, e.g. model key properties.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Topic, self).__init__()

        self.citations = []                               # shared.Citation (0.N)
        self.description = None                           # unicode (0.1)
        self.keywords = []                                # unicode (0.N)
        self.overview = None                              # unicode (0.1)
        self.properties = []                              # science.TopicProperty (1.N)
        self.property_sets = []                           # science.TopicPropertySet (1.N)
        self.responsible_parties = []                     # shared.Responsibility (0.N)
        self.short_name = None                            # unicode (0.1)
        self.specialization_id = None                     # unicode (0.1)


class TopicProperty(object):
    """A concrete class within the cim v2 type system.

    A specialized question asked of the scientic community.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(TopicProperty, self).__init__()

        self.specialization_id = None                     # unicode (0.1)
        self.value = None                                 # unicode (1.1)


class TopicPropertySet(object):
    """A concrete class within the cim v2 type system.

    Provides specific details related to a topic (i.e. process, sub-process,
    grid, key properties, etc).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(TopicPropertySet, self).__init__()

        self.description = None                           # unicode (0.1)
        self.properties = []                              # science.TopicProperty (1.N)
        self.short_name = None                            # unicode (0.1)
        self.specialization_id = None                     # unicode (0.1)


class Process(Topic):
    """A concrete class within the cim v2 type system.

    Provides structure for description of a process simulated within a
    particular area (or domain/realm/component) of a model. This will
    often be subclassed within a specific implementation so that
    constraints can be used to ensure that the process details
    requested are consistent with project requirements for
    information.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Process, self).__init__()

        self.sub_processes = []                           # science.Topic (0.N)


class Realm(Topic):
    """A concrete class within the cim v2 type system.

    Scientific area of a numerical model - usually a sub-model or component.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Realm, self).__init__()

        self.grid = None                                  # science.Process (0.1)
        self.key_properties = None                        # science.Process (0.1)
        self.meta = shared.DocMetaInfo()                  # shared.DocMetaInfo (1.1)
        self.processes = []                               # science.Process (1.N)
        self.realm_type = None                            # unicode (0.1)
        self.software_frameworks = []                     # software.Implementation (0.N)


class ModelTypes(object):
    """An enumeration within the cim v2 type system.

    Defines a set of gross model classes.
    """
    is_open = False
    members = [
        "Atm Only",
        "Ocean Only",
        "Regional",
        "ESM",
        "GCM",
        "IGCM",
        "GCM-MLO",
        "Mesoscale",
        "Process",
        "Planetary"
        ]
    descriptions = [
        "Atmosphere Only",
        "Ocean Only",
        "Regional Model",
        "Earth System Model (Atmosphere, Ocean, Land, Sea-ice and cycles)",
        "Global Climate Model (Atmosphere, Ocean, no carbon cycle)",
        "Intermediate Complexity GCM",
        "GCM with mixed layer ocean",
        "Mesoscale Model",
        "Limited Area process model",
        "Non-Earth model"
        ]


