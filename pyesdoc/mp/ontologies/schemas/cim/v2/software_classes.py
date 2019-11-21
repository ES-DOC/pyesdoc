"""
.. module:: software_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def component_base():
    """Base class for software component properties, whether a top level model,
    or a specific piece of code known as a component. In software terms, a
    component is a discrete set of code that takes input data and generates output data.
    Components may or may not have scientific descriptions.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'pstr': ('{}', ('name',)),
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('canonical_id', 'str', '0.1',
                "Vocabulary identifier, where this framework/component description was constructed via a controlled vocabulary."),
            ('description', 'str', '0.1',
                "Textural description of component."),
            ('long_name', 'str', '0.1',
                "Long name for component."),
            ('name', 'str', '1.1',
                "Short name of component."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "People or organisations responsible for providing this information."),

            ('development_history', 'software.development_path', '0.1',
                "History of the development of this component."),
            ('release_date', 'datetime', '0.1',
                "The date of publication of the component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)."),
            ('repository', 'shared.online_resource', '0.1',
                "Location of code for this component."),
            ('version', 'str', '0.1',
                "Version identifier."),
        ]
    }



def implementation():
    """Implementation information for a software framework/component, whether a top level model,
    or a specific piece of code known as a 'component'. In software terms, a
    software framework/component is a discrete set of code that takes input data and generates output data.
    Software frameworks/components may or may not have scientific descriptions.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{}', ('name',)),
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('canonical_id', 'str', '0.1',
                "Vocabulary identifier, where this framework/component description was constructed via a controlled vocabulary."),
            ('description', 'str', '0.1',
                "Textural description of framework/component."),
            ('development_history', 'software.development_path', '0.1',
                "History of the development of this framework/component."),
            ('long_name', 'str', '0.1',
                "Long name for framework/component."),
            ('name', 'str', '1.1',
                "Short name of framework/component."),
            ('release_date', 'datetime', '0.1',
                "The date of publication of the framework/component code."),
            ('repository', 'shared.online_resource', '0.1',
                "Location of code for this framework/component."),
            ('version', 'str', '0.1',
                "Version identifier.")
        ]
    }


def composition():
    """Describes how component variables are coupled together either to/from other
    SoftwareComponents or external data files. The variables specified by a component's
    composition must be owned by that component, or a  child of that component;
    child components cannot couple together parent variables.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('couplings', 'str', '0.N',
                "#FIXME."),
            ('description', 'str', '0.1',
                "#FIXME.")
        ]
    }


def development_path():
    """Describes the software development path for this model/component.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('consortium_name', 'str', '0.1',
                "If model/component is developed as part of a consortium, provide consortium name."),
            ('creators', 'shared.responsibility', '0.N',
                "Those responsible for creating this component."),
            ('was_developed_in_house', 'bool', '1.1',
                "Model or component was mostly developed in house."),
            ('funding_sources', 'shared.responsibility', '0.N',
                "The entities that funded this software component."),
            ('previous_version', 'str', '0.1',
                "Name of a previous version.")
        ]
    }


def entry_point():
    """Describes a function or subroutine of a SoftwareComponent.
    BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model.
    Currently, a very basic schedule can be approximated by using the 'proceeds' and 'follows' attributes,
    however a more complete system is required for full BFG compatibility.
    Every EntryPoint can have a set of arguments associated with it.
    These reference (previously defined) variables.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('name', 'str', '0.1',
                "#FIXME.")
        ]
    }


def gridspec():
    """Fully defines the computational grid used.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '1.1',
                "Textural description.")
        ]
    }


def software_component():
    """An embedded piece of software that does not normally function as a standalone model (although
    it may be used standalone in a test harness).

    """
    return {
        'type': 'class',
        'base': 'software.component_base',
        'is_abstract': False,
        'properties': [
            ('composition', 'software.composition', '0.1',
                "#FIXME."),
            ('connection_points', 'software.variable', '0.N',
                "The set of data entities which are available for I/O and/or coupling."),
            ('coupling_framework', 'software.coupling_framework', '0.1',
                "The coupling framework that this entire component conforms to."),
            ('dependencies', 'software.entry_point', '0.N',
                "#FIXME."),
            ('grid', 'software.gridspec', '0.1',
                "A reference to the grid that is used by this component."),
            ('language', 'software.programming_language', '0.1',
                "Language the component is written in."),
            ('license', 'str', '0.1',
                "The license held by this piece of software."),
            ('sub_components', 'software.software_component', '0.N',
                "Internal software sub-components of this component."),
            ('depends_on', 'software.software_component', '0.N',        # added dch/ssw 1016-0804
                "The software components whose outputs are inputs to this software component."),
            # Would like to think about making this a stand-alone document
        ]
    }


def variable():
    """An instance of a model software variable which may be prognostic or diagnostic, and which is
    available as a connection to other software components. Note that these variables may only exist
    within the software workflow as interim quantities or coupling endpoints. Input and output
    variables will be a subset of these software variables.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1',
                "Description of how the variable is being used in the s/w."),
            ('name', 'str', '1.1',
                "Short name for the variable."),
            ('is_prognostic', 'bool', '1.1',
                "Whether or not prognostic or diagnostic.")
        ]
    }
