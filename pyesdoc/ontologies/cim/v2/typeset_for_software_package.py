"""
.. module:: cim.v2.typeset_for_software_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: The set of types of the cim.v2.software package.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""
import abc
import datetime
import uuid




class ComponentBase(object):
    """An abstract class within the cim v2 type system.

    Base class for software component properties, whether a top level model,
    or a specific piece of code known as a component. In software terms, a
    component is a discrete set of code that takes input data and generates output data.
    Components may or may not have scientific descriptions.

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Instance constructor.

        """
        super(ComponentBase, self).__init__()

        self.canonical_id = None                          # unicode (0.1)
        self.citations = []                               # shared.Citation (0.N)
        self.description = None                           # unicode (0.1)
        self.development_history = None                   # software.DevelopmentPath (0.1)
        self.long_name = None                             # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.release_date = None                          # datetime.datetime (0.1)
        self.repository = None                            # shared.OnlineResource (0.1)
        self.responsible_parties = []                     # shared.Responsibility (0.N)
        self.version = None                               # unicode (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class Composition(object):
    """A concrete class within the cim v2 type system.

    Describes how component variables are coupled together either to/from other
    SoftwareComponents or external data files. The variables specified by a component's
    composition must be owned by that component, or a  child of that component;
    child components cannot couple together parent variables.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Composition, self).__init__()

        self.couplings = []                               # unicode (0.N)
        self.description = None                           # unicode (0.1)


class DevelopmentPath(object):
    """A concrete class within the cim v2 type system.

    Describes the software development path for this model/component.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(DevelopmentPath, self).__init__()

        self.consortium_name = None                       # unicode (0.1)
        self.creators = []                                # shared.Responsibility (0.N)
        self.funding_sources = []                         # shared.Responsibility (0.N)
        self.previous_version = None                      # unicode (0.1)
        self.was_developed_in_house = None                # bool (1.1)


class EntryPoint(object):
    """A concrete class within the cim v2 type system.

    Describes a function or subroutine of a SoftwareComponent.
    BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model.
    Currently, a very basic schedule can be approximated by using the 'proceeds' and 'follows' attributes,
    however a more complete system is required for full BFG compatibility.
    Every EntryPoint can have a set of arguments associated with it.
    These reference (previously defined) variables.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(EntryPoint, self).__init__()

        self.name = None                                  # unicode (0.1)


class Gridspec(object):
    """A concrete class within the cim v2 type system.

    Fully defines the computational grid used.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Gridspec, self).__init__()

        self.description = None                           # unicode (1.1)


class Implementation(object):
    """A concrete class within the cim v2 type system.

    Implementation information for a software framework/component, whether a top level model,
    or a specific piece of code known as a 'component'. In software terms, a
    software framework/component is a discrete set of code that takes input data and generates output data.
    Software frameworks/components may or may not have scientific descriptions.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Implementation, self).__init__()

        self.canonical_id = None                          # unicode (0.1)
        self.citations = []                               # shared.Citation (0.N)
        self.description = None                           # unicode (0.1)
        self.development_history = None                   # software.DevelopmentPath (0.1)
        self.long_name = None                             # unicode (0.1)
        self.name = None                                  # unicode (1.1)
        self.release_date = None                          # datetime.datetime (0.1)
        self.repository = None                            # shared.OnlineResource (0.1)
        self.version = None                               # unicode (0.1)


    @property
    def __str__(self):
	    """Instrance string representation.

	    """
	    return "{}".format(self.name)


class Variable(object):
    """A concrete class within the cim v2 type system.

    An instance of a model software variable which may be prognostic or diagnostic, and which is
    available as a connection to other software components. Note that these variables may only exist
    within the software workflow as interim quantities or coupling endpoints. Input and output
    variables will be a subset of these software variables.

    """
    def __init__(self):
        """Instance constructor.

        """
        super(Variable, self).__init__()

        self.description = None                           # unicode (0.1)
        self.is_prognostic = None                         # bool (1.1)
        self.name = None                                  # unicode (1.1)


class SoftwareComponent(ComponentBase):
    """A concrete class within the cim v2 type system.

    An embedded piece of software that does not normally function as a standalone model (although
    it may be used standalone in a test harness).

    """
    def __init__(self):
        """Instance constructor.

        """
        super(SoftwareComponent, self).__init__()

        self.composition = None                           # software.Composition (0.1)
        self.connection_points = []                       # software.Variable (0.N)
        self.coupling_framework = None                    # software.CouplingFramework (0.1)
        self.dependencies = []                            # software.EntryPoint (0.N)
        self.depends_on = []                              # software.SoftwareComponent (0.N)
        self.grid = None                                  # software.Gridspec (0.1)
        self.language = None                              # software.ProgrammingLanguage (0.1)
        self.license = None                               # unicode (0.1)
        self.sub_components = []                          # software.SoftwareComponent (0.N)


class CouplingFramework(object):
    """An enumeration within the cim v2 type system.

    The set of terms which define known coupling frameworks.
    """
    is_open = False
    members = [
        "OASIS",
        "OASIS3-MCT",
        "ESMF",
        "NUOPC",
        "Bespoke",
        "Unknown",
        "None"
        ]
    descriptions = [
        "The OASIS coupler - prior to OASIS-MCT",
        "The MCT variant of the OASIS coupler",
        "Vanilla Earth System Modelling Framework",
        "National Unified Operational Prediction Capability variant of ESMF",
        "Customised coupler developed for this model",
        "It is not known what/if-a coupler is used",
        "No coupler is used"
        ]


class ProgrammingLanguage(object):
    """An enumeration within the cim v2 type system.

    The set of terms which define programming languages used for earth
    system simulation.
    """
    is_open = False
    members = [
        "Fortran",
        "C",
        "C++",
        "Python"
        ]
    descriptions = [
        "Fortran Programming Language",
        "C Programmming Language",
        "C++ Programming Language",
        "Python Programming Language"
        ]


